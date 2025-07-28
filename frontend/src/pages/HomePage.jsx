import React, { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import api from '../api';
import './HomePage.css';

const HomePage = () => {
    const { language } = useParams(); // URL에서 현재 언어를 가져옵니다.
    const [dashboardData, setDashboardData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchDashboardData = async () => {
            if (!language) return;
            setLoading(true);
            try {
                // API 호출 시 language를 포함하여 요청
                const response = await api.get(`/dashboard/${language}`);
                setDashboardData(response.data);
            } catch (error) {
                console.error("Failed to fetch dashboard data", error);
            } finally {
                setLoading(false);
            }
        };
        fetchDashboardData();
    }, [language]); // language가 바뀔 때마다 데이터를 다시 불러옵니다.

    if (loading) return <div className="loading-message">로딩 중...</div>;
    if (!dashboardData) return <div className="loading-message">대시보드 정보를 불러올 수 없습니다.</div>;

    // 백엔드에서 받은 데이터에서 earned_badges를 추출합니다.
    const { user, rank_info, all_chapters, completed_problem_ids, next_problem_url, earned_badges } = dashboardData;

    return (
        <main className="dashboard-main">
            <div className="dashboard-header">
                <h2>환영합니다, {user.username}님!</h2>
                <p>오늘도 양햄이와 함께 즐겁게 코딩해봐요!</p>
            </div>

            <div className="dashboard-card summary-card-group">
                <div className="welcome-card">
                    <h3>내 계급</h3>
                    <img src={`/img/${rank_info.image}`} alt={rank_info.name} className="rank-icon-large" />
                    <p className="rank-name">{rank_info.name}</p>
                </div>

                <div className="continue-card">
                    <h3>이어서 학습하기</h3>
                    <p>가장 최근에 학습하던 곳부터 다시 시작하세요.</p>
                    <Link to={next_problem_url} className="continue-btn">
                        학습 계속하기 →
                    </Link>
                </div>
            </div>

            {/* --- 획득한 배지 섹션 --- */}
            {earned_badges && earned_badges.length > 0 && (
                <div className="dashboard-card badge-card">
                    <h3>획득한 배지 🏆</h3>
                    <div className="badge-grid">
                        {earned_badges.map(badge => (
                            <div key={badge.id} className="badge-item" title={`${badge.name}: ${badge.description}`}>
                                <img src={`/img/${badge.image}`} alt={badge.name} />
                            </div>
                        ))}
                    </div>
                </div>
            )}

            <div className="dashboard-grid">
                {all_chapters.map(chapter => {
                    if (!chapter.problems.length) return null;

                    const total = chapter.problems.length;
                    const completed = chapter.problems.filter(p => completed_problem_ids.includes(p.id)).length;
                    const percent = total > 0 ? Math.round((completed / total) * 100) : 0;

                    return (
                        <div key={chapter.slug} className="dashboard-card chapter-summary-card">
                            <h3>{chapter.title}</h3>
                            <div className="summary-progress-bar">
                                <div className="summary-progress-bar-fill" style={{ width: `${percent}%` }}></div>
                            </div>
                            <p>{completed} / {total} 문제 완료 ({percent}%)</p>
                            <Link to={`/${language}/${chapter.slug}/1`} className="shortcut-button chapter-shortcut">
                                바로가기
                            </Link>
                        </div>
                    );
                })}
            </div>
        </main>
    );
};

export default HomePage;
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import api from '../api';
import './LanguageSelectionPage.css';
import { LANGUAGES } from '../config';

// HomePage의 대시보드 스타일을 재사용하기 위해 import 합니다.
import './HomePage.css'; 

const LanguageSelectionPage = () => {
    const [progressData, setProgressData] = useState(null);
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [dashboardData, setDashboardData] = useState(null);
    const [isLoading, setIsLoading] = useState(true); // 로딩 상태 추가

    useEffect(() => {
        // 로그인 상태를 확인하고, 로그인했다면 대시보드와 진행률 데이터를 모두 가져옵니다.
        api.get('/users/me')
            .then(res => {
                setIsLoggedIn(true);
                // 두 개의 API를 동시에 호출하여 데이터를 가져옵니다.
                Promise.all([
                    api.get('/overall-progress'),
                    api.get('/simple-dashboard') // 언어와 무관한 대시보드 정보 요청
                ]).then(([progressRes, dashboardRes]) => {
                    setProgressData(progressRes.data);
                    setDashboardData(dashboardRes.data);
                }).catch(error => {
                    console.error("데이터 로딩 실패:", error);
                }).finally(() => {
                    setIsLoading(false);
                });
            })
            .catch(() => {
                setIsLoggedIn(false);
                setIsLoading(false);
            });
    }, []); // 이 useEffect는 컴포넌트가 처음 렌더링될 때 한 번만 실행됩니다.

    return (
        <main className="language-selection-main">
            <div className="hero">
                {!isLoggedIn}
                <h2>학습할 언어를 선택하세요!</h2>
                <p>기초 문법부터 차근차근 마스터해보세요.</p>
            </div>
            {/* --- 로그인 시에만 보이는 대시보드 정보 --- */}
            {isLoggedIn && !isLoading && dashboardData && (
                <div className="summary-section">
                    <div className="dashboard-card summary-card-group">
                        <div className="welcome-card">
                            <h3>내 계급</h3>
                            <img src={`/img/${dashboardData.rank_info.image}`} alt={dashboardData.rank_info.name} className="rank-icon-large" />
                            <p className="rank-name">{dashboardData.rank_info.name}</p>
                        </div>
                        <div className="continue-card">
                            <h3>이어서 학습하기</h3>
                            <p>가장 최근에 학습하던 곳부터 다시 시작하세요.</p>
                            <Link to={dashboardData.next_problem_url} className="continue-btn">
                                학습 계속하기 →
                            </Link>
                        </div>
                    </div>
                    {dashboardData.earned_badges && dashboardData.earned_badges.length > 0 && (
                        <div className="dashboard-card badge-card">
                            <h3>획득한 배지 🏆</h3>
                            <div className="badge-grid">
                                {dashboardData.earned_badges.map(badge => (
                                    <div key={badge.id} className="badge-item" title={`${badge.name}: ${badge.description}`}>
                                        <img src={`/img/${badge.image}`} alt={badge.name} />
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}
                </div>
            )}
            
            <div className="language-grid">
                {LANGUAGES.map(lang => {
                    const langProgress = progressData?.[lang.slug];
                    const percent = langProgress && langProgress.total > 0
                        ? Math.round((langProgress.completed / langProgress.total) * 100)
                        : 0;
                    return (
                        <Link to={`/${lang.slug}`} key={lang.slug} className="language-card" style={{'--lang-color': lang.color}}>
                            <span className="language-name">{lang.name}</span>
                            {isLoggedIn && langProgress && (
                                <div className="progress-info">
                                    <div className="progress-bar-background">
                                        <div className="progress-bar-fill" style={{ width: `${percent}%`, backgroundColor: lang.color }}></div>
                                    </div>
                                    <span className="progress-text">{percent}% 완료</span>
                                </div>
                            )}
                        </Link>
                    );
                })}
            </div>
        </main>
    );
};

export default LanguageSelectionPage;
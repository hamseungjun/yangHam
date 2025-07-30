import React, { useState, useEffect } from 'react';
import api from '../api';
import './LeaderboardPage.css';

const LeaderboardPage = () => {
    const [leaderboard, setLeaderboard] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchLeaderboard = async () => {
            try {
                const response = await api.get('/leaderboard');
                setLeaderboard(response.data);
            } catch (err) {
                setError('리더보드 데이터를 불러오는 데 실패했습니다.');
                console.error(err);
            } finally {
                setLoading(false);
            }
        };

        fetchLeaderboard();
    }, []);

    const getMedal = (rank) => {
        if (rank === 1) return '🥇';
        if (rank === 2) return '🥈';
        if (rank === 3) return '🥉';
        return null;
    };

    if (loading) {
        return <div className="leaderboard-container loading">로딩 중...</div>;
    }

    if (error) {
        return <div className="leaderboard-container error">{error}</div>;
    }

    return (
        <div className="leaderboard-container">
            <h1>🏆 리더보드</h1>
            <p>다른 학습자들과 순위를 비교해보세요!</p>
            <div className="leaderboard-list">
                {leaderboard.map((user) => (
                    <div key={user.rank} className={`leaderboard-item rank-${user.rank}`}>
                        <span className="rank-number">
                            {getMedal(user.rank) || user.rank}
                        </span>
                        <div className="rank-user-info">
                            <img src={`/img/${user.rank_image}`} alt={user.rank_name} className="rank-icon" />
                            <span className="rank-username">{user.username}</span>
                        </div>
                        <div className="rank-details">
                            <div className="rank-badges">
                                {user.earned_badges && user.earned_badges.map(badge => (
                                    <img 
                                        key={badge.id} 
                                        src={`/img/${badge.image}`} 
                                        alt={badge.name} 
                                        title={`${badge.name}: ${badge.description}`}
                                        className="rank-badge-icon"
                                    />
                                ))}
                            </div>
                            <span className="rank-name">{user.rank_name}</span>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default LeaderboardPage;
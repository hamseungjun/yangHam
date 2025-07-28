import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import api from '../api'; // api.js 임포트
import './LanguageSelectionPage.css';
import { LANGUAGES } from '../config';

const LanguageSelectionPage = () => {
    const [progressData, setProgressData] = useState(null);
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    // 컴포넌트가 마운트될 때 사용자의 로그인 상태와 전체 진행률을 가져옵니다.
    useEffect(() => {
        // 1. 로그인 상태 확인
        api.get('/users/me')
            .then(res => {
                setIsLoggedIn(true);
                // 2. 로그인 상태이면, 전체 진행률 데이터 요청
                return api.get('/overall-progress');
            })
            .then(res => {
                setProgressData(res.data);
            })
            .catch(() => {
                // 로그인하지 않았거나 API 요청에 실패하면 상태를 초기화합니다.
                setIsLoggedIn(false);
                setProgressData(null);
            });
    }, []); // 이 useEffect는 처음 한 번만 실행됩니다.

    return (
        <main className="language-selection-main">
            <div className="hero">
                <img src="/final_logo.png" alt="양햄이 코딩스쿨" className="hero-logo" />
                <h2>학습할 언어를 선택하세요!</h2>
                <p>기초 문법부터 차근차근 마스터해보세요.</p>
            </div>
            <div className="language-grid">
                {LANGUAGES.map(lang => {
                    const langProgress = progressData?.[lang.slug];
                    const percent = langProgress && langProgress.total > 0
                        ? Math.round((langProgress.completed / langProgress.total) * 100)
                        : 0;

                    return (
                        <Link 
                            to={`/${lang.slug}`} 
                            key={lang.slug} 
                            className="language-card" 
                            style={{'--lang-color': lang.color}}
                        >
                            <span className="language-name">{lang.name}</span>
                            
                            {/* 로그인 상태이고 진행률 데이터가 있을 때만 진행률 바를 표시합니다. */}
                            {isLoggedIn && langProgress && (
                                <div className="progress-info">
                                    <div className="progress-bar-background">
                                        <div 
                                            className="progress-bar-fill"
                                            style={{ width: `${percent}%`, backgroundColor: lang.color }}
                                        ></div>
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
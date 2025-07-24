import React from 'react';
import { Link } from 'react-router-dom';
import './LanguageSelectionPage.css';
import { LANGUAGES } from '../config'; // 기존 배열 대신 config 파일에서 가져옵니다.

const LanguageSelectionPage = () => {
    return (
        <main className="language-selection-main">
            <div className="hero">
                <img src="/final_logo.png" alt="양햄이 코딩스쿨" className="hero-logo" />
                <h2>학습할 언어를 선택하세요!</h2>
                <p>기초 문법부터 차근차근 마스터해보세요.</p>
            </div>
            <div className="language-grid">
                {LANGUAGES.map(lang => (
                    <Link 
                        to={`/${lang.slug}`} 
                        key={lang.slug} 
                        className="language-card" 
                        // CSS 변수를 이용해 각 카드에 고유 색상을 적용합니다.
                        style={{'--lang-color': lang.color}}
                    >
                        <span>{lang.name}</span>
                    </Link>
                ))}
            </div>
        </main>
    );
};

export default LanguageSelectionPage;
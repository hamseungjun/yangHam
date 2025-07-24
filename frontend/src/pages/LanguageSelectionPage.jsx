import React from 'react';
import { Link } from 'react-router-dom';
import './LanguageSelectionPage.css';

const LANGUAGES = [
    { slug: 'python', name: 'Python', color: '#3776AB' },
    { slug: 'javascript', name: 'JavaScript', color: '#F7DF1E' },
    { slug: 'c', name: 'C', color: '#5C6BC0' },
    { slug: 'java', name: 'Java', color: '#E52D27' },
];

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
                    <Link to={`/${lang.slug}`} key={lang.slug} className="language-card" style={{'--lang-color': lang.color}}>
                        <span>{lang.name}</span>
                    </Link>
                ))}
            </div>
        </main>
    );
};

export default LanguageSelectionPage;
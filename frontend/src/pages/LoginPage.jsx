import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import api from '../api';
import './Auth.css'; // ✨ 공유 CSS 임포트

const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const formData = new FormData();
            formData.append('username', username);
            formData.append('password', password);
            
            await api.post('/login', formData);
            navigate('/'); // 로그인 성공 시 홈으로 이동
        } catch (err) {
            setError('사용자 이름 또는 비밀번호가 올바르지 않습니다.');
            console.error(err);
        }
    };

    return (
        <main className="auth-main">
            <div className="auth-card">
                <h2>로그인</h2>
                {error && <p className="error-message">{error}</p>}
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="username">사용자 이름</label>
                        <div className="input-wrapper">
                            <span className="icon">👤</span>
                            <input type="text" id="username" value={username} onChange={e => setUsername(e.target.value)} placeholder="사용자 이름을 입력하세요" required />
                        </div>
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">비밀번호</label>
                        <div className="input-wrapper">
                            <span className="icon">🔒</span>
                            <input type="password" id="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="비밀번호를 입력하세요" required />
                        </div>
                    </div>
                    <button type="submit">로그인</button>
                </form>
                <p className="switch-form-text">계정이 없으신가요? <Link to="/signup">회원가입</Link></p>
            </div>
        </main>
    );
};
export default LoginPage;
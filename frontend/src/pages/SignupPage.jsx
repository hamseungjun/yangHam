import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import api from '../api';
import './Auth.css'; // ✨ 공유 CSS 임포트


const SignupPage = () => {
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

            await api.post('/signup', formData);
            navigate('/login'); // 회원가입 성공 시 로그인 페이지로 이동
        } catch (err) {
            setError(err.response?.data?.detail || '회원가입 중 오류가 발생했습니다.');
            console.error(err);
        }
    };

    return (
        <main className="auth-main">
            <div className="auth-card">
                <h2>회원가입</h2>
                {error && <p className="error-message">{error}</p>}
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="username">사용자 이름</label>
                        <div className="input-wrapper">
                            <span className="icon" placeholder = "사용할 이름을 입력하세요"></span>
                            <input type="text" id="username" value={username} onChange={e => setUsername(e.target.value)} placeholder="사용할 이름을 입력하세요" required />
                        </div>
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">비밀번호</label>
                        <div className="input-wrapper">
                            <span placeholder="사용할 비밀번호를 입력하세요"></span>
                            <input type="password" id="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="사용할 비밀번호를 입력하세요" required />
                        </div>
                    </div>
                    <button type="submit">가입하기</button>
                </form>
                <p className="switch-form-text">이미 계정이 있으신가요? <Link to="/login">로그인</Link></p>
            </div>
        </main>
    );
};
export default SignupPage;
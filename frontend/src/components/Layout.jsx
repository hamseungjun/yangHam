import React, { useState, useEffect } from 'react';
import { Outlet, Link, NavLink, useParams } from 'react-router-dom';
import api from '../api';
import './Layout.css';

const Layout = () => {
  const [chapters, setChapters] = useState([]);
  const [user, setUser] = useState(null);
  const { language } = useParams(); // URL에서 현재 언어 slug를 가져옵니다.

  // 사용자 정보 가져오기
  useEffect(() => {
    api.get('/users/me')
      .then(res => setUser(res.data))
      .catch(() => setUser(null));
  }, []);

  // 언어가 변경될 때마다 해당 언어의 챕터 목록을 가져오기
  useEffect(() => {
    if (language) {
      api.get(`/chapters/${language}`)
        .then(res => setChapters(res.data))
        .catch(err => {
            console.error(`Failed to fetch chapters for ${language}`, err);
            setChapters([]);
        });
    } else {
        setChapters([]); // 언어 선택 페이지에서는 챕터 목록을 비웁니다.
    }
  }, [language]);

  const handleLogout = async () => {
    try {
      await api.post('/logout');
      setUser(null);
      window.location.href = '/login';
    } catch (error) {
      console.error("Logout failed", error);
    }
  };

  return (
    <>
      <div className="sub-header">
        <div className="sub-header-inner">
          {user ? (
            <>
              <span>환영합니다, <strong>{user.username}</strong>님!</span>
              <Link to={`/${language}`}>학습 홈</Link>
              <button onClick={handleLogout} className="logout-button">로그아웃</button>
            </>
          ) : (
            <>
              <Link to="/login">로그인</Link>
              <Link to="/signup">회원가입</Link>
            </>
          )}
        </div>
      </div>
      <header className="top-nav">
        <Link to="/" className="logo-link">
            <img src="/final_logo.png" alt="양햄이 코딩스쿨 로고" className="logo" />
        </Link>
        {/* language가 URL에 있을 때만 네비게이션 바를 렌더링합니다. */}
        {language && chapters.length > 0 && (
            <nav className="nav">
              <ul className="nav-list">
                {chapters.map(chapter => (
                    <li key={chapter.slug}>
                        {chapter.problems && chapter.problems.length > 0 ? (
                            <NavLink to={`/${language}/${chapter.slug}/1`} className={({ isActive }) => isActive ? "active" : ""}>
                                {chapter.title}
                            </NavLink>
                        ) : (
                            <a href="#" className="disabled">{chapter.title}</a>
                        )}
                    </li>
                ))}
              </ul>
            </nav>
        )}
      </header>
      <Outlet context={{ user }} />
    </>
  );
};
export default Layout;
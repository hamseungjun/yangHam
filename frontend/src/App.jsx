import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import ProtectedRoute from './components/ProtectedRoute';
import ProblemPage from './pages/ProblemPage';
import LoginPage from './pages/LoginPage';
import SignupPage from './pages/SignupPage';
import HomePage from './pages/HomePage';
import LanguageSelectionPage from './pages/LanguageSelectionPage';
import LeaderboardPage from './pages/LeaderboardPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* 이제 Layout이 모든 페이지의 부모 역할을 합니다. */}
        <Route path="/" element={<Layout />}>
          
          {/* --- 누구나 접근 가능한 페이지들 --- */}
          <Route index element={<LanguageSelectionPage />} />
          <Route path="login" element={<LoginPage />} />
          <Route path="signup" element={<SignupPage />} />
          
          {/* --- 로그인이 필요한 보호된 페이지들 --- */}
          <Route element={<ProtectedRoute />}>
            <Route path="leaderboard" element={<LeaderboardPage />} />
            <Route path=":language" element={<HomePage />} />
            <Route path=":language/:chapterSlug/:problemId" element={<ProblemPage />} />
          </Route>
          
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
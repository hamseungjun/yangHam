import React, { useState, useEffect } from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import api from '../api';

const ProtectedRoute = () => {
    const [isAuthenticated, setIsAuthenticated] = useState(null);

    useEffect(() => {
        api.get('/users/me')
            .then(res => setIsAuthenticated(true))
            .catch(() => setIsAuthenticated(false));
    }, []);

    if (isAuthenticated === null) {
        return <div>로딩 중...</div>; // 인증 상태 확인 중
    }

    // 인증되었으면 자식 페이지(학습 페이지 등)를 보여주고,
    // 그렇지 않으면 로그인 페이지로 보냅니다.
    return isAuthenticated ? <Outlet /> : <Navigate to="/login" replace />;
};

export default ProtectedRoute;
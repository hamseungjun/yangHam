import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:8000/api',
    withCredentials: true, // 쿠키를 주고받기 위한 필수 설정
});

export default api;
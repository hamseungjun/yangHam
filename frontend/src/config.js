// 각 언어의 이름, 슬러그(slug), 대표 색상, 호버 시 색상을 정의합니다.
export const LANGUAGES = [
    { slug: 'python', name: 'Python', color: '#3776AB', hover: '#2b5f8a' , logo :"img/logo/python_logo.png"},
    { slug: 'javascript', name: 'JavaScript', color: '#F7DF1E', hover: '#d4bb1a' , logo :"img/logo/javascript_logo.png"},
    { slug: 'c', name: 'C', color: '#5C6BC0', hover: '#4a5598' , logo :"img/logo/c_logo.png"},
    { slug: 'java', name: 'Java', color: '#E52D27', hover: '#b8241f' , logo :"img/logo/java_logo.png"},
];

// 기본 테마 색상도 이곳에서 관리합니다.
export const DEFAULT_THEME = {
    color: '#007BFF',
    hover: '#0056b3'
};
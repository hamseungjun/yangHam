import React, { useState, useEffect, useRef, useCallback } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import api from '../api';
import CodeMirror from '@uiw/react-codemirror';
import './ProblemPage.css'; // 문제 페이지 전용 CSS
// CodeMirror 언어 지원 동적 로딩을 위한 설정
import { python } from '@codemirror/lang-python';
import { javascript } from '@codemirror/lang-javascript';
import { cpp } from '@codemirror/lang-cpp';
import { java } from '@codemirror/lang-java';

const languageExtensions = {
    python: python(),
    javascript: javascript(),
    c: cpp(), // C언어는 cpp 확장을 사용합니다.
    java: java()
};

const ProblemPage = () => {
    const { language, chapterSlug, problemId } = useParams();
    const navigate = useNavigate();

    const [data, setData] = useState(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState('');

    const [userCode, setUserCode] = useState("# 여기에 코드를 작성하세요.");
    const [executionOutput, setExecutionOutput] = useState(null);
    const [feedback, setFeedback] = useState(null);
    
    // Pyodide (Python 실행 환경) 관련 상태
    const [isPyodideReady, setPyodideReady] = useState(false);
    const pyodide = useRef(null);

    // '핵심 이론' 접기/펴기 상태
    const [showTheory, setShowTheory] = useState(true);

    // Python 코드를 브라우저에서 실행하기 위해 Pyodide를 로딩합니다.
    useEffect(() => {
        // Python 문제가 아닐 경우 Pyodide를 로드할 필요가 없습니다.
        if (language === 'python') {
            const loadPyodideInstance = async () => {
                try {
                    // window.loadPyodide는 public/index.html에 추가된 스크립트를 통해 전역으로 접근 가능
                    pyodide.current = await window.loadPyodide();
                    setPyodideReady(true);
                } catch(e) { console.error("Pyodide 로딩 실패:", e); }
            };
            loadPyodideInstance();
        } else {
            // 다른 언어의 경우, Pyodide가 필요 없으므로 바로 준비된 것으로 간주합니다.
            // (주의: 이 부분은 향후 다른 언어의 브라우저 실행 환경을 추가할 때 수정 필요)
            setPyodideReady(true); 
        }
    }, [language]);

    // URL 파라미터가 바뀔 때마다 문제 데이터를 새로 불러오는 함수
    const fetchData = useCallback(async () => {
        if (!language || !chapterSlug || !problemId) return;
        setIsLoading(true);
        setError('');
        setFeedback(null);
        setExecutionOutput(null);
        setUserCode(`# 여기에 ${language} 코드를 작성하세요.`);
        try {
            const res = await api.get(`/chapters/${language}/${chapterSlug}/problems/${problemId}`);
            setData(res.data);
        } catch (err) {
            setError("문제를 불러오는 데 실패했습니다.");
            console.error(err);
        } finally {
            setIsLoading(false);
        }
    }, [language, chapterSlug, problemId]);

    // fetchData 함수를 호출
    useEffect(() => { fetchData(); }, [fetchData]);

    // 정답 확인 버튼 클릭 시 실행되는 함수
    // ProblemPage.jsx

const handleCheckAnswer = async () => {
    if (language === 'python') {
        if (!isPyodideReady) return;
        setExecutionOutput("실행 중...");
        try {
            let stdout = "";
            pyodide.current.setStdout({ batched: (str) => stdout += str + "\n" });
            await pyodide.current.runPythonAsync(userCode);
            setExecutionOutput(stdout.trim() || "(출력 없음)");
        } catch (err) { 
            setExecutionOutput(`에러 발생:\n${err}`);
        }
    } else {
        setExecutionOutput("(백엔드에서 채점 중...)");
    }

    try {
        const formData = new FormData();
        formData.append('user_code', userCode);
        const res = await api.post(`/check-answer/${language}/${chapterSlug}/${problemId}`, formData);
        
        setFeedback(res.data); // 1. AI 피드백 상태를 먼저 설정합니다.

        // 2. 정답일 경우, fetchData() 대신 로컬 상태를 직접 업데이트합니다.
        if (res.data.is_correct) {
            setData(prevData => ({
                ...prevData,
                // 기존에 완료한 문제 목록에 현재 문제 ID를 추가합니다.
                completed_problem_ids: [...prevData.completed_problem_ids, prevData.problem.id]
            }));
        }
    } catch (error) { console.error("API 요청 실패", error); }
};

    if (isLoading) return <div className="loading-message">로딩 중...</div>;
    if (error) return <div className="loading-message">{error}</div>;
    if (!data) return <div className="loading-message">데이터가 없습니다.</div>;

    // 데이터 로딩이 완료된 후에 변수들을 선언합니다.
    const { chapter, problem, total_problems, completed_problem_ids } = data;
    const currentProblemNum = parseInt(problemId);
    const isCompleted = completed_problem_ids?.includes(problem.id);
    const completedCount = chapter.problems.filter(p => completed_problem_ids.includes(p.id)).length;
    const progressPercent = total_problems > 0 ? (completedCount / total_problems) * 100 : 0;
    
    return (
        <div className="problem-container">
            <aside className="theory-sidebar">
                <div className="theory-header">
                    <h3>💡 핵심 이론</h3>
                    
                </div>
                <div className={`theory-content ${showTheory ? 'open' : ''}`} dangerouslySetInnerHTML={{ __html: problem.theory }} />
            </aside>

            <main className="problem-area">
                <div className="chapter-summary-card">
                    <div className="progress-header">
                        <h3>{chapter.title}</h3>
                        <div className="problem-step-buttons">
                            <Link to={`/${language}/${chapterSlug}/${currentProblemNum - 1}`} className={`step-button ${currentProblemNum <= 1 ? 'disabled' : ''}`}>
                                이전 문제
                            </Link>
                            <span className="current-step">{currentProblemNum} / {total_problems}</span>
                            <Link to={`/${language}/${chapterSlug}/${currentProblemNum + 1}`} className={`step-button ${currentProblemNum >= total_problems ? 'disabled' : ''}`}>
                                다음 문제
                            </Link>
                        </div>
                    </div>
                    <div className="summary-progress-bar">
                        <div className="summary-progress-bar-fill" style={{ width: `${progressPercent}%` }}></div>
                    </div>
                    <p>{completedCount} / {total_problems} 문제 완료 ({Math.round(progressPercent)}%)</p>
                </div>

                <div className="content-card">
                    <div className="problem-header">
                        <h2>{problem.title}</h2>
                        <div className="completion-indicator" title={isCompleted ? "완료한 문제" : "미완료 문제"}>
                            {isCompleted ? <span className="completed"></span> : <span className="incomplete"></span>}
                        </div>
                    </div>
                    <p className="question">{problem.question}</p>
                </div>

                <div className="content-card">
                    <div className="editor-container">
                        <CodeMirror
                            value={userCode}
                            height="300px"
                            extensions={[languageExtensions[language]]} // 현재 언어에 맞는 확장 기능 적용
                            onChange={(value) => setUserCode(value)}
                            theme="light"
                        />
                    </div>
                    <div className="button-area">
                        <button onClick={handleCheckAnswer} disabled={!isPyodideReady}>
                            {!isPyodideReady ? '실행 환경 준비 중...' : '정답 확인하기'}
                        </button>
                    </div>
                </div>

                {/* 실행 결과 및 피드백 창 */}
                {executionOutput !== null && (
                    <div className="result-box output-box">
                        <h4>💻 실행 결과</h4>
                        <pre>{executionOutput}</pre>
                    </div>
                )}
                {feedback && (
                    <div className={`result-box ${feedback.is_correct ? 'feedback-correct' : 'feedback-incorrect'}`}>
                        <h4>🤖 AI 피드백</h4>
                        <p dangerouslySetInnerHTML={{ __html: feedback.feedback.replace(/\n/g, '<br>') }} />
                    </div>
                )}
            </main>
        </div>
    );
};

export default ProblemPage;
import React, { useState, useEffect, useRef, useCallback } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import api from '../api';
import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python'; // (향후 언어별로 동적 import 필요)
import './ProblemPage.css';

const ProblemPage = () => {
    const { language, chapterSlug, problemId } = useParams();
    const navigate = useNavigate();
    
    const [data, setData] = useState(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState('');

    const [userCode, setUserCode] = useState("# 여기에 코드를 작성하세요.");
    const [executionOutput, setExecutionOutput] = useState(null);
    const [feedback, setFeedback] = useState(null);
    
    const [isPyodideReady, setPyodideReady] = useState(false);
    const pyodide = useRef(null);

    useEffect(() => {
        const loadPyodideInstance = async () => {
            try {
                pyodide.current = await window.loadPyodide();
                setPyodideReady(true);
            } catch(e) { console.error("Pyodide 로딩 실패:", e); }
        };
        loadPyodideInstance();
    }, []);

    const fetchData = useCallback(async () => {
        if (!language || !chapterSlug || !problemId) return;
        setIsLoading(true);
        setError('');
        setFeedback(null);
        setExecutionOutput(null);
        setUserCode("# 여기에 코드를 작성하세요.");
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

    useEffect(() => { fetchData(); }, [fetchData]);

    const handleCheckAnswer = async () => {
        if (!isPyodideReady) return;
        setExecutionOutput("실행 중...");
        setFeedback(null);
        try {
            let stdout = "";
            pyodide.current.setStdout({ batched: (str) => stdout += str + "\n" });
            await pyodide.current.runPythonAsync(userCode);
            setExecutionOutput(stdout.trim() || "(출력 없음)");
        } catch (err) { setExecutionOutput(`에러 발생:\n${err}`); }

        try {
            const formData = new FormData();
            formData.append('user_code', userCode);
            const res = await api.post(`/check-answer/${language}/${chapterSlug}/${problemId}`, formData);
            setFeedback(res.data);
            if (res.data.is_correct) {
                fetchData();
            }
        } catch (error) { console.error(error); }
    };

    if (isLoading) return <div className="loading-message">로딩 중...</div>;
    if (error) return <div className="loading-message">{error}</div>;
    if (!data) return <div className="loading-message">데이터가 없습니다.</div>;

    const { chapter, problem, total_problems, completed_problem_ids } = data;
    const currentProblemNum = parseInt(problemId);
    const isCompleted = completed_problem_ids?.includes(problem.id);

    return (
        <div className="problem-container">
            <aside className="theory-sidebar">
                <div className="theory-header">
                    <h3>💡 핵심 이론</h3>
                    <button onClick={() => setShowTheory(!showTheory)} className="theory-toggle">
                        {showTheory ? '▲' : '▼'}
                    </button>
                </div>
                <div className={`theory-content ${showTheory ? 'open' : ''}`} dangerouslySetInnerHTML={{ __html: problem.theory }} />
            </aside>

            <main className="problem-area">
                <div className="chapter-summary-card">
                    <div className="progress-header">
                        <h3>{chapter.title}</h3>
                        <div className="problem-step-buttons">
                            <Link to={`/${chapterSlug}/${currentProblemNum - 1}`} className={`step-button ${currentProblemNum <= 1 ? 'disabled' : ''}`}>
                                이전 문제
                            </Link>
                            <span className="current-step">{currentProblemNum} / {total_problems}</span>
                            <Link to={`/${chapterSlug}/${currentProblemNum + 1}`} className={`step-button ${currentProblemNum >= total_problems ? 'disabled' : ''}`}>
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
                        <div className="completion-indicator">
                            {isCompleted ? <span className="completed"></span> : <span className="incomplete"></span>}
                        </div>
                    </div>
                    <p className="question">{problem.question}</p>
                </div>

                <div className="content-card">
                    <div className="editor-container">
                        <CodeMirror
                            value={userCode} height="300px" extensions={[python()]}
                            onChange={(value) => setUserCode(value)} theme="light"
                        />
                    </div>
                    <div className="button-area">
                        <button onClick={handleCheckAnswer} disabled={!isPyodideReady}>
                            {!isPyodideReady ? '실행 환경 준비 중...' : '정답 확인하기'}
                        </button>
                    </div>
                </div>

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
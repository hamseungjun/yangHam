import React, { useState, useEffect, useCallback } from 'react';
import { useParams, Link } from 'react-router-dom';
import api from '../api';
import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';
import { javascript } from '@codemirror/lang-javascript';
import { cpp } from '@codemirror/lang-cpp';
import { java } from '@codemirror/lang-java';
import './ProblemPage.css';

const languageExtensions = {
    python: python(),
    javascript: javascript(),
    c: cpp(),
    java: java()
};

const ProblemPage = () => {
    const { language, chapterSlug, problemId } = useParams();
    const [data, setData] = useState(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState('');
    const [userCode, setUserCode] = useState("");
    const [feedback, setFeedback] = useState(null);
    const [isChecking, setIsChecking] = useState(false);
    const [showTheory, setShowTheory] = useState(true);

    const fetchData = useCallback(async () => {
        if (!language || !chapterSlug || !problemId) return;
        setIsLoading(true);
        setError('');
        setFeedback(null);
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

    useEffect(() => {
        fetchData();
    }, [fetchData]);

    const handleCheckAnswer = async () => {
        setIsChecking(true);
        setFeedback(null);

        try {
            const formData = new FormData();
            formData.append('user_code', userCode);
            const res = await api.post(`/check-answer/${language}/${chapterSlug}/${problemId}`, formData);
            
            // execution_output 없이 feedback 상태만 설정합니다.
            setFeedback(res.data);
            
            if (res.data.is_correct) {
                setData(prevData => {
                    const alreadyCompleted = prevData.completed_problem_ids.includes(prevData.problem.id);
                    if (alreadyCompleted) return prevData;
                    return {
                        ...prevData,
                        completed_problem_ids: [...prevData.completed_problem_ids, prevData.problem.id]
                    };
                });
            }
        } catch (error) {
            console.error("API 요청 실패:", error);
            // 에러 발생 시 피드백 창에 메시지를 표시합니다.
            setFeedback({
                is_correct: false,
                feedback: "채점 서버와 통신하는 데 실패했습니다. 잠시 후 다시 시도해주세요."
            });
        } finally {
            setIsChecking(false);
        }
    };

    if (isLoading) return <div className="loading-message">로딩 중...</div>;
    if (error) return <div className="loading-message">{error}</div>;
    if (!data) return <div className="loading-message">데이터를 불러올 수 없습니다.</div>;

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
                            extensions={[languageExtensions[language]]}
                            onChange={(value) => setUserCode(value)}
                            theme="light"
                        />
                    </div>
                    <div className="button-area">
                        <button onClick={handleCheckAnswer} disabled={isChecking}>
                            {isChecking ? '채점 중...' : '정답 확인하기'}
                        </button>
                    </div>
                </div>

                {/* 실행 결과(executionOutput) 섹션이 완전히 제거되었습니다. */}

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
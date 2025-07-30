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
    
    // 다음 문제로 가는 URL을 미리 만들어 둡니다.
    const nextProblemUrl = `/${language}/${chapterSlug}/${currentProblemNum + 1}`;
    const isLastProblem = currentProblemNum >= total_problems;

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
                            <Link to={nextProblemUrl} className={`step-button ${isLastProblem ? 'disabled' : ''}`}>
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
                    
                    {/* --- 이 버튼 영역 전체가 수정되었습니다 --- */}
                    <div className="button-area">
                        {feedback && feedback.is_correct ? (
                            // 정답을 맞혔을 때:
                            isLastProblem ? (
                                // 마지막 문제인 경우
                                <button disabled className="next-problem-btn">챕터 완료!</button>
                            ) : (
                                // 마지막 문제가 아닌 경우
                                <Link to={nextProblemUrl} className="next-problem-btn">
                                    다음 문제로 →
                                </Link>
                            )
                        ) : (
                            // 기본 상태 (채점 전 또는 오답)
                            <button onClick={handleCheckAnswer} disabled={isChecking}>
                                {isChecking ? '채점 중...' : '정답 확인하기'}
                            </button>
                        )}
                    </div>
                    {/* ------------------------------------ */}
                </div>

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
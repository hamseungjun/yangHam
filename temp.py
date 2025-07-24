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
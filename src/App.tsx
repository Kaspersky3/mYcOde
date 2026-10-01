import React, { useState, useEffect } from 'react';
import { UserProgress, Question, CourseDefinition, Abbreviation, KeyNumber, AmbiguityItem, QuestionReport } from './types';
import { loadProgress, saveProgress, recordQuestionResult, recordExamResult, addQuestionReport, DEFAULT_PROGRESS } from './services/storage';

// Data imports
import rawQuestions from './data/questions.json';
import rawCourseContent from './data/courseContent.json';
import rawAmbiguities from './data/ambiguites.json';

// Components
import { PWAInstallButton } from './components/PWAInstallButton';
import { OfflineIndicator } from './components/OfflineIndicator';
import { DailyRoadmap } from './components/DailyRoadmap';
import { ChapterQuizSelector } from './components/ChapterQuizSelector';
import { RevisionSheets } from './components/RevisionSheets';
import { MistakesNotebook } from './components/MistakesNotebook';
import { DashboardView } from './components/DashboardView';
import { QuizPlayer } from './components/QuizPlayer';

// Icons
import { 
  Compass, 
  Layers, 
  Award, 
  BookMarked, 
  BarChart3, 
  Moon, 
  Sun, 
  AlertCircle, 
  Sparkles,
  Flame,
  CheckCircle2,
  Calendar,
  X
} from 'lucide-react';

const questions: Question[] = rawQuestions as unknown as Question[];
const courseContent = rawCourseContent as unknown as {
  abbreviations: Abbreviation[];
  definitions: CourseDefinition[];
  chiffresCles: KeyNumber[];
};
const ambiguites: AmbiguityItem[] = rawAmbiguities as unknown as AmbiguityItem[];

type ActiveTab = 'roadmap' | 'chapters' | 'exam' | 'sheets' | 'mistakes' | 'dashboard';

export default function App() {
  const [progress, setProgress] = useState<UserProgress>(loadProgress);
  const [activeTab, setActiveTab] = useState<ActiveTab>('roadmap');
  const [revisionInitialTab, setRevisionInitialTab] = useState<'attention' | 'traps' | 'numbers' | 'ambiguities'>('attention');
  
  // Active Quiz session state
  const [activeQuizQuestions, setActiveQuizQuestions] = useState<Question[] | null>(null);
  const [activeQuizTitle, setActiveQuizTitle] = useState<string>('');
  const [isExamActive, setIsExamActive] = useState<boolean>(false);

  // Onboarding state
  const [showOnboarding, setShowOnboarding] = useState<boolean>(() => {
    return !localStorage.getItem('code_benin_b_onboarded');
  });

  const isDark = progress.settings.darkMode;

  useEffect(() => {
    if (isDark) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [isDark]);

  const toggleDarkMode = () => {
    const updated = {
      ...progress,
      settings: { ...progress.settings, darkMode: !isDark },
    };
    setProgress(updated);
    saveProgress(updated);
  };

  const handleStartQuiz = (qs: Question[], title: string, isExam = false) => {
    setActiveQuizQuestions(qs);
    setActiveQuizTitle(title);
    setIsExamActive(isExam);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleFinishQuiz = (score: number, total: number, mistakes: number[]) => {
    if (isExamActive) {
      const result = {
        id: `exam-${Date.now()}`,
        date: new Date().toISOString(),
        score,
        total,
        passed: score >= progress.settings.examPassingScore,
        timeSpentSeconds: (progress.settings.examDurationMinutes * 60),
        mistakeQuestionIds: mistakes,
      };
      const updated = recordExamResult(progress, result);
      setProgress(updated);
    }

    // Update day progress if it was day quiz
    if (activeQuizTitle.includes('Jour 1')) {
      const updated = {
        ...progress,
        dayProgress: {
          ...progress.dayProgress,
          1: { ...progress.dayProgress[1], quizDone: true, bestScore: Math.max(progress.dayProgress[1].bestScore, score) }
        }
      };
      setProgress(updated);
      saveProgress(updated);
    } else if (activeQuizTitle.includes('Jour 2')) {
      const updated = {
        ...progress,
        dayProgress: {
          ...progress.dayProgress,
          2: { ...progress.dayProgress[2], quizDone: true, bestScore: Math.max(progress.dayProgress[2].bestScore, score) }
        }
      };
      setProgress(updated);
      saveProgress(updated);
    } else if (activeQuizTitle.includes('Jour 3')) {
      const updated = {
        ...progress,
        dayProgress: {
          ...progress.dayProgress,
          3: { ...progress.dayProgress[3], quizDone: true, bestScore: Math.max(progress.dayProgress[3].bestScore, score) }
        }
      };
      setProgress(updated);
      saveProgress(updated);
    }
  };

  const handleRecordQuestionResult = (questionId: number, isCorrect: boolean) => {
    const updated = recordQuestionResult(progress, questionId, isCorrect);
    setProgress(updated);
  };

  const handleToggleFavorite = (questionId: number) => {
    const exists = progress.favoriteQuestionIds.includes(questionId);
    const updated = {
      ...progress,
      favoriteQuestionIds: exists
        ? progress.favoriteQuestionIds.filter((id) => id !== questionId)
        : [...progress.favoriteQuestionIds, questionId],
    };
    setProgress(updated);
    saveProgress(updated);
  };

  const handleReportQuestion = (report: QuestionReport) => {
    const updated = addQuestionReport(progress, report);
    setProgress(updated);
  };

  const handleStartExamTab = () => {
    // Balanced selection of 40 questions for Category B
    const catB = questions.filter((q) => q.tags.includes('categorie-b'));
    const shuffled = [...catB].sort(() => 0.5 - Math.random()).slice(0, progress.settings.examQuestionsCount);
    handleStartQuiz(shuffled, "Examen Blanc Officiel DGTT", true);
  };

  const dismissOnboarding = (date?: string) => {
    localStorage.setItem('code_benin_b_onboarded', 'true');
    setShowOnboarding(false);
    if (date) {
      const updated = { ...progress, targetExamDate: date };
      setProgress(updated);
      saveProgress(updated);
    }
  };

  return (
    <div className="min-h-screen bg-slate-100 dark:bg-slate-950 text-slate-900 dark:text-slate-100 flex flex-col font-sans antialiased selection:bg-emerald-500 selection:text-white">
      {/* Top Main Navigation Header */}
      <header className="sticky top-0 z-40 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 shadow-sm">
        <div className="max-w-2xl mx-auto px-4 h-16 flex items-center justify-between gap-3">
          {/* Logo & Brand */}
          <div 
            onClick={() => {
              setActiveQuizQuestions(null);
              setActiveTab('roadmap');
            }} 
            className="flex items-center gap-2.5 cursor-pointer select-none"
          >
            <div className="w-10 h-10 rounded-2xl bg-gradient-to-br from-emerald-700 to-emerald-900 text-white flex items-center justify-center shadow-md border border-emerald-500/30">
              <span className="font-black text-xl tracking-tighter">B</span>
            </div>
            <div>
              <div className="flex items-center gap-1.5">
                <h1 className="font-black text-base tracking-tight leading-none text-slate-900 dark:text-white">
                  Code Bénin B
                </h1>
                <span className="text-[10px] font-black px-1.5 py-0.5 rounded bg-amber-400 text-slate-950 uppercase">
                  3 Jours
                </span>
              </div>
              <p className="text-[10px] text-slate-400 font-medium leading-tight">
                Manuel Officiel DGTT 2011
              </p>
            </div>
          </div>

          {/* Right Action Icons */}
          <div className="flex items-center gap-2">
            <PWAInstallButton />
            
            <button
              onClick={toggleDarkMode}
              className="p-2 rounded-xl text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800 transition"
              title="Basculer le mode sombre"
            >
              {isDark ? <Sun className="w-4 h-4 text-amber-400" /> : <Moon className="w-4 h-4" />}
            </button>
          </div>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 max-w-2xl w-full mx-auto p-4 md:p-6">
        {activeQuizQuestions ? (
          <QuizPlayer
            questions={activeQuizQuestions}
            title={activeQuizTitle}
            isExamMode={isExamActive}
            timeLimitMinutes={progress.settings.examDurationMinutes}
            passingScore={progress.settings.examPassingScore}
            onFinish={handleFinishQuiz}
            onExit={() => setActiveQuizQuestions(null)}
            onRecordQuestionResult={handleRecordQuestionResult}
            favorites={progress.favoriteQuestionIds}
            onToggleFavorite={handleToggleFavorite}
            onReportQuestion={handleReportQuestion}
          />
        ) : (
          <>
            {activeTab === 'roadmap' && (
              <DailyRoadmap
                progress={progress}
                questions={questions}
                onStartQuiz={handleStartQuiz}
                onOpenRevisionTab={(tab) => {
                  setRevisionInitialTab(tab);
                  setActiveTab('sheets');
                }}
                onChangeDay={(day) => {
                  const updated = { ...progress, currentDay: day };
                  setProgress(updated);
                  saveProgress(updated);
                }}
              />
            )}

            {activeTab === 'chapters' && (
              <ChapterQuizSelector
                questions={questions}
                completedQuestionIds={progress.completedQuestionIds}
                onStartQuiz={handleStartQuiz}
                showOtherCategories={progress.settings.showOtherCategories}
                onToggleOtherCategories={(show) => {
                  const updated = {
                    ...progress,
                    settings: { ...progress.settings, showOtherCategories: show },
                  };
                  setProgress(updated);
                  saveProgress(updated);
                }}
              />
            )}

            {activeTab === 'exam' && (
              <div className="space-y-6 animate-fade-in pb-16">
                <div className="bg-gradient-to-br from-slate-900 via-emerald-950 to-slate-900 text-white p-6 rounded-3xl shadow-xl border border-emerald-600/40 relative overflow-hidden">
                  <div className="relative z-10 space-y-4">
                    <span className="text-[10px] font-extrabold uppercase tracking-wider bg-emerald-500/20 text-emerald-300 px-3 py-1 rounded-full border border-emerald-400/30 inline-flex items-center gap-1.5">
                      <Award className="w-3.5 h-3.5" />
                      Conditions Réelles de l'Épreuve
                    </span>
                    <h2 className="text-2xl font-black">Simulation d'Examen Blanc</h2>
                    <p className="text-xs text-slate-300 leading-relaxed max-w-md">
                      Évaluez-vous dans les mêmes conditions que le centre d'examen DGTT : {progress.settings.examQuestionsCount} questions tirées au sort, temps limité à {progress.settings.examDurationMinutes} minutes, sans correction immédiate.
                    </p>

                    <div className="grid grid-cols-2 gap-2 text-xs">
                      <div className="bg-white/10 backdrop-blur-md p-3 rounded-2xl border border-white/10">
                        <span className="text-emerald-300 text-[10px] font-bold">NOMBRE DE QUESTIONS</span>
                        <p className="text-xl font-black mt-0.5">{progress.settings.examQuestionsCount} questions</p>
                      </div>
                      <div className="bg-white/10 backdrop-blur-md p-3 rounded-2xl border border-white/10">
                        <span className="text-emerald-300 text-[10px] font-bold">SEUIL D'ADMISSIBILITÉ</span>
                        <p className="text-xl font-black mt-0.5">{progress.settings.examPassingScore} / {progress.settings.examQuestionsCount}</p>
                      </div>
                    </div>

                    <button
                      onClick={handleStartExamTab}
                      className="w-full py-4 rounded-2xl bg-gradient-to-r from-emerald-500 to-teal-400 hover:from-emerald-400 hover:to-teal-300 text-slate-950 font-black text-base shadow-lg transition active:scale-95 flex items-center justify-center gap-2 cursor-pointer"
                    >
                      <Award className="w-5 h-5" />
                      <span>Commencer l'Épreuve Chronométrée</span>
                    </button>
                  </div>
                </div>

                {/* Exam Tips */}
                <div className="bg-white dark:bg-slate-900 p-5 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-sm space-y-3 text-xs">
                  <h4 className="font-extrabold text-sm text-slate-900 dark:text-white flex items-center gap-2">
                    <Sparkles className="w-4 h-4 text-emerald-600" />
                    Conseils pour réussir le jour J
                  </h4>
                  <ul className="space-y-2 text-slate-600 dark:text-slate-300 leading-relaxed">
                    <li className="flex items-start gap-2">
                      <span className="text-emerald-600 font-bold">•</span>
                      <span>Lisez attentivement l'énoncé : vérifiez s'il s'agit d'une question à <strong>réponse unique</strong> ou à <strong>réponses multiples</strong>.</span>
                    </li>
                    <li className="flex items-start gap-2">
                      <span className="text-emerald-600 font-bold">•</span>
                      <span>Aux carrefours sans panneau, cherchez toujours si un véhicule a sa droite libre avant de déterminer l'ordre.</span>
                    </li>
                    <li className="flex items-start gap-2">
                      <span className="text-emerald-600 font-bold">•</span>
                      <span>Rappelez-vous que les <strong>gestes de l'agent priment toujours</strong> sur les feux et les panneaux.</span>
                    </li>
                  </ul>
                </div>
              </div>
            )}

            {activeTab === 'sheets' && (
              <RevisionSheets
                initialTab={revisionInitialTab}
                courseContent={courseContent}
                ambiguites={ambiguites}
                questions={questions}
                onStartQuizWithQuestions={(qs, title) => handleStartQuiz(qs, title)}
              />
            )}

            {activeTab === 'mistakes' && (
              <MistakesNotebook
                progress={progress}
                questions={questions}
                onStartQuiz={handleStartQuiz}
              />
            )}

            {activeTab === 'dashboard' && (
              <DashboardView
                progress={progress}
                questions={questions}
                onUpdateProgress={(p) => {
                  setProgress(p);
                  saveProgress(p);
                }}
                onResetProgress={() => {
                  setProgress(DEFAULT_PROGRESS);
                  saveProgress(DEFAULT_PROGRESS);
                }}
              />
            )}
          </>
        )}
      </main>

      {/* Offline Toast */}
      <OfflineIndicator />

      {/* Bottom Sticky Mobile Navigation Tabs */}
      {!activeQuizQuestions && (
        <nav className="sticky bottom-0 z-40 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-t border-slate-200 dark:border-slate-800 shadow-lg">
          <div className="max-w-2xl mx-auto px-2 h-16 flex items-center justify-around">
            <button
              onClick={() => setActiveTab('roadmap')}
              className={`flex-1 py-1 flex flex-col items-center justify-center gap-1 transition ${
                activeTab === 'roadmap'
                  ? 'text-emerald-700 dark:text-emerald-400 font-black scale-105'
                  : 'text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-white font-medium'
              }`}
            >
              <Compass className="w-5 h-5" />
              <span className="text-[10px]">3 Jours</span>
            </button>

            <button
              onClick={() => setActiveTab('chapters')}
              className={`flex-1 py-1 flex flex-col items-center justify-center gap-1 transition ${
                activeTab === 'chapters'
                  ? 'text-emerald-700 dark:text-emerald-400 font-black scale-105'
                  : 'text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-white font-medium'
              }`}
            >
              <Layers className="w-5 h-5" />
              <span className="text-[10px]">Quiz</span>
            </button>

            <button
              onClick={() => setActiveTab('exam')}
              className={`flex-1 py-1 flex flex-col items-center justify-center gap-1 transition ${
                activeTab === 'exam'
                  ? 'text-emerald-700 dark:text-emerald-400 font-black scale-105'
                  : 'text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-white font-medium'
              }`}
            >
              <div className="relative">
                <Award className="w-5 h-5" />
                <span className="absolute -top-1 -right-1 w-2 h-2 rounded-full bg-emerald-500" />
              </div>
              <span className="text-[10px]">Examen</span>
            </button>

            <button
              onClick={() => setActiveTab('sheets')}
              className={`flex-1 py-1 flex flex-col items-center justify-center gap-1 transition ${
                activeTab === 'sheets'
                  ? 'text-emerald-700 dark:text-emerald-400 font-black scale-105'
                  : 'text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-white font-medium'
              }`}
            >
              <BookMarked className="w-5 h-5" />
              <span className="text-[10px]">Fiches</span>
            </button>

            <button
              onClick={() => setActiveTab('mistakes')}
              className={`flex-1 py-1 flex flex-col items-center justify-center gap-1 transition ${
                activeTab === 'mistakes'
                  ? 'text-rose-600 dark:text-rose-400 font-black scale-105'
                  : 'text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-white font-medium'
              }`}
            >
              <div className="relative">
                <AlertCircle className="w-5 h-5" />
                {progress.mistakeHistory.length > 0 && (
                  <span className="absolute -top-1 -right-2 px-1 py-0.2 rounded-full bg-rose-600 text-white text-[9px] font-bold">
                    {progress.mistakeHistory.length}
                  </span>
                )}
              </div>
              <span className="text-[10px]">Erreurs</span>
            </button>

            <button
              onClick={() => setActiveTab('dashboard')}
              className={`flex-1 py-1 flex flex-col items-center justify-center gap-1 transition ${
                activeTab === 'dashboard'
                  ? 'text-emerald-700 dark:text-emerald-400 font-black scale-105'
                  : 'text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-white font-medium'
              }`}
            >
              <BarChart3 className="w-5 h-5" />
              <span className="text-[10px]">Suivi</span>
            </button>
          </div>
        </nav>
      )}

      {/* Onboarding Welcome Modal */}
      {showOnboarding && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 p-4 backdrop-blur-sm animate-fade-in">
          <div className="w-full max-w-sm rounded-3xl bg-white dark:bg-slate-900 p-6 shadow-2xl border border-slate-200 dark:border-slate-800 space-y-4">
            <div className="text-center space-y-2">
              <div className="w-14 h-14 mx-auto rounded-3xl bg-emerald-600 text-white flex items-center justify-center shadow-lg font-black text-2xl">
                B
              </div>
              <h3 className="text-xl font-black text-slate-900 dark:text-white">
                Bienvenue sur Code Bénin B
              </h3>
              <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                Préparez et réussissez l'épreuve théorique du permis de conduire catégorie B en <strong>3 jours</strong>, avec les <strong>questions officielles de la DGTT (Édition 2011)</strong>.
              </p>
            </div>

            <div className="space-y-2.5 text-xs text-slate-700 dark:text-slate-300">
              <div className="flex items-center gap-2 p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-100 dark:border-slate-800">
                <CheckCircle2 className="w-4 h-4 text-emerald-600 flex-shrink-0" />
                <span><strong>Jour 1 :</strong> Signalisation (panneaux, feux, agents)</span>
              </div>
              <div className="flex items-center gap-2 p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-100 dark:border-slate-800">
                <CheckCircle2 className="w-4 h-4 text-emerald-600 flex-shrink-0" />
                <span><strong>Jour 2 :</strong> Règles de circulation & carrefours</span>
              </div>
              <div className="flex items-center gap-2 p-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-100 dark:border-slate-800">
                <CheckCircle2 className="w-4 h-4 text-emerald-600 flex-shrink-0" />
                <span><strong>Jour 3 :</strong> Sécurité, secourisme & examens blancs</span>
              </div>
            </div>

            <div className="pt-2 space-y-2">
              <button
                onClick={() => dismissOnboarding()}
                className="w-full py-3 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-sm shadow-md transition"
              >
                Commencer ma préparation !
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

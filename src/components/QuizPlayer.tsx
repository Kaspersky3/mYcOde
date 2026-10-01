import React, { useState, useEffect } from 'react';
import { Question } from '../types';
import { TrafficSign } from './TrafficSign';
import { ReportModal } from './ReportModal';
import { 
  CheckCircle, 
  XCircle, 
  Clock, 
  ChevronRight, 
  ChevronLeft, 
  RotateCcw, 
  Bookmark, 
  BookmarkCheck, 
  AlertCircle, 
  HelpCircle,
  Flag,
  Share2,
  BookOpen,
  Copy,
  Check
} from 'lucide-react';

interface QuizPlayerProps {
  questions: Question[];
  title: string;
  isExamMode?: boolean;
  timeLimitMinutes?: number;
  passingScore?: number;
  onFinish: (score: number, total: number, mistakes: number[]) => void;
  onExit: () => void;
  onRecordQuestionResult?: (questionId: number, isCorrect: boolean) => void;
  favorites?: number[];
  onToggleFavorite?: (questionId: number) => void;
  onReportQuestion?: (report: any) => void;
}

export const QuizPlayer: React.FC<QuizPlayerProps> = ({
  questions,
  title,
  isExamMode = false,
  timeLimitMinutes = 30,
  passingScore = 35,
  onFinish,
  onExit,
  onRecordQuestionResult,
  favorites = [],
  onToggleFavorite,
  onReportQuestion,
}) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState<Record<number, string[]>>({});
  const [isAnswerSubmitted, setIsAnswerSubmitted] = useState<Record<number, boolean>>({});
  const [timeLeft, setTimeLeft] = useState(timeLimitMinutes * 60);
  const [isFinished, setIsFinished] = useState(false);
  const [copiedShare, setCopiedShare] = useState(false);
  const [reportingQuestion, setReportingQuestion] = useState<Question | null>(null);
  const [showConfirmFinish, setShowConfirmFinish] = useState(false);

  const currentQ = questions[currentIndex];
  const currentSelections = selectedAnswers[currentQ?.numero] || [];
  const currentSubmitted = isAnswerSubmitted[currentQ?.numero] || false;

  // Countdown timer for Exam mode
  useEffect(() => {
    if (!isExamMode || isFinished) return;
    const interval = setInterval(() => {
      setTimeLeft((prev) => {
        if (prev <= 1) {
          clearInterval(interval);
          handleFinishQuiz();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(interval);
  }, [isExamMode, isFinished]);

  if (!currentQ && !isFinished) {
    return (
      <div className="p-8 text-center bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800">
        <p className="text-slate-600 dark:text-slate-400">Aucune question disponible pour ce module.</p>
        <button onClick={onExit} className="mt-4 px-4 py-2 bg-emerald-600 text-white rounded-xl text-sm font-semibold">
          Retour
        </button>
      </div>
    );
  }

  const handleSelectOption = (optId: string) => {
    if (currentSubmitted && !isExamMode) return; // locked in training once verified

    if (currentQ.multiReponses) {
      const exists = currentSelections.includes(optId);
      const next = exists
        ? currentSelections.filter((id) => id !== optId)
        : [...currentSelections, optId].sort();
      setSelectedAnswers((prev) => ({ ...prev, [currentQ.numero]: next }));
    } else {
      setSelectedAnswers((prev) => ({ ...prev, [currentQ.numero]: [optId] }));
      // Optional subtle haptic
      if (typeof navigator !== 'undefined' && navigator.vibrate) {
        navigator.vibrate(15);
      }
    }
  };

  const handleValidateAnswer = () => {
    if (currentSelections.length === 0) return;
    
    setIsAnswerSubmitted((prev) => ({ ...prev, [currentQ.numero]: true }));

    // Verify correctness
    const isCorrect =
      currentSelections.length === currentQ.bonnesReponses.length &&
      currentSelections.every((r) => currentQ.bonnesReponses.includes(r));

    if (onRecordQuestionResult) {
      onRecordQuestionResult(currentQ.numero, isCorrect);
    }

    if (typeof navigator !== 'undefined' && navigator.vibrate) {
      navigator.vibrate(isCorrect ? 30 : [50, 50, 50]);
    }
  };

  const handleFinishQuiz = () => {
    let score = 0;
    const mistakes: number[] = [];

    questions.forEach((q) => {
      const ans = selectedAnswers[q.numero] || [];
      const isCorrect =
        ans.length === q.bonnesReponses.length &&
        ans.every((r) => q.bonnesReponses.includes(r));

      if (isCorrect) {
        score += 1;
      } else {
        mistakes.push(q.numero);
      }

      if (onRecordQuestionResult) {
        onRecordQuestionResult(q.numero, isCorrect);
      }
    });

    setIsFinished(true);
    onFinish(score, questions.length, mistakes);
  };

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
  };

  // Check state for review screen
  if (isFinished) {
    let score = 0;
    const mistakes: Question[] = [];
    questions.forEach((q) => {
      const ans = selectedAnswers[q.numero] || [];
      const isCorrect =
        ans.length === q.bonnesReponses.length &&
        ans.every((r) => q.bonnesReponses.includes(r));
      if (isCorrect) score += 1;
      else mistakes.push(q);
    });

    const isPassed = isExamMode ? score >= passingScore : (score / questions.length) >= 0.75;
    const percentage = Math.round((score / questions.length) * 100);

    return (
      <div className="w-full max-w-xl mx-auto space-y-5 animate-fade-in pb-16">
        {/* Score banner */}
        <div className={`p-6 rounded-3xl text-center shadow-lg border ${
          isPassed 
            ? 'bg-gradient-to-b from-emerald-600 to-emerald-800 text-white border-emerald-500' 
            : 'bg-gradient-to-b from-rose-600 to-rose-800 text-white border-rose-500'
        }`}>
          <div className="w-16 h-16 mx-auto mb-3 rounded-full bg-white/20 backdrop-blur-md flex items-center justify-center">
            {isPassed ? <CheckCircle className="w-10 h-10 text-white" /> : <AlertCircle className="w-10 h-10 text-white" />}
          </div>
          <span className="text-xs uppercase tracking-wider font-extrabold text-emerald-200">
            {isExamMode ? "Simulation Officielle DGTT" : "Bilan de la Session"}
          </span>
          <h2 className="text-3xl font-black mt-1">
            {isPassed ? (isExamMode ? "FÉLICITATIONS ! ADMIS" : "EXCELLENT TRAVAIL !") : (isExamMode ? "AJOURNÉ" : "ENCORE UN EFFORT !")}
          </h2>
          <p className="text-4xl font-extrabold my-3 tracking-tight">
            {score} <span className="text-xl font-normal opacity-80">/ {questions.length}</span>
          </p>
          <p className="text-sm text-emerald-100 max-w-sm mx-auto">
            {isExamMode
              ? isPassed
                ? `Vous avez dépassé le seuil de réussite fixé à ${passingScore}/${questions.length}. Vous êtes sur la bonne voie pour le permis !`
                : `Le seuil d'admissibilité est de ${passingScore}/${questions.length}. Analysez vos erreurs ci-dessous et recommencez.`
              : `Taux de réussite : ${percentage}%. Répétez régulièrement pour ancrer les règles dans votre mémoire.`}
          </p>

          <div className="flex flex-wrap justify-center gap-2 mt-5">
            <a
              href={`https://api.whatsapp.com/send?text=${encodeURIComponent(
                `🚗 J'ai obtenu ${score}/${questions.length} (${percentage}%) sur Code Bénin B ! Prêt pour le permis B au Bénin en 3 jours ! 🇧🇯`
              )}`}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-white text-slate-900 font-bold text-sm shadow hover:bg-slate-50 transition cursor-pointer"
            >
              <Share2 className="w-4 h-4 text-emerald-700" />
              <span>Partager sur WhatsApp</span>
            </a>
            <button
              onClick={() => {
                navigator.clipboard?.writeText(
                  `🚗 J'ai obtenu ${score}/${questions.length} (${percentage}%) sur Code Bénin B ! Prêt pour le permis B au Bénin en 3 jours ! 🇧🇯`
                );
                setCopiedShare(true);
                setTimeout(() => setCopiedShare(false), 2500);
              }}
              className="flex items-center gap-2 px-4 py-2.5 rounded-xl bg-white/20 hover:bg-white/30 text-white font-bold text-sm transition cursor-pointer"
            >
              {copiedShare ? <Check className="w-4 h-4 text-emerald-300" /> : <Copy className="w-4 h-4" />}
              <span>{copiedShare ? 'Copié !' : 'Copier'}</span>
            </button>
            <button
              onClick={onExit}
              className="px-5 py-2.5 rounded-xl bg-white/20 hover:bg-white/30 text-white font-semibold text-sm transition cursor-pointer"
            >
              Terminer
            </button>
          </div>
        </div>

        {/* Breakdown of questions */}
        <div className="bg-white dark:bg-slate-900 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 shadow-sm space-y-4">
          <div className="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-slate-800">
            <h3 className="font-bold text-slate-900 dark:text-white flex items-center gap-2 text-sm">
              <BookOpen className="w-4 h-4 text-emerald-600" />
              Détail des réponses ({mistakes.length} faute{mistakes.length > 1 ? 's' : ''})
            </h3>
            <span className="text-xs font-semibold px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400">
              {questions.length} questions
            </span>
          </div>

          <div className="space-y-4">
            {questions.map((q, idx) => {
              const ans = selectedAnswers[q.numero] || [];
              const isCorrect =
                ans.length === q.bonnesReponses.length &&
                ans.every((r) => q.bonnesReponses.includes(r));

              return (
                <div
                  key={q.id}
                  className={`p-4 rounded-xl border text-sm transition ${
                    isCorrect
                      ? 'border-emerald-200 dark:border-emerald-950/70 bg-emerald-50/40 dark:bg-emerald-950/20'
                      : 'border-rose-200 dark:border-rose-950/70 bg-rose-50/40 dark:bg-rose-950/20'
                  }`}
                >
                  <div className="flex items-start justify-between gap-3 mb-2">
                    <span className="text-xs font-extrabold px-2 py-0.5 rounded bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-300 shadow-sm">
                      Question n°{q.numero}
                    </span>
                    <span className={`text-xs font-bold flex items-center gap-1 ${
                      isCorrect ? 'text-emerald-700 dark:text-emerald-400' : 'text-rose-600 dark:text-rose-400'
                    }`}>
                      {isCorrect ? (
                        <>
                          <CheckCircle className="w-4 h-4" /> Correct
                        </>
                      ) : (
                        <>
                          <XCircle className="w-4 h-4" /> Erreur
                        </>
                      )}
                    </span>
                  </div>

                  <p className="font-semibold text-slate-900 dark:text-white mb-2">{q.enonce}</p>

                  {q.image && (
                    <div className="my-2 flex justify-start">
                      <TrafficSign code={q.image} />
                    </div>
                  )}

                  <div className="space-y-1.5 my-2">
                    {q.options.map((opt) => {
                      const wasSelected = ans.includes(opt.id);
                      const isGood = q.bonnesReponses.includes(opt.id);
                      return (
                        <div
                          key={opt.id}
                          className={`flex items-center gap-2 p-2 rounded-lg text-xs font-medium ${
                            isGood
                              ? 'bg-emerald-100 text-emerald-950 dark:bg-emerald-900/40 dark:text-emerald-200 font-bold border border-emerald-300 dark:border-emerald-700'
                              : wasSelected
                              ? 'bg-rose-100 text-rose-900 dark:bg-rose-900/40 dark:text-rose-200 line-through'
                              : 'text-slate-600 dark:text-slate-400'
                          }`}
                        >
                          <span className="w-5 h-5 rounded-full bg-white/70 dark:bg-slate-800 flex items-center justify-center font-bold text-[10px]">
                            {opt.id.toUpperCase()}
                          </span>
                          <span>{opt.texte}</span>
                          {isGood && <span className="ml-auto text-[10px] text-emerald-700 dark:text-emerald-400 font-bold">✓ Bonne réponse</span>}
                          {wasSelected && !isGood && <span className="ml-auto text-[10px] text-rose-600 font-bold">✗ Votre choix</span>}
                        </div>
                      );
                    })}
                  </div>

                  {q.explication && (
                    <div className="mt-2 text-xs bg-white dark:bg-slate-800 p-2.5 rounded-lg border border-slate-200/80 dark:border-slate-700 text-slate-700 dark:text-slate-300">
                      <span className="font-bold text-emerald-700 dark:text-emerald-400">Règle DGTT : </span>
                      {q.explication}
                    </div>
                  )}
                  <p className="mt-1.5 text-[10px] text-slate-400">
                    Manuel officiel DGTT 2011 — Chapitre {q.chapitre}, Page {q.page}
                  </p>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    );
  }

  // Active Question view
  const isFavorite = favorites.includes(currentQ.numero);
  const isCorrect =
    currentSelections.length === currentQ.bonnesReponses.length &&
    currentSelections.every((r) => currentQ.bonnesReponses.includes(r));

  return (
    <div className="w-full max-w-xl mx-auto space-y-4 pb-20 animate-fade-in">
      {/* Top Header bar */}
      <div className="flex items-center justify-between gap-2 px-1">
        <button
          onClick={onExit}
          className="text-xs font-semibold text-slate-500 hover:text-slate-800 dark:hover:text-white px-2 py-1.5 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition"
        >
          ← Quitter
        </button>

        <div className="flex items-center gap-2">
          {isExamMode && (
            <div className={`flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold border shadow-sm ${
              timeLeft < 300 
                ? 'bg-rose-50 text-rose-700 border-rose-300 animate-pulse' 
                : 'bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200 border-slate-200 dark:border-slate-700'
            }`}>
              <Clock className="w-3.5 h-3.5" />
              <span>{formatTime(timeLeft)}</span>
            </div>
          )}

          <span className="text-xs font-bold px-2.5 py-1 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
            {currentIndex + 1} / {questions.length}
          </span>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="w-full h-2 rounded-full bg-slate-100 dark:bg-slate-800 overflow-hidden">
        <div
          className="h-full bg-emerald-600 transition-all duration-300 rounded-full"
          style={{ width: `${((currentIndex + 1) / questions.length) * 100}%` }}
        />
      </div>

      {/* Main Question Card */}
      <div className="bg-white dark:bg-slate-900 rounded-3xl p-5 md:p-6 shadow-sm border border-slate-200 dark:border-slate-800 relative">
        {/* Badges & Actions */}
        <div className="flex items-center justify-between gap-2 mb-3">
          <div className="flex flex-wrap items-center gap-1.5">
            <span className="px-2.5 py-0.5 rounded-md bg-emerald-100 dark:bg-emerald-950/80 text-emerald-800 dark:text-emerald-300 font-extrabold text-xs">
              Question n°{currentQ.numero}
            </span>
            {currentQ.multiReponses ? (
              <span className="px-2 py-0.5 rounded-md bg-amber-100 dark:bg-amber-950/80 text-amber-900 dark:text-amber-300 font-bold text-xs flex items-center gap-1">
                <span>☑️</span> Plusieurs réponses possibles
              </span>
            ) : (
              <span className="px-2 py-0.5 rounded-md bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 font-medium text-xs">
                Une seule réponse
              </span>
            )}
            {currentQ.tags.includes('piege') && (
              <span className="px-2 py-0.5 rounded-md bg-rose-100 dark:bg-rose-950/80 text-rose-800 dark:text-rose-300 font-bold text-xs">
                ⚠️ Piège
              </span>
            )}
            {currentQ.tags.includes('ambiguite') && (
              <span className="px-2 py-0.5 rounded-md bg-purple-100 dark:bg-purple-950/80 text-purple-800 dark:text-purple-300 font-bold text-xs">
                🔍 Ambiguïté DGTT
              </span>
            )}
          </div>

          <div className="flex items-center gap-1">
            {onToggleFavorite && (
              <button
                onClick={() => onToggleFavorite(currentQ.numero)}
                className="p-2 rounded-xl text-slate-400 hover:text-amber-500 hover:bg-slate-50 dark:hover:bg-slate-800 transition"
                title={isFavorite ? "Retirer des favoris" : "Ajouter aux favoris"}
              >
                {isFavorite ? (
                  <BookmarkCheck className="w-5 h-5 text-amber-500 fill-amber-500" />
                ) : (
                  <Bookmark className="w-5 h-5" />
                )}
              </button>
            )}
            <button
              onClick={() => setReportingQuestion(currentQ)}
              className="p-2 rounded-xl text-slate-400 hover:text-rose-500 hover:bg-slate-50 dark:hover:bg-slate-800 transition"
              title="Signaler cette question"
            >
              <Flag className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Question Text */}
        <h2 className="text-base md:text-lg font-bold text-slate-900 dark:text-white leading-snug">
          {currentQ.enonce}
        </h2>

        {/* Traffic Sign / Schema Image */}
        {currentQ.image && (
          <div className="my-4 flex flex-col items-center justify-center p-3 rounded-2xl bg-slate-50 dark:bg-slate-800/40 border border-slate-100 dark:border-slate-800">
            <TrafficSign code={currentQ.image} />
          </div>
        )}

        {/* Options List */}
        <div className="mt-5 space-y-2.5">
          {currentQ.options.map((opt) => {
            const isSelected = currentSelections.includes(opt.id);
            const isGoodAnswer = currentQ.bonnesReponses.includes(opt.id);

            // In training mode when submitted, highlight correct/incorrect
            let optionStyles = 'border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800/80 text-slate-800 dark:text-slate-200 hover:border-emerald-300';
            let circleStyles = 'border-slate-300 dark:border-slate-600 text-slate-600 dark:text-slate-400';

            if (isSelected) {
              optionStyles = 'border-emerald-600 bg-emerald-50/60 dark:bg-emerald-950/40 text-emerald-950 dark:text-emerald-100 ring-1 ring-emerald-500 font-semibold';
              circleStyles = 'bg-emerald-600 text-white border-emerald-600';
            }

            if (!isExamMode && currentSubmitted) {
              if (isGoodAnswer) {
                optionStyles = 'border-emerald-500 bg-emerald-100/80 dark:bg-emerald-950/60 text-emerald-950 dark:text-emerald-100 font-bold ring-2 ring-emerald-500';
                circleStyles = 'bg-emerald-600 text-white border-emerald-600';
              } else if (isSelected && !isGoodAnswer) {
                optionStyles = 'border-rose-400 bg-rose-50/80 dark:bg-rose-950/50 text-rose-950 dark:text-rose-200 line-through';
                circleStyles = 'bg-rose-600 text-white border-rose-600';
              }
            }

            return (
              <button
                key={opt.id}
                type="button"
                onClick={() => handleSelectOption(opt.id)}
                className={`w-full min-h-[52px] p-3.5 rounded-2xl border text-left flex items-start gap-3 transition cursor-pointer active:scale-[0.99] select-none ${optionStyles}`}
              >
                <div
                  className={`flex-shrink-0 w-7 h-7 rounded-xl border flex items-center justify-center font-bold text-xs transition ${circleStyles}`}
                >
                  {opt.id.toUpperCase()}
                </div>
                <span className="text-sm md:text-base leading-relaxed pt-0.5">{opt.texte}</span>
              </button>
            );
          })}
        </div>

        {/* Instant explanation card in training mode */}
        {!isExamMode && currentSubmitted && (
          <div className="mt-5 p-4 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-700 space-y-2 animate-fade-in">
            <div className="flex items-center gap-2">
              {isCorrect ? (
                <div className="flex items-center gap-1.5 text-emerald-600 dark:text-emerald-400 font-bold text-sm">
                  <CheckCircle className="w-5 h-5" />
                  <span>Excellente réponse !</span>
                </div>
              ) : (
                <div className="flex items-center gap-1.5 text-rose-600 dark:text-rose-400 font-bold text-sm">
                  <XCircle className="w-5 h-5" />
                  <span>Mauvaise réponse.</span>
                </div>
              )}
            </div>

            <p className="text-xs text-slate-700 dark:text-slate-300 font-medium">
              Bonne{currentQ.bonnesReponses.length > 1 ? 's' : ''} réponse{currentQ.bonnesReponses.length > 1 ? 's' : ''} du manuel officiel :{' '}
              <strong className="text-emerald-700 dark:text-emerald-300 uppercase">
                {currentQ.bonnesReponses.join(', ')}
              </strong>
            </p>

            {currentQ.explication && (
              <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed pt-1 border-t border-slate-200 dark:border-slate-700">
                💡 <span className="font-semibold text-slate-800 dark:text-slate-200">Explication : </span>
                {currentQ.explication}
              </p>
            )}

            <p className="text-[11px] text-slate-400 dark:text-slate-500 pt-1">
              Source : Manuel DGTT 2011 — Chapitre {currentQ.chapitre}, Page {currentQ.page}
            </p>
          </div>
        )}
      </div>

      {/* Bottom Action Footer */}
      <div className="flex items-center justify-between gap-3 pt-2">
        <button
          onClick={() => setCurrentIndex((i) => Math.max(0, i - 1))}
          disabled={currentIndex === 0}
          className="flex items-center gap-1 px-4 py-3 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 text-sm font-semibold disabled:opacity-30 transition"
        >
          <ChevronLeft className="w-4 h-4" />
          <span>Précédent</span>
        </button>

        {!isExamMode ? (
          !currentSubmitted ? (
            <button
              onClick={handleValidateAnswer}
              disabled={currentSelections.length === 0}
              className="flex-1 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-700 active:bg-emerald-800 text-white font-bold text-sm shadow-md transition disabled:opacity-40 disabled:pointer-events-none"
            >
              Valider
            </button>
          ) : currentIndex < questions.length - 1 ? (
            <button
              onClick={() => setCurrentIndex((i) => i + 1)}
              className="flex-1 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-sm shadow-md flex items-center justify-center gap-1 transition"
            >
              <span>Question Suivante</span>
              <ChevronRight className="w-4 h-4" />
            </button>
          ) : (
            <button
              onClick={handleFinishQuiz}
              className="flex-1 py-3 rounded-xl bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm shadow-lg transition"
            >
              Voir mon Bilan
            </button>
          )
        ) : (
          currentIndex < questions.length - 1 ? (
            <button
              onClick={() => setCurrentIndex((i) => i + 1)}
              className="flex-1 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-sm shadow transition flex items-center justify-center gap-1"
            >
              <span>Suivante</span>
              <ChevronRight className="w-4 h-4" />
            </button>
          ) : (
            <button
              onClick={() => setShowConfirmFinish(true)}
              className="flex-1 py-3 rounded-xl bg-emerald-700 hover:bg-emerald-800 text-white font-extrabold text-sm shadow-lg transition"
            >
              Terminer l'Examen
            </button>
          )
        )}

        {isExamMode && (
          <button
            onClick={() => setShowConfirmFinish(true)}
            className="px-3.5 py-3 rounded-xl border border-rose-300 dark:border-rose-900 bg-rose-50 dark:bg-rose-950/40 text-rose-700 dark:text-rose-300 text-xs font-bold transition"
          >
            Rendre
          </button>
        )}
      </div>

      {/* Exam Navigation Quick Grid */}
      {isExamMode && (
        <div className="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800">
          <p className="text-xs font-bold text-slate-600 dark:text-slate-400 mb-2">
            Grille des questions ({Object.keys(selectedAnswers).length}/{questions.length} répondues) :
          </p>
          <div className="grid grid-cols-8 sm:grid-cols-10 gap-1.5">
            {questions.map((q, idx) => {
              const isAnswered = (selectedAnswers[q.numero] || []).length > 0;
              const isCurr = idx === currentIndex;
              return (
                <button
                  key={q.id}
                  onClick={() => setCurrentIndex(idx)}
                  className={`h-8 rounded-lg text-xs font-bold transition ${
                    isCurr
                      ? 'ring-2 ring-emerald-500 bg-emerald-600 text-white'
                      : isAnswered
                      ? 'bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-300'
                      : 'bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-400'
                  }`}
                >
                  {idx + 1}
                </button>
              );
            })}
          </div>
        </div>
      )}

      {/* Confirmation Modal before finishing exam */}
      {showConfirmFinish && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4 backdrop-blur-sm">
          <div className="w-full max-w-sm rounded-2xl bg-white p-6 shadow-2xl dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-center">
            <HelpCircle className="w-12 h-12 text-emerald-600 mx-auto mb-2" />
            <h3 className="text-lg font-bold text-slate-900 dark:text-white">Confirmer la soumission</h3>
            <p className="text-sm text-slate-600 dark:text-slate-300 mt-2">
              Vous avez répondu à {Object.keys(selectedAnswers).length} sur {questions.length} questions.
              Souhaitez-vous finaliser l'épreuve maintenant ?
            </p>
            <div className="flex gap-2 mt-5">
              <button
                onClick={() => setShowConfirmFinish(false)}
                className="flex-1 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 text-sm font-semibold text-slate-700 dark:text-slate-300"
              >
                Continuer
              </button>
              <button
                onClick={() => {
                  setShowConfirmFinish(false);
                  handleFinishQuiz();
                }}
                className="flex-1 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-sm font-bold text-white shadow"
              >
                Finaliser
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Report Modal */}
      {reportingQuestion && (
        <ReportModal
          question={reportingQuestion}
          isOpen={!!reportingQuestion}
          onClose={() => setReportingQuestion(null)}
          onSubmit={(report) => {
            if (onReportQuestion) onReportQuestion(report);
          }}
        />
      )}
    </div>
  );
};

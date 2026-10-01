import React, { useState } from 'react';
import { UserProgress, Question } from '../types';
import { exportProgressJSON, importProgressJSON } from '../services/storage';
import { 
  TrendingUp, 
  Share2, 
  Download, 
  Upload, 
  Settings, 
  AlertCircle, 
  Award, 
  CheckCircle2, 
  Clock, 
  Flame, 
  Info,
  Calendar,
  ShieldCheck,
  Copy,
  Check,
  Trash2,
  RotateCcw
} from 'lucide-react';

interface DashboardViewProps {
  progress: UserProgress;
  questions: Question[];
  onUpdateProgress: (newProgress: UserProgress) => void;
  onResetProgress: () => void;
}

export const DashboardView: React.FC<DashboardViewProps> = ({
  progress,
  questions,
  onUpdateProgress,
  onResetProgress,
}) => {
  const [showSettings, setShowSettings] = useState(false);
  const [importStatus, setImportStatus] = useState<string | null>(null);
  const [copiedShare, setCopiedShare] = useState(false);
  const [showResetConfirm, setShowResetConfirm] = useState(false);

  // Stats calculation
  const catBQuestions = questions.filter(q => q.tags.includes('categorie-b'));
  const totalCatB = catBQuestions.length;
  const completedCount = progress.completedQuestionIds.length;
  const coverageRate = Math.min(100, Math.round((completedCount / totalCatB) * 100));

  // Success rate from exams
  let avgExamPct = 0;
  if (progress.examHistory.length > 0) {
    const totalScore = progress.examHistory.reduce((acc, curr) => acc + (curr.score / curr.total) * 100, 0);
    avgExamPct = Math.round(totalScore / progress.examHistory.length);
  } else {
    // Estimator based on Leitner box 2 and 3
    const box2 = Object.values(progress.questionLeitner).filter(b => b === 2).length;
    const box3 = Object.values(progress.questionLeitner).filter(b => b === 3).length;
    avgExamPct = completedCount > 0 ? Math.round(((box2 * 0.5 + box3 * 1.0) / completedCount) * 100) : 0;
  }

  // Transparent readiness score: 40% syllabus coverage + 60% mastery rate
  const readinessScore = Math.min(100, Math.round(coverageRate * 0.4 + avgExamPct * 0.6));

  const handleExport = () => {
    const jsonStr = exportProgressJSON(progress);
    const blob = new Blob([jsonStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `code-benin-b-progression-${new Date().toISOString().split('T')[0]}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleImportFile = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (event) => {
      const text = event.target?.result as string;
      const imported = importProgressJSON(text);
      if (imported) {
        onUpdateProgress(imported);
        setImportStatus("Progression importée avec succès !");
      } else {
        setImportStatus("Fichier invalide ou endommagé.");
      }
      setTimeout(() => setImportStatus(null), 3000);
    };
    reader.readAsText(file);
  };



  return (
    <div className="space-y-6 animate-fade-in pb-20">
      {/* Readiness gauge card */}
      <div className="bg-gradient-to-br from-emerald-800 via-teal-900 to-slate-900 text-white p-6 rounded-3xl shadow-xl border border-emerald-700/50 relative overflow-hidden">
        <div className="relative z-10 space-y-4">
          <div className="flex items-center justify-between">
            <span className="text-xs uppercase font-extrabold tracking-wider bg-emerald-500/20 text-emerald-300 px-3 py-1 rounded-full border border-emerald-400/30 flex items-center gap-1.5">
              <TrendingUp className="w-3.5 h-3.5" />
              Indice de Préparation Permis B
            </span>
            <div className="flex items-center gap-1 text-xs font-bold text-amber-300 bg-amber-500/20 px-2.5 py-1 rounded-full border border-amber-400/30">
              <Flame className="w-3.5 h-3.5 fill-amber-400 text-amber-400" />
              <span>Série : {progress.streak.count} jour{progress.streak.count > 1 ? 's' : ''}</span>
            </div>
          </div>

          <div className="flex items-center justify-between gap-4">
            <div>
              <p className="text-4xl sm:text-5xl font-black tracking-tight">{readinessScore}%</p>
              <p className="text-xs text-emerald-200 mt-1">
                {readinessScore >= 85
                  ? "Niveau Excellent ! Vous êtes prêt pour l'examen officiel."
                  : readinessScore >= 60
                  ? "En bonne voie. Continuez les quiz pour solidifier vos acquis."
                  : "Début de préparation. Suivez le plan 3 jours pour monter en puissance."}
              </p>
            </div>

            <div className="w-20 h-20 rounded-full border-4 border-emerald-400/30 flex items-center justify-center p-2 text-center bg-white/5 backdrop-blur-sm">
              <span className="text-[11px] font-bold leading-tight text-emerald-100">
                {completedCount}<br /><span className="text-[9px] opacity-75 font-normal">/ {totalCatB} Q</span>
              </span>
            </div>
          </div>

          {/* Transparent calculation breakdown */}
          <div className="pt-3 border-t border-emerald-700/60 grid grid-cols-2 gap-2 text-xs">
            <div className="bg-emerald-950/40 p-2.5 rounded-xl border border-emerald-500/20">
              <span className="text-[10px] text-emerald-300 uppercase font-semibold">Couverture Programme</span>
              <p className="font-bold text-sm mt-0.5">{coverageRate}%</p>
            </div>
            <div className="bg-emerald-950/40 p-2.5 rounded-xl border border-emerald-500/20">
              <span className="text-[10px] text-emerald-300 uppercase font-semibold">Taux de Succès</span>
              <p className="font-bold text-sm mt-0.5">{avgExamPct}%</p>
            </div>
          </div>

          <div className="flex gap-2">
            <a
              href={`https://api.whatsapp.com/send?text=${encodeURIComponent(
                `🚦 Code Bénin B (Permis en 3 jours) : Mon indice de préparation est de ${readinessScore}% avec ${completedCount}/${totalCatB} questions étudiées ! 🇧🇯\nPrépare ton permis B toi aussi !`
              )}`}
              target="_blank"
              rel="noopener noreferrer"
              className="flex-1 py-3 px-4 rounded-2xl bg-white text-slate-900 font-extrabold text-xs shadow hover:bg-slate-50 transition flex items-center justify-center gap-2 cursor-pointer"
            >
              <Share2 className="w-4 h-4 text-emerald-600" />
              <span>Partager sur WhatsApp</span>
            </a>
            <button
              onClick={() => {
                navigator.clipboard?.writeText(
                  `🚦 Code Bénin B (Permis en 3 jours) : Mon indice de préparation est de ${readinessScore}% avec ${completedCount}/${totalCatB} questions étudiées ! 🇧🇯\nPrépare ton permis B toi aussi !`
                );
                setCopiedShare(true);
                setTimeout(() => setCopiedShare(false), 2500);
              }}
              className="px-3.5 py-3 rounded-2xl bg-white/20 hover:bg-white/30 text-white font-bold text-xs transition flex items-center justify-center gap-1.5 cursor-pointer"
              title="Copier le texte"
            >
              {copiedShare ? <Check className="w-4 h-4 text-emerald-300" /> : <Copy className="w-4 h-4" />}
              <span>{copiedShare ? "Copié !" : "Copier"}</span>
            </button>
          </div>
        </div>
      </div>

      {/* Target Exam Date Banner */}
      <div className="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm flex items-center justify-between gap-3 text-xs">
        <div className="flex items-center gap-2.5">
          <Calendar className="w-5 h-5 text-emerald-600" />
          <div>
            <p className="font-bold text-slate-900 dark:text-white">Date de votre examen DGTT</p>
            <p className="text-slate-500">
              {progress.targetExamDate ? `Échéance fixée au : ${progress.targetExamDate}` : "Aucune date fixée"}
            </p>
          </div>
        </div>
        <input
          type="date"
          value={progress.targetExamDate || ''}
          onChange={(e) => {
            const updated = { ...progress, targetExamDate: e.target.value || null };
            onUpdateProgress(updated);
          }}
          className="border border-slate-300 dark:border-slate-700 rounded-xl px-2.5 py-1.5 text-xs bg-slate-50 dark:bg-slate-800 text-slate-800 dark:text-slate-200"
        />
      </div>

      {/* Exam History */}
      <div className="bg-white dark:bg-slate-900 p-5 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-sm space-y-3">
        <div className="flex items-center justify-between pb-2 border-b border-slate-100 dark:border-slate-800">
          <h3 className="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-2">
            <Award className="w-4 h-4 text-emerald-600" />
            Historique des Examens Blancs ({progress.examHistory.length})
          </h3>
        </div>

        {progress.examHistory.length === 0 ? (
          <p className="text-xs text-slate-500 py-3 text-center">
            Vous n'avez pas encore passé d'examen blanc complet. Lancez l'examen blanc dans l'onglet Examen !
          </p>
        ) : (
          <div className="space-y-2">
            {progress.examHistory.slice(0, 5).map((ex, i) => (
              <div
                key={ex.id || i}
                className="flex items-center justify-between p-3 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-100 dark:border-slate-800 text-xs"
              >
                <div className="space-y-0.5">
                  <div className="flex items-center gap-2">
                    <span className="font-bold text-slate-800 dark:text-slate-200">
                      {new Date(ex.date).toLocaleDateString('fr-FR', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' })}
                    </span>
                    <span className={`px-2 py-0.5 rounded-full text-[10px] font-black ${
                      ex.passed
                        ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300'
                        : 'bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300'
                    }`}>
                      {ex.passed ? 'ADMIS' : 'AJOURNÉ'}
                    </span>
                  </div>
                  <p className="text-[11px] text-slate-500">
                    Durée : {Math.round(ex.timeSpentSeconds / 60)} min • {ex.mistakeQuestionIds.length} erreur(s)
                  </p>
                </div>
                <div className="text-right">
                  <span className="text-base font-black text-slate-900 dark:text-white">{ex.score}</span>
                  <span className="text-xs text-slate-400">/{ex.total}</span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Backup, Sync & Settings */}
      <div className="bg-white dark:bg-slate-900 p-5 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-sm space-y-4">
        <h3 className="font-bold text-sm text-slate-900 dark:text-white flex items-center gap-2">
          <Settings className="w-4 h-4 text-emerald-600" />
          Sauvegarde Locale & Paramètres d'Examen
        </h3>

        {importStatus && (
          <div className="p-3 rounded-xl bg-emerald-50 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 text-xs font-semibold">
            {importStatus}
          </div>
        )}

        <div className="grid grid-cols-2 gap-2 text-xs">
          <button
            onClick={handleExport}
            className="p-3 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/60 font-bold text-slate-800 dark:text-slate-200 hover:border-emerald-500 flex items-center justify-center gap-2 transition"
          >
            <Download className="w-4 h-4 text-emerald-600" />
            <span>Exporter mes données</span>
          </button>

          <label className="p-3 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/60 font-bold text-slate-800 dark:text-slate-200 hover:border-emerald-500 flex items-center justify-center gap-2 cursor-pointer transition">
            <Upload className="w-4 h-4 text-emerald-600" />
            <span>Importer une sauvegarde</span>
            <input type="file" accept=".json" onChange={handleImportFile} className="hidden" />
          </label>
        </div>

        {/* Exam settings form */}
        <div className="pt-3 border-t border-slate-100 dark:border-slate-800 space-y-3">
          <button
            onClick={() => setShowSettings(!showSettings)}
            className="text-xs font-bold text-emerald-700 dark:text-emerald-400 hover:underline flex items-center gap-1"
          >
            <span>{showSettings ? '▲ Masquer' : '▼ Personnaliser les paramètres de l’examen blanc'}</span>
          </button>

          {showSettings && (
            <div className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-800/50 border border-slate-200 dark:border-slate-700 space-y-3 text-xs animate-fade-in">
              <p className="text-slate-500 text-[11px] leading-relaxed">
                ℹ️ Le nombre de questions et le barème d'admissibilité exacts de la DGTT peuvent varier selon les centres. Vous pouvez ajuster vos objectifs ici :
              </p>

              <div className="grid grid-cols-3 gap-2">
                <div>
                  <label className="block text-[11px] font-bold text-slate-700 dark:text-slate-300 mb-1">Questions</label>
                  <input
                    type="number"
                    value={progress.settings.examQuestionsCount}
                    onChange={(e) => {
                      const count = Number(e.target.value) || 40;
                      onUpdateProgress({
                        ...progress,
                        settings: { ...progress.settings, examQuestionsCount: count },
                      });
                    }}
                    className="w-full p-2 border rounded-xl dark:bg-slate-800 border-slate-300 dark:border-slate-700 font-bold text-center"
                  />
                </div>

                <div>
                  <label className="block text-[11px] font-bold text-slate-700 dark:text-slate-300 mb-1">Durée (min)</label>
                  <input
                    type="number"
                    value={progress.settings.examDurationMinutes}
                    onChange={(e) => {
                      const mins = Number(e.target.value) || 30;
                      onUpdateProgress({
                        ...progress,
                        settings: { ...progress.settings, examDurationMinutes: mins },
                      });
                    }}
                    className="w-full p-2 border rounded-xl dark:bg-slate-800 border-slate-300 dark:border-slate-700 font-bold text-center"
                  />
                </div>

                <div>
                  <label className="block text-[11px] font-bold text-slate-700 dark:text-slate-300 mb-1">Seuil Réussite</label>
                  <input
                    type="number"
                    value={progress.settings.examPassingScore}
                    onChange={(e) => {
                      const score = Number(e.target.value) || 35;
                      onUpdateProgress({
                        ...progress,
                        settings: { ...progress.settings, examPassingScore: score },
                      });
                    }}
                    className="w-full p-2 border rounded-xl dark:bg-slate-800 border-slate-300 dark:border-slate-700 font-bold text-center"
                  />
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Reset progress */}
        <div className="pt-3 border-t border-slate-100 dark:border-slate-800">
          {!showResetConfirm ? (
            <button
              onClick={() => setShowResetConfirm(true)}
              className="text-xs text-rose-600 dark:text-rose-400 hover:text-rose-700 flex items-center gap-1.5 font-bold cursor-pointer"
            >
              <Trash2 className="w-3.5 h-3.5" />
              <span>Réinitialiser toute ma progression...</span>
            </button>
          ) : (
            <div className="p-3.5 rounded-2xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900 space-y-2 text-xs">
              <p className="font-bold text-rose-900 dark:text-rose-200">
                Êtes-vous sûr de vouloir tout remettre à zéro ?
              </p>
              <p className="text-[11px] text-rose-700 dark:text-rose-300 leading-relaxed">
                Tous vos scores, séries, historique d'examens et erreurs enregistrées seront effacés de la mémoire locale.
              </p>
              <div className="flex gap-2 pt-1">
                <button
                  onClick={() => {
                    onResetProgress();
                    setShowResetConfirm(false);
                  }}
                  className="px-3.5 py-1.5 rounded-xl bg-rose-600 text-white font-bold text-xs hover:bg-rose-700 cursor-pointer shadow-sm"
                >
                  Oui, réinitialiser
                </button>
                <button
                  onClick={() => setShowResetConfirm(false)}
                  className="px-3.5 py-1.5 rounded-xl bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 text-xs font-semibold hover:bg-slate-300 dark:hover:bg-slate-700 cursor-pointer"
                >
                  Annuler
                </button>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Official Legal Notice */}
      <div className="p-4 rounded-2xl bg-amber-50/70 dark:bg-amber-950/20 border border-amber-200/80 dark:border-amber-900/60 text-xs text-amber-900 dark:text-amber-300 space-y-1">
        <div className="flex items-center gap-1.5 font-bold">
          <Info className="w-4 h-4 text-amber-600" />
          <span>Mention Légale & Source Officielle</span>
        </div>
        <p className="text-[11px] text-amber-800/90 dark:text-amber-400 leading-relaxed">
          Application basée strictement sur <em>« Le manuel du candidat à l'examen du permis de conduire »</em>, Direction Générale des Transports Terrestres (DGTT), République du Bénin, Édition 2011. Pour les éventuelles évolutions récentes (montant des amendes, tarifs de timbres fiscaux ou formalités administratives de délivrance), veuillez vous rapprocher de la DGTT ou de votre auto-école agréée.
        </p>
      </div>
    </div>
  );
};

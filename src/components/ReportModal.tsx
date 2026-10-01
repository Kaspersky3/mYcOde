import React, { useState } from 'react';
import { Question, QuestionReport } from '../types';
import { AlertTriangle, X, Send, Check } from 'lucide-react';

interface ReportModalProps {
  question: Question;
  isOpen: boolean;
  onClose: () => void;
  onSubmit: (report: QuestionReport) => void;
}

export const ReportModal: React.FC<ReportModalProps> = ({
  question,
  isOpen,
  onClose,
  onSubmit,
}) => {
  const [reason, setReason] = useState('reponse_douteuse');
  const [comment, setComment] = useState('');
  const [submitted, setSubmitted] = useState(false);

  if (!isOpen) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const report: QuestionReport = {
      questionId: question.numero,
      questionText: question.enonce,
      reason,
      comment,
      date: new Date().toISOString(),
    };
    onSubmit(report);
    setSubmitted(true);
    setTimeout(() => {
      setSubmitted(false);
      onClose();
    }, 1500);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4 backdrop-blur-sm">
      <div className="w-full max-w-md rounded-2xl bg-white p-6 shadow-2xl dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
        <div className="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-slate-800">
          <div className="flex items-center gap-2 text-amber-600 dark:text-amber-400 font-bold">
            <AlertTriangle className="w-5 h-5" />
            <h3>Signaler la Question n°{question.numero}</h3>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-lg text-slate-400 hover:text-slate-600 dark:hover:text-white"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {submitted ? (
          <div className="py-8 text-center text-emerald-600 dark:text-emerald-400 flex flex-col items-center gap-2">
            <div className="w-12 h-12 rounded-full bg-emerald-100 dark:bg-emerald-950 flex items-center justify-center">
              <Check className="w-6 h-6" />
            </div>
            <p className="font-semibold">Signalement enregistré localement !</p>
            <p className="text-xs text-slate-500">Vous pouvez l'exporter depuis l'onglet « Mon Suivi ».</p>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="mt-4 space-y-4">
            <div>
              <p className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1">Énoncé concerné :</p>
              <p className="text-sm font-medium text-slate-800 dark:text-slate-200 line-clamp-2 bg-slate-50 dark:bg-slate-800/50 p-2.5 rounded-lg border border-slate-200/70 dark:border-slate-700/60">
                {question.enonce}
              </p>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
                Motif du signalement :
              </label>
              <select
                value={reason}
                onChange={(e) => setReason(e.target.value)}
                className="w-full text-sm rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 px-3 py-2 text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-emerald-500"
              >
                <option value="reponse_douteuse">Réponse contestable ou ambiguë</option>
                <option value="coquille_texte">Erreur ou faute de frappe dans l'énoncé</option>
                <option value="panneau_incoherent">Illustration ou panneau non concordant</option>
                <option value="evolution_reglement">Évolution réglementaire depuis 2011</option>
                <option value="autre">Autre motif</option>
              </select>
            </div>

            <div>
              <label className="block text-xs font-semibold text-slate-700 dark:text-slate-300 mb-1">
                Votre commentaire ou précision :
              </label>
              <textarea
                value={comment}
                onChange={(e) => setComment(e.target.value)}
                required
                rows={3}
                placeholder="Expliquez ce qui vous semble incorrect ou à vérifier..."
                className="w-full text-sm rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 p-3 text-slate-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-emerald-500"
              />
            </div>

            <div className="flex gap-2 pt-2">
              <button
                type="button"
                onClick={onClose}
                className="flex-1 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 text-sm font-semibold text-slate-700 dark:text-slate-300 hover:bg-slate-50 dark:hover:bg-slate-800 transition"
              >
                Annuler
              </button>
              <button
                type="submit"
                className="flex-1 py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-sm font-semibold text-white flex items-center justify-center gap-1.5 shadow-sm transition"
              >
                <Send className="w-4 h-4" />
                <span>Envoyer</span>
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  );
};

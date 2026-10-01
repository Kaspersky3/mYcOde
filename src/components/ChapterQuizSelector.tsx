import React, { useState } from 'react';
import { Question } from '../types';
import { 
  BookOpen, 
  HelpCircle, 
  Sparkles, 
  ChevronRight, 
  Layers, 
  Filter,
  CheckCircle2
} from 'lucide-react';

interface ChapterQuizSelectorProps {
  questions: Question[];
  completedQuestionIds: number[];
  onStartQuiz: (questions: Question[], title: string) => void;
  showOtherCategories: boolean;
  onToggleOtherCategories: (show: boolean) => void;
}

export const ChapterQuizSelector: React.FC<ChapterQuizSelectorProps> = ({
  questions,
  completedQuestionIds,
  onStartQuiz,
  showOtherCategories,
  onToggleOtherCategories,
}) => {
  const [selectedChapitre, setSelectedChapitre] = useState<number | null>(null);

  // Group chapters
  const chaptersMeta = [
    { num: 2, title: "Chapitre II : Signalisation Routière", desc: "Panneaux, marquages, feux et agents", count: 205, isCatB: true },
    { num: 3, title: "Chapitre III : Règles de Priorité & Dépassement", desc: "Carrefours, priorité à droite, croisements", count: 154, isCatB: true },
    { num: 4, title: "Chapitre IV : Arrêt, Stationnement & Vitesse", desc: "Immobilisation, freinage, manœuvres", count: 111, isCatB: true },
    { num: 5, title: "Chapitre V : Route pour Automobile & Autoroute", desc: "Voies d'insertion, circulation, pannes", count: 37, isCatB: true },
    { num: 6, title: "Chapitre VI : Infractions & Secourisme", desc: "Alcoolémie, accident, protocole PAS, PLS", count: 138, isCatB: true },
    { num: 8, title: "Chapitre VIII : Permis Catégorie B", desc: "Règles spécifiques au permis voiture B", count: 10, isCatB: true },
    { num: 11, title: "Chapitre XI : Équipement & Mécanique", desc: "Moteur 4 temps, entretien, pneumatiques, pièces", count: 131, isCatB: true },
    // Other categories
    { num: 7, title: "Chapitre VII : Permis Motos (A1, A2, A3)", desc: "Spécificités cyclomoteurs et motocyclettes", count: 33, isCatB: false },
    { num: 9, title: "Chapitre IX : Permis Poids Lourds (C et C1)", desc: "Véhicules de marchandises > 3,5 tonnes", count: 50, isCatB: false },
    { num: 10, title: "Chapitre X : Permis Transports en Commun (D)", desc: "Autobus et autocars de plus de 18 places", count: 61, isCatB: false },
  ];

  const visibleChapters = chaptersMeta.filter(c => c.isCatB || showOtherCategories);

  const startChapterQuiz = (chapNum: number, title: string) => {
    const chapQs = questions.filter(q => q.chapitre === chapNum);
    onStartQuiz(chapQs, title);
  };

  const startFlashReview = () => {
    // Pick 10 random Category B questions
    const catB = questions.filter(q => q.tags.includes('categorie-b'));
    const shuffled = [...catB].sort(() => 0.5 - Math.random()).slice(0, 10);
    onStartQuiz(shuffled, "⚡ Révision Éclair (10 questions)");
  };

  return (
    <div className="space-y-5 animate-fade-in pb-16">
      {/* Flash Review Banner */}
      <div className="bg-gradient-to-r from-amber-500 to-orange-500 rounded-3xl p-5 text-white shadow-md flex items-center justify-between gap-3">
        <div>
          <span className="text-[10px] font-extrabold uppercase tracking-wider bg-white/20 px-2 py-0.5 rounded-full">
            Session Rapide • 5 Minutes
          </span>
          <h3 className="text-lg font-black mt-1">Mode Révision Éclair</h3>
          <p className="text-xs text-amber-100 mt-0.5">10 questions express ciblées pour tester vos réflexes.</p>
        </div>
        <button
          onClick={startFlashReview}
          className="flex-shrink-0 px-4 py-3 rounded-2xl bg-white text-slate-950 font-bold text-xs shadow-md hover:bg-slate-50 transition active:scale-95"
        >
          Lancer (10 Q)
        </button>
      </div>

      {/* Filter toggle for other categories */}
      <div className="flex items-center justify-between p-3.5 rounded-2xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 text-xs">
        <div className="flex items-center gap-2">
          <Filter className="w-4 h-4 text-emerald-600" />
          <span className="font-bold text-slate-800 dark:text-slate-200">
            Questions des autres catégories (Motos A, Poids lourds C, Bus D)
          </span>
        </div>
        <label className="relative inline-flex items-center cursor-pointer">
          <input
            type="checkbox"
            checked={showOtherCategories}
            onChange={(e) => onToggleOtherCategories(e.target.checked)}
            className="sr-only peer"
          />
          <div className="w-9 h-5 bg-slate-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-4 after:w-4 after:transition-all peer-checked:bg-emerald-600"></div>
        </label>
      </div>

      {/* Chapter Cards Grid */}
      <div className="space-y-3">
        <h3 className="text-xs font-bold uppercase tracking-wider text-slate-400 px-1">
          Parcours libre par chapitre ({visibleChapters.length} chapitres)
        </h3>

        {visibleChapters.map((chap) => {
          const chapQuestions = questions.filter(q => q.chapitre === chap.num);
          const completedInChap = chapQuestions.filter(q => completedQuestionIds.includes(q.numero)).length;
          const pct = Math.round((completedInChap / (chapQuestions.length || 1)) * 100);

          return (
            <div
              key={chap.num}
              className={`p-4 rounded-2xl border transition bg-white dark:bg-slate-900 shadow-sm ${
                chap.isCatB 
                  ? 'border-slate-200 dark:border-slate-800 hover:border-emerald-400' 
                  : 'border-slate-200/60 dark:border-slate-800/60 bg-slate-50/50 dark:bg-slate-900/40'
              }`}
            >
              <div className="flex items-start justify-between gap-3">
                <div className="space-y-1">
                  <div className="flex items-center gap-2">
                    <span className={`text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full ${
                      chap.isCatB
                        ? 'bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300'
                        : 'bg-slate-200 dark:bg-slate-800 text-slate-600 dark:text-slate-400'
                    }`}>
                      {chap.isCatB ? 'Catégorie B (Prioritaire)' : 'Autre Catégorie'}
                    </span>
                    <span className="text-xs text-slate-400">
                      {chapQuestions.length} questions
                    </span>
                  </div>
                  <h4 className="font-extrabold text-sm text-slate-900 dark:text-white leading-tight">
                    {chap.title}
                  </h4>
                  <p className="text-xs text-slate-500 leading-tight">
                    {chap.desc}
                  </p>
                </div>

                <button
                  onClick={() => startChapterQuiz(chap.num, chap.title)}
                  className="flex-shrink-0 p-2.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 hover:bg-emerald-600 hover:text-white transition"
                  title="S'entraîner sur ce chapitre"
                >
                  <ChevronRight className="w-5 h-5" />
                </button>
              </div>

              {/* Progress bar inside chapter */}
              <div className="mt-3 pt-2.5 border-t border-slate-100 dark:border-slate-800 flex items-center justify-between text-xs text-slate-500">
                <span>Progression : {completedInChap} / {chapQuestions.length}</span>
                <span className="font-bold text-emerald-600 dark:text-emerald-400">{pct}%</span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

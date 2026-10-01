import React, { useState } from 'react';
import { Question, UserProgress } from '../types';
import { TrafficSign } from './TrafficSign';
import { 
  RotateCcw, 
  Trash2, 
  AlertCircle, 
  CheckCircle2, 
  Layers, 
  BookX,
  Search,
  ChevronRight
} from 'lucide-react';

interface MistakesNotebookProps {
  progress: UserProgress;
  questions: Question[];
  onStartQuiz: (questions: Question[], title: string) => void;
  onClearMistakes?: () => void;
}

export const MistakesNotebook: React.FC<MistakesNotebookProps> = ({
  progress,
  questions,
  onStartQuiz,
  onClearMistakes,
}) => {
  const [selectedBox, setSelectedBox] = useState<1 | 2 | 3 | 'all'>('all');
  const [searchTerm, setSearchTerm] = useState('');

  // Map questions with their Leitner box
  const mistakesWithData = progress.mistakeHistory
    .map((num) => {
      const q = questions.find((item) => item.numero === num);
      const box = progress.questionLeitner[num] || 1;
      return { q, box };
    })
    .filter((item): item is { q: Question; box: 1 | 2 | 3 } => !!item.q);

  const box1List = mistakesWithData.filter((item) => item.box === 1);
  const box2List = mistakesWithData.filter((item) => item.box === 2);
  const box3List = mistakesWithData.filter((item) => item.box === 3);

  const displayedList = mistakesWithData.filter((item) => {
    if (selectedBox !== 'all' && item.box !== selectedBox) return false;
    if (searchTerm) {
      const t = searchTerm.toLowerCase();
      return (
        item.q.enonce.toLowerCase().includes(t) ||
        item.q.numero.toString().includes(t) ||
        item.q.theme.toLowerCase().includes(t)
      );
    }
    return true;
  });

  const startReplaySession = (items: { q: Question }[], title: string) => {
    if (items.length === 0) return;
    onStartQuiz(items.map((i) => i.q), title);
  };

  return (
    <div className="space-y-5 animate-fade-in pb-16">
      {/* Top Banner */}
      <div className="bg-gradient-to-br from-slate-900 to-slate-800 text-white p-5 rounded-3xl shadow-lg border border-slate-700/60">
        <div className="flex items-start justify-between gap-3">
          <div>
            <span className="text-[10px] uppercase font-bold tracking-wider text-rose-400 bg-rose-950/60 px-2 py-0.5 rounded-full border border-rose-800">
              Répétition Espacée • Système Leitner
            </span>
            <h2 className="text-xl font-black mt-1">Cahier d'Erreurs Intelligent</h2>
            <p className="text-xs text-slate-300 mt-1 max-w-sm leading-relaxed">
              Toutes les questions où vous avez trébuché sont stockées ici. Plus vous les réussissez, plus elles s'espacent jusqu'à maîtrise totale.
            </p>
          </div>
          <div className="w-12 h-12 rounded-2xl bg-rose-500/20 text-rose-400 flex items-center justify-center">
            <BookX className="w-6 h-6" />
          </div>
        </div>

        {/* Big Replay Button */}
        {mistakesWithData.length > 0 && (
          <div className="mt-4 pt-4 border-t border-slate-700 flex flex-wrap items-center gap-2">
            <button
              onClick={() => startReplaySession(mistakesWithData, `Rattrapage des ${mistakesWithData.length} erreurs`)}
              className="flex-1 py-3 px-4 rounded-xl bg-rose-600 hover:bg-rose-500 active:bg-rose-700 text-white font-extrabold text-xs shadow-md transition flex items-center justify-center gap-2"
            >
              <RotateCcw className="w-4 h-4" />
              <span>Rejouer toutes les erreurs ({mistakesWithData.length})</span>
            </button>
            {box1List.length > 0 && (
              <button
                onClick={() => startReplaySession(box1List, `Rattrapage Urgence (Boîte 1)`)}
                className="py-3 px-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-rose-300 font-bold text-xs border border-rose-500/40"
              >
                Urgence Boîte 1 ({box1List.length})
              </button>
            )}
          </div>
        )}
      </div>

      {/* Leitner 3 Boxes Tabs */}
      <div className="grid grid-cols-4 gap-1.5 p-1.5 bg-slate-100 dark:bg-slate-800/80 rounded-2xl text-xs font-bold">
        <button
          onClick={() => setSelectedBox('all')}
          className={`py-2 px-1 rounded-xl transition ${
            selectedBox === 'all'
              ? 'bg-white dark:bg-slate-900 text-slate-900 dark:text-white shadow-sm'
              : 'text-slate-600 dark:text-slate-400'
          }`}
        >
          Tout ({mistakesWithData.length})
        </button>

        <button
          onClick={() => setSelectedBox(1)}
          className={`py-2 px-1 rounded-xl transition flex items-center justify-center gap-1 ${
            selectedBox === 1
              ? 'bg-white dark:bg-slate-900 text-rose-600 dark:text-rose-400 shadow-sm'
              : 'text-slate-600 dark:text-slate-400'
          }`}
        >
          <span className="w-2 h-2 rounded-full bg-rose-500" />
          <span>Boîte 1 ({box1List.length})</span>
        </button>

        <button
          onClick={() => setSelectedBox(2)}
          className={`py-2 px-1 rounded-xl transition flex items-center justify-center gap-1 ${
            selectedBox === 2
              ? 'bg-white dark:bg-slate-900 text-amber-600 dark:text-amber-400 shadow-sm'
              : 'text-slate-600 dark:text-slate-400'
          }`}
        >
          <span className="w-2 h-2 rounded-full bg-amber-500" />
          <span>Boîte 2 ({box2List.length})</span>
        </button>

        <button
          onClick={() => setSelectedBox(3)}
          className={`py-2 px-1 rounded-xl transition flex items-center justify-center gap-1 ${
            selectedBox === 3
              ? 'bg-white dark:bg-slate-900 text-emerald-600 dark:text-emerald-400 shadow-sm'
              : 'text-slate-600 dark:text-slate-400'
          }`}
        >
          <span className="w-2 h-2 rounded-full bg-emerald-500" />
          <span>Boîte 3 ({box3List.length})</span>
        </button>
      </div>

      {/* Search Input */}
      {mistakesWithData.length > 0 && (
        <div className="relative">
          <Search className="w-4 h-4 absolute left-3.5 top-3.5 text-slate-400" />
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Filtrer mes erreurs par mot-clé ou numéro..."
            className="w-full pl-10 pr-4 py-2.5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 text-xs text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-rose-500"
          />
        </div>
      )}

      {/* List of mistakes */}
      {displayedList.length === 0 ? (
        <div className="p-8 text-center bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 space-y-2">
          <div className="w-12 h-12 mx-auto rounded-full bg-emerald-100 dark:bg-emerald-950 flex items-center justify-center text-emerald-600">
            <CheckCircle2 className="w-6 h-6" />
          </div>
          <h4 className="font-bold text-slate-900 dark:text-white text-sm">
            {mistakesWithData.length === 0 ? "Aucune erreur enregistrée !" : "Aucune question trouvée dans ce filtre."}
          </h4>
          <p className="text-xs text-slate-500 max-w-xs mx-auto">
            {mistakesWithData.length === 0
              ? "Pratiquez des quiz dans le parcours 3 jours ou par chapitre. Vos erreurs viendront s'alimenter ici automatiquement."
              : "Changez de boîte ou effacez votre recherche pour voir les autres questions."}
          </p>
        </div>
      ) : (
        <div className="space-y-3">
          {displayedList.map(({ q, box }) => (
            <div
              key={q.id}
              className="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm space-y-2"
            >
              <div className="flex items-center justify-between gap-2">
                <div className="flex items-center gap-1.5">
                  <span className="text-xs font-extrabold text-slate-800 dark:text-slate-200">
                    Question n°{q.numero}
                  </span>
                  <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                    box === 1
                      ? 'bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300'
                      : box === 2
                      ? 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300'
                      : 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300'
                  }`}>
                    {box === 1 ? 'Niveau 1 : À revoir' : box === 2 ? 'Niveau 2 : En progrès' : 'Niveau 3 : Maîtrisé'}
                  </span>
                </div>

                <button
                  onClick={() => onStartQuiz([q], `Rejouer Question n°${q.numero}`)}
                  className="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 hover:bg-emerald-600 hover:text-white text-slate-700 dark:text-slate-300 text-xs font-semibold flex items-center gap-1 transition"
                >
                  <span>Rejouer</span>
                  <ChevronRight className="w-3.5 h-3.5" />
                </button>
              </div>

              <p className="text-xs font-semibold text-slate-900 dark:text-white">{q.enonce}</p>

              {q.image && (
                <div className="my-1.5">
                  <TrafficSign code={q.image} />
                </div>
              )}

              <div className="text-xs bg-slate-50 dark:bg-slate-800/60 p-2.5 rounded-xl border border-slate-100 dark:border-slate-800 text-slate-700 dark:text-slate-300">
                <span className="font-bold text-emerald-700 dark:text-emerald-400">Bonne(s) réponse(s) : </span>
                <span className="uppercase font-extrabold text-emerald-800 dark:text-emerald-300">{q.bonnesReponses.join(', ')}</span>
                {q.explication && (
                  <p className="mt-1 text-[11px] text-slate-500 leading-snug">
                    {q.explication}
                  </p>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

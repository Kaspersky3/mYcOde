import React from 'react';
import { UserProgress, Question } from '../types';
import { 
  CheckCircle2, 
  Circle, 
  ArrowRight, 
  Flame, 
  BookOpen, 
  HelpCircle, 
  AlertTriangle, 
  Award,
  Sparkles,
  Calendar,
  Clock,
  Zap,
  Search
} from 'lucide-react';

interface DailyRoadmapProps {
  progress: UserProgress;
  questions: Question[];
  onStartQuiz: (filteredQuestions: Question[], title: string, isExam?: boolean) => void;
  onOpenRevisionTab: (tab: 'attention' | 'traps' | 'numbers' | 'ambiguities') => void;
  onChangeDay: (day: 1 | 2 | 3) => void;
}

export const DailyRoadmap: React.FC<DailyRoadmapProps> = ({
  progress,
  questions,
  onStartQuiz,
  onOpenRevisionTab,
  onChangeDay,
}) => {
  const currentDay = progress.currentDay;
  const day1Prog = progress.dayProgress[1];
  const day2Prog = progress.dayProgress[2];
  const day3Prog = progress.dayProgress[3];

  // Questions filtered per day for Category B
  const day1Questions = questions.filter((q) => q.chapitre === 2 && q.tags.includes('categorie-b'));
  const day2Questions = questions.filter((q) => [3, 4, 5].includes(q.chapitre) && q.tags.includes('categorie-b'));
  const day3Questions = questions.filter((q) => [6, 8, 11].includes(q.chapitre) && q.tags.includes('categorie-b'));

  // Traps per day
  const day1Traps = day1Questions.filter((q) => q.tags.includes('piege') || q.multiReponses);
  const day2Traps = day2Questions.filter((q) => q.tags.includes('piege') || q.multiReponses);
  const day3Traps = day3Questions.filter((q) => q.tags.includes('piege') || q.multiReponses);

  // Determine what the user needs next
  const getContinueAction = () => {
    if (currentDay === 1) {
      if (!day1Prog.learned) {
        return {
          title: "Jour 1 • Fiches Signalisation",
          subtitle: "Découvrez les panneaux et marquages indispensables",
          action: () => onOpenRevisionTab('attention'),
          btnText: "Ouvrir les Fiches du Jour 1",
          icon: <BookOpen className="w-5 h-5" />,
        };
      }
      if (!day1Prog.quizDone) {
        return {
          title: "Jour 1 • Quiz d'entraînement",
          subtitle: "25 questions clés de signalisation",
          action: () => onStartQuiz(day1Questions.slice(0, 25), "Jour 1 • Entraînement Signalisation"),
          btnText: "Lancer le Quiz du Jour 1",
          icon: <HelpCircle className="w-5 h-5" />,
        };
      }
      return {
        title: "Jour 1 • Pièges & Bilan",
        subtitle: "Maîtrisez les questions à réponses multiples de signalisation",
        action: () => onStartQuiz(day1Traps.slice(0, 15), "Jour 1 • Pièges de Signalisation"),
        btnText: "Défier les Pièges du Jour 1",
        icon: <AlertTriangle className="w-5 h-5" />,
      };
    }

    if (currentDay === 2) {
      if (!day2Prog.learned) {
        return {
          title: "Jour 2 • Fiches Circulation & Priorités",
          subtitle: "Règles de carrefours, dépassement et vitesses",
          action: () => onOpenRevisionTab('numbers'),
          btnText: "Réviser les Règles du Jour 2",
          icon: <BookOpen className="w-5 h-5" />,
        };
      }
      if (!day2Prog.quizDone) {
        return {
          title: "Jour 2 • Quiz de Circulation",
          subtitle: "25 questions sur les priorités et manœuvres",
          action: () => onStartQuiz(day2Questions.slice(0, 25), "Jour 2 • Entraînement Circulation"),
          btnText: "Lancer le Quiz du Jour 2",
          icon: <HelpCircle className="w-5 h-5" />,
        };
      }
      return {
        title: "Jour 2 • Pièges de Circulation",
        subtitle: "Priorité en montagne, rase campagne et intersections",
        action: () => onStartQuiz(day2Traps.slice(0, 15), "Jour 2 • Pièges de Circulation"),
        btnText: "Défier les Pièges du Jour 2",
        icon: <AlertTriangle className="w-5 h-5" />,
      };
    }

    // Day 3
    if (!day3Prog.quizDone) {
      return {
        title: "Jour 3 • Sécurité & Spécificités B",
        subtitle: "Secourisme P.A.S, mécanique et permis B",
        action: () => onStartQuiz(day3Questions.slice(0, 25), "Jour 3 • Entraînement Sécurité"),
        btnText: "Lancer le Quiz du Jour 3",
        icon: <HelpCircle className="w-5 h-5" />,
      };
    }
    return {
      title: "Jour 3 • Grand Examen Blanc Officiel",
      subtitle: "Simulation réelle : 40 questions en 30 minutes",
      action: () => {
        // Pick 40 balanced questions across all chapters
        const sample = [
          ...day1Questions.slice(0, 15),
          ...day2Questions.slice(0, 15),
          ...day3Questions.slice(0, 10),
        ].sort(() => 0.5 - Math.random());
        onStartQuiz(sample, "Examen Blanc Officiel DGTT", true);
      },
      btnText: "Passer l'Examen Blanc (Chronométré)",
      icon: <Award className="w-5 h-5" />,
    };
  };

  const nextAction = getContinueAction();

  return (
    <div className="space-y-6 animate-fade-in pb-12">
      {/* Top Banner with streak & big CONTINUE CTA */}
      <div className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-emerald-800 via-emerald-900 to-slate-900 text-white p-6 shadow-xl border border-emerald-700/50">
        <div className="absolute top-0 right-0 -mt-8 -mr-8 w-44 h-44 rounded-full bg-emerald-500/10 blur-2xl pointer-events-none" />
        
        <div className="relative z-10 space-y-4">
          <div className="flex items-center justify-between">
            <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 text-xs font-bold border border-emerald-500/30">
              <Sparkles className="w-3.5 h-3.5" />
              Programme Intensif 72H
            </span>
            <div className="flex items-center gap-1 text-xs font-bold text-amber-300 bg-amber-500/20 px-2.5 py-1 rounded-full border border-amber-400/30">
              <Flame className="w-3.5 h-3.5 fill-amber-400 text-amber-400" />
              <span>Série : {progress.streak.count} jour{progress.streak.count > 1 ? 's' : ''}</span>
            </div>
          </div>

          <div>
            <h2 className="text-2xl font-black tracking-tight">{nextAction.title}</h2>
            <p className="text-sm text-emerald-200/90 mt-1">{nextAction.subtitle}</p>
          </div>

          <button
            onClick={nextAction.action}
            className="w-full py-4 px-6 rounded-2xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 active:scale-[0.99] text-slate-950 font-extrabold text-base shadow-lg transition flex items-center justify-center gap-2 group cursor-pointer"
          >
            {nextAction.icon}
            <span>{nextAction.btnText}</span>
            <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition" />
          </button>
        </div>
      </div>

      {/* Quick Action Shortcuts: 5-min express & search */}
      <div className="grid grid-cols-2 gap-2.5">
        <button
          onClick={() => {
            const catB = questions.filter((q) => q.tags.includes('categorie-b'));
            const sample = [...catB].sort(() => 0.5 - Math.random()).slice(0, 10);
            onStartQuiz(sample, "⚡ Révision Express (5 min - 10 questions)");
          }}
          className="p-3.5 rounded-2xl bg-gradient-to-r from-amber-500/10 to-orange-500/10 hover:from-amber-500/20 hover:to-orange-500/20 border border-amber-300/40 dark:border-amber-700/40 text-left transition flex items-center gap-3 cursor-pointer group shadow-sm"
        >
          <div className="w-10 h-10 rounded-xl bg-amber-500 text-white flex items-center justify-center flex-shrink-0 group-hover:scale-105 transition shadow-sm">
            <Zap className="w-5 h-5 fill-white" />
          </div>
          <div>
            <div className="flex items-center gap-1.5">
              <span className="text-[10px] font-black uppercase text-amber-700 dark:text-amber-400">5 Minutes</span>
            </div>
            <p className="text-xs font-black text-slate-900 dark:text-white leading-tight mt-0.5">
              Révision Express
            </p>
            <p className="text-[10px] text-slate-500 leading-none mt-0.5">10 Q aléatoires</p>
          </div>
        </button>

        <button
          onClick={() => onOpenRevisionTab('attention')}
          className="p-3.5 rounded-2xl bg-slate-50 dark:bg-slate-900 hover:bg-slate-100 dark:hover:bg-slate-800/80 border border-slate-200 dark:border-slate-800 text-left transition flex items-center gap-3 cursor-pointer group shadow-sm"
        >
          <div className="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center flex-shrink-0 group-hover:scale-105 transition shadow-sm">
            <Search className="w-5 h-5" />
          </div>
          <div>
            <div className="flex items-center gap-1.5">
              <span className="text-[10px] font-black uppercase text-emerald-700 dark:text-emerald-400">Recherche</span>
            </div>
            <p className="text-xs font-black text-slate-900 dark:text-white leading-tight mt-0.5">
              Fiches & Règles
            </p>
            <p className="text-[10px] text-slate-500 leading-none mt-0.5">Chiffres, pièges...</p>
          </div>
        </button>
      </div>

      {/* Day Selector Buttons */}
      <div className="flex items-center justify-between gap-2 p-1.5 bg-slate-100 dark:bg-slate-800/80 rounded-2xl">
        {[1, 2, 3].map((d) => {
          const isSelected = currentDay === d;
          return (
            <button
              key={d}
              onClick={() => onChangeDay(d as 1 | 2 | 3)}
              className={`flex-1 py-2.5 px-3 rounded-xl text-xs font-extrabold transition flex items-center justify-center gap-1.5 ${
                isSelected
                  ? 'bg-white dark:bg-slate-900 text-emerald-700 dark:text-emerald-400 shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
              }`}
            >
              <Calendar className="w-3.5 h-3.5" />
              <span>Jour {d}</span>
            </button>
          );
        })}
      </div>

      {/* The 3 Days Detailed Track */}
      <div className="space-y-4">
        {/* DAY 1 */}
        <div className={`rounded-3xl p-5 border transition ${
          currentDay === 1
            ? 'bg-white dark:bg-slate-900 border-emerald-500/60 shadow-md ring-1 ring-emerald-500/20'
            : 'bg-white/80 dark:bg-slate-900/60 border-slate-200 dark:border-slate-800 opacity-90'
        }`}>
          <div className="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-slate-800">
            <div className="flex items-center gap-2.5">
              <div className="w-9 h-9 rounded-xl bg-emerald-100 dark:bg-emerald-950 flex items-center justify-center text-emerald-700 dark:text-emerald-300 font-black text-sm">
                J1
              </div>
              <div>
                <h3 className="font-extrabold text-slate-900 dark:text-white text-base">
                  Jour 1 : La Signalisation
                </h3>
                <p className="text-xs text-slate-500">Chapitre II • 205 questions officielles</p>
              </div>
            </div>
            <button
              onClick={() => onChangeDay(1)}
              className="text-xs font-bold text-emerald-600 hover:text-emerald-700"
            >
              {currentDay === 1 ? 'En cours' : 'Sélectionner'}
            </button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5 mt-4">
            <button
              onClick={() => onOpenRevisionTab('attention')}
              className="p-3 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/40 text-left hover:border-emerald-300 transition"
            >
              <div className="flex items-center justify-between text-xs font-bold mb-1">
                <span className="text-slate-800 dark:text-slate-200">1. Apprendre</span>
                {day1Prog.learned ? <CheckCircle2 className="w-4 h-4 text-emerald-600" /> : <Circle className="w-4 h-4 text-slate-300" />}
              </div>
              <p className="text-[11px] text-slate-500 leading-tight">Panneaux, marquages, feux et agents de police.</p>
            </button>

            <button
              onClick={() => onStartQuiz(day1Questions.slice(0, 25), "Jour 1 • Quiz Signalisation")}
              className="p-3 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/40 text-left hover:border-emerald-300 transition"
            >
              <div className="flex items-center justify-between text-xs font-bold mb-1">
                <span className="text-slate-800 dark:text-slate-200">2. S'entraîner</span>
                {day1Prog.quizDone ? <CheckCircle2 className="w-4 h-4 text-emerald-600" /> : <Circle className="w-4 h-4 text-slate-300" />}
              </div>
              <p className="text-[11px] text-slate-500 leading-tight">25 questions types avec correction immédiate.</p>
            </button>

            <button
              onClick={() => onStartQuiz(day1Traps.slice(0, 15), "Jour 1 • Pièges de Signalisation")}
              className="p-3 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/40 text-left hover:border-emerald-300 transition"
            >
              <div className="flex items-center justify-between text-xs font-bold mb-1">
                <span className="text-slate-800 dark:text-slate-200">3. Pièges du Jour</span>
                {day1Prog.trapsDone ? <CheckCircle2 className="w-4 h-4 text-emerald-600" /> : <Circle className="w-4 h-4 text-slate-300" />}
              </div>
              <p className="text-[11px] text-slate-500 leading-tight">Multi-réponses, feux, B6a1 vs B6d, A18.</p>
            </button>
          </div>
        </div>

        {/* DAY 2 */}
        <div className={`rounded-3xl p-5 border transition ${
          currentDay === 2
            ? 'bg-white dark:bg-slate-900 border-emerald-500/60 shadow-md ring-1 ring-emerald-500/20'
            : 'bg-white/80 dark:bg-slate-900/60 border-slate-200 dark:border-slate-800 opacity-90'
        }`}>
          <div className="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-slate-800">
            <div className="flex items-center gap-2.5">
              <div className="w-9 h-9 rounded-xl bg-amber-100 dark:bg-amber-950 flex items-center justify-center text-amber-700 dark:text-amber-300 font-black text-sm">
                J2
              </div>
              <div>
                <h3 className="font-extrabold text-slate-900 dark:text-white text-base">
                  Jour 2 : Les Règles de Circulation
                </h3>
                <p className="text-xs text-slate-500">Chapitres III, IV, V • Priorités, dépassement, autoroute</p>
              </div>
            </div>
            <button
              onClick={() => onChangeDay(2)}
              className="text-xs font-bold text-emerald-600 hover:text-emerald-700"
            >
              {currentDay === 2 ? 'En cours' : 'Sélectionner'}
            </button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5 mt-4">
            <button
              onClick={() => onOpenRevisionTab('numbers')}
              className="p-3 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/40 text-left hover:border-emerald-300 transition"
            >
              <div className="flex items-center justify-between text-xs font-bold mb-1">
                <span className="text-slate-800 dark:text-slate-200">1. Apprendre</span>
                {day2Prog.learned ? <CheckCircle2 className="w-4 h-4 text-emerald-600" /> : <Circle className="w-4 h-4 text-slate-300" />}
              </div>
              <p className="text-[11px] text-slate-500 leading-tight">Intersections I1-I26, distances et vitesses.</p>
            </button>

            <button
              onClick={() => onStartQuiz(day2Questions.slice(0, 25), "Jour 2 • Quiz Circulation")}
              className="p-3 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/40 text-left hover:border-emerald-300 transition"
            >
              <div className="flex items-center justify-between text-xs font-bold mb-1">
                <span className="text-slate-800 dark:text-slate-200">2. S'entraîner</span>
                {day2Prog.quizDone ? <CheckCircle2 className="w-4 h-4 text-emerald-600" /> : <Circle className="w-4 h-4 text-slate-300" />}
              </div>
              <p className="text-[11px] text-slate-500 leading-tight">25 questions de manœuvres et carrefours.</p>
            </button>

            <button
              onClick={() => onStartQuiz(day2Traps.slice(0, 15), "Jour 2 • Pièges de Circulation")}
              className="p-3 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/40 text-left hover:border-emerald-300 transition"
            >
              <div className="flex items-center justify-between text-xs font-bold mb-1">
                <span className="text-slate-800 dark:text-slate-200">3. Pièges du Jour</span>
                {day2Prog.trapsDone ? <CheckCircle2 className="w-4 h-4 text-emerald-600" /> : <Circle className="w-4 h-4 text-slate-300" />}
              </div>
              <p className="text-[11px] text-slate-500 leading-tight">Pente, route en terre en ville vs rase campagne.</p>
            </button>
          </div>
        </div>

        {/* DAY 3 */}
        <div className={`rounded-3xl p-5 border transition ${
          currentDay === 3
            ? 'bg-white dark:bg-slate-900 border-emerald-500/60 shadow-md ring-1 ring-emerald-500/20'
            : 'bg-white/80 dark:bg-slate-900/60 border-slate-200 dark:border-slate-800 opacity-90'
        }`}>
          <div className="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-slate-800">
            <div className="flex items-center gap-2.5">
              <div className="w-9 h-9 rounded-xl bg-purple-100 dark:bg-purple-950 flex items-center justify-center text-purple-700 dark:text-purple-300 font-black text-sm">
                J3
              </div>
              <div>
                <h3 className="font-extrabold text-slate-900 dark:text-white text-base">
                  Jour 3 : Sécurité, Catégorie B & Examen
                </h3>
                <p className="text-xs text-slate-500">Chapitres VI, VIII, XI • Secourisme, entretien et examen blanc</p>
              </div>
            </div>
            <button
              onClick={() => onChangeDay(3)}
              className="text-xs font-bold text-emerald-600 hover:text-emerald-700"
            >
              {currentDay === 3 ? 'En cours' : 'Sélectionner'}
            </button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5 mt-4">
            <button
              onClick={() => onStartQuiz(day3Questions.slice(0, 25), "Jour 3 • Sécurité & Mécanique")}
              className="p-3 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/40 text-left hover:border-emerald-300 transition"
            >
              <div className="flex items-center justify-between text-xs font-bold mb-1">
                <span className="text-slate-800 dark:text-slate-200">1. Pratique & Sécurité</span>
                {day3Prog.quizDone ? <CheckCircle2 className="w-4 h-4 text-emerald-600" /> : <Circle className="w-4 h-4 text-slate-300" />}
              </div>
              <p className="text-[11px] text-slate-500 leading-tight">Secourisme PAS/PLS, moteur 4 temps, pneus.</p>
            </button>

            <button
              onClick={() => onStartQuiz(day3Traps.slice(0, 15), "Jour 3 • Pièges Finaux")}
              className="p-3 rounded-2xl border border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800/40 text-left hover:border-emerald-300 transition"
            >
              <div className="flex items-center justify-between text-xs font-bold mb-1">
                <span className="text-slate-800 dark:text-slate-200">2. Pièges Finaux</span>
                {day3Prog.trapsDone ? <CheckCircle2 className="w-4 h-4 text-emerald-600" /> : <Circle className="w-4 h-4 text-slate-300" />}
              </div>
              <p className="text-[11px] text-slate-500 leading-tight">Alcoolémie, 5 roues, chargement avant 0m.</p>
            </button>

            <button
              onClick={() => {
                const sample = [
                  ...day1Questions.slice(0, 15),
                  ...day2Questions.slice(0, 15),
                  ...day3Questions.slice(0, 10),
                ].sort(() => 0.5 - Math.random());
                onStartQuiz(sample, "Examen Blanc Officiel DGTT", true);
              }}
              className="p-3 rounded-2xl border border-emerald-300 dark:border-emerald-800 bg-emerald-50/60 dark:bg-emerald-950/40 text-left hover:bg-emerald-100/60 transition"
            >
              <div className="flex items-center justify-between text-xs font-extrabold text-emerald-800 dark:text-emerald-300 mb-1">
                <span>3. Examen Blanc</span>
                <Clock className="w-4 h-4 text-emerald-600" />
              </div>
              <p className="text-[11px] text-emerald-700 dark:text-emerald-400 font-medium leading-tight">
                40 questions chrono en 30 min (seuil 35/40).
              </p>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

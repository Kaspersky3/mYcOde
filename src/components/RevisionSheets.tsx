import React, { useState } from 'react';
import { CourseDefinition, Abbreviation, KeyNumber, AmbiguityItem, Question } from '../types';
import { TrafficSign } from './TrafficSign';
import { 
  AlertTriangle, 
  HelpCircle, 
  Hash, 
  BookMarked, 
  Search, 
  ShieldAlert, 
  Check, 
  Lightbulb,
  FileText
} from 'lucide-react';

interface RevisionSheetsProps {
  initialTab?: 'attention' | 'traps' | 'numbers' | 'ambiguities';
  courseContent: {
    abbreviations: Abbreviation[];
    definitions: CourseDefinition[];
    chiffresCles: KeyNumber[];
  };
  ambiguites: AmbiguityItem[];
  questions: Question[];
  onStartQuizWithQuestions: (questions: Question[], title: string) => void;
}

export const RevisionSheets: React.FC<RevisionSheetsProps> = ({
  initialTab = 'attention',
  courseContent,
  ambiguites,
  questions,
  onStartQuizWithQuestions,
}) => {
  const [activeTab, setActiveTab] = useState<'attention' | 'traps' | 'numbers' | 'ambiguities'>(initialTab);
  const [searchTerm, setSearchTerm] = useState('');

  // Pre-filter traps from questions
  const trapQuestions = questions.filter(
    (q) => q.tags.includes('piege') || q.multiReponses || q.tags.includes('ambiguite')
  );

  return (
    <div className="space-y-5 animate-fade-in pb-16">
      {/* Tab Switcher */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-1.5 p-1.5 bg-slate-100 dark:bg-slate-800/80 rounded-2xl">
        <button
          onClick={() => setActiveTab('attention')}
          className={`py-2.5 px-3 rounded-xl text-xs font-bold transition flex items-center justify-center gap-1.5 ${
            activeTab === 'attention'
              ? 'bg-white dark:bg-slate-900 text-emerald-700 dark:text-emerald-400 shadow-sm'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
          }`}
        >
          <BookMarked className="w-4 h-4" />
          <span>Points d'Attention</span>
        </button>

        <button
          onClick={() => setActiveTab('traps')}
          className={`py-2.5 px-3 rounded-xl text-xs font-bold transition flex items-center justify-center gap-1.5 ${
            activeTab === 'traps'
              ? 'bg-white dark:bg-slate-900 text-rose-700 dark:text-rose-400 shadow-sm'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
          }`}
        >
          <AlertTriangle className="w-4 h-4" />
          <span>Pièges Fréquents</span>
        </button>

        <button
          onClick={() => setActiveTab('numbers')}
          className={`py-2.5 px-3 rounded-xl text-xs font-bold transition flex items-center justify-center gap-1.5 ${
            activeTab === 'numbers'
              ? 'bg-white dark:bg-slate-900 text-blue-700 dark:text-blue-400 shadow-sm'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
          }`}
        >
          <Hash className="w-4 h-4" />
          <span>Chiffres & Règles</span>
        </button>

        <button
          onClick={() => setActiveTab('ambiguities')}
          className={`py-2.5 px-3 rounded-xl text-xs font-bold transition flex items-center justify-center gap-1.5 ${
            activeTab === 'ambiguities'
              ? 'bg-white dark:bg-slate-900 text-purple-700 dark:text-purple-400 shadow-sm'
              : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
          }`}
        >
          <ShieldAlert className="w-4 h-4" />
          <span>Ambiguïtés DGTT</span>
        </button>
      </div>

      {/* Search Input */}
      <div className="relative">
        <Search className="w-4 h-4 absolute left-3.5 top-3.5 text-slate-400" />
        <input
          type="text"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Rechercher une règle, un panneau, un chiffre..."
          className="w-full pl-10 pr-4 py-2.5 rounded-2xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 text-sm text-slate-900 dark:text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-emerald-500"
        />
      </div>

      {/* TAB 1: POINTS D'ATTENTION (Une règle = Une carte) */}
      {activeTab === 'attention' && (
        <div className="space-y-4">
          <div className="p-4 rounded-2xl bg-emerald-50/70 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800">
            <h3 className="font-extrabold text-emerald-950 dark:text-emerald-200 text-sm flex items-center gap-2">
              <Lightbulb className="w-4 h-4 text-emerald-600" />
              Principes fondamentaux du code béninois
            </h3>
            <p className="text-xs text-emerald-800 dark:text-emerald-300 mt-1">
              Chaque carte résume une règle essentielle extraite des chapitres I à VI du manuel officiel.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {courseContent.definitions
              .filter((d) => !searchTerm || d.titre.toLowerCase().includes(searchTerm.toLowerCase()) || d.contenu.toLowerCase().includes(searchTerm.toLowerCase()))
              .map((def, idx) => (
                <div key={idx} className="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm space-y-2">
                  <div className="flex items-center gap-2">
                    <span className="w-6 h-6 rounded-lg bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 font-extrabold text-xs flex items-center justify-center">
                      {idx + 1}
                    </span>
                    <h4 className="font-bold text-slate-900 dark:text-white text-sm">{def.titre}</h4>
                  </div>
                  <p className="text-xs text-slate-600 dark:text-slate-300 whitespace-pre-line leading-relaxed">
                    {def.contenu}
                  </p>
                </div>
              ))}
          </div>

          {/* Abréviations officielles */}
          <div className="mt-6 bg-white dark:bg-slate-900 p-5 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm">
            <h4 className="font-bold text-slate-900 dark:text-white text-sm mb-3 flex items-center gap-2">
              <FileText className="w-4 h-4 text-emerald-600" />
              Abréviations officielles du Manuel (Page 3)
            </h4>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs">
              {courseContent.abbreviations.map((abbr, i) => (
                <div key={i} className="flex items-center justify-between p-2 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-100 dark:border-slate-800">
                  <span className="font-extrabold text-emerald-700 dark:text-emerald-400">{abbr.sigle}</span>
                  <span className="text-slate-600 dark:text-slate-300 text-right">{abbr.definition}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: PIÈGES FRÉQUENTS */}
      {activeTab === 'traps' && (
        <div className="space-y-4">
          <div className="p-4 rounded-2xl bg-rose-50/70 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-900 flex items-start justify-between gap-3">
            <div>
              <h3 className="font-extrabold text-rose-950 dark:text-rose-200 text-sm flex items-center gap-2">
                <AlertTriangle className="w-4 h-4 text-rose-600" />
                Pièges Fréquents à l'Examen DGTT
              </h3>
              <p className="text-xs text-rose-800 dark:text-rose-300 mt-1">
                La majorité des échecs provient des questions à <strong>plusieurs réponses valides</strong> et des subtilités de formulation.
              </p>
            </div>
            <button
              onClick={() => onStartQuizWithQuestions(trapQuestions.slice(0, 20), "Défi Spécial Pièges")}
              className="flex-shrink-0 px-3 py-2 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs shadow-sm"
            >
              Tester les 20 pièges
            </button>
          </div>

          <div className="space-y-3">
            {/* Piège 1 */}
            <div className="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm space-y-2">
              <div className="flex items-center gap-2 text-rose-600 dark:text-rose-400 font-bold text-xs">
                <span>⚠️ PIÈGE N°1</span>
                <span className="text-slate-400">•</span>
                <span>Signalisation horizontale</span>
              </div>
              <h4 className="font-extrabold text-slate-900 dark:text-white text-sm">
                Panneau B6a1 (Stationnement interdit) vs Panneau B6d (Arrêt et stationnement interdits)
              </h4>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 my-2">
                <div className="flex items-center gap-3 p-3 rounded-xl bg-slate-50 dark:bg-slate-800/40 border border-slate-200 dark:border-slate-700">
                  <TrafficSign code="B6a1" zoomable={false} />
                  <div className="text-xs">
                    <p className="font-bold text-slate-900 dark:text-white">B6a1 : 1 barre oblique</p>
                    <p className="text-slate-500">Seul le <strong>stationnement</strong> est interdit à partir du panneau. <strong>L'arrêt reste autorisé !</strong></p>
                  </div>
                </div>
                <div className="flex items-center gap-3 p-3 rounded-xl bg-slate-50 dark:bg-slate-800/40 border border-slate-200 dark:border-slate-700">
                  <TrafficSign code="B6d" zoomable={false} />
                  <div className="text-xs">
                    <p className="font-bold text-slate-900 dark:text-white">B6d : Croix rouge (2 barres)</p>
                    <p className="text-slate-500"><strong>L'arrêt ET le stationnement</strong> sont formellement interdits.</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Piège 2 */}
            <div className="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm space-y-2">
              <div className="flex items-center gap-2 text-rose-600 dark:text-rose-400 font-bold text-xs">
                <span>⚠️ PIÈGE N°2</span>
                <span className="text-slate-400">•</span>
                <span>Distance d'effet d'un panneau de danger</span>
              </div>
              <h4 className="font-extrabold text-slate-900 dark:text-white text-sm">
                L'exception unique du panneau A18 (Circulation dans les deux sens)
              </h4>
              <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                Normalement, un panneau triangulaire de danger est placé à <strong>50 mètres</strong> en agglomération et à <strong>150 mètres</strong> en rase campagne.
                <br />
                <strong>LE PIÈGE :</strong> Le panneau <strong>A18</strong> (circulation dans les deux sens avec deux flèches en sens opposé) prend effet <strong>immédiatement à hauteur du panneau (0 mètre)</strong> !
              </p>
            </div>

            {/* Piège 3 */}
            <div className="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm space-y-2">
              <div className="flex items-center gap-2 text-rose-600 dark:text-rose-400 font-bold text-xs">
                <span>⚠️ PIÈGE N°3</span>
                <span className="text-slate-400">•</span>
                <span>Croisement difficile en pente</span>
              </div>
              <h4 className="font-extrabold text-slate-900 dark:text-white text-sm">
                Qui doit s'arrêter ou reculer dans une pente ?
              </h4>
              <div className="text-xs text-slate-600 dark:text-slate-300 space-y-1">
                <p>• <strong>Véhicule qui s'arrête :</strong> Le véhicule <strong>descendant</strong> doit toujours s'arrêter à temps pour laisser passer le véhicule montant (plus difficile à relancer).</p>
                <p>• <strong>Marche arrière obligatoire :</strong> A gabarit égal, c'est le <strong>descendant</strong> qui recule. Mais entre un véhicule isolé et un ensemble articulé (avec remorque), c'est <strong>l'isolé</strong> qui recule !</p>
              </div>
            </div>

            {/* Piège 4 */}
            <div className="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm space-y-2">
              <div className="flex items-center gap-2 text-rose-600 dark:text-rose-400 font-bold text-xs">
                <span>⚠️ PIÈGE N°4</span>
                <span className="text-slate-400">•</span>
                <span>Dépassement du chargement</span>
              </div>
              <h4 className="font-extrabold text-slate-900 dark:text-white text-sm">
                Transport d'objets longs (ex : échelle de 5m sur voiture de 4m)
              </h4>
              <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
                Le chargement ne doit <strong>JAMAIS dépasser à l'avant (0 mètre)</strong>. Tout dépassement s'effectue exclusivement à l'arrière, dans la limite de <strong>3 mètres</strong>. Au-delà de 1 mètre, il doit obligatoirement être signalé.
              </p>
            </div>
          </div>
        </div>
      )}

      {/* TAB 3: CHIFFRES & RÈGLES À RETENIR */}
      {activeTab === 'numbers' && (
        <div className="space-y-4">
          <div className="p-4 rounded-2xl bg-blue-50/70 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-900">
            <h3 className="font-extrabold text-blue-950 dark:text-blue-200 text-sm flex items-center gap-2">
              <Hash className="w-4 h-4 text-blue-600" />
              Tous les Chiffres Officiels du Manuel DGTT 2011 à retenir par cœur
            </h3>
            <p className="text-xs text-blue-800 dark:text-blue-300 mt-1">
              Les inspecteurs de la DGTT posent de nombreuses questions chiffrées précises.
            </p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {courseContent.chiffresCles
              .filter((c) => !searchTerm || c.label.toLowerCase().includes(searchTerm.toLowerCase()) || c.valeur.toLowerCase().includes(searchTerm.toLowerCase()))
              .map((item, idx) => (
                <div key={idx} className="bg-white dark:bg-slate-900 p-3.5 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm flex items-center justify-between gap-3">
                  <div className="space-y-0.5">
                    <p className="text-xs font-bold text-slate-800 dark:text-slate-200">{item.label}</p>
                    <p className="text-[11px] text-slate-500">{item.contexte}</p>
                  </div>
                  <div className="flex-shrink-0 px-3 py-1.5 rounded-xl bg-blue-50 dark:bg-blue-950/80 text-blue-700 dark:text-blue-300 font-black text-sm border border-blue-200 dark:border-blue-800 text-right">
                    {item.valeur}
                  </div>
                </div>
              ))}
          </div>
        </div>
      )}

      {/* TAB 4: AMBIGUÏTÉS DGTT */}
      {activeTab === 'ambiguities' && (
        <div className="space-y-4">
          <div className="p-4 rounded-2xl bg-purple-50/70 dark:bg-purple-950/30 border border-purple-200 dark:border-purple-900">
            <h3 className="font-extrabold text-purple-950 dark:text-purple-200 text-sm flex items-center gap-2">
              <ShieldAlert className="w-4 h-4 text-purple-600" />
              Points d'Ambiguïté et Cas Particuliers du Manuel
            </h3>
            <p className="text-xs text-purple-800 dark:text-purple-300 mt-1">
              Certaines questions du manuel de 2011 comportent des coquilles ou des contradictions. Voici comment les aborder à l'examen.
            </p>
          </div>

          <div className="space-y-3">
            {ambiguites.map((amb) => (
              <div key={amb.id} className="bg-white dark:bg-slate-900 p-4 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm space-y-2">
                <div className="flex items-center justify-between gap-2">
                  <span className="text-xs font-extrabold text-purple-700 dark:text-purple-400">
                    Question(s) n°{amb.questions.join(', ')}
                  </span>
                  <span className="text-[10px] uppercase font-bold px-2 py-0.5 rounded bg-purple-100 dark:bg-purple-950 text-purple-800 dark:text-purple-300">
                    {amb.statut}
                  </span>
                </div>
                <h4 className="font-bold text-slate-900 dark:text-white text-sm">{amb.titre}</h4>
                <p className="text-xs text-slate-600 dark:text-slate-300 leading-relaxed bg-slate-50 dark:bg-slate-800/40 p-2.5 rounded-xl border border-slate-100 dark:border-slate-800">
                  {amb.description}
                </p>
                <div className="pt-1 text-xs">
                  <span className="font-bold text-emerald-700 dark:text-emerald-400">Ce qu'il faut retenir : </span>
                  <span className="text-slate-700 dark:text-slate-200 font-medium">{amb.regleOfficielle}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

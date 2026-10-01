import React, { useState } from 'react';
import { ZoomIn, X } from 'lucide-react';

interface TrafficSignProps {
  code?: string | null;
  className?: string;
  zoomable?: boolean;
}

export const TrafficSign: React.FC<TrafficSignProps> = ({ code, className = '', zoomable = true }) => {
  const [isOpen, setIsOpen] = useState(false);

  if (!code) return null;

  const renderSign = () => {
    switch (code) {
      // PANNEAUX DE DANGER (Triangles listel rouge fond blanc/jaune)
      case 'A1c': // Virages 1er à droite
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <path d="M42 66 L42 54 C42 46 58 48 58 40 L58 28" fill="none" stroke="#1e293b" strokeWidth="5" strokeLinecap="round" />
            <polyline points="53,33 58,26 63,33" fill="none" stroke="#1e293b" strokeWidth="5" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        );

      case 'A1d':
      case 'A1d_500m':
        return (
          <div className="flex flex-col items-center">
            <svg viewBox="0 0 100 90" className="w-24 h-24">
              <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
              <path d="M58 66 L58 54 C58 46 42 48 42 40 L42 28" fill="none" stroke="#1e293b" strokeWidth="5" strokeLinecap="round" />
              <polyline points="47,33 42,26 37,33" fill="none" stroke="#1e293b" strokeWidth="5" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
            {code === 'A1d_500m' && (
              <div className="mt-1 px-3 py-0.5 border-2 border-slate-700 bg-white text-slate-900 font-bold text-xs rounded">
                500m
              </div>
            )}
          </div>
        );

      case 'A1d1':
        return (
          <div className="flex flex-col items-center">
            <svg viewBox="0 0 100 90" className="w-24 h-24">
              <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
              <path d="M58 66 L58 54 C58 46 42 48 42 40 L42 28" fill="none" stroke="#1e293b" strokeWidth="5" strokeLinecap="round" />
            </svg>
            <div className="mt-1 px-3 py-0.5 border-2 border-slate-700 bg-white text-slate-900 font-bold text-xs rounded flex items-center gap-1">
              <span>↑</span> 5 Km <span>↑</span>
            </div>
          </div>
        );

      case 'A3':
      case 'A3a1':
        return (
          <div className="flex flex-col items-center">
            <svg viewBox="0 0 100 90" className="w-24 h-24">
              <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
              <path d="M38 68 L38 32 M62 68 L50 48 L50 32" fill="none" stroke="#1e293b" strokeWidth="6" strokeLinecap="round" />
            </svg>
            {code === 'A3a1' && (
              <div className="mt-1 px-3 py-0.5 border-2 border-slate-700 bg-white text-slate-900 font-bold text-xs rounded">
                200m
              </div>
            )}
          </div>
        );

      case 'A6': // Pont mobile
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <path d="M30 65 L44 65 L56 50 M44 65 L70 65" stroke="#1e293b" strokeWidth="4" />
            <path d="M32 72 Q 40 68 48 72 T 64 72" fill="none" stroke="#0284c7" strokeWidth="3" />
          </svg>
        );

      case 'A7':
      case 'A7_1':
        return (
          <div className="flex flex-col items-center">
            <svg viewBox="0 0 100 90" className="w-24 h-24">
              <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
              <rect x="36" y="44" width="28" height="24" fill="none" stroke="#1e293b" strokeWidth="3" />
              <line x1="36" y1="52" x2="64" y2="52" stroke="#1e293b" strokeWidth="2" />
              <line x1="36" y1="60" x2="64" y2="60" stroke="#1e293b" strokeWidth="2" />
              <line x1="43" y1="44" x2="43" y2="68" stroke="#1e293b" strokeWidth="2" />
              <line x1="57" y1="44" x2="57" y2="68" stroke="#1e293b" strokeWidth="2" />
            </svg>
            {code === 'A7_1' && (
              <div className="mt-1 px-2 py-0.5 border border-slate-700 bg-white text-[10px] font-bold text-center leading-tight">
                SIGNAL<br />AUTOMATIQUE
              </div>
            )}
          </div>
        );

      case 'A8': // Train sans barrière
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <path d="M38 65 L62 65 L60 48 L40 48 Z" fill="#1e293b" />
            <circle cx="44" cy="67" r="4" fill="#64748b" />
            <circle cx="56" cy="67" r="4" fill="#64748b" />
            <rect x="42" y="38" width="6" height="10" fill="#1e293b" />
            <circle cx="50" cy="54" r="3" fill="#facc15" />
          </svg>
        );

      case 'A13a': // Enfants
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <circle cx="44" cy="40" r="4" fill="#1e293b" />
            <path d="M44 45 L44 60 M38 52 L50 52 M44 60 L40 70 M44 60 L48 70" stroke="#1e293b" strokeWidth="3" strokeLinecap="round" />
            <circle cx="58" cy="48" r="3" fill="#1e293b" />
            <path d="M58 52 L58 64 M54 57 L62 57 M58 64 L55 70 M58 64 L61 70" stroke="#1e293b" strokeWidth="2.5" strokeLinecap="round" />
          </svg>
        );

      case 'A13b': // Piétons
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <circle cx="50" cy="38" r="4" fill="#1e293b" />
            <path d="M50 43 L50 58 M42 49 L58 49 M50 58 L44 70 M50 58 L56 70" stroke="#1e293b" strokeWidth="3.5" strokeLinecap="round" />
            <line x1="36" y1="72" x2="64" y2="72" stroke="#1e293b" strokeWidth="3" strokeDasharray="4 3" />
          </svg>
        );

      case 'A14': // Danger autre (!)
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <rect x="47" y="34" width="6" height="24" rx="3" fill="#1e293b" />
            <circle cx="50" cy="68" r="3.5" fill="#1e293b" />
          </svg>
        );

      case 'A15a1': // Animaux domestiques
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <path d="M38 52 C38 48 42 46 48 46 L60 46 C64 46 66 48 66 52 L66 60 L62 60 L62 70 L58 70 L58 60 L46 60 L46 70 L42 70 L42 60 Z" fill="#1e293b" />
          </svg>
        );

      case 'A15c': // Cavaliers
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <circle cx="52" cy="38" r="3" fill="#1e293b" />
            <path d="M40 54 L62 54 L66 68 M44 68 L48 54" stroke="#1e293b" strokeWidth="3" />
          </svg>
        );

      case 'A16': // Descente dangereuse 10%
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <polygon points="36,66 66,66 66,48" fill="#1e293b" />
            <text x="50" y="63" fill="#ffffff" fontSize="9" fontWeight="bold" textAnchor="middle">10%</text>
          </svg>
        );

      case 'A18': // Circulation double sens
      case 'A18_1':
        return (
          <div className="flex flex-col items-center">
            <svg viewBox="0 0 100 90" className="w-24 h-24">
              <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
              {/* Flèche montante gauche */}
              <line x1="43" y1="68" x2="43" y2="40" stroke="#1e293b" strokeWidth="4" />
              <polygon points="43,34 38,42 48,42" fill="#1e293b" />
              {/* Flèche descendante droite */}
              <line x1="57" y1="40" x2="57" y2="68" stroke="#1e293b" strokeWidth="4" />
              <polygon points="57,74 52,66 62,66" fill="#1e293b" />
            </svg>
            {code === 'A18_1' && (
              <div className="mt-1 px-3 py-0.5 border-2 border-slate-700 bg-white text-slate-900 font-bold text-xs rounded">
                150m
              </div>
            )}
          </div>
        );

      case 'A19': // Chute de pierres
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <polygon points="36,70 56,42 66,70" fill="#1e293b" />
            <circle cx="58" cy="50" r="2.5" fill="#dc2626" />
            <circle cx="62" cy="56" r="2" fill="#dc2626" />
          </svg>
        );

      case 'A20': // Débouché sur quai
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <rect x="34" y="58" width="16" height="12" fill="#1e293b" />
            <path d="M50 58 L58 48 L64 54" stroke="#1e293b" strokeWidth="3" />
            <path d="M30 72 Q 40 68 50 72 T 70 72" fill="none" stroke="#0284c7" strokeWidth="3" />
          </svg>
        );

      case 'A21a':
      case 'A21b':
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <circle cx="42" cy="60" r="7" fill="none" stroke="#1e293b" strokeWidth="2.5" />
            <circle cx="58" cy="60" r="7" fill="none" stroke="#1e293b" strokeWidth="2.5" />
            <path d="M42 60 L48 50 L56 50 L58 60 M48 50 L54 60 M52 46 L58 46" fill="none" stroke="#1e293b" strokeWidth="2" />
          </svg>
        );

      case 'A25': // Sens giratoire triangle
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <circle cx="50" cy="54" r="14" fill="none" stroke="#1e293b" strokeWidth="3.5" strokeDasharray="16 10" />
            <polygon points="62,44 68,48 64,54" fill="#1e293b" />
          </svg>
        );

      // PANNEAUX DE TRAVAUX (AK Fond Jaune)
      case 'AK4': // Chaussée glissante temporaire
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#facc15" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <path d="M42 58 C46 54 44 48 50 46" stroke="#1e293b" strokeWidth="3" fill="none" />
            <path d="M54 62 C58 58 56 52 62 50" stroke="#1e293b" strokeWidth="3" fill="none" />
          </svg>
        );

      case 'AK5': // Travaux
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#facc15" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <circle cx="52" cy="38" r="3.5" fill="#1e293b" />
            <path d="M50 44 L44 56 L38 56 M44 56 L44 68 M48 48 L56 58 L62 58" stroke="#1e293b" strokeWidth="3" strokeLinecap="round" />
            <line x1="36" y1="70" x2="66" y2="70" stroke="#1e293b" strokeWidth="3" />
          </svg>
        );

      case 'AK22': // Gravillons
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#facc15" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <rect x="36" y="52" width="16" height="8" rx="2" fill="#1e293b" />
            <circle cx="58" cy="62" r="2" fill="#1e293b" />
            <circle cx="62" cy="58" r="1.5" fill="#1e293b" />
            <circle cx="66" cy="64" r="2" fill="#1e293b" />
          </svg>
        );

      // PANNEAUX DE PRIORITÉ
      case 'AB1': // Priorité à droite
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            <line x1="36" y1="40" x2="64" y2="68" stroke="#1e293b" strokeWidth="6" strokeLinecap="round" />
            <line x1="64" y1="40" x2="36" y2="68" stroke="#1e293b" strokeWidth="6" strokeLinecap="round" />
          </svg>
        );

      case 'AB2': // Flèche barrée (Priorité ponctuelle)
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,6 94,84 6,84" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
            {/* Axe prioritaire */}
            <path d="M50 70 L50 40 M50 34 L42 44 M50 34 L58 44" fill="none" stroke="#1e293b" strokeWidth="7" strokeLinecap="round" strokeLinejoin="round" />
            {/* Voie secondaire barrée */}
            <line x1="36" y1="52" x2="64" y2="52" stroke="#dc2626" strokeWidth="4" />
          </svg>
        );

      case 'AB3a': // Cédez le passage
        return (
          <svg viewBox="0 0 100 90" className="w-full h-full">
            <polygon points="50,84 6,6 94,6" fill="#ffffff" stroke="#dc2626" strokeWidth="9" strokeLinejoin="round" />
          </svg>
        );

      case 'AB4_STOP': // STOP
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <polygon points="30,5 70,5 95,30 95,70 70,95 30,95 5,70 5,30" fill="#dc2626" stroke="#ffffff" strokeWidth="4" />
            <text x="50" y="60" fill="#ffffff" fontSize="24" fontWeight="900" fontFamily="sans-serif" textAnchor="middle">STOP</text>
          </svg>
        );

      case 'AB6': // Route prioritaire (losange jaune)
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <polygon points="50,8 92,50 50,92 8,50" fill="#ffffff" stroke="#1e293b" strokeWidth="2" />
            <polygon points="50,18 82,50 50,82 18,50" fill="#facc15" stroke="#f59e0b" strokeWidth="1" />
          </svg>
        );

      case 'AB7': // Fin de route prioritaire (losange barré)
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <polygon points="50,8 92,50 50,92 8,50" fill="#ffffff" stroke="#1e293b" strokeWidth="2" />
            <polygon points="50,18 82,50 50,82 18,50" fill="#facc15" stroke="#f59e0b" strokeWidth="1" />
            <line x1="20" y1="80" x2="80" y2="20" stroke="#1e293b" strokeWidth="8" />
          </svg>
        );

      // PANNEAUX DE PRESCRIPTION (Ronds)
      case 'B0': // Circulation interdite 2 sens
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
          </svg>
        );

      case 'B1': // Sens interdit
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#dc2626" stroke="#ffffff" strokeWidth="2" />
            <rect x="20" y="42" width="60" height="16" fill="#ffffff" rx="2" />
          </svg>
        );

      case 'B2a': // Interdit à gauche
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <path d="M54 70 L54 44 L38 44" fill="none" stroke="#1e293b" strokeWidth="6" strokeLinecap="round" />
            <polyline points="44,38 36,44 44,50" fill="none" stroke="#1e293b" strokeWidth="6" strokeLinecap="round" strokeLinejoin="round" />
            <line x1="24" y1="24" x2="76" y2="76" stroke="#dc2626" strokeWidth="8" />
          </svg>
        );

      case 'B2b': // Interdit à droite
      case 'B2b_6t':
        return (
          <div className="flex flex-col items-center">
            <svg viewBox="0 0 100 100" className="w-24 h-24">
              <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
              <path d="M46 70 L46 44 L62 44" fill="none" stroke="#1e293b" strokeWidth="6" strokeLinecap="round" />
              <polyline points="56,38 64,44 56,50" fill="none" stroke="#1e293b" strokeWidth="6" strokeLinecap="round" strokeLinejoin="round" />
              <line x1="24" y1="24" x2="76" y2="76" stroke="#dc2626" strokeWidth="8" />
            </svg>
            {code === 'B2b_6t' && (
              <div className="mt-1 px-3 py-0.5 border border-slate-700 bg-white text-slate-900 font-bold text-xs rounded">
                6t
              </div>
            )}
          </div>
        );

      case 'B2c': // Demi-tour interdit
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <path d="M60 68 L60 46 C60 34 40 34 40 46 L40 64" fill="none" stroke="#1e293b" strokeWidth="6" strokeLinecap="round" />
            <polyline points="34,58 40,66 46,58" fill="none" stroke="#1e293b" strokeWidth="6" strokeLinecap="round" strokeLinejoin="round" />
            <line x1="24" y1="24" x2="76" y2="76" stroke="#dc2626" strokeWidth="8" />
          </svg>
        );

      case 'B3': // Interdiction de dépasser
      case 'B3_fin':
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <rect x="26" y="42" width="20" height="16" rx="3" fill="#dc2626" />
            <rect x="54" y="42" width="20" height="16" rx="3" fill="#1e293b" />
          </svg>
        );

      case 'B3a': // Dépassement camions
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <rect x="22" y="38" width="26" height="22" rx="3" fill="#dc2626" />
            <rect x="54" y="44" width="20" height="16" rx="3" fill="#1e293b" />
          </svg>
        );

      case 'B5c': // Arrêt péage
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <text x="50" y="44" fill="#1e293b" fontSize="13" fontWeight="bold" textAnchor="middle">HALTE</text>
            <line x1="25" y1="50" x2="75" y2="50" stroke="#1e293b" strokeWidth="2" />
            <text x="50" y="66" fill="#1e293b" fontSize="13" fontWeight="bold" textAnchor="middle">PEAGE</text>
          </svg>
        );

      case 'B6a1': // Stationnement interdit
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#1d4ed8" stroke="#dc2626" strokeWidth="10" />
            <line x1="22" y1="22" x2="78" y2="78" stroke="#dc2626" strokeWidth="8" />
          </svg>
        );

      case 'B6a1_1': // Zone bleue
        return (
          <div className="flex flex-col items-center">
            <svg viewBox="0 0 100 100" className="w-24 h-24">
              <circle cx="50" cy="50" r="44" fill="#1d4ed8" stroke="#dc2626" strokeWidth="10" />
              <line x1="22" y1="22" x2="78" y2="78" stroke="#dc2626" strokeWidth="8" />
            </svg>
            <div className="mt-1 w-6 h-6 bg-slate-900 rounded-sm flex items-center justify-center">
              <span className="text-[10px] text-white font-bold">P</span>
            </div>
          </div>
        );

      case 'B6b1': // Zone stationnement interdit
        return (
          <div className="p-2 border-2 border-slate-700 bg-white rounded flex flex-col items-center">
            <svg viewBox="0 0 100 100" className="w-16 h-16">
              <circle cx="50" cy="50" r="44" fill="#1d4ed8" stroke="#dc2626" strokeWidth="10" />
              <line x1="22" y1="22" x2="78" y2="78" stroke="#dc2626" strokeWidth="8" />
            </svg>
            <span className="text-[10px] font-bold text-slate-800 uppercase mt-1">Zone</span>
          </div>
        );

      case 'B6d': // Arrêt et stationnement interdits
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#1d4ed8" stroke="#dc2626" strokeWidth="10" />
            <line x1="22" y1="22" x2="78" y2="78" stroke="#dc2626" strokeWidth="8" />
            <line x1="78" y1="22" x2="22" y2="78" stroke="#dc2626" strokeWidth="8" />
          </svg>
        );

      case 'B7a': // Interdit autos et motos
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <rect x="36" y="30" width="28" height="18" rx="3" fill="#1e293b" />
            <circle cx="42" cy="66" r="6" stroke="#1e293b" strokeWidth="2" fill="none" />
            <circle cx="58" cy="66" r="6" stroke="#1e293b" strokeWidth="2" fill="none" />
          </svg>
        );

      case 'B7b': // Interdit véhicules moteur
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <rect x="36" y="32" width="28" height="16" rx="3" fill="#1e293b" />
            <circle cx="44" cy="66" r="5" stroke="#1e293b" strokeWidth="2" fill="none" />
            <circle cx="56" cy="66" r="5" stroke="#1e293b" strokeWidth="2" fill="none" />
          </svg>
        );

      case 'B8': // Interdit camions marchandises
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <rect x="28" y="38" width="30" height="20" fill="#1e293b" />
            <rect x="58" y="44" width="14" height="14" fill="#1e293b" />
            <circle cx="36" cy="64" r="5" fill="#64748b" />
            <circle cx="64" cy="64" r="5" fill="#64748b" />
          </svg>
        );

      case 'B9c': // Traction animale
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <rect x="30" y="45" width="24" height="14" fill="#1e293b" />
            <circle cx="34" cy="62" r="5" fill="#1e293b" />
            <circle cx="48" cy="62" r="5" fill="#1e293b" />
          </svg>
        );

      case 'B9g': // Interdit cyclomoteurs
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <circle cx="36" cy="56" r="8" stroke="#1e293b" strokeWidth="2.5" fill="none" />
            <circle cx="64" cy="56" r="8" stroke="#1e293b" strokeWidth="2.5" fill="none" />
            <path d="M36 56 L48 46 L60 46 L64 56" stroke="#1e293b" strokeWidth="2.5" fill="none" />
          </svg>
        );

      case 'B10a': // Longueur > 10m
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <rect x="28" y="40" width="44" height="18" fill="#1e293b" />
            <text x="50" y="54" fill="#ffffff" fontSize="10" fontWeight="bold" textAnchor="middle">◀ 10m ▶</text>
          </svg>
        );

      case 'B13': // Poids > 5,5T
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <text x="50" y="58" fill="#1e293b" fontSize="24" fontWeight="bold" textAnchor="middle">5,5t</text>
          </svg>
        );

      case 'B14_50': // Limitation vitesse 50
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <text x="50" y="60" fill="#1e293b" fontSize="34" fontWeight="bold" fontFamily="sans-serif" textAnchor="middle">50</text>
          </svg>
        );

      case 'B14_3': // Limitation 60 panonceau moto
        return (
          <div className="flex flex-col items-center">
            <svg viewBox="0 0 100 100" className="w-24 h-24">
              <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
              <text x="50" y="60" fill="#1e293b" fontSize="34" fontWeight="bold" textAnchor="middle">60</text>
            </svg>
            <div className="mt-1 px-3 py-1 border border-slate-700 bg-white rounded flex items-center justify-center">
              <span className="text-xs">🏍️</span>
            </div>
          </div>
        );

      case 'B14_4': // Limitation 50 panonceau camion
        return (
          <div className="flex flex-col items-center">
            <svg viewBox="0 0 100 100" className="w-24 h-24">
              <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
              <text x="50" y="60" fill="#1e293b" fontSize="34" fontWeight="bold" textAnchor="middle">50</text>
            </svg>
            <div className="mt-1 px-3 py-1 border border-slate-700 bg-white rounded flex items-center justify-center">
              <span className="text-xs">🚚</span>
            </div>
          </div>
        );

      case 'B14_300m': // Limitation 50 panonceau 300m fléché
        return (
          <div className="flex flex-col items-center">
            <svg viewBox="0 0 100 100" className="w-24 h-24">
              <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
              <text x="50" y="60" fill="#1e293b" fontSize="34" fontWeight="bold" textAnchor="middle">50</text>
            </svg>
            <div className="mt-1 px-3 py-0.5 border-2 border-slate-700 bg-white text-slate-900 font-bold text-xs rounded flex items-center gap-1">
              <span>↑</span> 300m <span>↑</span>
            </div>
          </div>
        );

      case 'B14_B25': // 50 et 30 min
        return (
          <div className="flex flex-col gap-1 items-center">
            <svg viewBox="0 0 100 100" className="w-16 h-16">
              <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
              <text x="50" y="60" fill="#1e293b" fontSize="34" fontWeight="bold" textAnchor="middle">50</text>
            </svg>
            <svg viewBox="0 0 100 100" className="w-16 h-16">
              <circle cx="50" cy="50" r="44" fill="#1d4ed8" stroke="#ffffff" strokeWidth="3" />
              <text x="50" y="60" fill="#ffffff" fontSize="34" fontWeight="bold" textAnchor="middle">30</text>
            </svg>
          </div>
        );

      case 'B14_B8': // 50 et camion
        return (
          <div className="flex flex-col gap-1 items-center">
            <svg viewBox="0 0 100 100" className="w-16 h-16">
              <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
              <text x="50" y="60" fill="#1e293b" fontSize="34" fontWeight="bold" textAnchor="middle">50</text>
            </svg>
            <svg viewBox="0 0 100 100" className="w-16 h-16">
              <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
              <rect x="28" y="38" width="30" height="20" fill="#1e293b" />
              <rect x="58" y="44" width="14" height="14" fill="#1e293b" />
            </svg>
          </div>
        );

      case 'B15': // Céder passage sens inverse
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            {/* Flèche montante rouge à droite */}
            <path d="M60 70 L60 38 M60 30 L54 40 M60 30 L66 40" fill="none" stroke="#dc2626" strokeWidth="5" strokeLinecap="round" strokeLinejoin="round" />
            {/* Flèche descendante noire à gauche */}
            <path d="M40 30 L40 62 M40 70 L34 60 M40 70 L46 60" fill="none" stroke="#1e293b" strokeWidth="7" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        );

      case 'B18a': // Explosifs
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#dc2626" strokeWidth="10" />
            <polygon points="50,30 58,44 72,42 62,54 68,68 52,62 40,70 44,54 30,46 44,42" fill="#dc2626" />
          </svg>
        );

      case 'B21b': // Tout droit obligation
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#1d4ed8" stroke="#ffffff" strokeWidth="3" />
            <path d="M50 72 L50 32 M50 24 L38 38 M50 24 L62 38" fill="none" stroke="#ffffff" strokeWidth="8" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        );

      case 'B21c1': // Tourner à droite
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#1d4ed8" stroke="#ffffff" strokeWidth="3" />
            <path d="M38 68 C38 46 46 38 66 38" fill="none" stroke="#ffffff" strokeWidth="8" strokeLinecap="round" />
            <polyline points="56,28 68,38 56,48" fill="none" stroke="#ffffff" strokeWidth="8" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        );

      case 'B21c2': // Tourner à gauche
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#1d4ed8" stroke="#ffffff" strokeWidth="3" />
            <path d="M62 68 C62 46 54 38 34 38" fill="none" stroke="#ffffff" strokeWidth="8" strokeLinecap="round" />
            <polyline points="44,28 32,38 44,48" fill="none" stroke="#ffffff" strokeWidth="8" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        );

      case 'B22a': // Piste cyclable
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#1d4ed8" stroke="#ffffff" strokeWidth="3" />
            <circle cx="34" cy="56" r="9" stroke="#ffffff" strokeWidth="3" fill="none" />
            <circle cx="66" cy="56" r="9" stroke="#ffffff" strokeWidth="3" fill="none" />
            <path d="M34 56 L46 44 L58 44 L66 56" stroke="#ffffff" strokeWidth="3" fill="none" strokeLinecap="round" />
          </svg>
        );

      case 'B25': // Vitesse minimale 30
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#1d4ed8" stroke="#ffffff" strokeWidth="3" />
            <text x="50" y="60" fill="#ffffff" fontSize="34" fontWeight="bold" fontFamily="sans-serif" textAnchor="middle">30</text>
          </svg>
        );

      case 'B27': // Voie bus
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#1d4ed8" stroke="#ffffff" strokeWidth="3" />
            <rect x="28" y="38" width="44" height="24" rx="4" fill="#ffffff" />
            <circle cx="38" cy="62" r="4" fill="#1d4ed8" />
            <circle cx="62" cy="62" r="4" fill="#1d4ed8" />
          </svg>
        );

      case 'B31': // Fin de toutes interdictions
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#1e293b" strokeWidth="3" />
            <line x1="20" y1="80" x2="80" y2="20" stroke="#1e293b" strokeWidth="9" />
          </svg>
        );

      case 'B33': // Fin limitation 50
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#1e293b" strokeWidth="3" />
            <text x="50" y="60" fill="#94a3b8" fontSize="34" fontWeight="bold" textAnchor="middle">50</text>
            <line x1="20" y1="80" x2="80" y2="20" stroke="#1e293b" strokeWidth="8" />
          </svg>
        );

      case 'B34': // Fin interdiction dépasser
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#1e293b" strokeWidth="3" />
            <rect x="28" y="44" width="18" height="14" rx="2" fill="#94a3b8" />
            <rect x="54" y="44" width="18" height="14" rx="2" fill="#94a3b8" />
            <line x1="20" y1="80" x2="80" y2="20" stroke="#1e293b" strokeWidth="8" />
          </svg>
        );

      case 'B34a': // Fin dépasser camions
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#ffffff" stroke="#1e293b" strokeWidth="3" />
            <rect x="24" y="40" width="24" height="20" rx="2" fill="#94a3b8" />
            <rect x="54" y="46" width="18" height="14" rx="2" fill="#94a3b8" />
            <line x1="20" y1="80" x2="80" y2="20" stroke="#1e293b" strokeWidth="8" />
          </svg>
        );

      case 'B43': // Fin vitesse minimale 30
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#1d4ed8" stroke="#ffffff" strokeWidth="3" />
            <text x="50" y="60" fill="#ffffff" fontSize="34" fontWeight="bold" textAnchor="middle">30</text>
            <line x1="20" y1="80" x2="80" y2="20" stroke="#dc2626" strokeWidth="8" />
          </svg>
        );

      case 'B45': // Fin voie bus
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <circle cx="50" cy="50" r="44" fill="#1d4ed8" stroke="#ffffff" strokeWidth="3" />
            <rect x="28" y="38" width="44" height="24" rx="4" fill="#ffffff" />
            <line x1="20" y1="80" x2="80" y2="20" stroke="#dc2626" strokeWidth="8" />
          </svg>
        );

      // PANNEAUX D'INDICATION (Carrés/Rectangles)
      case 'C12': // Sens unique
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <rect x="6" y="6" width="88" height="88" rx="8" fill="#1d4ed8" stroke="#ffffff" strokeWidth="3" />
            <path d="M50 78 L50 30 M50 20 L36 36 M50 20 L64 36" fill="none" stroke="#ffffff" strokeWidth="8" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        );

      case 'C13': // Impasse
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <rect x="6" y="6" width="88" height="88" rx="8" fill="#1d4ed8" stroke="#ffffff" strokeWidth="3" />
            <rect x="42" y="36" width="16" height="42" fill="#ffffff" />
            <rect x="30" y="24" width="40" height="14" fill="#dc2626" />
          </svg>
        );

      case 'C27': // Voie de détresse
        return (
          <svg viewBox="0 0 100 100" className="w-full h-full">
            <rect x="6" y="6" width="88" height="88" rx="8" fill="#1d4ed8" stroke="#ffffff" strokeWidth="3" />
            <path d="M30 76 L48 30 L66 76" stroke="#ffffff" strokeWidth="7" fill="none" />
            <rect x="42" y="24" width="16" height="10" fill="#dc2626" />
          </svg>
        );

      case 'EB10':
      case 'EB10_Save':
        return (
          <div className="border-4 border-red-600 bg-white px-5 py-2.5 rounded shadow text-center">
            <span className="text-xl font-black text-slate-900 tracking-wider">
              {code === 'EB10_Save' ? 'SAVÈ' : 'DASSA'}
            </span>
          </div>
        );

      case 'J3': // Balise intersection
        return (
          <svg viewBox="0 0 40 100" className="w-16 h-32">
            <path d="M12 20 L20 8 L28 20 L28 95 L12 95 Z" fill="#ffffff" stroke="#475569" strokeWidth="2" />
            <rect x="12" y="35" width="16" height="15" fill="#dc2626" />
          </svg>
        );

      case 'J4': // Chevrons
        return (
          <div className="flex bg-blue-800 p-2 rounded items-center justify-center gap-1 w-28">
            <span className="text-white font-black text-2xl tracking-tighter">«««</span>
          </div>
        );

      case 'G1': // Croix de Saint-André
        return (
          <svg viewBox="0 0 100 50" className="w-full h-full">
            <line x1="10" y1="10" x2="90" y2="40" stroke="#dc2626" strokeWidth="8" strokeDasharray="10 5" />
            <line x1="10" y1="40" x2="90" y2="10" stroke="#dc2626" strokeWidth="8" strokeDasharray="10 5" />
          </svg>
        );

      default:
        // Generic schematics or numbered images
        return (
          <div className="p-3 rounded-xl border border-emerald-500/30 bg-emerald-50/50 dark:bg-emerald-950/30 flex flex-col items-center justify-center text-center">
            <div className="w-12 h-12 rounded-full bg-emerald-600/10 text-emerald-700 dark:text-emerald-300 flex items-center justify-center font-bold text-base mb-1">
              {code.startsWith('I') ? '🚥' : code.startsWith('PN') ? '🚂' : '📋'}
            </div>
            <span className="text-xs font-bold text-emerald-900 dark:text-emerald-300">Schéma : {code}</span>
            <span className="text-[10px] text-slate-500">Conforme au manuel officiel DGTT</span>
          </div>
        );
    }
  };

  return (
    <>
      <div className={`relative inline-flex items-center justify-center cursor-pointer select-none group ${className}`} onClick={() => zoomable && setIsOpen(true)}>
        <div className="w-20 h-20 flex items-center justify-center p-1 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 shadow-sm transition group-hover:scale-105 group-hover:shadow-md">
          {renderSign()}
        </div>
        {zoomable && (
          <div className="absolute -bottom-1 -right-1 p-1 bg-emerald-700 text-white rounded-full shadow opacity-80 group-hover:opacity-100 transition">
            <ZoomIn className="w-3 h-3" />
          </div>
        )}
      </div>

      {/* Modal Zoom */}
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 p-4 backdrop-blur-sm" onClick={() => setIsOpen(false)}>
          <div className="relative max-w-sm w-full bg-white dark:bg-slate-900 rounded-2xl p-6 shadow-2xl border border-slate-200 dark:border-slate-800 flex flex-col items-center" onClick={(e) => e.stopPropagation()}>
            <button
              onClick={() => setIsOpen(false)}
              className="absolute top-3 right-3 p-1.5 rounded-lg text-slate-400 hover:text-slate-600 dark:hover:text-white"
            >
              <X className="w-6 h-6" />
            </button>
            <div className="w-48 h-48 flex items-center justify-center my-4">
              {renderSign()}
            </div>
            <p className="text-sm font-bold text-slate-800 dark:text-slate-200">Illustration DGTT : {code}</p>
            <p className="text-xs text-slate-500 mt-1">Conforme au code officiel de la route de la République du Bénin</p>
          </div>
        </div>
      )}
    </>
  );
};

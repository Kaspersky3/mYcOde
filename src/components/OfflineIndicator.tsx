import React from 'react';
import { useOnlineStatus } from '../hooks/usePWAInstall';
import { WifiOff } from 'lucide-react';

export const OfflineIndicator: React.FC = () => {
  const isOnline = useOnlineStatus();

  if (isOnline) return null;

  return (
    <div className="fixed bottom-20 left-4 right-4 md:left-auto md:right-4 z-40 flex items-center justify-center gap-2 rounded-xl bg-slate-900/95 text-amber-300 border border-amber-500/40 px-3.5 py-2 text-xs font-semibold shadow-xl backdrop-blur-md animate-bounce-subtle">
      <WifiOff className="w-4 h-4 text-amber-400" />
      <span>Mode Hors-Ligne actif — Toutes les questions et cours fonctionnent sans réseau</span>
    </div>
  );
};

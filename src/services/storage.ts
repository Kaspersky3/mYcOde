import { UserProgress, ExamResult, QuestionReport } from '../types';

const STORAGE_KEY = 'code_benin_b_progress_v1';

export const DEFAULT_PROGRESS: UserProgress = {
  currentDay: 1,
  dayProgress: {
    1: { learned: false, quizDone: false, trapsDone: false, bestScore: 0 },
    2: { learned: false, quizDone: false, trapsDone: false, bestScore: 0 },
    3: { learned: false, quizDone: false, trapsDone: false, bestScore: 0 },
  },
  questionLeitner: {},
  mistakeHistory: [],
  favoriteQuestionIds: [],
  completedQuestionIds: [],
  examHistory: [],
  reports: [],
  targetExamDate: null,
  streak: {
    count: 1,
    lastActiveDate: new Date().toISOString().split('T')[0],
  },
  settings: {
    examQuestionsCount: 40,
    examDurationMinutes: 30,
    examPassingScore: 35,
    showOtherCategories: false,
    darkMode: false,
  },
};

export function loadProgress(): UserProgress {
  try {
    if (typeof window === 'undefined' || !window.localStorage) {
      return DEFAULT_PROGRESS;
    }
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return DEFAULT_PROGRESS;
    const parsed = JSON.parse(raw);
    
    // Check and update streak
    const today = new Date().toISOString().split('T')[0];
    const last = parsed.streak?.lastActiveDate || today;
    let count = parsed.streak?.count || 1;
    
    const diffDays = Math.round(
      (new Date(today).getTime() - new Date(last).getTime()) / (1000 * 3600 * 24)
    );
    
    if (diffDays === 1) {
      count += 1;
    } else if (diffDays > 1) {
      count = 1;
    }

    const updated: UserProgress = {
      ...DEFAULT_PROGRESS,
      ...parsed,
      dayProgress: {
        ...DEFAULT_PROGRESS.dayProgress,
        ...(parsed.dayProgress || {}),
      },
      settings: {
        ...DEFAULT_PROGRESS.settings,
        ...(parsed.settings || {}),
      },
      streak: {
        count,
        lastActiveDate: today,
      },
    };
    saveProgress(updated);
    return updated;
  } catch (err) {
    console.error('Error loading progress:', err);
    return DEFAULT_PROGRESS;
  }
}

export function saveProgress(progress: UserProgress): void {
  try {
    if (typeof window !== 'undefined' && window.localStorage) {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
    }
  } catch (err) {
    console.error('Error saving progress:', err);
  }
}

export function exportProgressJSON(progress: UserProgress): string {
  return JSON.stringify(progress, null, 2);
}

export function importProgressJSON(jsonString: string): UserProgress | null {
  try {
    const parsed = JSON.parse(jsonString);
    if (parsed && typeof parsed === 'object' && parsed.dayProgress) {
      saveProgress(parsed);
      return parsed as UserProgress;
    }
    return null;
  } catch {
    return null;
  }
}

export function recordQuestionResult(
  current: UserProgress,
  questionId: number,
  isCorrect: boolean
): UserProgress {
  const newProgress = { ...current };
  const currentBox = newProgress.questionLeitner[questionId] || 1;

  if (isCorrect) {
    // Move up in Leitner box (max 3)
    newProgress.questionLeitner[questionId] = Math.min(3, currentBox + 1) as 1 | 2 | 3;
    // Remove from mistake history if promoted to 3
    if (newProgress.questionLeitner[questionId] === 3) {
      newProgress.mistakeHistory = newProgress.mistakeHistory.filter(id => id !== questionId);
    }
  } else {
    // Move down to box 1
    newProgress.questionLeitner[questionId] = 1;
    if (!newProgress.mistakeHistory.includes(questionId)) {
      newProgress.mistakeHistory.push(questionId);
    }
  }

  if (!newProgress.completedQuestionIds.includes(questionId)) {
    newProgress.completedQuestionIds.push(questionId);
  }

  saveProgress(newProgress);
  return newProgress;
}

export function addQuestionReport(
  current: UserProgress,
  report: QuestionReport
): UserProgress {
  const newProgress = {
    ...current,
    reports: [report, ...(current.reports || [])],
  };
  saveProgress(newProgress);
  return newProgress;
}

export function recordExamResult(
  current: UserProgress,
  result: ExamResult
): UserProgress {
  const newProgress = {
    ...current,
    examHistory: [result, ...(current.examHistory || [])],
  };
  saveProgress(newProgress);
  return newProgress;
}

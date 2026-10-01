export interface QuestionOption {
  id: string;
  texte: string;
}

export interface Question {
  id: string;
  numero: number;
  chapitre: number;
  theme: string;
  enonce: string;
  options: QuestionOption[];
  bonnesReponses: string[];
  multiReponses: boolean;
  image?: string | null;
  page: number;
  explication?: string | null;
  sourceExplication?: 'manuel' | 'redige' | null;
  tags: string[];
  difficulte: number;
  groupeDoublon?: string | null;
}

export interface CourseDefinition {
  titre: string;
  contenu: string;
}

export interface Abbreviation {
  sigle: string;
  definition: string;
}

export interface KeyNumber {
  label: string;
  valeur: string;
  contexte: string;
}

export interface AmbiguityItem {
  id: string;
  questions: number[];
  titre: string;
  description: string;
  regleOfficielle: string;
  statut: string;
}

export interface QuestionReport {
  questionId: number;
  questionText: string;
  reason: string;
  comment: string;
  date: string;
}

export interface ExamResult {
  id: string;
  date: string;
  score: number;
  total: number;
  passed: boolean;
  timeSpentSeconds: number;
  mistakeQuestionIds: number[];
}

export interface UserProgress {
  currentDay: 1 | 2 | 3;
  dayProgress: {
    1: { learned: boolean; quizDone: boolean; trapsDone: boolean; bestScore: number };
    2: { learned: boolean; quizDone: boolean; trapsDone: boolean; bestScore: number };
    3: { learned: boolean; quizDone: boolean; trapsDone: boolean; bestScore: number };
  };
  // Leitner system: 1 = to review, 2 = learning, 3 = mastered
  questionLeitner: Record<number, 1 | 2 | 3>;
  mistakeHistory: number[]; // question IDs
  favoriteQuestionIds: number[];
  completedQuestionIds: number[];
  examHistory: ExamResult[];
  reports: QuestionReport[];
  targetExamDate?: string | null;
  streak: {
    count: number;
    lastActiveDate: string;
  };
  settings: {
    examQuestionsCount: number;
    examDurationMinutes: number;
    examPassingScore: number;
    showOtherCategories: boolean;
    darkMode: boolean;
  };
}

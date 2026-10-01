import { describe, it, expect } from 'vitest';
import { UserProgress } from '../types';
import questionsData from '../data/questions.json';
import { recordQuestionResult, DEFAULT_PROGRESS } from '../services/storage';

describe('Quiz Logic & Spaced Repetition (Leitner)', () => {
  it('correctly handles single choice vs multi-choice questions', () => {
    // Single choice question test
    const q1 = questionsData.find((q) => q.numero === 1);
    expect(q1).toBeDefined();
    expect(q1?.multiReponses).toBe(false);
    expect(q1?.bonnesReponses).toEqual(['a']);

    // Multi-choice question test
    const q9 = questionsData.find((q) => q.numero === 9);
    expect(q9).toBeDefined();
    expect(q9?.multiReponses).toBe(true);
    expect(q9?.bonnesReponses).toEqual(['a', 'b']);
  });

  it('promotes questions in Leitner boxes on correct answer and resets to 1 on mistake', () => {
    let state: UserProgress = { ...DEFAULT_PROGRESS, questionLeitner: {}, mistakeHistory: [] };

    // Initial state: not answered yet
    expect(state.questionLeitner[10]).toBeUndefined();

    // 1st correct answer -> promotes to box 2
    state = recordQuestionResult(state, 10, true);
    expect(state.questionLeitner[10]).toBe(2);

    // 2nd correct answer -> promotes to box 3 (mastered)
    state = recordQuestionResult(state, 10, true);
    expect(state.questionLeitner[10]).toBe(3);

    // Incorrect answer -> drops back to box 1 (review needed) and adds to mistakes
    state = recordQuestionResult(state, 10, false);
    expect(state.questionLeitner[10]).toBe(1);
    expect(state.mistakeHistory).toContain(10);
  });

  it('smoke test: verifies integrity of the extracted question bank', () => {
    expect(questionsData.length).toBeGreaterThan(800);

    for (const q of questionsData) {
      expect(q.id).toBe(`q${q.numero}`);
      expect(q.numero).toBeGreaterThan(0);
      expect(q.chapitre).toBeGreaterThanOrEqual(1);
      expect(q.chapitre).toBeLessThanOrEqual(11);
      expect(q.enonce.length).toBeGreaterThan(3);
      expect(q.options.length).toBeGreaterThanOrEqual(2);
      expect(q.bonnesReponses.length).toBeGreaterThanOrEqual(1);
      
      // Each good response must match an existing option id
      const optionIds = q.options.map((opt) => opt.id);
      for (const ans of q.bonnesReponses) {
        expect(optionIds).toContain(ans);
      }
    }
  });

  it('identifies Category B priority scope vs other categories', () => {
    const catB = questionsData.filter((q) => q.tags.includes('categorie-b'));
    const others = questionsData.filter((q) => q.tags.includes('autres-categories'));

    expect(catB.length).toBeGreaterThan(700);
    expect(others.length).toBeGreaterThan(50);
  });
});

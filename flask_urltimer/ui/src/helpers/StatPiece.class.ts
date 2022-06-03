import { StatItemI } from '@/interfaces/stat-item.interface';

type Mark = {
  name: string;
  timing: number;
  line: number;
}

export class StatPiece {
  constructor(
    private idx: number,
    private start: Mark,
    private end: Mark
  ) {}

  get order(): number {
    return this.idx + 1;
  }

  get title(): string {
    return `[${this.order}] ${this.start.name}- ${this.end.name}`;
  }

  get duration(): number {
    return this.end.timing - this.start.timing;
  }
}


export const buildStatPieces = (stats: StatItemI): StatPiece[] => {
  const data: StatPiece[] = [];

  const markKeysOrdered = Object.keys(stats.timemarks)
    .sort((a, b) => stats.timemarks[a][0] - stats.timemarks[b][0]);

  markKeysOrdered
    .forEach((curKey, idx) => {
      if (idx === 0) return;
      const prevKey = markKeysOrdered[idx - 1];
      const [prevTime, prevLine] = stats.timemarks[prevKey];
      const [curTime, curLine] = stats.timemarks[curKey];

      data.push(new StatPiece(
        idx - 1,
        { name: prevKey, timing: prevTime, line: prevLine },
        { name: curKey, timing: curTime, line: curLine },
      ))
    });

  return data;
};

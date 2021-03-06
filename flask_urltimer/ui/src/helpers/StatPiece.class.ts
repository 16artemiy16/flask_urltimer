import { StatItemI } from '@/interfaces/stat-item.interface';
import { colors } from '@/constants';

type Mark = {
  name: string;
  timing: number;
  line: number;
}

export class StatPiece {
  constructor(
    private _idx: number,
    private start: Mark,
    private end: Mark
  ) {}

  get idx(): number {
    return this._idx;
  }

  get order(): number {
    return this.idx + 1;
  }

  get title(): string {
    return `[${this.order}] ${this.start.name} - ${this.end.name}`;
  }

  get duration(): number {
    const value = this.end.timing - this.start.timing;
    return +value.toFixed(4);
  }

  calcPercentage(total: number): number {
    const value = (this.duration * 100) / total;
    return +value.toFixed(1);
  }

  hasLineByIdx(lineIdx: number): boolean {
    return this.start.line <= lineIdx && this.end.line > lineIdx;
  }

  getLineStyle({
    isSmthSelected,
    isSelected
  }: { isSmthSelected: boolean, isSelected: boolean }
  ): Record<string, string | number> {
    return {
      opacity: (!isSelected && isSmthSelected) ? 0.5 : 1,
      background: colors[this.idx],
    };
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

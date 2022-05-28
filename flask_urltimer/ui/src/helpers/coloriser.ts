import { StatItemI } from '@/interfaces/stat-item.interface';
import { colors } from '@/constants';

export const getSortedMarkNames = (timemarks: Record<string, [number, number]>) => {
  return Object
    .keys(timemarks)
    .sort((a, b) => timemarks[a][0] - timemarks[b][0]);
};

export const getTimemarkNameByLine = (stats: StatItemI, idx: number): string => {
  let lastCandidateName = 'start';
  let lastCandidateEndLine = 0;
  Object
    .entries(stats.timemarks)
    .forEach(([name, data]) => {
      const [, endLine] = data;
      if (endLine < idx && endLine > lastCandidateEndLine) {
        lastCandidateName = name;
        lastCandidateEndLine = endLine;
      }
    });
  return lastCandidateName;
};

export const getColorByIdx = (stats: StatItemI, idx: number): string => {
  const name = getTimemarkNameByLine(stats, idx);
  const marks = getSortedMarkNames(stats.timemarks);
  const colorIdx = marks.findIndex((v) => v === name);
  return colors[colorIdx];
};

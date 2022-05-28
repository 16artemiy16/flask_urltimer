import { StatItemI } from '@/interfaces/stat-item.interface';

type Point = { name: string, y: number };

const statsToChartData = (stats: StatItemI): Point[] => {
  const data: Point[] = [];

  const marksKeys = Object.keys(stats.timemarks)
    .sort((a, b) => stats.timemarks[a][0] - stats.timemarks[b][0]);

  marksKeys
    .forEach((curKey, idx) => {
      if (idx === 0) return;
      const prevKey = marksKeys[idx - 1];
      const prevValue = stats.timemarks[prevKey][0];
      const curValue = stats.timemarks[curKey][0];

      data.push({ name: `[${idx}] ${prevKey} - ${curKey}`, y: curValue - prevValue });
    });

  return data;
};

export default statsToChartData;

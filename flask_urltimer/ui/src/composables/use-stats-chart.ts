import * as Highcharts from 'highcharts';
import { StatItemI } from '@/interfaces/stat-item.interface';
import statsToChartData from '@/helpers/stats-to-chart-data';

const useStatsChart = (selector: string) => {
  const draw = (stats: StatItemI) => {
    const data = statsToChartData(stats);

    Highcharts.chart(selector, {
      credits: { enabled: false },
      chart: {
        type: 'pie',
      },
      title: {
        text: `${stats.req.path} total duration - ${stats.duration}ms`
      },
      series: [{
        data,
        name: 'ms',
        colorByPoint: true,
      }]
    } as any);
  }

  return {
    draw,
  };
};

export default useStatsChart;

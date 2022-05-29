import * as Highcharts from 'highcharts';
import { StatItemI } from '@/interfaces/stat-item.interface';
import statsToChartData from '@/helpers/stats-to-chart-data';
import { colors } from '@/constants';
import { reactive } from 'vue';

const useStatsChart = (selector: string) => {
  const selectedNames = reactive<Set<string>>(new Set<string>());
  const draw = (stats: StatItemI) => {
    const data = statsToChartData(stats);

    Highcharts.chart(selector, {
      colors,
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
        allowPointSelect: true,
        point:{
          events:{
            select: function (event: any) {
              selectedNames.add(event.target.name)
            },
            unselect: function (event: any) {
              selectedNames.delete(event.target.name)
            },
          }
        }
      }],
    } as any);
  }

  return {
    draw,
    selectedNames,
  };
};

export default useStatsChart;

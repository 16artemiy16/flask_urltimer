import * as Highcharts from 'highcharts';
import { StatItemI } from '@/interfaces/stat-item.interface';
import statsToChartData from '@/helpers/stats-to-chart-data';
import { colors } from '@/constants';
import { reactive, ref } from 'vue';

const useStatsChart = (selector: string) => {
  const selectedNames = reactive<Set<string>>(new Set<string>());
  const selectedPieceName = ref<null | string>();
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
              selectedPieceName.value = event.target.name;
            },
            unselect: function (event: any) {
              if (event.target.name === selectedPieceName.value) {
                selectedPieceName.value = null;
              }
            },
          }
        }
      }],
    } as any);
  }

  return {
    draw,
    selectedNames,
    selectedPieceName,
  };
};

export default useStatsChart;

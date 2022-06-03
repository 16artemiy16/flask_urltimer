import * as Highcharts from 'highcharts';
import { StatItemI } from '@/interfaces/stat-item.interface';
import { colors } from '@/constants';
import { reactive, ref } from 'vue';
import { buildStatPieces } from '@/helpers/StatPiece.class';

const useStatsChart = (selector: string) => {
  const selectedNames = reactive<Set<string>>(new Set<string>());
  const selectedPieceName = ref<null | string>();
  const draw = (stats: StatItemI) => {
    const pieces = buildStatPieces(stats);

    const data = pieces.map(({ title, duration }) => ({
      name: title,
      y: duration,
    }));

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

<script setup lang="ts">
import { onMounted } from 'vue';
import { currentStat } from '@/store/stats.store';
import useStatsChart from '@/composables/use-stats-chart';
import { StatItemI } from '@/interfaces/stat-item.interface';
import { getColorByIdx, getPieceBySeriesName, getPieceOrderByLine } from '@/helpers/coloriser';

const { draw, selectedNames } = useStatsChart('container');

const stats = currentStat.value;

onMounted(() => {
  if (stats) {
    draw(stats);
  }
})

const getStyleByIdx = (idx: number): Record<string, any> => {
  const order = getPieceOrderByLine(stats as StatItemI, idx);
  const opacity = selectedNames.size && getPieceBySeriesName([...selectedNames][0]) !== order ? 0.5 : 1;
  return {
    opacity,
    background: getColorByIdx(stats as StatItemI, idx),
  };
}

</script>


<template>
  <div style="display: flex">
    <div style="width: 700px;">
      <div id="container"></div>
    </div>
    <div>
      <h3>{{ [...selectedNames][0] }}</h3>
    </div>
  </div>

  <div v-if="stats">
    <div
      class="line"
      :style="getStyleByIdx(idx)"
      :key="line"
      v-for="(line, idx) in stats.source.lines"
    >{{ line }}</div>
  </div>
  <div v-else>
    Stats with this ID does not exist! <br />
    <router-link to="/">Back</router-link>
  </div>
</template>

<style scoped lang="scss">
.chart-wrapper {
  width: 500px;
  height: 500px;
}

.line {
  white-space: pre;
}
</style>

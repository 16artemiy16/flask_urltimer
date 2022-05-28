<script setup lang="ts">
import { onMounted } from 'vue';
import { currentStat } from '@/store/stats.store';
import useStatsChart from '@/composables/use-stats-chart';
import { StatItemI } from '@/interfaces/stat-item.interface';
import { getColorByIdx } from '@/helpers/coloriser';

const { draw } = useStatsChart('container');

const stats = currentStat.value;

onMounted(() => {
  if (stats) {
    draw(stats);
  }
})

const getStyleByIdx = (idx: number) => ({ background: getColorByIdx(stats as StatItemI, idx) });

</script>


<template>
  <div id="container"></div>
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

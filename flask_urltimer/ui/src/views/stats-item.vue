<script setup lang="ts">
import { onMounted } from 'vue';
import { currentStat } from '@/store/stats.store';
import useStatsChart from '@/composables/use-stats-chart';

const { draw } = useStatsChart('container');

const stats = currentStat.value;

onMounted(() => {
  if (stats) {
    draw(stats);
  }
})

</script>


<template>
  <div id="container"></div>
  <div v-if="stats">
    <div
      style="white-space: pre"
      :key="line"
      v-for="(line, idx) in stats.source.lines"
      :class="['line-' + idx]"
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
</style>

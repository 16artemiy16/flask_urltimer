<script setup lang="ts">
import { computed, onMounted, watch } from 'vue';
import { getStatById, fetchIfFirstLoad, fetchItems } from '@/store/stats.store';
import useStatsChart from '@/composables/use-stats-chart';
import { StatItemI } from '@/interfaces/stat-item.interface';
import { useRoute } from 'vue-router';
import { getColorByIdx, getPieceBySeriesName, getPieceOrderByLine } from '@/helpers/coloriser';

fetchIfFirstLoad();
const { params } = useRoute();
const { draw, selectedNames } = useStatsChart('container');

const stats = computed<StatItemI | undefined>(() => getStatById(params.id as string));

onMounted(() => {
  watch(stats, (value) => {
    if (value) {
      draw(value as StatItemI);
    }
  }, { immediate: true });
});

const getStyleByIdx = (idx: number): Record<string, any> => {
  const order = getPieceOrderByLine(stats.value as StatItemI, idx);
  const opacity = selectedNames.size && getPieceBySeriesName([...selectedNames][0]) !== order ? 0.5 : 1;
  return {
    opacity,
    background: getColorByIdx(stats.value as StatItemI, idx),
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

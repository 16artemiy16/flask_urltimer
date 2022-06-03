<script setup lang="ts">
import { computed, onMounted, watch } from 'vue';
import {
  getStatById,
  fetchIfFirstLoad,
  selectedPiece,
  initStatPiecesByStatId,
  setSelectedPieceByTitle, statPieces, isPieceSelectedByIdx
} from '@/store/stats.store';
import useStatsChart from '@/composables/use-stats-chart';
import { StatItemI } from '@/interfaces/stat-item.interface';
import { useRoute } from 'vue-router';

fetchIfFirstLoad();
const { params } = useRoute();
const { draw, selectedPieceName } = useStatsChart('container');

const stats = computed<StatItemI | undefined>(() => getStatById(params.id as string));

onMounted(() => {
  watch(stats, (value) => {
    if (value) {
      initStatPiecesByStatId(value.id);
      draw(value as StatItemI);
    }
  }, { immediate: true });
  watch(selectedPieceName, (name) => setSelectedPieceByTitle(name));
});

const getStyleByIdx = (idx: number): Record<string, string | number> => {
  const piece = statPieces.value.find((item) => item.hasLineByIdx(idx));
  if (!piece) {
    return {};
  }
  return piece.getLineStyle({
    isSmthSelected: !!selectedPiece.value,
    isSelected: isPieceSelectedByIdx(piece.idx)
  });
};

</script>


<template>
  <div style="display: flex">
    <div style="width: 700px;">
      <div id="container"></div>
    </div>
    <div v-if="selectedPiece">
      <h3>{{ selectedPiece.title }}</h3>
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

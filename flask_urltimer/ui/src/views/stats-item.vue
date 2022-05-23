<script setup lang="ts">
import { onMounted } from 'vue';
import * as Highcharts from 'highcharts';
import { statItems } from '@/store/stats.store';
import { useRoute } from 'vue-router';

const stats = statItems.value.find(({ id }) => id === useRoute().params.id);

const data = [];

const marksKeys = Object.keys(stats.timemarks)
    .sort((a, b) => stats.timemarks[a] - stats.timemarks[b]);

marksKeys
  .forEach((curKey, idx) => {
    if (idx === 0) return;
    const prevKey = marksKeys[idx - 1];
    const prevValue = stats.timemarks[prevKey];
    const curValue = stats.timemarks[curKey];

    data.push({ name: `[${idx}] ${prevKey} - ${curKey}`, y: curValue - prevValue });
  });

onMounted(() => {
  Highcharts.chart('container', {
    credits: { enabled: false },
    chart: {
      type: 'pie',
    },
    title: {
      text: `${stats.req.url} total duration - ${stats.duration}ms`
    },
    series: [{
      data,
      name: 'ms',
      colorByPoint: true,
    }]
  });
})

</script>


<template>
  <div id="container"></div>
  <pre><code>{{ stats.source }}</code></pre>
</template>

<style scoped lang="scss">
.chart-wrapper {
  width: 500px;
  height: 500px;
}
</style>

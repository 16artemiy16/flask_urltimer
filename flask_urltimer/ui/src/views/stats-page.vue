<script setup lang="ts">
import { onMounted } from 'vue';
import * as Highcharts from 'highcharts';

const stats = {
  "timestamp": 1652705117.394714,
  "req": {"url": "http://localhost:5000/first"},
  "timemarks": {
    "start": 0,
    "After sum": 0.000685723000000138,
    "After sleep": 0.502594117000001,
    "end": 0.7036128370000021}
}

const marksKeys = Object.keys(stats.timemarks);

const data = [];
marksKeys
  .forEach((curKey, idx) => {
    if (idx === 0) return;
    const prevKey = marksKeys[idx - 1];
    const prevValue = stats.timemarks[prevKey];
    const curValue = stats.timemarks[curKey];

    data.push({ name: `[${idx}] ${prevKey} - ${curKey}`, y: curValue - prevValue });
  });

const totalDuration = data.reduce((prev, { y }) => prev + y, 0);

onMounted(() => {
  Highcharts.chart('container', {
    credits: { enabled: false },
    chart: {
      type: 'pie',
    },
    title: {
      text: `${stats.req.url} total duration - ${totalDuration}ms`
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
</template>

<style scoped lang="scss">
.chart-wrapper {
  width: 500px;
  height: 500px;
}
</style>

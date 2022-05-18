<script setup lang="ts">
import { onMounted } from 'vue';
import * as Highcharts from 'highcharts';

const stats = {
  "timestamp": 1652705117.394714,
  "req": {"url": "http://localhost:5000/first"},
  "timemarks": {
    "start": 0,
    "After sum": 0.2036128370000021,
    "After sleep": 0.502594117000001,
    "end": 0.7036128370000021},
  "source": `
@app.get('/first')
@check_source
def first():
    sum = 0
    for i in range(10000):
      sum += 1

    add_timemark('After sum')
    time.sleep(0.5)
    add_timemark('After sleep')

    for i in range(10000):
      sum += 1
    return 'Hello from First!'
  `.trim(),
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
  <pre><code>{{ stats.source }}</code></pre>
</template>

<style scoped lang="scss">
.chart-wrapper {
  width: 500px;
  height: 500px;
}
</style>

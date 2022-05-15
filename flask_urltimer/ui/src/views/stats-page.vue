<script setup lang="ts">
import { Pie } from 'vue-chartjs'
import { Chart as ChartJS, Title, Legend, Tooltip, ArcElement } from 'chart.js'

ChartJS.register(Title, ArcElement, Legend, Tooltip)

const chartData = {
  labels: [
    'Start - Mark 1',
    'Mark 1 - Mark 2',
    'Mark 2 - End'
  ],
  datasets: [{
    label: 'Total: 6.2s',
    data: [2, 1, 3.2],
    backgroundColor: [
      'rgb(255, 99, 132)',
      'rgb(54, 162, 235)',
      'rgb(255, 205, 86)'
    ],
  }]
};

</script>


<template>
  <div class="chart-wrapper">
    <Pie :chart-data="chartData"  />
  </div>
</template>

<style scoped lang="scss">
.chart-wrapper {
  width: 500px;
  height: 500px;
}
</style>

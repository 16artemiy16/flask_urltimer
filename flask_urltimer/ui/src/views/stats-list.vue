<script setup lang="ts">
import {
  isLoadingItems,
  sortedStatItems,
  toggleSorting,
  getFieldSorting,
  statsItemsPaths,
  fetchIfFirstLoad,
} from '@/store/stats.store';

fetchIfFirstLoad();

</script>

<template>
  <ul>
    <li v-for="url in statsItemsPaths" :key="url">{{ url }}</li>
  </ul>
  <div>
    <h2>Sorting</h2>
    <div>
      Duration: {{ getFieldSorting('duration') || 'No' }}
      <button @click="toggleSorting('duration')">Toggle</button>
    </div>
    <div>
      Timestamp: {{ getFieldSorting('timestamp') || 'No' }}
      <button @click="toggleSorting('timestamp')">Toggle</button>
    </div>
  </div>
  <div v-if="isLoadingItems">Loading</div>

  <div>
    <div class="row">
      <div class="c1">path</div>
      <div class="c2">time, ms</div>
      <div class="c2">Date and time</div>
    </div>
    <div
      class="row"
      v-for="item in sortedStatItems"
      :key="item.timestamp"
    >
      <div class="c1">
        <router-link :to="{ path: '/' + item.id }">{{ item.req.path }}</router-link>
      </div>
      <div class="c2">{{ item.duration }}</div>
      <div class="c3">{{ new Date(item.timestamp).toLocaleString() }}</div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.row {
  display: flex;
}
.c1 {
  width: 100px;
}
.c2 {
  width: 150px;
}
.c3 {
  width: 250px;
}
</style>

<script setup lang="ts">
import {
  isLoadingItems,
  fetchItems,
  sortedStatItems,
  toggleSorting,
  getFieldSorting,
  statsItemsUrls,
} from '@/store/stats.store';

fetchItems();

</script>

<template>
  <ul>
    <li v-for="url in statsItemsUrls" :key="url">{{ url }}</li>
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
  <div v-else>
    <div
        v-for="item in sortedStatItems"
        :key="item.timestamp"
    >
      <div>{{ item.req.url }} ({{ item.duration }}ms)</div>
    </div>
  </div>
</template>

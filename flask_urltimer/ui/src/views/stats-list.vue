<script setup lang="ts">
import { isLoadingItems, fetchItems, sortedStatItems, toggleSorting, getFieldSorting } from '@/store/stats.store';

fetchItems();

const calcMarkDuration = (mark: Record<string, number>): number => {
    const {start, end} = mark;
    return end - start;
};

</script>

<template>
  <div>
    <h2>Sorting</h2>
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
      <div>{{ item.req.url }} ({{ calcMarkDuration(item.timemarks) }}ms)</div>
    </div>
  </div>
</template>

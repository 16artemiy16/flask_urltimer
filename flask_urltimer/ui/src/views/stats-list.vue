<script setup lang="ts">
import { useGetStatsList } from '@/composables/stats-api';

const { result, isLoading, request } = useGetStatsList();

request();

const calcMarkDuration = (mark: Record<string, number>): number => {
    const {start, end} = mark;
    return end - start;
};

</script>

<template>
  <div v-if="isLoading">Loading</div>
  <div v-else>
    <div
        v-for="item in result"
        :key="item.timestamp"
    >
      <div>{{ item.req.url }} ({{ calcMarkDuration(item.timemarks) }}ms)</div>
    </div>
  </div>
</template>

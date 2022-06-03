<script setup lang="ts">
import { statsItemsPaths } from '@/store/stats.store';
</script>

<template>
  <div class="stats-filter">
      <span
          class="stats-filter__item"
          v-for="url in statsItemsPaths"
          :key="url"
      >
    {{ url }}
  </span>
  </div>
</template>

<style scoped lang="scss">
.stats-filter {
  display: flex;

  &__item {
    margin-right: 1rem;
  }
}
</style>

<script setup lang="ts">
import StatListFilter from '@/components/stat-list/stat-list-filter.vue';

import {
  isLoadingItems,
  sortedStatItems,
  getFieldSorting,
  fetchIfFirstLoad,
  setSorting,
} from '@/store/stats.store';

fetchIfFirstLoad();

</script>

<template>
  <div>
    <StatListFilter class="py-4" />
  </div>

  <div v-if="isLoadingItems">Loading</div>

  <div>
    <div class="row">
      <div class="c-header c1">path</div>
      <div class="c-header c2">
        time, ms
        <AppSortingBtn
            :value="getFieldSorting('duration')"
            @changed="(value) => setSorting('duration', value)"
        />
      </div>
      <div class="c-header c3">
        Date and time
        <AppSortingBtn
            :value="getFieldSorting('timestamp')"
            @changed="(value) => setSorting('timestamp', value)"
        />
      </div>
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
.c1, .c2, .c3 {
  border: 1px black solid;
  padding: .5rem;
}
.c-header {
  font-weight: bold;
  display: flex;
  justify-content: space-between;
}
</style>

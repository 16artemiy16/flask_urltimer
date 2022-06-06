<script setup lang="ts">
import PageLayoutTopNav from './page-layout-top-nav.vue';
</script>

<template>
  <PageLayoutTopNav />
  <main>
    <router-view/>
  </main>
</template>

<style scoped lang="scss">
main {
  padding: 1rem;
}
</style>

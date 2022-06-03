<template>
  <div class="top-nav">
    <h1 class="top-nav__title">flask-urltimer</h1>
    <nav class="top-nav__links">
      <router-link :to="{ name: 'statsList' }">Stats</router-link>
    </nav>
  </div>
</template>

<style scoped lang="scss">
.top-nav {
  display: flex;
  align-items: center;
  border: 1px solid $grey;
  padding: 0.25rem 0.75rem;

  &__title, &__links {
    font-size: 1.25em;
  }

  &__links {
    margin-left: 1.5rem;
  }
}
</style>

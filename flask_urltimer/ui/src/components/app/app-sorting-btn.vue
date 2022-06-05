<script lang="ts">
import { defineComponent, PropType } from 'vue'
import { Sorting } from '@/types/common.types';
import useCircularGenerator from '@/composables/useCircularGenerator';

export default defineComponent({
  props: {
    value: {
      type: [String, null] as PropType<Sorting>,
      default: null,
    },
  },
  watch: {
    value: function(v) {
      this.set(v);
    }
  },
  setup(props, { emit }) {
    const { value, next, set } = useCircularGenerator<Sorting>([null, 'asc', 'desc']);

    set(props.value as Sorting);

    return {
      handleChange: function () {
        next();
        emit('changed', value.value);
      },
      set,
    }
  }
});

</script>

<template>
  <div class="app-sorting-btn" @click="handleChange">
    <i class="fa fa-arrow-up" :class="{ 'app-sorting-btn-active': value === 'asc' }" />
    <i class="fa fa-arrow-down" :class="{ 'app-sorting-btn-active': value === 'desc' }" />
  </div>
</template>

<style scoped lang="scss">
.app-sorting-btn {
  color: $grey;
  cursor: pointer;
  &-active {
    color: $black;
  }
}
</style>

import { computed, ref } from 'vue';

const useCircularGenerator = <T>(values: T[]) => {
  const curIdx = ref<number>(0)
  const value = computed(() => values[curIdx.value]);
  const next = () => {
    curIdx.value = curIdx.value === (values.length - 1)
      ? 0
      : (curIdx.value + 1);
  };
  const set = (value: T) => {
    const idx = values.findIndex((item) => item === value);
    if (idx !== -1) {
      curIdx.value = idx;
    }
  }

  return { value, next, set };
};

export default useCircularGenerator;

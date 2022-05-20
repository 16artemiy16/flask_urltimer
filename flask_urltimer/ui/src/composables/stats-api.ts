import { ref } from 'vue';
import { StatItemI } from '@/interfaces/stat-item.interface';

const getStatsListURL = '/timings/api/items';

export const useGetStatsList = () => {
  const result = ref<StatItemI[]>([]);
  const error = ref(null);
  const isLoading = ref(false);

  const request = () => {
    isLoading.value = true;
    return fetch(getStatsListURL)
      .then(async (res) => {
        isLoading.value = false;
        result.value = await res.json().then(({ items }) => items);
        return result.value;
      })
      .catch((e) => {
        error.value = e;
        isLoading.value = false;
      })
  }

  return { result, error, isLoading, request };
}

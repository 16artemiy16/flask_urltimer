import { useGetStatsList } from '@/composables/stats-api';
import { StatItemI } from '@/interfaces/stat-item.interface';
import { computed, ref, watch } from 'vue';
import { useRoute } from 'vue-router';

type SortingDir = 'asc' | 'desc';

interface SortingI {
  field: keyof StatItemI,
  dir: SortingDir,
}

const { request, isLoading, result } = useGetStatsList();

export const statItems = result;
export const fetchItems = request;
export const isLoadingItems = isLoading;

export const isFirstLoad = ref<boolean>(true);

const isFirstLoadWatcher = watch(statItems, () => {
  isFirstLoad.value = false;
  isFirstLoadWatcher();
});

export const fetchIfFirstLoad = () => {
  if (isFirstLoad.value) {
    request();
  }
};

export const getStatById = (id: string): StatItemI | undefined => {
  return statItems.value.find((item) => item.id === id);
};

export const statsItemsPaths = computed(() => {
  return Array.from(
    new Set(
      statItems.value.map(({ req }: any) => req.path)
    )
  );
});

export const sorting = ref<SortingI | null>(null);

export const getFieldSorting = (field: keyof StatItemI): SortingDir | null => {
  if (!sorting.value) { return null; }
  if ((sorting.value as SortingI).field === field) {
    return (sorting.value as SortingI).dir;
  }
  return null;
}

export const resetSorting = () => { sorting.value = null };
export const setSorting = (field: keyof StatItemI, dir: SortingDir): void => {
  sorting.value = { field, dir };
}

export const toggleSorting = (fieldToSet: keyof StatItemI): void => {
  if (!sorting.value) {
    return setSorting(fieldToSet, 'asc');
  }
  const { field, dir } = sorting.value;
  if (fieldToSet !== field) {
    return setSorting(fieldToSet, 'asc');
  }
  if (dir === null) {
    return setSorting(fieldToSet, 'asc');
  }
  if (dir === 'asc') {
    return setSorting(fieldToSet, 'desc');
  }
  resetSorting()
}


export const sortedStatItems = computed(() => {
  if (!sorting.value) {
    return statItems.value;
  }
  const { field, dir } = sorting.value as SortingI;
  return [...statItems.value].sort((a, b) => {
    const multiplier = dir === 'desc' ? -1 : 1;
    const v1: any = a[field];
    const v2: any = b[field];
    return (v1 - v2) * multiplier;
  });
});

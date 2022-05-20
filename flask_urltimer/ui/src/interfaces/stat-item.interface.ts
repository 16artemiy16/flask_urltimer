export interface StatItemI {
  req: {
    url: string,
  }
  source: string | null
  timemarks: Record<string, number>
  timestamp: number;
}

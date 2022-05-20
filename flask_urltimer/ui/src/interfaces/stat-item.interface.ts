export interface StatItemI {
  uuid: string,
  req: {
    url: string,
  }
  source: string | null
  timemarks: Record<string, number>
  timestamp: number;
}

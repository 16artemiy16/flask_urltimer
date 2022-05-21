export interface StatItemI {
  uuid: string;
  duration: number;
  req: {
    url: string;
    path: string;
  }
  source: string | null;
  timemarks: Record<string, number>;
  timestamp: number;
}

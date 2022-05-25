export interface StatItemI {
  id: string;
  duration: number;
  req: {
    url: string;
    path: string;
  }
  source: {
    lines: string,
    linenum: number,
  }[];
  timemarks: Record<string, [number, number]>;
  timestamp: number;
}

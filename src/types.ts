export interface Publication {
  id: string;
  year: number;
  type: string;
  title: string;
  authors: string;
  venue: string;
  volume?: string;
  issue?: string;
  pages?: string;
  doi?: string;
  url?: string;
  keywords?: string[];
  featured?: boolean;
  source?: string;
}

export interface Project {
  id: string;
  title: string;
  role?: string;
  category?: string;
  fundingBody?: string;
  year?: string;
  status?: string;
  description?: string;
  keywords?: string[];
  outputs?: string[];
  url?: string;
  featured?: boolean;
  source?: string;
}

export interface Course {
  id: string;
  code?: string;
  title: string;
  level: string;
  language?: string;
  description?: string;
  topics?: string[];
}

export interface AaaCitation {
  id: string;
  year?: number;
  title: string;
  authors?: string;
  venue?: string;
  publicationType?: string;
  doi?: string;
  url?: string;
  applicationArea?: string;
  usageType?: string;
  notes?: string;
  source?: string;
  verified?: boolean;
}

export interface ResearchArea {
  title: string;
  description?: string;
  keywords?: string[];
}

export interface AaaCode {
  language: string;
  title: string;
  description?: string;
  url?: string;
  repository?: string;
}

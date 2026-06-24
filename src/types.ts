export interface Publication {
  id: string;
  year: number;
  category: string;
  publicationType: string;
  title: string;
  authors: string;
  venue: string;
  publisher?: string;
  editors?: string;
  volume?: string;
  issue?: string;
  pages?: string;
  doi?: string;
  url?: string;
  isbn?: string;
  presentationType?: string;
  keywords?: string[];
  featured?: boolean;
  source?: string;
}

export interface Project {
  id: string;
  title: string;
  projectType?: string;
  fundingSource?: string;
  role?: string;
  startDate?: string;
  endDate?: string;
  status?: string;
  keywords?: string[];
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

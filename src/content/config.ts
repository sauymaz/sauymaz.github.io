import { defineCollection, z } from 'astro:content';

const aaa = defineCollection({
  type: 'content',
  schema: z.object({ title: z.string() })
});

export const collections = { aaa };

// News-image entry (Node 22, standard library only): the image is stored beside
// this file as base64 text (entry.png.b64) and decoded to /output/entry.png.
// The picture itself is drawn in code by make_image.py (PIL + DejaVu) and saved
// as a 1024x1024 PNG of at most 1 MiB; the judge sees exactly the bytes written.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
const b64 = readFileSync(new URL('./entry.png.b64', import.meta.url), 'utf8').replace(/\s+/g, '');
writeFileSync(join(outDir, 'entry.png'), Buffer.from(b64, 'base64'));

import { defineConfig } from "astro/config";

export default defineConfig({
  site: "https://sunathappy.com",
  output: "static",
  build: {
    format: "directory",
  },
});

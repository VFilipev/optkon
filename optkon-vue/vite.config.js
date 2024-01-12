// Plugins
import vue from "@vitejs/plugin-vue";
import vuetify, { transformAssetUrls } from "vite-plugin-vuetify";
import ViteFonts from "unplugin-fonts/vite";
import dns from "dns";
// Utilities
import { defineConfig } from "vite";
import { fileURLToPath, URL } from "node:url";

// const HOST = 'http://192.168.0.4:8000/'
const HOST = "http://127.0.0.1:8000/";

dns.setDefaultResultOrder("verbatim");
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue({
      template: { transformAssetUrls },
    }),
    // https://github.com/vuetifyjs/vuetify-loader/tree/master/packages/vite-plugin#readme
    vuetify({
      autoImport: true,
      styles: {
        configFile: "src/styles/settings.scss",
      },
    }),
    ViteFonts({
      google: {
        families: [
          {
            name: "Roboto",
            styles: "wght@100;300;400;500;700;900",
          },
        ],
      },
    }),
  ],
  define: { "process.env": {} },
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
    extensions: [".js", ".json", ".jsx", ".mjs", ".ts", ".tsx", ".vue"],
  },
  build: {
    assetsDir: "static",
  },
  server: {
    port: 8080,
    host: "127.0.0.1",
    proxy: {
      "^/api": {
        target: HOST,
        ws: true,
        changeOrigin: true,
      },
      "^/media": {
        target: HOST,
        ws: true,
        changeOrigin: true,
      },
      "^/admin": {
        target: HOST,
        ws: true,
        changeOrigin: true,
      },
      "^/static": {
        target: HOST,
        ws: true,
        changeOrigin: true,
      },
    },
  },
});

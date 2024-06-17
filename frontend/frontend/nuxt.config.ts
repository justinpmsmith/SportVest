// https://nuxt.com/docs/api/configuration/nuxt-config
import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
//   app: {
//     buildAssetsDir: "/BuildFolderWithoutUnderscore/",
// },
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
    '@pinia-plugin-persistedstate/nuxt',
    'nuxt-icon',
  ],

  css: ["vuetify/styles/main.sass"],
  build: {
    transpile: ["vuetify"],
  },

});

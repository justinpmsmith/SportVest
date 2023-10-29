// https://nuxt.com/docs/api/configuration/nuxt-config
import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
  modules: [
    '@nuxtjs/tailwindcss',
  ],

  css: ["vuetify/styles/main.sass"],
  build: {
    transpile: ["vuetify"],
  },

  plugins: [
    '@/plugins/pinia.js', 
  ],
});

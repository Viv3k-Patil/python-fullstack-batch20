
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'
import fullReload from 'vite-plugin-full-reload'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    fullReload(['src/**/*', 'index.html']),
  ],
  server: {
    watch: {
      usePolling: true,
    },
  },
})

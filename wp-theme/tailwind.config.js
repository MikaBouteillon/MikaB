/**
 * Tailwind config — USAM Nîmes Gard
 *
 * Compilation :
 *   npx tailwindcss -i ./assets/css/input.css -o ./assets/css/main.css --watch
 */
module.exports = {
  content: [
    './**/*.php',
    './assets/js/**/*.js',
  ],
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: '1rem',
        lg: '2rem',
      },
    },
    extend: {
      colors: {
        usam: {
          volt:     '#00E676',
          forest:   '#0B3D2E',
          charcoal: '#0A0A0A',
          bone:     '#F5F5F0',
          yellow:   '#E8FF59',
          'slate-200': '#E2E8F0',
          'slate-700': '#334155',
        },
      },
      fontFamily: {
        display: ['Anton', 'Impact', 'sans-serif'],
        sans:    ['Inter', 'system-ui', 'sans-serif'],
        head:    ['Sora', 'Inter', 'sans-serif'],
        mono:    ['JetBrains Mono', 'monospace'],
      },
      letterSpacing: {
        widest: '.25em',
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
};

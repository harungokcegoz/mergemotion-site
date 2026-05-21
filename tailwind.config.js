/** @type {import('tailwindcss').Config} */
module.exports = {
  prefix: 'tw-',
  content: ['./public/**/*.html', './public/**/*.js'],
  theme: {
    extend: {
      colors: {
        ink: '#0A0A0F', surface: '#14141B',
        accent: { DEFAULT: '#7C3AED', light: '#A855F7' }, paper: '#F5F5F7',
      },
      fontFamily: { display: ['"SF Pro Display"', 'system-ui', '-apple-system', 'Segoe UI', 'sans-serif'] },
      backgroundImage: { 'accent-grad': 'linear-gradient(135deg, #7C3AED 0%, #A855F7 100%)' },
    },
  },
  plugins: [],
};

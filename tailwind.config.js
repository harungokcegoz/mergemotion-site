/** @type {import('tailwindcss').Config} */
module.exports = {
  prefix: 'tw-',
  content: ['./public/**/*.html', './public/**/*.js'],
  theme: {
    extend: {
      colors: {
        ink: '#0B0B0D', surface: '#16161A',
        accent: { DEFAULT: '#FF8A4C', light: '#FFA76B' }, paper: '#FFFFFF',
        muted: '#B8B8BD',
      },
      fontFamily: { display: ['"SF Pro Display"', 'system-ui', '-apple-system', 'Segoe UI', 'sans-serif'] },
      backgroundImage: { 'accent-grad': 'linear-gradient(135deg, #FF8A4C 0%, #FF6B3D 100%)' },
    },
  },
  plugins: [],
};

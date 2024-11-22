/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors')

tailwind.config = {
  darkMode: 'class', // Enable class-based dark mode
  content: [
   "./EcomProducts/templates/**/*.html", // Matches all templates inside EcomProducts/templates
  "./node_modules/flowbite/**/*.js"     // Flowbite components
  ],
  
  theme: {
    extend: {
        colors: {
          primary: {"50":"#eff6ff","100":"#dbeafe","200":"#bfdbfe","300":"#93c5fd","400":"#60a5fa","500":"#3b82f6","600":"#2563eb","700":"#1d4ed8","800":"#1e40af","900":"#1e3a8a","950":"#172554"}
        }
      },
      fontFamily: {
        'body': [
          'Roboto', 
          'ui-sans-serif', 
          'system-ui', 
          '-apple-system', 
      'system-ui', 
      'Segoe UI', 
      'Roboto', 
      'Helvetica Neue', 
      'Arial', 
      'Noto Sans', 
      'sans-serif', 
      'Apple Color Emoji', 
      'Segoe UI Emoji', 
      'Segoe UI Symbol', 
      'Noto Color Emoji'
    ],
        'sans': [
          'Roboto', 
          'ui-sans-serif', 
          'system-ui',
      '-apple-system', 
      'system-ui', 
      'Segoe UI', 
      'Roboto', 
      'Helvetica Neue', 
      'Arial', 
      'Noto Sans', 
      'sans-serif', 
      'Apple Color Emoji', 
      'Segoe UI Emoji', 
      'Segoe UI Symbol', 
      'Noto Color Emoji'
    ]
      }
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
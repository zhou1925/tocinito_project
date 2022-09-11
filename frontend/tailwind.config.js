/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'custom-yellow': '#ffca40',
        'custom-red': '#c8161D',
        'custom-red': '#c8161D',
        'custom-white': '#f8f8f7',
        'custom-black': '#000000',
      },
    },
    
  },
  plugins: [
    require("daisyui")
  ],
  daisyui: {
    themes: ["light", "luxury"]
    // "dark", "cupcake", "bumblebee", "emerald", "corporate", 
    // "synthwave", "retro", "cyberpunk", "valentine", "halloween", "garden", 
    // "forest", "aqua", "lofi", "pastel", "fantasy", "wireframe", "black", "luxury", 
    // "dracula", "cmyk", "autumn", "business", "acid", "lemonade", "night", "coffee", "winter"],
  }
}

// Wiseble Virtual System — Tailwind tokens
tailwind.config = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'midnight-void': '#000000',
        'ghost-white': '#ffffff',
        'muted-ash': '#666666',
        'accent-orange': '#ff5c00',
        surface: '#131313',
        'surface-container': '#1f1f1f',
        'surface-container-low': '#1b1b1b',
        'surface-container-lowest': '#0e0e0e',
        'surface-container-high': '#2a2a2a',
        'on-surface': '#e2e2e2',
        'on-surface-variant': '#c4c7c8',
        outline: '#8e9192',
        'outline-variant': '#444748',
      },
      fontFamily: {
        display: ['"Space Grotesk"', 'system-ui', 'sans-serif'],
        heading: ['"Space Grotesk"', 'system-ui', 'sans-serif'],
        body: ['Inter', 'system-ui', 'sans-serif'],
      },
      spacing: {
        xs: '10px', sm: '11px', md: '17px', lg: '25px', xl: '30px', xxl: '35px',
        'section-gap': '156px',
      },
      maxWidth: { content: '1280px', wide: '1440px' },
    },
  },
};

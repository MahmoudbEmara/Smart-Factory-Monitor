/**
 * App Configuration Module
 * 
 * Centralized configuration for the mobile app.
 * Update the RAILWAY_URL when deploying or changing environments.
 */

const AppConfig = {
  // Your Railway deployment URL - Update this with your actual Railway URL
  // Example: 'https://your-app-name.railway.app' or your custom domain
  RAILWAY_URL: process.env.RAILWAY_URL || 'https://kattameya-dashboard.up.railway.app/',
  
  // App Settings
  APP_NAME: 'Rock Dashboard',
  
  // WebView Settings
  WEBVIEW: {
    // Enable JavaScript (required for Chart.js and dashboard functionality)
    javaScriptEnabled: true,
    
    // Allow third-party cookies (needed for session management)
    thirdPartyCookiesEnabled: true,
    
    // Cache mode
    cacheEnabled: true,
    
    // User agent (optional - can customize if needed)
    userAgent: 'RockDashboardMobile/1.0',
  },
  
  // Navigation Settings
  NAVIGATION: {
    // Pages configuration - Add new pages here as your web app grows
    PAGES: {
      LOGIN: '/',
      DASHBOARD: '/dashboard',
      HISTORY: '/history',
      DAILY_TREND: '/dailytrend',
    },
    
    // Page titles for navigation
    TITLES: {
      '/': 'Login',
      '/dashboard': 'Dashboard',
      '/history': 'History',
      '/dailytrend': 'Daily Trend',
    },
  },
  
  // Loading/Error Handling
  TIMEOUT: {
    PAGE_LOAD: 30000, // 30 seconds
    API_REQUEST: 15000, // 15 seconds
  },
};

export default AppConfig;


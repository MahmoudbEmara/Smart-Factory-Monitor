/**
 * Navigation Helper
 * 
 * Utilities for handling navigation between web pages and React Native screens
 */

import AppConfig from '../config/app.config';
import { isRailwayUrl, extractPath } from '../config/url.helper';

/**
 * Map web routes to React Native screen names
 */
const routeToScreenMap = {
  '/': 'Login',
  '/dashboard': 'Dashboard',
  '/history': 'History',
  '/dailytrend': 'DailyTrend',
};

/**
 * Check if a navigation should trigger a React Native screen change
 * @param {string} url - URL being navigated to
 * @param {object} navigation - React Navigation object
 * @returns {boolean} Whether navigation was handled
 */
export const handleWebNavigation = (url, navigation) => {
  if (!url || !isRailwayUrl(url)) {
    return false;
  }

  const path = extractPath(url);
  
  // Check if this path maps to a React Native screen
  const screenName = routeToScreenMap[path];
  
  if (screenName && navigation) {
    // Navigate to the corresponding React Native screen
    // Only navigate if not already on that screen
    navigation.navigate(screenName);
    return true;
  }

  return false;
};

/**
 * Get screen name for a given path
 * @param {string} path - Web path
 * @returns {string|null} Screen name or null
 */
export const getScreenForPath = (path) => {
  return routeToScreenMap[path] || null;
};

/**
 * Check if URL should be opened externally
 * @param {string} url - URL to check
 * @returns {boolean}
 */
export const shouldOpenExternally = (url) => {
  // Allow external URLs for specific cases (e.g., documentation)
  // By default, block all external URLs for security
  return false;
};


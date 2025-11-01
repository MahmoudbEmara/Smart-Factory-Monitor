/**
 * URL Helper Module
 * 
 * Utility functions for URL management and validation
 */

import AppConfig from './app.config';

/**
 * Get the full URL for a given path
 * @param {string} path - The path to navigate to (e.g., '/dashboard')
 * @returns {string} Full URL with Railway domain
 */
export const getFullUrl = (path = '/') => {
  const baseUrl = AppConfig.RAILWAY_URL;
  if (!baseUrl || baseUrl === 'YOUR_RAILWAY_URL_HERE') {
    console.warn('⚠️  RAILWAY_URL not configured! Please update config/app.config.js');
    return null;
  }
  
  // Ensure base URL doesn't end with slash
  const cleanBaseUrl = baseUrl.replace(/\/$/, '');
  
  // Ensure path starts with slash
  const cleanPath = path.startsWith('/') ? path : `/${path}`;
  
  return `${cleanBaseUrl}${cleanPath}`;
};

/**
 * Check if a URL belongs to the Railway domain
 * @param {string} url - URL to check
 * @returns {boolean}
 */
export const isRailwayUrl = (url) => {
  if (!url) return false;
  const baseUrl = AppConfig.RAILWAY_URL.replace(/^https?:\/\//, '').replace(/\/$/, '');
  const urlDomain = url.replace(/^https?:\/\//, '').split('/')[0];
  return urlDomain === baseUrl;
};

/**
 * Extract path from full URL
 * @param {string} url - Full URL
 * @returns {string} Path portion
 */
export const extractPath = (url) => {
  try {
    const urlObj = new URL(url);
    return urlObj.pathname + urlObj.search;
  } catch {
    return url;
  }
};


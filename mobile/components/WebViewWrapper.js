/**
 * WebView Wrapper Component
 * 
 * A reusable, professional WebView component with:
 * - Loading states
 * - Error handling
 * - Navigation detection
 * - Session management
 */

import React, { useState, useRef } from 'react';
import {
  View,
  StyleSheet,
  ActivityIndicator,
  Text,
  TouchableOpacity,
  Platform,
} from 'react-native';
import { WebView } from 'react-native-webview';
import AppConfig from '../config/app.config';
import { getFullUrl, isRailwayUrl } from '../config/url.helper';

const WebViewWrapper = ({
  route,
  initialPath = '/',
  onNavigationStateChange,
  showLoading = true,
}) => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [canGoBack, setCanGoBack] = useState(false);
  const [canGoForward, setCanGoForward] = useState(false);
  const webViewRef = useRef(null);

  const url = getFullUrl(initialPath);

  if (!url) {
    return (
      <View style={styles.errorContainer}>
        <Text style={styles.errorText}>
          Configuration Error: Please set RAILWAY_URL in config/app.config.js
        </Text>
      </View>
    );
  }

  const handleLoadStart = () => {
    setLoading(true);
    setError(null);
  };

  const handleLoadEnd = () => {
    setLoading(false);
    // Inject styles after page loads to ensure they're applied
    if (webViewRef.current) {
      webViewRef.current.injectJavaScript(injectedCSS);
    }
  };

  const handleError = (syntheticEvent) => {
    const { nativeEvent } = syntheticEvent;
    console.error('WebView error: ', nativeEvent);
    setError('Failed to load page. Please check your connection.');
    setLoading(false);
  };

  const handleNavigationStateChange = (navState) => {
    setCanGoBack(navState.canGoBack);
    setCanGoForward(navState.canGoForward);

    // Call parent's navigation handler if provided
    if (onNavigationStateChange) {
      onNavigationStateChange(navState);
    }
  };

  const handleRetry = () => {
    setError(null);
    setLoading(true);
    webViewRef.current?.reload();
  };

  const handleGoBack = () => {
    if (webViewRef.current && canGoBack) {
      webViewRef.current.goBack();
    }
  };

  const handleGoForward = () => {
    if (webViewRef.current && canGoForward) {
      webViewRef.current.goForward();
    }
  };

  // Inject CSS to fix header overlap and center content
  // This runs both on initial load and onLoadEnd for reliability
  const injectedCSS = `
    (function() {
      function applyStyles() {
        // Remove existing style if present to avoid duplicates
        const existing = document.getElementById('mobile-content-fix');
        if (existing) existing.remove();
        
        const style = document.createElement('style');
        style.id = 'mobile-content-fix';
        style.textContent = \`
          /* Prevent header overlap - increase padding for mobile header */
          body {
            padding-top: 80px !important;
            min-height: 100vh !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: center !important;
            align-items: center !important;
          }
          
          /* Override existing flex-start alignment */
          body[style*="align-items: flex-start"] {
            align-items: center !important;
          }
          
          /* Center main content containers */
          #content-wrapper,
          .container {
            margin-top: auto !important;
            margin-bottom: auto !important;
            flex: 0 0 auto !important;
          }
          
          /* Dashboard: Make content wrapper full width on mobile */
          #content-wrapper {
            max-width: 100% !important;
            width: 100% !important;
            margin: auto 10px !important;
            padding: 15px 20px !important;
          }
          
          /* Adjust container margins for history/dailytrend */
          .container {
            margin: auto 20px !important;
          }
          
          /* Make tables and charts full width inside dashboard */
          #content-wrapper table,
          #content-wrapper #barChart {
            width: 100% !important;
            max-width: 100% !important;
          }
          
          /* Ensure chart canvas is full width */
          #content-wrapper canvas#barChart {
            width: 100% !important;
            max-width: 100% !important;
          }
          
          /* Center tables and charts */
          table,
          #barChart,
          #chart-container,
          canvas {
            margin: 0 auto !important;
          }
          
          /* Adjust login box centering */
          .login-box {
            margin: auto !important;
          }
        \`;
        document.head.appendChild(style);
        
        // Force body styles directly to override inline styles
        if (document.body) {
          // Remove any conflicting inline styles first
          document.body.style.removeProperty('align-items');
          document.body.style.removeProperty('justify-content');
          
          // Apply new styles with !important via CSSOM
          const bodyStyle = document.body.style;
          bodyStyle.setProperty('display', 'flex', 'important');
          bodyStyle.setProperty('flex-direction', 'column', 'important');
          bodyStyle.setProperty('justify-content', 'center', 'important');
          bodyStyle.setProperty('align-items', 'center', 'important');
          bodyStyle.setProperty('min-height', '100vh', 'important');
          bodyStyle.setProperty('padding-top', '80px', 'important');
          
          // Also use CSS to override inline styles that might conflict
          const importantStyle = document.createElement('style');
          importantStyle.id = 'mobile-body-override';
          importantStyle.textContent = 'body { align-items: center !important; justify-content: center !important; }';
          document.head.appendChild(importantStyle);
        }
      }
      
      // Apply immediately
      applyStyles();
      
      // Also apply after a short delay to catch dynamically loaded content
      setTimeout(applyStyles, 500);
      setTimeout(applyStyles, 1000);
    })();
    true;
  `;

  return (
    <View style={styles.container}>
      <WebView
        ref={webViewRef}
        source={{ uri: url }}
        style={styles.webview}
        javaScriptEnabled={AppConfig.WEBVIEW.javaScriptEnabled}
        thirdPartyCookiesEnabled={AppConfig.WEBVIEW.thirdPartyCookiesEnabled}
        cacheEnabled={AppConfig.WEBVIEW.cacheEnabled}
        userAgent={AppConfig.WEBVIEW.userAgent}
        injectedJavaScript={injectedCSS}
        onLoadStart={handleLoadStart}
        onLoadEnd={handleLoadEnd}
        onError={handleError}
        onHttpError={(syntheticEvent) => {
          const { nativeEvent } = syntheticEvent;
          console.error('HTTP error: ', nativeEvent.statusCode);
          setError(`HTTP Error: ${nativeEvent.statusCode}`);
          setLoading(false);
        }}
        onNavigationStateChange={handleNavigationStateChange}
        startInLoadingState={showLoading}
        renderLoading={() => (
          <View style={styles.loadingContainer}>
            <ActivityIndicator size="large" color="#4CAF50" />
            <Text style={styles.loadingText}>Loading dashboard...</Text>
          </View>
        )}
        // Allow navigation within Railway domain only
        onShouldStartLoadWithRequest={(request) => {
          // Allow navigation within Railway domain
          if (isRailwayUrl(request.url)) {
            return true;
          }
          // Block external URLs for security
          console.warn('Blocked external URL:', request.url);
          return false;
        }}
      />

      {/* Loading Overlay */}
      {loading && showLoading && (
        <View style={styles.loadingOverlay}>
          <ActivityIndicator size="large" color="#4CAF50" />
          <Text style={styles.loadingText}>Loading...</Text>
        </View>
      )}

      {/* Error Overlay */}
      {error && (
        <View style={styles.errorOverlay}>
          <Text style={styles.errorText}>{error}</Text>
          <TouchableOpacity style={styles.retryButton} onPress={handleRetry}>
            <Text style={styles.retryButtonText}>Retry</Text>
          </TouchableOpacity>
        </View>
      )}

      {/* Navigation Controls (Optional - can be hidden if not needed) */}
      {/* Uncomment if you want back/forward buttons */}
      {/* {(canGoBack || canGoForward) && (
        <View style={styles.navControls}>
          <TouchableOpacity
            style={[styles.navButton, !canGoBack && styles.navButtonDisabled]}
            onPress={handleGoBack}
            disabled={!canGoBack}
          >
            <Text style={styles.navButtonText}>← Back</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={[styles.navButton, !canGoForward && styles.navButtonDisabled]}
            onPress={handleGoForward}
            disabled={!canGoForward}
          >
            <Text style={styles.navButtonText}>Forward →</Text>
          </TouchableOpacity>
        </View>
      )} */}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  webview: {
    flex: 1,
    backgroundColor: 'transparent',
  },
  loadingContainer: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#ffffff',
  },
  loadingOverlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(255, 255, 255, 0.9)',
  },
  loadingText: {
    marginTop: 10,
    fontSize: 14,
    color: '#666',
  },
  errorOverlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#ffffff',
    padding: 20,
  },
  errorContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#ffffff',
  },
  errorText: {
    fontSize: 16,
    color: '#d32f2f',
    textAlign: 'center',
    marginBottom: 20,
  },
  retryButton: {
    backgroundColor: '#4CAF50',
    paddingHorizontal: 30,
    paddingVertical: 12,
    borderRadius: 5,
  },
  retryButtonText: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: '600',
  },
  navControls: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    padding: 10,
    backgroundColor: '#ffffff',
    borderTopWidth: 1,
    borderTopColor: '#e0e0e0',
  },
  navButton: {
    paddingHorizontal: 20,
    paddingVertical: 8,
    backgroundColor: '#4CAF50',
    borderRadius: 5,
  },
  navButtonDisabled: {
    backgroundColor: '#ccc',
  },
  navButtonText: {
    color: '#ffffff',
    fontSize: 14,
    fontWeight: '600',
  },
});

export default WebViewWrapper;


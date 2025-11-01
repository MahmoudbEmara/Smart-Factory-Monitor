/**
 * App Navigator
 * 
 * Main navigation structure for the app.
 * Modular design allows easy addition of new screens.
 */

import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import AppConfig from '../config/app.config';
import WebViewWrapper from '../components/WebViewWrapper';

const Stack = createStackNavigator();

// Screen components - dynamically generated from config
const createScreen = (path, title) => {
  return ({ route }) => (
    <WebViewWrapper
      route={route}
      initialPath={path}
      showLoading={true}
    />
  );
};

const AppNavigator = () => {
  const pages = AppConfig.NAVIGATION.PAGES;
  const titles = AppConfig.NAVIGATION.TITLES;

  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="Login"
        screenOptions={{
          headerStyle: {
            backgroundColor: '#4CAF50',
          },
          headerTintColor: '#fff',
          headerTitleStyle: {
            fontWeight: 'bold',
            fontSize: 18,
          },
          // Prevent native back button from interfering with WebView navigation
          headerBackTitleVisible: false,
        }}
      >
        {/* Login Screen */}
        <Stack.Screen
          name="Login"
          component={createScreen(pages.LOGIN, titles[pages.LOGIN])}
          options={{
            title: titles[pages.LOGIN] || 'Login',
            headerShown: false, // Hide header on login page to match web design
          }}
        />

        {/* Dashboard Screen */}
        <Stack.Screen
          name="Dashboard"
          component={createScreen(pages.DASHBOARD, titles[pages.DASHBOARD])}
          options={{
            title: titles[pages.DASHBOARD] || 'Dashboard',
          }}
        />

        {/* History Screen */}
        <Stack.Screen
          name="History"
          component={createScreen(pages.HISTORY, titles[pages.HISTORY])}
          options={{
            title: titles[pages.HISTORY] || 'History',
          }}
        />

        {/* Daily Trend Screen */}
        <Stack.Screen
          name="DailyTrend"
          component={createScreen(pages.DAILY_TREND, titles[pages.DAILY_TREND])}
          options={{
            title: titles[pages.DAILY_TREND] || 'Daily Trend',
          }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default AppNavigator;


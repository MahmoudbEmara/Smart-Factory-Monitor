/**
 * Main App Entry Point
 * 
 * Root component for the React Native application.
 */

import React from 'react';
import { Platform } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import 'react-native-gesture-handler';
import AppNavigator from './navigation/AppNavigator';

const App = () => {
  return (
    <>
      <StatusBar
        style={Platform.OS === 'ios' ? 'dark' : 'light'}
        backgroundColor="#4CAF50"
      />
      <AppNavigator />
    </>
  );
};

export default App;


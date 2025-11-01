# Expo Go Setup Guide

This guide is for setting up the Rock Dashboard mobile app using **Expo Go** on Windows.

## Prerequisites

- Node.js 18+ installed
- npm or yarn package manager
- Expo Go app installed on your phone:
  - [iOS App Store](https://apps.apple.com/app/expo-go/id982107779)
  - [Google Play Store](https://play.google.com/store/apps/details?id=host.exp.exponent)
- Your phone and computer on the same WiFi network

## Quick Start

### 1. Install Expo CLI (if not already installed)

```bash
npm install -g expo-cli
```

Or use npx (recommended):
```bash
npx expo-cli --version
```

### 2. Install Dependencies

```bash
cd mobile
npm install
```

### 3. Configure Railway URL

Edit `config/app.config.js`:

```javascript
RAILWAY_URL: 'https://kattameya-dashboard.up.railway.app',
```

(You've already done this! ✅)

### 4. Start Expo Development Server

```bash
npm start
```

Or:
```bash
expo start
```

### 5. Open in Expo Go

You'll see a QR code in the terminal. Then:

**Option A: Scan with Expo Go app**
1. Open Expo Go on your phone
2. Tap "Scan QR code"
3. Scan the QR code from your terminal

**Option B: Use Expo Go's connection**
1. Open Expo Go on your phone
2. The app should appear in "Recently opened" if you're on the same network

**Option C: Manual connection**
1. Open Expo Go
2. Enter the connection URL manually (shown in terminal)

## Development Commands

```bash
npm start          # Start Expo dev server
npm run android    # Start with Android focus
npm run ios        # Start with iOS focus
npm run web        # Start web version (for testing)
```

## Features with Expo Go

✅ **Hot Reload** - Changes appear instantly
✅ **No Build Needed** - Test immediately
✅ **Cross-Platform** - Works on iOS and Android
✅ **Easy Testing** - Scan QR code and run

## Limitations

⚠️ **Note:** Some native modules may not work in Expo Go. Our setup uses:
- ✅ `react-native-webview` - **Supported** (included in Expo SDK)
- ✅ `@react-navigation/native` - **Supported**
- ✅ `@react-native-async-storage/async-storage` - **Supported**

All our dependencies are compatible with Expo Go!

## Troubleshooting

### QR Code Not Scanning

1. **Check WiFi**: Phone and computer must be on same network
2. **Firewall**: Allow Expo through Windows Firewall
3. **Manual Connection**: Enter URL manually in Expo Go

### Connection Issues

If the app won't connect:

1. Check that `expo start` shows the QR code
2. Verify both devices are on the same WiFi
3. Try switching to "Tunnel" mode:
   ```bash
   expo start --tunnel
   ```
   (Note: Tunnel requires Expo account)

### "Unable to resolve module" Errors

1. Clear cache and restart:
   ```bash
   expo start -c
   ```
2. Reinstall dependencies:
   ```bash
   rm -rf node_modules
   npm install
   ```

### WebView Not Loading

1. Check `RAILWAY_URL` in `config/app.config.js`
2. Verify your Railway deployment is accessible
3. Check network connection on your phone

## Next Steps

Once it's running in Expo Go:

1. Test login functionality
2. Navigate between pages
3. Verify charts load correctly
4. Test session persistence (login and close/reopen app)

## Building for Production

When ready for production, you can:

1. **Build with EAS (Expo Application Services)**:
   ```bash
   npm install -g eas-cli
   eas login
   eas build:android
   eas build:ios
   ```

2. **Or eject to bare React Native** (if you need full native control)

For now, Expo Go is perfect for development and testing!

## Resources

- [Expo Documentation](https://docs.expo.dev/)
- [Expo Go Guide](https://docs.expo.dev/get-started/installation/)
- [Troubleshooting Guide](https://docs.expo.dev/troubleshooting/clear-cache-windows/)


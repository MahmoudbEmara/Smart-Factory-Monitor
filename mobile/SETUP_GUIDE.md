# Setup Guide - Rock Dashboard Mobile App

This guide will walk you through setting up the React Native mobile app for Rock Dashboard.

## Prerequisites

- Node.js 18+ installed
- npm or yarn package manager
- For iOS: macOS with Xcode installed
- For Android: Android Studio with Android SDK installed
- React Native CLI: `npm install -g react-native-cli`

## Step 1: Install Dependencies

```bash
cd mobile
npm install
```

## Step 2: Configure Railway URL

### Option A: Environment Variable (Recommended)

Create a `.env` file in the `mobile/` directory:

```bash
RAILWAY_URL=https://your-app-name.railway.app
```

### Option B: Direct Configuration

Edit `config/app.config.js` and update:

```javascript
RAILWAY_URL: 'https://your-app-name.railway.app',
```

## Step 3: iOS Setup

1. Install CocoaPods dependencies:

```bash
cd ios
pod install
cd ..
```

2. Open the project in Xcode:

```bash
open ios/RockDashboard.xcworkspace
```

3. In Xcode:
   - Select your development team in "Signing & Capabilities"
   - Choose a simulator or connect a device
   - Press Cmd+R to run

Or use the command line:

```bash
npm run ios
```

## Step 4: Android Setup

1. Make sure Android SDK is configured
2. Start an Android emulator or connect a device
3. Run:

```bash
npm run android
```

## Step 5: Verify Configuration

1. Launch the app
2. You should see the login page from your Railway deployment
3. Try logging in - the session should persist across navigation

## Troubleshooting

### iOS Build Errors

**Error: "No Podfile found"**
```bash
cd ios
pod init
pod install
cd ..
```

**Error: "Command 'pod' not found"**
```bash
sudo gem install cocoapods
```

### Android Build Errors

**Error: "SDK location not found"**
Create `android/local.properties`:
```
sdk.dir=/Users/YOUR_USERNAME/Library/Android/sdk
```

**Error: "Gradle build failed"**
```bash
cd android
./gradlew clean
cd ..
```

### WebView Not Loading

1. Check that `RAILWAY_URL` is correctly set
2. Verify your Railway deployment is accessible from your device/emulator
3. Check network connection
4. Check browser console in WebView (if debugging enabled)

### Session/Authentication Issues

1. Ensure `thirdPartyCookiesEnabled: true` in `config/app.config.js`
2. Clear app cache and try again
3. Check that your Flask session configuration allows cross-domain cookies (if using custom domain)

## Development Tips

### Debugging WebView

To debug the WebView content:

1. **iOS**: Use Safari Web Inspector
   - Enable "Web Inspector" in Settings > Safari > Advanced
   - Connect device and open Safari > Develop > [Your Device] > [WebView]

2. **Android**: Use Chrome DevTools
   - In your app, WebView will be listed under `chrome://inspect`
   - Click "inspect" to open DevTools

### Hot Reloading

The React Native app supports hot reloading:
- Press `R` twice to reload
- Press `Cmd+D` (iOS) or `Ctrl+M` (Android) to open developer menu

### Testing on Real Devices

**iOS:**
1. Connect iPhone/iPad
2. Trust the device when prompted
3. Select device in Xcode
4. Run

**Android:**
1. Enable Developer Options on device
2. Enable USB Debugging
3. Connect via USB
4. Run `npm run android`

## Production Build

### iOS

1. Open Xcode project
2. Product > Archive
3. Follow App Store or TestFlight upload process

### Android

```bash
cd android
./gradlew assembleRelease
```

APK will be in `android/app/build/outputs/apk/release/`

## Next Steps

- Customize app name and icon (see React Native documentation)
- Add app store metadata
- Set up continuous deployment (if desired)


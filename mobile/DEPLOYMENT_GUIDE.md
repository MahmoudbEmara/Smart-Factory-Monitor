# Deployment Guide - Rock Dashboard Mobile App

This guide covers deploying your mobile app to production and app stores.

## Table of Contents

1. [Version Control (GitHub)](#1-version-control-github)
2. [Production Builds](#2-production-builds)
3. [App Store Deployment](#3-app-store-deployment)
4. [Google Play Store Deployment](#4-google-play-store-deployment)
5. [Railway (Backend)](#5-railway-backend)

---

## 1. Version Control (GitHub)

### Initial Setup

If you haven't already:

```bash
cd mobile
git init
git add .
git commit -m "Initial mobile app commit"
```

### Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Link your local repo:

```bash
git remote add origin https://github.com/yourusername/rock-dashboard-mobile.git
git branch -M main
git push -u origin main
```

### Future Updates

```bash
git add .
git commit -m "Description of changes"
git push
```

**Note:** Don't commit:
- `node_modules/` (already in `.gitignore`)
- `.env` with secrets (already in `.gitignore`)
- Build artifacts

---

## 2. Production Builds

For **production builds** (not Expo Go), use **Expo Application Services (EAS)**.

### Setup EAS

1. **Install EAS CLI:**

```bash
npm install -g eas-cli
```

2. **Login to Expo:**

```bash
eas login
```

(If you don't have an Expo account, create one at [expo.dev](https://expo.dev))

3. **Configure EAS Build:**

```bash
cd mobile
eas build:configure
```

This creates `eas.json` with build profiles.

### Build for Android

```bash
eas build --platform android
```

This will:
- Build an `.apk` or `.aab` file
- Upload it to Expo servers
- Provide download link

**Options:**
- `--profile preview` - APK for testing
- `--profile production` - AAB for Play Store

### Build for iOS

```bash
eas build --platform ios
```

**Requirements:**
- Apple Developer account ($99/year)
- Xcode installed (macOS only)
- Or use EAS Build (cloud builds - recommended)

### Build for Both

```bash
eas build --platform all
```

---

## 3. App Store Deployment (iOS)

### Prerequisites

- **Apple Developer Account** - $99/year at [developer.apple.com](https://developer.apple.com)
- **Xcode** (or use EAS cloud builds)

### Steps

1. **Build with EAS:**

```bash
eas build --platform ios --profile production
```

2. **Submit to App Store:**

```bash
eas submit --platform ios
```

This requires:
- App Store Connect API key
- Or manual upload via Xcode/Transporter

### Manual Submission

1. Download the `.ipa` from EAS
2. Open **Transporter** app (macOS)
3. Upload the `.ipa` file
4. Complete metadata in **App Store Connect**:
   - App Store listing
   - Screenshots
   - Description
   - Privacy policy URL
   - App icon

### App Store Connect Setup

1. Go to [App Store Connect](https://appstoreconnect.apple.com)
2. Create new app
3. Fill in app information:
   - Name: "Rock Dashboard"
   - Bundle ID: (matches your `app.json`)
   - Category: Business/Productivity
4. Upload screenshots (required)
5. Submit for review

---

## 4. Google Play Store Deployment (Android)

### Prerequisites

- **Google Play Developer Account** - $25 one-time fee at [play.google.com/console](https://play.google.com/console)

### Steps

1. **Build with EAS:**

```bash
eas build --platform android --profile production
```

This creates an `.aab` (Android App Bundle) file.

2. **Submit to Play Store:**

```bash
eas submit --platform android
```

### Manual Submission

1. Download the `.aab` from EAS
2. Go to [Google Play Console](https://play.google.com/console)
3. Create new app
4. Upload the `.aab` file
5. Fill in store listing:
   - App name
   - Short description
   - Full description
   - Screenshots (required)
   - App icon
   - Feature graphic
6. Complete:
   - Content rating questionnaire
   - Privacy policy (required)
   - Target audience
7. Submit for review

### First Time Setup in Play Console

1. **Create Developer Account** ($25 one-time)
2. **Create App:**
   - App name
   - Default language
   - App type: App
   - Free/Paid
   - Privacy policy URL
3. **App Access:**
   - Choose release type (Internal/Closed/Open testing initially)
4. **Upload Release:**
   - Upload `.aab` file
   - Add release notes

---

## 5. Railway (Backend)

**Railway is ONLY for your Flask backend** - nothing to change for mobile!

Your mobile app already points to:
```javascript
RAILWAY_URL: 'https://kattameya-dashboard.up.railway.app/'
```

### Ensure Railway is Running

1. Check your Railway dashboard
2. Verify the app is deployed
3. Test that the URL is accessible

**The mobile app will use this URL automatically** - no Railway changes needed!

---

## Quick Start: Testing Before Full Deployment

### Option 1: Share Expo Go Link (Easiest)

For testing with others:

1. **Start Expo:**

```bash
npm start
```

2. **Publish to Expo:**

```bash
expo publish
```

This gives you a permanent link like: `exp://exp.host/@yourusername/rock-dashboard`

3. **Share the link** - users need Expo Go app to open it

### Option 2: Internal Testing Builds

**Android (APK):**

```bash
eas build --platform android --profile preview
```

Download the `.apk` and share it directly (side-loading).

**iOS (TestFlight):**

```bash
eas build --platform ios --profile preview
eas submit --platform ios
```

Distribute via TestFlight.

---

## Cost Summary

| Service | Cost | Frequency |
|---------|------|-----------|
| **Expo EAS** | Free (limited) / $29/month | Optional |
| **Apple Developer** | $99/year | Required for App Store |
| **Google Play** | $25 | One-time |
| **Railway** | Already paying | For backend |
| **GitHub** | Free | Optional |

**Free Option:** Use Expo Go sharing for internal testing.

---

## Recommended Deployment Path

### Phase 1: Internal Testing (Free)
1. Share Expo Go link with team
2. Get feedback

### Phase 2: Test Builds ($25)
1. Build Android APK via EAS
2. Share APK for testing
3. Optionally: iOS TestFlight

### Phase 3: Store Deployment ($124)
1. Apple Developer: $99/year
2. Google Play: $25 one-time
3. Build and submit both

---

## Important Files to Update Before Deployment

### `app.json`

Update these for production:

```json
{
  "expo": {
    "name": "Rock Dashboard",
    "slug": "rock-dashboard-mobile",
    "version": "1.0.0",  // Update for each release
    "ios": {
      "bundleIdentifier": "com.yourcompany.rockdashboard",
      "buildNumber": "1"  // Increment for each build
    },
    "android": {
      "package": "com.yourcompany.rockdashboard",
      "versionCode": 1  // Increment for each build
    }
  }
}
```

### Environment Check

Before building, verify:
- ✅ Railway URL is correct in `config/app.config.js`
- ✅ App name is correct in `app.json`
- ✅ Bundle ID/Package name is unique
- ✅ Version numbers are set

---

## Troubleshooting

### Build Fails

1. **Check logs:**
   ```bash
   eas build:list
   eas build:view [build-id]
   ```

2. **Common issues:**
   - Missing environment variables
   - Invalid bundle ID
   - Missing app icons

### Submission Fails

1. **iOS:** Check App Store Connect for errors
2. **Android:** Check Play Console for policy violations

---

## Resources

- [EAS Build Docs](https://docs.expo.dev/build/introduction/)
- [App Store Connect](https://appstoreconnect.apple.com)
- [Google Play Console](https://play.google.com/console)
- [Expo Documentation](https://docs.expo.dev/)

---

## Quick Commands Reference

```bash
# Build
eas build --platform android
eas build --platform ios
eas build --platform all

# Submit
eas submit --platform android
eas submit --platform ios

# Check status
eas build:list
eas build:view [build-id]

# Configure
eas build:configure
```

---

Good luck with your deployment! 🚀


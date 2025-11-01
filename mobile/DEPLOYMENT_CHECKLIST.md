# Deployment Checklist

Use this checklist before deploying to app stores.

## Pre-Deployment

### Code Preparation

- [ ] Code is committed to GitHub
- [ ] All features tested and working
- [ ] No console errors or warnings
- [ ] Railway URL is correct in `config/app.config.js`
- [ ] App tested on real devices (iOS and Android)

### Configuration

- [ ] Update `app.json`:
  - [ ] App name
  - [ ] Version number
  - [ ] Bundle ID / Package name (unique)
  - [ ] Build numbers

- [ ] Update `config/app.config.js`:
  - [ ] Railway URL is production URL
  - [ ] No debug/test URLs

### Assets

- [ ] App icon (1024x1024 PNG)
  - Place in `assets/icon.png`
- [ ] Splash screen (2048x2048 PNG)
  - Place in `assets/splash.png`
- [ ] Adaptive icon (Android, 1024x1024)
  - Place in `assets/adaptive-icon.png`
- [ ] Favicon (Web, 48x48)
  - Place in `assets/favicon.png`

### Screenshots (Required for Stores)

- [ ] iOS screenshots:
  - [ ] 6.5" display (iPhone 14 Pro Max): 1284 x 2778
  - [ ] 5.5" display: 1242 x 2208
  - [ ] At least 1 screenshot required

- [ ] Android screenshots:
  - [ ] Phone: 1080 x 1920 (at least 2)
  - [ ] Tablet: 1920 x 1200 (optional)
  - [ ] Feature graphic: 1024 x 500

### Store Listings

#### App Store (iOS)

- [ ] App name (max 30 characters)
- [ ] Subtitle (max 30 characters)
- [ ] Description (4000 characters max)
- [ ] Keywords (100 characters max)
- [ ] Privacy policy URL (required)
- [ ] Support URL
- [ ] Marketing URL (optional)
- [ ] Category selection
- [ ] Age rating completed
- [ ] App icon uploaded
- [ ] Screenshots uploaded

#### Google Play (Android)

- [ ] App name (50 characters max)
- [ ] Short description (80 characters max)
- [ ] Full description (4000 characters max)
- [ ] Graphics:
  - [ ] App icon (512 x 512)
  - [ ] Feature graphic (1024 x 500)
  - [ ] Screenshots (at least 2)
- [ ] Privacy policy URL (required)
- [ ] Content rating questionnaire completed
- [ ] Target audience defined
- [ ] Category selection

### Legal / Compliance

- [ ] Privacy policy created and hosted
  - Must cover data collection
  - WebView usage
  - Session/cookie handling
- [ ] Terms of service (optional but recommended)
- [ ] GDPR compliance (if applicable)

### Accounts Setup

- [ ] Apple Developer Account ($99/year)
  - [ ] Account created
  - [ ] Payment method added
  - [ ] Team admin access
- [ ] Google Play Developer Account ($25 one-time)
  - [ ] Account created
  - [ ] Payment method added
  - [ ] Developer agreement accepted

### EAS Build Setup

- [ ] EAS CLI installed
- [ ] Expo account created
- [ ] Logged in: `eas login`
- [ ] Build configured: `eas build:configure`
- [ ] `eas.json` created and reviewed

## Build Phase

### Android Build

- [ ] Preview build tested:
  ```bash
  eas build --platform android --profile preview
  ```
- [ ] Production build created:
  ```bash
  eas build --platform android --profile production
  ```
- [ ] `.aab` file downloaded
- [ ] Build tested on Android device(s)

### iOS Build

- [ ] Preview build tested (if possible)
- [ ] Production build created:
  ```bash
  eas build --platform ios --profile production
  ```
- [ ] `.ipa` file downloaded
- [ ] Build tested on iOS device(s) or TestFlight

## Submission Phase

### App Store Submission

- [ ] App Store Connect app created
- [ ] App information filled
- [ ] Screenshots uploaded
- [ ] Privacy policy URL added
- [ ] Age rating completed
- [ ] Version information set
- [ ] Build uploaded via EAS or manually
- [ ] App submitted for review

### Google Play Submission

- [ ] Play Console app created
- [ ] Store listing completed
- [ ] Content rating completed
- [ ] Privacy policy URL added
- [ ] `.aab` uploaded
- [ ] Release notes added
- [ ] App submitted for review

## Post-Submission

- [ ] Review status monitored
- [ ] Rejection reasons addressed (if any)
- [ ] App approved ✅
- [ ] App published to store
- [ ] Store listing verified
- [ ] Download and test from store

## Version Updates (Future)

- [ ] Increment version in `app.json`
- [ ] Increment build numbers
- [ ] Update changelog
- [ ] Test new version
- [ ] Build new version
- [ ] Submit update

---

## Quick Notes

**Version Format:**
- iOS: `1.0.0` (version) + `1` (buildNumber)
- Android: `1.0.0` (versionName) + `1` (versionCode)

**First Submission:**
- iOS: 24-48 hour review
- Android: Usually faster, but can take 1-7 days

**Update Submissions:**
- Usually faster than first submission
- iOS: Often approved in hours
- Android: Often approved in hours to days

---

**Good luck! 🚀**


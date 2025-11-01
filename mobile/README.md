# Rock Dashboard Mobile App

React Native mobile app (using **Expo**) that wraps the Rock Dashboard web application using WebView.

## Architecture

This app uses a **modular WebView approach** - it wraps your existing Flask web dashboard running on Railway, making it easy to maintain and extend:

- **No backend changes needed** - Your Flask app continues to work as-is
- **Modular navigation** - Easy to add new pages as your web app grows
- **Session persistence** - WebView handles cookies/sessions automatically
- **Professional polish** - Loading states, error handling, and smooth navigation
- **Expo Go compatible** - Test instantly on your phone without building

## Project Structure

```
mobile/
├── components/
│   └── WebViewWrapper.js      # Reusable WebView component with loading/error states
├── config/
│   ├── app.config.js          # Centralized app configuration
│   └── url.helper.js          # URL utility functions
├── navigation/
│   └── AppNavigator.js        # Main navigation structure
├── App.js                      # Root component
├── index.js                    # Entry point
└── package.json                # Dependencies
```

## Setup Instructions

### Option A: Expo Go (Recommended for Development)

**Perfect for Windows users!** Test on your phone instantly.

1. **Install Dependencies:**
   ```bash
   cd mobile
   npm install
   ```

2. **Configure Railway URL:**
   Edit `config/app.config.js`:
   ```javascript
   RAILWAY_URL: 'https://your-app-name.railway.app',
   ```

3. **Start Expo Server:**
   ```bash
   npm start
   ```

4. **Open in Expo Go:**
   - Install [Expo Go](https://expo.dev/client) on your phone
   - Scan the QR code from your terminal
   - Your app will load!

See [EXPO_SETUP.md](./EXPO_SETUP.md) for detailed Expo Go instructions.

### Option B: Development Build (iOS/Android)

If you need native development:

1. **Install Dependencies:**
   ```bash
   cd mobile
   npm install
   ```

2. **Configure Railway URL:**
   Edit `config/app.config.js`

3. **Run:**
   ```bash
   npm run android  # For Android
   npm run ios      # For iOS (macOS only)
   ```

## Adding New Pages

When you add new pages to your Flask web app, simply update `config/app.config.js`:

```javascript
NAVIGATION: {
  PAGES: {
    LOGIN: '/',
    DASHBOARD: '/dashboard',
    HISTORY: '/history',
    DAILY_TREND: '/dailytrend',
    // Add your new page here:
    NEW_PAGE: '/new-page',
  },
  
  TITLES: {
    '/': 'Login',
    '/dashboard': 'Dashboard',
    '/history': 'History',
    '/dailytrend': 'Daily Trend',
    // Add title for new page:
    '/new-page': 'New Page Title',
  },
},
```

Then add the screen to `navigation/AppNavigator.js`:

```javascript
<Stack.Screen
  name="NewPage"
  component={createScreen(pages.NEW_PAGE, titles[pages.NEW_PAGE])}
  options={{
    title: titles[pages.NEW_PAGE] || 'New Page',
  }}
/>
```

That's it! The navigation system will automatically create the new screen.

## Features

- ✅ **Automatic Session Management** - WebView handles Flask sessions/cookies
- ✅ **Loading States** - Professional loading indicators
- ✅ **Error Handling** - Graceful error messages with retry
- ✅ **Navigation** - Stack navigation with proper back/forward support
- ✅ **Security** - Blocks external URLs, only allows Railway domain
- ✅ **Modular** - Easy to extend without touching core code

## Configuration Options

All settings are in `config/app.config.js`:

- `RAILWAY_URL` - Your Railway deployment URL
- `WEBVIEW` - WebView settings (JavaScript, cookies, cache)
- `NAVIGATION` - Pages and titles
- `TIMEOUT` - Loading and API timeouts

## Troubleshooting

### WebView not loading
- Check that `RAILWAY_URL` is correctly set in `config/app.config.js`
- Verify your Railway deployment is accessible
- Check network connection

### Authentication not working
- WebView should handle cookies automatically
- If issues persist, check that `thirdPartyCookiesEnabled: true` in config

### Charts not rendering
- Ensure `javaScriptEnabled: true` in WebView config
- Check that Chart.js CDN is accessible from mobile device

## Building for Production

### Android
```bash
cd android
./gradlew assembleRelease
```

### iOS
Open Xcode, select Product > Archive, and follow the prompts.

## License

Same as main project.


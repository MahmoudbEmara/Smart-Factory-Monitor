# Quick Start Guide

## 🚀 5-Minute Setup

### 1. Configure Railway URL

Edit `config/app.config.js`:

```javascript
RAILWAY_URL: 'https://your-app-name.railway.app',
```

### 2. Install Dependencies

```bash
cd mobile
npm install
```

### 3. iOS Setup (if building for iOS)

```bash
cd ios
pod install
cd ..
npm run ios
```

### 4. Android Setup (if building for Android)

```bash
npm run android
```

## ✅ That's It!

The app will:
- Load your Railway dashboard
- Handle authentication automatically
- Support all your existing pages
- Work offline with cached content (if configured)

## 📱 Adding New Pages

When you add new pages to your Flask app:

1. **Update `config/app.config.js`:**

```javascript
PAGES: {
  // ... existing pages
  NEW_PAGE: '/new-page',  // Add here
},

TITLES: {
  // ... existing titles
  '/new-page': 'New Page',  // Add here
},
```

2. **Add to `navigation/AppNavigator.js`:**

```javascript
<Stack.Screen
  name="NewPage"
  component={createScreen(pages.NEW_PAGE, titles[pages.NEW_PAGE])}
  options={{
    title: titles[pages.NEW_PAGE] || 'New Page',
  }}
/>
```

Done! The new page will appear in navigation.

## 🔧 Common Tasks

### Change App Name
Edit `app.json`:
```json
{
  "name": "YourAppName",
  "displayName": "Your Display Name"
}
```

### Change App Colors
Edit `navigation/AppNavigator.js`:
```javascript
headerStyle: {
  backgroundColor: '#YOUR_COLOR',  // Change here
},
```

### Disable Loading Indicator
In `components/WebViewWrapper.js`:
```javascript
<WebViewWrapper showLoading={false} />
```

### Enable Debug Mode
```bash
npm start -- --reset-cache
```

## 🐛 Troubleshooting

**WebView blank?** → Check `RAILWAY_URL` in config
**Can't login?** → Check network connection
**Charts not loading?** → Verify JavaScript is enabled in config

## 📚 Full Documentation

See `README.md` and `SETUP_GUIDE.md` for detailed information.


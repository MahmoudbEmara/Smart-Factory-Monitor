# Project Structure

```
mobile/
├── components/
│   └── WebViewWrapper.js          # Reusable WebView component
│
├── config/
│   ├── app.config.js              # Centralized configuration
│   └── url.helper.js              # URL utilities
│
├── navigation/
│   └── AppNavigator.js            # Navigation setup
│
├── utils/
│   └── navigation.helper.js      # Navigation utilities
│
├── App.js                         # Root component
├── index.js                       # Entry point
├── app.json                       # App metadata
├── package.json                   # Dependencies
├── .babelrc.js                    # Babel config
├── metro.config.js                # Metro bundler config
│
├── README.md                      # Main documentation
├── SETUP_GUIDE.md                 # Detailed setup instructions
├── QUICK_START.md                 # Quick reference
└── PROJECT_STRUCTURE.md           # This file
```

## Component Overview

### `components/WebViewWrapper.js`
- Main WebView component with loading/error states
- Handles navigation, session management
- Reusable across all screens

### `config/app.config.js`
- **Central configuration file**
- Update `RAILWAY_URL` here
- Add new pages here as your web app grows

### `config/url.helper.js`
- URL validation and manipulation
- Domain checking utilities

### `navigation/AppNavigator.js`
- React Navigation setup
- Screen definitions
- Add new screens here when adding pages

### `utils/navigation.helper.js`
- Helper functions for navigation
- Route-to-screen mapping

## Adding New Pages

When you add pages to your Flask web app:

1. **Update `config/app.config.js`:**
   ```javascript
   PAGES: {
     // ... existing
     NEW_PAGE: '/new-page',
   },
   TITLES: {
     // ... existing
     '/new-page': 'New Page',
   },
   ```

2. **Update `navigation/AppNavigator.js`:**
   ```javascript
   <Stack.Screen
     name="NewPage"
     component={createScreen(pages.NEW_PAGE, titles[pages.NEW_PAGE])}
     options={{ title: titles[pages.NEW_PAGE] }}
   />
   ```

That's it! The modular design makes it easy to extend.

## File Responsibilities

| File | Purpose |
|------|---------|
| `App.js` | App entry point, status bar setup |
| `index.js` | React Native registration |
| `app.config.js` | **Main config - update this first!** |
| `WebViewWrapper.js` | WebView component with all features |
| `AppNavigator.js` | Navigation structure |


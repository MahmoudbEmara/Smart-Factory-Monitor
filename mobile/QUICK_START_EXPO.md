# Quick Start - Expo Go (Windows)

## 🚀 3-Step Setup

### 1. Reinstall Dependencies (for Expo)

Since we converted to Expo, you need to reinstall:

```bash
cd mobile
rm -rf node_modules package-lock.json
npm install
```

This installs Expo SDK 51 and compatible packages.

### 2. Configure Railway URL

Your Railway URL is already set in `config/app.config.js`:
```javascript
RAILWAY_URL: 'https://kattameya-dashboard.up.railway.app/',
```

✅ Already done!

### 3. Start Expo and Test

```bash
npm start
```

Then:
1. Install [Expo Go](https://expo.dev/client) on your phone
2. Scan the QR code from your terminal
3. App loads on your phone!

## ⚡ That's It!

Your app will:
- ✅ Load your Railway dashboard
- ✅ Handle login automatically
- ✅ Work on iOS and Android
- ✅ Update instantly when you save files

## 📱 What You'll See

- QR code in terminal
- Connection URL
- "Expo Go" button to open on device

## 🔧 Next Time

Just run:
```bash
npm start
```

And scan the QR code!

## 🐛 Troubleshooting

**No QR code?** → Check that both devices are on same WiFi  
**Can't connect?** → Try `npm start --tunnel` (requires Expo account)  
**App not loading?** → Check Railway URL in `config/app.config.js`

See [EXPO_SETUP.md](./EXPO_SETUP.md) for detailed troubleshooting.


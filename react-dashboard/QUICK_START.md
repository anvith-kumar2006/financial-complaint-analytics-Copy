# React Dashboard — Quick Start Guide

**Last Updated:** November 24, 2026  
**Status:** ✅ Production Ready

---

## 🚀 Deploy to Vercel (1 minute)

```powershell
npm install -g vercel
cd react-dashboard
vercel --prod
```

Then go to Vercel dashboard → Settings → Environment Variables → Add `VITE_POWERBI_EMBED_URL`

---

## 🔧 Local Development

```powershell
cd react-dashboard
npm install
npm run dev
```

Runs on `http://localhost:5173` with hot reload.

---

## 📦 Build & Test

```powershell
npm run build      # Production build (outputs to dist/)
npm run preview    # Test production build locally
npm run lint       # Run linter
```

---

## 🔐 Power BI Setup (Optional)

### If NO Embed URL:
- Power BI tab shows setup guide
- Download .pbix button available
- All other features work normally

### To Enable Power BI Embedding:
1. Publish report to Power BI Service
2. File → Embed report → Publish to web (or Secure embed)
3. Copy embed URL
4. Create `.env.local` in `react-dashboard/`:
   ```
   VITE_POWERBI_EMBED_URL=https://your-embed-url
   ```
5. Run: `npm run dev` (Vite auto-reloads)

**For Production (Vercel):**
1. Go to Vercel dashboard
2. Settings → Environment Variables
3. Add `VITE_POWERBI_EMBED_URL`
4. Redeploy: `vercel --prod`

---

## 📊 Dashboard Contents

### React Analytics Tab
- **KPI Cards** — 7 key metrics (Total, Open, Closed, Timely Rate, etc.)
- **Charts** — 5 visualizations (Products, Channels, States, Response Time, Trends)
- **Table** — Top 15 issue categories with rates

### Power BI Dashboard Tab
- **Embedded Report** — Interactive Power BI dashboard (if configured)
- **Setup Guide** — Instructions if not configured
- **Download** — Get .pbix file for local analysis

---

## 📁 Project Structure

```
react-dashboard/
├── src/
│   ├── components/        # React components
│   ├── App.tsx           # Main component
│   ├── types.ts          # TypeScript interfaces
│   └── index.css         # Styles
├── public/
│   ├── complaints_cleaned.csv      # Data (1.07 MB)
│   └── Financial_Complaint_Analytics.pbix  # Power BI file
├── dist/                 # Production build
├── .env.local.example    # Env template (don't commit .env.local)
├── package.json
└── vite.config.ts
```

---

## ✅ Verification Checklist

- [ ] `npm run build` succeeds (zero errors)
- [ ] React Analytics tab displays all charts
- [ ] KPI values match: Total=4,975, Timely Rate=90.08%
- [ ] IssueTable shows top 15 categories with contrast fixed
- [ ] Power BI tab shows setup guide (if no env var) OR embedded report (if configured)
- [ ] All buttons work (Download, Fullscreen, etc.)
- [ ] Mobile layout is responsive

---

## 🔗 Resources

- **Build Tool:** Vite + React 18 + TypeScript
- **Styling:** Tailwind CSS
- **Charts:** Recharts
- **Icons:** Lucide React
- **Data Source:** Client-side CSV parsing (1.07 MB)
- **Backend:** None (100% static frontend)

---

## 💡 Tips

**Slower build?**
```powershell
npm cache clean --force
rm -r node_modules
npm install
```

**TypeScript errors?**
```powershell
npm run type-check
```

**Bundle too large?**
Check `npm run build` output — look for large dependencies.

**Data not loading?**
1. Check browser DevTools → Network tab
2. Verify `/complaints_cleaned.csv` loads
3. Check file is in `public/` folder
4. Clear browser cache

---

## 🚨 Common Issues

| Issue | Fix |
|-------|-----|
| Power BI tab shows setup guide | Add `VITE_POWERBI_EMBED_URL` env var (see above) |
| Charts don't render | Check CSV loaded in Network tab |
| Contrast warning | ✅ Fixed in IssueTable with `text-gray-900` |
| ChannelChart labels overlap | ✅ Fixed with custom label renderer |
| Build fails | Run `npm cache clean --force` then `npm install` |

---

## 📞 Support

**Documentation:**
- `DEPLOYMENT_AND_POWERBI_SETUP.md` — Detailed deployment guide
- `REACT_DASHBOARD_IMPROVEMENTS_SUMMARY.md` — All changes made
- `FINAL_VERIFICATION_CHECKLIST.md` — Full QA checklist

---

**🎯 Summary:** Dashboard is production-ready. Deploy with `vercel --prod` and optionally configure Power BI embed URL in Vercel dashboard.

import { useState } from 'react'
import { Download, Maximize2, AlertCircle } from 'lucide-react'

function PowerBISection() {
  const [isFullscreen, setIsFullscreen] = useState(false)
  const embedUrl = import.meta.env.VITE_POWERBI_EMBED_URL

  const handleDownload = () => {
    const link = document.createElement('a')
    link.href = '/Financial_Complaint_Analytics.pbix'
    link.download = 'Financial_Complaint_Analytics.pbix'
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }

  const toggleFullscreen = () => {
    setIsFullscreen(!isFullscreen)
  }

  // If no embed URL is configured, show setup message
  if (!embedUrl) {
    return (
      <div className="space-y-6">
        {/* Setup Message */}
        <div className="chart-container border-l-4 border-blue-500">
          <div className="flex items-start gap-4">
            <div className="bg-blue-100 p-3 rounded-lg flex-shrink-0">
              <AlertCircle className="w-6 h-6 text-blue-600" />
            </div>
            <div className="flex-1">
              <h2 className="text-xl font-bold text-gray-900 mb-2">
                Power BI Report Setup Required
              </h2>
              <p className="text-gray-700 mb-4">
                To display the interactive Power BI report here, the report must first be published to Power BI Service 
                and configured with an embed URL.
              </p>
              
              <div className="bg-gray-50 p-4 rounded-lg mb-4 border border-gray-200">
                <h3 className="font-semibold text-gray-900 mb-2">Setup Steps:</h3>
                <ol className="list-decimal list-inside space-y-2 text-sm text-gray-700">
                  <li>Open <code className="bg-gray-200 px-2 py-1 rounded">Financial_Complaint_Analytics.pbix</code> in Power BI Desktop</li>
                  <li>Publish to Power BI Service (File → Publish → Publish to Power BI)</li>
                  <li>In Power BI Service, open the report and click File → Embed report → Publish to web (for public) or Secure embed (for authenticated users)</li>
                  <li>Copy the embed URL</li>
                  <li>Add to your environment: <code className="bg-gray-200 px-2 py-1 rounded">VITE_POWERBI_EMBED_URL=your-embed-url</code></li>
                  <li>Rebuild and redeploy the application</li>
                </ol>
              </div>

              <div className="bg-yellow-50 p-4 rounded-lg border border-yellow-200 mb-4">
                <h3 className="font-semibold text-yellow-900 mb-1 flex items-center gap-2">
                  <AlertCircle className="w-4 h-4" />
                  Security Note
                </h3>
                <p className="text-sm text-yellow-800">
                  <strong>Do not use "Publish to web"</strong> for confidential data. For secure embedding with authentication, 
                  you'll need to implement a backend service that generates embed tokens. Never expose access tokens or 
                  service principal credentials in frontend code.
                </p>
              </div>

              <div className="flex gap-3 flex-wrap">
                <button
                  onClick={handleDownload}
                  className="flex items-center gap-2 bg-blue-600 text-white px-5 py-2.5 rounded-lg hover:bg-blue-700 transition-colors"
                >
                  <Download className="w-4 h-4" />
                  Download .pbix File
                </button>
                <a
                  href="https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-embed-secure"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-2 bg-gray-100 text-gray-700 px-5 py-2.5 rounded-lg hover:bg-gray-200 transition-colors border border-gray-300"
                >
                  Embedding Documentation
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }

  // If embed URL is configured, show the embedded report
  return (
    <div className={isFullscreen ? 'fixed inset-0 z-50 bg-white p-4' : ''}>
      <div className="space-y-4">
        {/* Header with controls */}
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-bold text-gray-900">Power BI Analytics Dashboard</h2>
          <div className="flex gap-2">
            <button
              onClick={handleDownload}
              className="flex items-center gap-2 bg-gray-100 text-gray-700 px-4 py-2 rounded-lg hover:bg-gray-200 transition-colors text-sm"
              title="Download .pbix file"
            >
              <Download className="w-4 h-4" />
              Download
            </button>
            <button
              onClick={toggleFullscreen}
              className="flex items-center gap-2 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition-colors text-sm"
              title={isFullscreen ? 'Exit fullscreen' : 'Enter fullscreen'}
            >
              <Maximize2 className="w-4 h-4" />
              {isFullscreen ? 'Exit' : 'Fullscreen'}
            </button>
          </div>
        </div>

        {/* Power BI Embed */}
        <div className="chart-container p-0 overflow-hidden">
          <iframe
            title="Power BI Report"
            src={embedUrl}
            className="w-full border-0"
            style={{ height: isFullscreen ? 'calc(100vh - 100px)' : '800px' }}
            allowFullScreen
          />
        </div>

        {isFullscreen && (
          <div className="text-sm text-gray-600 text-center">
            Press ESC or click Exit Fullscreen to return
          </div>
        )}
      </div>
    </div>
  )
}

export default PowerBISection

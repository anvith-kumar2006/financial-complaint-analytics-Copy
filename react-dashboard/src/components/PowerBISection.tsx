import { Download, FileSpreadsheet, Check } from 'lucide-react'

const reportUrl = `${import.meta.env.BASE_URL}Financial_Complaint_Analytics.pbix`

const downloadSteps = [
  'Download the .pbix file.',
  'Open Microsoft Power BI Desktop.',
  'Open the downloaded report.',
  'Explore the interactive complaint analytics dashboard.',
]

function PowerBISection() {
  return (
    <section className="powerbi-page">
      <div className="powerbi-download-card">
        <div className="powerbi-report-art" aria-hidden="true">
          <div className="powerbi-report-icon">
            <FileSpreadsheet className="h-10 w-10" strokeWidth={1.7} />
          </div>
          <div className="powerbi-preview">
            <div className="powerbi-preview-heading">
              <span />
              <span />
              <span />
            </div>
            <div className="powerbi-preview-content">
              <div className="powerbi-preview-chart">
                <i />
                <i />
                <i />
                <i />
                <i />
              </div>
              <div className="powerbi-preview-lines">
                <i />
                <i />
                <i />
              </div>
            </div>
          </div>
        </div>

        <div className="powerbi-copy">
          <span className="powerbi-eyebrow">FINANCIAL COMPLAINT ANALYTICS</span>
          <h1>Your Power BI Dashboard Is Ready!</h1>
          <p>
            Explore the interactive Financial Complaint Analytics report using Microsoft Power BI Desktop.
          </p>

          <p className="powerbi-download-prompt">
            Click the button below to download your Power BI report!
          </p>
          <a
            className="powerbi-download-button"
            href={reportUrl}
            download="Financial_Complaint_Analytics.pbix"
          >
            <Download className="h-5 w-5" aria-hidden="true" />
            <span>⬇ Download Power BI Report (.PBIX)</span>
          </a>
          <p className="powerbi-download-hint">
            Click above to get your Power BI report file.
          </p>
        </div>

        <div className="powerbi-steps">
          {downloadSteps.map((step, index) => (
            <div className="powerbi-step" key={step}>
              <span className="powerbi-step-number">
                {index + 1}
              </span>
              <p>{step}</p>
              <Check className="powerbi-step-check" aria-hidden="true" />
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

export default PowerBISection

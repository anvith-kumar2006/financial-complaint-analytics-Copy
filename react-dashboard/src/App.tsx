import { useState, useEffect } from 'react'
import './App.css'
import KPICards from './components/KPICards'
import ProductChart from './components/ProductChart'
import StateChart from './components/StateChart'
import ChannelChart from './components/ChannelChart'
import TrendsChart from './components/TrendsChart'
import ResponseTimeChart from './components/ResponseTimeChart'
import IssueTable from './components/IssueTable'
import PowerBISection from './components/PowerBISection'
import { ComplaintData } from './types'
import { BarChart3, FileSpreadsheet } from 'lucide-react'

type TabType = 'react' | 'powerbi'

function App() {
  const [data, setData] = useState<ComplaintData[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [activeTab, setActiveTab] = useState<TabType>('react')

  useEffect(() => {
    // Load CSV data from public folder
    fetch('/complaints_cleaned.csv')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to load data')
        }
        return response.text()
      })
      .then(csvText => {
        const parsed = parseCSV(csvText)
        setData(parsed)
        setLoading(false)
      })
      .catch(err => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  const parseCSV = (csvText: string): ComplaintData[] => {
    const lines = csvText.split('\n')
    // const headers = lines[0].split(',') // Headers are implicit in our mapping
    
    return lines.slice(1)
      .filter(line => line.trim())
      .map(line => {
        const values = line.split(',')
        return {
          complaint_id: values[0],
          date_received: values[1],
          financial_product: values[2],
          issue_category: values[3],
          issue_detail: values[4],
          company_name: values[5],
          state: values[6],
          submission_channel: values[7],
          response_due_date: values[8],
          date_company_responded: values[9],
          response_status: values[10],
          company_response: values[11],
          timely_response: values[12],
          short_complaint_summary: values[13],
          response_time_days: values[14] ? parseFloat(values[14]) : undefined
        }
      })
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-2xl text-gray-600">Loading dashboard...</div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-2xl text-red-600">Error: {error}</div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-blue-600 text-white shadow-lg">
        <div className="container mx-auto px-4 py-6">
          <h1 className="text-3xl font-bold">Financial Complaint Analytics Dashboard</h1>
          <p className="text-blue-100 mt-1">Comprehensive analysis of customer complaints (Oct 2025 - Oct 2026)</p>
        </div>
      </header>

      {/* Navigation Tabs */}
      <nav className="bg-white border-b border-gray-200 shadow-sm sticky top-0 z-10">
        <div className="container mx-auto px-4">
          <div className="flex gap-2">
            <button
              onClick={() => setActiveTab('react')}
              className={`flex items-center gap-2 px-6 py-4 font-semibold transition-colors border-b-2 ${
                activeTab === 'react'
                  ? 'border-blue-600 text-blue-600 bg-blue-50'
                  : 'border-transparent text-gray-600 hover:text-gray-900 hover:bg-gray-50'
              }`}
            >
              <BarChart3 className="w-5 h-5" />
              React Analytics
            </button>
            <button
              onClick={() => setActiveTab('powerbi')}
              className={`flex items-center gap-2 px-6 py-4 font-semibold transition-colors border-b-2 ${
                activeTab === 'powerbi'
                  ? 'border-blue-600 text-blue-600 bg-blue-50'
                  : 'border-transparent text-gray-600 hover:text-gray-900 hover:bg-gray-50'
              }`}
            >
              <FileSpreadsheet className="w-5 h-5" />
              Power BI Dashboard
            </button>
          </div>
        </div>
      </nav>

      <main className="container mx-auto px-4 py-8">
        {activeTab === 'react' && (
          <>
            {/* KPI Section */}
            <KPICards data={data} />

            {/* Charts Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">
              <ProductChart data={data} />
              <ChannelChart data={data} />
              <StateChart data={data} />
              <ResponseTimeChart data={data} />
            </div>

            {/* Trends Chart - Full Width */}
            <div className="mt-8">
              <TrendsChart data={data} />
            </div>

            {/* Issue Table */}
            <div className="mt-8">
              <IssueTable data={data} />
            </div>
          </>
        )}

        {activeTab === 'powerbi' && <PowerBISection />}
      </main>

      <footer className="bg-gray-800 text-white mt-12 py-6">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; 2026 Financial Complaint Analytics. Data processed: {data.length} complaints</p>
        </div>
      </footer>
    </div>
  )
}

export default App

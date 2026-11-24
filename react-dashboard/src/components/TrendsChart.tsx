import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { ComplaintData } from '../types'

interface Props {
  data: ComplaintData[]
}

function TrendsChart({ data }: Props) {
  const monthlyStats = data.reduce((acc, complaint) => {
    const month = complaint.date_received.substring(0, 7) // YYYY-MM format
    if (!acc[month]) {
      acc[month] = { month, total: 0, timely: 0, untimely: 0 }
    }
    acc[month].total++
    if (complaint.timely_response === 'Yes') acc[month].timely++
    if (complaint.timely_response === 'No') acc[month].untimely++
    return acc
  }, {} as Record<string, { month: string; total: number; timely: number; untimely: number }>)

  const chartData = Object.values(monthlyStats)
    .sort((a, b) => a.month.localeCompare(b.month))
    .map(item => ({
      ...item,
      timelyRate: item.timely + item.untimely > 0 
        ? ((item.timely / (item.timely + item.untimely)) * 100).toFixed(1) 
        : 0
    }))

  return (
    <div className="chart-container">
      <h2 className="text-xl font-bold mb-4 text-gray-800">Monthly Trends (Oct 2025 - Oct 2026)</h2>
      <ResponsiveContainer width="100%" height={350}>
        <LineChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="month" fontSize={12} />
          <YAxis yAxisId="left" />
          <YAxis yAxisId="right" orientation="right" />
          <Tooltip />
          <Legend />
          <Line yAxisId="left" type="monotone" dataKey="total" stroke="#3b82f6" name="Total Complaints" strokeWidth={2} />
          <Line yAxisId="right" type="monotone" dataKey="timelyRate" stroke="#10b981" name="Timely Rate (%)" strokeWidth={2} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}

export default TrendsChart

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { ComplaintData } from '../types'

interface Props {
  data: ComplaintData[]
}

function ResponseTimeChart({ data }: Props) {
  const buckets: Record<string, number> = {
    '0-3 days': 0,
    '4-7 days': 0,
    '8-15 days': 0,
    '16-30 days': 0,
    '30+ days': 0,
  }

  data.forEach(complaint => {
    if (complaint.response_status === 'Closed' && complaint.response_time_days) {
      const days = complaint.response_time_days
      if (days <= 3) buckets['0-3 days']++
      else if (days <= 7) buckets['4-7 days']++
      else if (days <= 15) buckets['8-15 days']++
      else if (days <= 30) buckets['16-30 days']++
      else buckets['30+ days']++
    }
  })

  const chartData = Object.entries(buckets).map(([bucket, count]) => ({
    bucket,
    count,
  }))

  return (
    <div className="chart-container">
      <h2 className="text-xl font-bold mb-4 text-gray-800">Response Time Distribution</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="bucket" fontSize={12} />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="count" fill="#f59e0b" name="Complaint Count" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}

export default ResponseTimeChart

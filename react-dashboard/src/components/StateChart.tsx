import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { ComplaintData } from '../types'

interface Props {
  data: ComplaintData[]
}

function StateChart({ data }: Props) {
  const stateStats = data.reduce((acc, complaint) => {
    const state = complaint.state || 'Missing'
    if (!acc[state]) {
      acc[state] = { state, total: 0 }
    }
    acc[state].total++
    return acc
  }, {} as Record<string, { state: string; total: number }>)

  const chartData = Object.values(stateStats)
    .sort((a, b) => b.total - a.total)
    .slice(0, 15) // Top 15 states

  return (
    <div className="chart-container">
      <h2 className="text-xl font-bold mb-4 text-gray-800">Top 15 States by Complaint Volume</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="state" fontSize={12} />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="total" fill="#3b82f6" name="Total Complaints" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}

export default StateChart

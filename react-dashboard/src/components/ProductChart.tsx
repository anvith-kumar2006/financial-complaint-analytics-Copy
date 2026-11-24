import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { ComplaintData } from '../types'

interface Props {
  data: ComplaintData[]
}

function ProductChart({ data }: Props) {
  const productStats = data.reduce((acc, complaint) => {
    const product = complaint.financial_product
    if (!acc[product]) {
      acc[product] = { product, total: 0, open: 0, closed: 0 }
    }
    acc[product].total++
    if (complaint.response_status === 'Open') acc[product].open++
    if (complaint.response_status === 'Closed') acc[product].closed++
    return acc
  }, {} as Record<string, { product: string; total: number; open: number; closed: number }>)

  const chartData = Object.values(productStats)
    .sort((a, b) => b.total - a.total)

  return (
    <div className="chart-container">
      <h2 className="text-xl font-bold mb-4 text-gray-800">Complaints by Financial Product</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={chartData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="product" angle={-45} textAnchor="end" height={100} fontSize={12} />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="closed" fill="#10b981" name="Closed" />
          <Bar dataKey="open" fill="#fbbf24" name="Open" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}

export default ProductChart

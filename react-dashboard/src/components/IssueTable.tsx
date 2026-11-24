import { ComplaintData } from '../types'

interface Props {
  data: ComplaintData[]
}

function IssueTable({ data }: Props) {
  const issueStats = data.reduce((acc, complaint) => {
    const issue = complaint.issue_category
    if (!acc[issue]) {
      acc[issue] = { 
        issue, 
        total: 0, 
        closed: 0, 
        timely: 0, 
        untimely: 0 
      }
    }
    acc[issue].total++
    if (complaint.response_status === 'Closed') acc[issue].closed++
    if (complaint.timely_response === 'Yes') acc[issue].timely++
    if (complaint.timely_response === 'No') acc[issue].untimely++
    return acc
  }, {} as Record<string, { 
    issue: string
    total: number
    closed: number
    timely: number
    untimely: number
  }>)

  const tableData = Object.values(issueStats)
    .sort((a, b) => b.total - a.total)
    .slice(0, 15)
    .map(item => ({
      ...item,
      closureRate: ((item.closed / item.total) * 100).toFixed(1),
      timelyRate: item.timely + item.untimely > 0 
        ? ((item.timely / (item.timely + item.untimely)) * 100).toFixed(1)
        : 'N/A'
    }))

  return (
    <div className="table-container">
      <h2 className="text-xl font-bold mb-4 text-gray-800">Top 15 Issue Categories</h2>
      <table>
        <thead>
          <tr>
            <th>Issue Category</th>
            <th className="text-right">Total</th>
            <th className="text-right">Closed</th>
            <th className="text-right">Closure Rate</th>
            <th className="text-right">Timely</th>
            <th className="text-right">Timely Rate</th>
          </tr>
        </thead>
        <tbody>
          {tableData.map((row, index) => (
            <tr key={index}>
              <td className="font-medium text-gray-900">{row.issue}</td>
              <td className="text-right text-gray-900">{row.total.toLocaleString()}</td>
              <td className="text-right text-gray-900">{row.closed.toLocaleString()}</td>
              <td className="text-right text-gray-900">{row.closureRate}%</td>
              <td className="text-right text-gray-900">{row.timely.toLocaleString()}</td>
              <td className="text-right text-gray-900">{row.timelyRate}{typeof row.timelyRate === 'string' ? '' : '%'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default IssueTable

import { ComplaintData } from '../types'

interface Props {
  data: ComplaintData[]
}

function KPICards({ data }: Props) {
  const totalComplaints = data.length
  const openComplaints = data.filter(d => d.response_status === 'Open').length
  const closedComplaints = data.filter(d => d.response_status === 'Closed').length
  const timelyYes = data.filter(d => d.timely_response === 'Yes').length
  const timelyNo = data.filter(d => d.timely_response === 'No').length
  const timelyRate = timelyYes + timelyNo > 0 ? (timelyYes / (timelyYes + timelyNo)) * 100 : 0
  
  const closedWithTime = data.filter(d => d.response_status === 'Closed' && d.response_time_days)
  const avgResponseDays = closedWithTime.length > 0
    ? closedWithTime.reduce((sum, d) => sum + (d.response_time_days || 0), 0) / closedWithTime.length
    : 0

  const kpis = [
    { label: 'Total Complaints', value: totalComplaints.toLocaleString(), color: 'blue', subtext: '100%' },
    { label: 'Open', value: openComplaints.toLocaleString(), color: 'yellow', subtext: `${((openComplaints/totalComplaints)*100).toFixed(2)}%` },
    { label: 'Closed', value: closedComplaints.toLocaleString(), color: 'green', subtext: `${((closedComplaints/totalComplaints)*100).toFixed(2)}%` },
    { label: 'Timely Response Rate', value: `${timelyRate.toFixed(2)}%`, color: 'purple', subtext: `${timelyYes.toLocaleString()} timely` },
    { label: 'Avg Response Time', value: `${avgResponseDays.toFixed(2)} days`, color: 'orange', subtext: 'For closed complaints' },
  ]

  const colorClasses: Record<string, string> = {
    blue: 'border-l-blue-500',
    yellow: 'border-l-yellow-500',
    green: 'border-l-green-500',
    purple: 'border-l-purple-500',
    orange: 'border-l-orange-500',
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6">
      {kpis.map((kpi, index) => (
        <div key={index} className={`kpi-card border-l-4 ${colorClasses[kpi.color]}`}>
          <div className="text-sm text-gray-600 font-semibold mb-1">{kpi.label}</div>
          <div className="text-3xl font-bold text-gray-900">{kpi.value}</div>
          <div className="text-xs text-gray-500 mt-1">{kpi.subtext}</div>
        </div>
      ))}
    </div>
  )
}

export default KPICards

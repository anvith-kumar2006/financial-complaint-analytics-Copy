export interface ComplaintData {
  complaint_id: string
  date_received: string
  financial_product: string
  issue_category: string
  issue_detail: string
  company_name: string
  state: string
  submission_channel: string
  response_due_date: string
  date_company_responded: string
  response_status: string
  company_response: string
  timely_response: string
  short_complaint_summary: string
  response_time_days?: number
}

export interface KPIMetrics {
  total_complaints: number
  open_complaints: number
  closed_complaints: number
  timely_yes: number
  timely_no: number
  timely_rate: number
  avg_response_days: number
}

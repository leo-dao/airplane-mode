# Copyright (c) 2024, Leo Dao and contributors
# For license information, please see license.txt
import frappe
from frappe.utils import flt

def execute(filters=None):
    columns, data = [], []

    columns = [
        {"fieldname": "airline", "label": "Airline", "fieldtype": "Link", "options": "Airline", "width": 150},
        {"fieldname": "revenue", "label": "Revenue", "fieldtype": "Currency", "width": 150}
    ]
    airlines = frappe.db.sql("""
		SELECT 
			ap.name AS airline, 
			COALESCE(SUM(at.total_amount), 0) AS revenue 
		FROM 
			`tabAirline` ap
		LEFT JOIN 
			`tabAirplane` af ON af.airline = ap.name
		LEFT JOIN 
			`tabAirplane Flight` aff ON aff.airplane = af.name
		LEFT JOIN 
			`tabAirplane Ticket` at ON at.flight = aff.name
		GROUP BY 
			ap.name
		ORDER BY 
			revenue DESC
		""", as_dict=1)
    
    chart_data = {'labels': [], 'datasets': []}
    dataset = {'name': 'Revenue', 'values': []}

    total_revenue = 0
    
    for airline in airlines:
        data.append({
            "airline": airline['airline'],
            "revenue": flt(airline['revenue'])
        })
        total_revenue += flt(airline['revenue'])
        chart_data['labels'].append(airline['airline'])
        dataset['values'].append(airline['revenue'])
        
    chart_data['datasets'].append(dataset)

    chart = {
        "data": chart_data,
        "type": 'donut',
        "height": 250
    }
    
    summary = [{
        "value": total_revenue,
        "indicator": "Green",
        "label": "Total Revenue",
    }]
    
    return columns, data, None, chart, summary
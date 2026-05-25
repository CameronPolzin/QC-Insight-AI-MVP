import { useEffect, useState } from "react";
import {BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer} from "recharts";

function App() {

    //stores analytics data fetched from backend
    const [analytics, setAnalytics] = useState(null);

    //runs once when when the page loads
    useEffect(() => {

        //requests analytics data from the FastAPI backend
        fetch("http://127.0.0.1:8000/analytics/summary")
            .then((response) => response.json())
            .then((data) => setAnalytics(data));

    }, []);

    //show loading message while waiting for backend data
    if (!analytics) {
        return <h1>Loading analytics...</h1>;
    }

    //convert backend data into chart format
    const defectData = Object.entries(
        analytics.defect_types
    ).map(([name, value]) => ({
        name,
        value
    }));

    const severityData = Object.entries(
        analytics.severity_breakdown
    ).map(([name, value]) => ({
        name,
        value
    }));

    return (
        <div style={{ padding: "30px", fontFamily: "Arial", minHeight: "100vh" }}>

            <h1>QC Insight AI Dashboard</h1>

            <h2>Total Reports</h2>
            <p>{analytics.total_reports}</p>

            <h2>Top Products</h2>
            <ul>
                {Object.entries(analytics.top_products).map(([product, count]) => (
                    <li key={product}>
                        {product}: {count}
                    </li>
                ))}
            </ul>

            <h2>Top Employees</h2>
            <ul>
                {Object.entries(analytics.top_employees).map(([employee, count]) => (
                    <li key={employee}>
                        {employee}: {count}
                    </li>
                ))}
            </ul>

            <h2>Severity Breakdown</h2>
            <ResponsiveContainer width="100%" height={300}>
                <BarChart data={severityData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="value" />
                </BarChart>
            </ResponsiveContainer>
            <ul>
                {Object.entries(analytics.severity_breakdown).map(([severity, count]) => (
                    <li key={severity}>
                        {severity}: {count}
                    </li>
                ))}
            </ul>

            <h2>Defect Types</h2>
            <ResponsiveContainer width="100%" height={300}>
                <BarChart data={defectData}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="value" />
                </BarChart>
            </ResponsiveContainer>
            <ul>
                {Object.entries(analytics.defect_types).map(([defect, count]) => (
                    <li key={defect}>
                        {defect}: {count}
                    </li>
                ))}
            </ul>

        </div>
    );
}

export default App;
import { useEffect, useState } from "react";

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

    return (
        <div style={{ padding: "20px", fontFamily: "Arial" }}>

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
            <ul>
                {Object.entries(analytics.severity_breakdown).map(([severity, count]) => (
                    <li key={severity}>
                        {severity}: {count}
                    </li>
                ))}
            </ul>

            <h2>Defect Types</h2>
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
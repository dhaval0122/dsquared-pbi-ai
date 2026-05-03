def generate_visual_layout():
    """
    Returns a simple dashboard layout definition
    """

    return {
        "visuals": [
            {
                "type": "card",
                "title": "Total Sales",
                "measure": "Total Sales"
            },
            {
                "type": "lineChart",
                "title": "Sales Trend",
                "x": "Date[Date]",
                "y": "Total Sales"
            },
            {
                "type": "barChart",
                "title": "Sales Comparison",
                "x": "Category",
                "y": "Total Sales"
            }
        ]
    }
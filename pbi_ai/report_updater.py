import json

def update_report_json(pbip_path, layout):
    report_file = f"{pbip_path}/report/report.json"

    with open(report_file, "r", encoding="utf-8") as f:
        report = json.load(f)

    if "sections" not in report:
        report["sections"] = []

    section = {
        "name": "AI Dashboard",
        "visualContainers": []
    }

    for v in layout["visuals"]:
        section["visualContainers"].append({
            "visualType": v["type"],
            "title": v["title"],
            "query": {
                "x": v.get("x"),
                "y": v.get("y"),
                "measure": v.get("measure")
            }
        })

    report["sections"].append(section)

    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("✅ Report visuals updated")
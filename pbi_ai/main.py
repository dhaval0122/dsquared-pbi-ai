import subprocess
import json
#from .dax_generator import generate_dax
from .dashboard_generator import generate_dashboard_plan
from .visual_generator import generate_visual_layout
from .report_updater import update_report_json

def create_measure(name, dax):
    cmd = [
        "pbi",
        "measure",
        "create",
        "--name", name,
        "--expression", dax
    ]
    subprocess.run(cmd, check=True)

PBIP_PATH = "YOUR_PBIP_PROJECT_PATH"

def run():
    user_input = input("Describe dashboard: ")

    # 1. AI dashboard plan
    plan_raw = generate_dashboard_plan(user_input)

    plan = json.loads(plan_raw)

    # 2. Create measures
    for m in plan["measures"]:
        create_measure(m["name"], m["dax"])

    # 3. Generate visuals
    layout = generate_visual_layout()

    # 4. Inject into Power BI report
    update_report_json(PBIP_PATH, layout)

    print("\n🎉 Dashboard fully generated (measures + visuals)")

if __name__ == "__main__":
    run()
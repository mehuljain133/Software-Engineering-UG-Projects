# Quality Control and Risk Management: Quality Control and Quality Assurance, SoftwareProcess Assessment and Improvement Capability Maturity Model Integration (CMMI); SoftwareRisks, Risk Identification, Risk Projection and Risk Refinement, Risk Mitigation, Monitoringand Management. 

import random
import matplotlib.pyplot as plt

# --- 1. Quality Control and Quality Assurance ---
class QualityControlAndAssurance:
    def __init__(self):
        self.qc_description = "Quality Control (QC) focuses on identifying defects in the final product to ensure it meets specifications."
        self.qa_description = "Quality Assurance (QA) focuses on improving processes to prevent defects during software development."
    
    def display_descriptions(self):
        print("\n--- Quality Control and Quality Assurance ---")
        print(f"Quality Control: {self.qc_description}")
        print(f"Quality Assurance: {self.qa_description}")


# --- 2. Capability Maturity Model Integration (CMMI) ---
class CMMI:
    def __init__(self):
        self.maturity_levels = [
            "Level 1: Initial - Processes are unpredictable and poorly controlled.",
            "Level 2: Managed - Processes are planned, measured, and controlled.",
            "Level 3: Defined - Processes are well defined and standardized.",
            "Level 4: Quantitatively Managed - Processes are controlled using statistical and quantitative methods.",
            "Level 5: Optimizing - Continuous improvement is enabled by optimizing processes."
        ]

    def display_maturity_levels(self):
        print("\n--- Capability Maturity Model Integration (CMMI) ---")
        for level in self.maturity_levels:
            print(level)


# --- 3. Software Risk Management ---
class RiskManagement:
    def __init__(self):
        self.risks = [
            {"name": "Technical Complexity", "probability": 0.8, "impact": 9},
            {"name": "Team Skill Gap", "probability": 0.6, "impact": 8},
            {"name": "Requirement Changes", "probability": 0.7, "impact": 7},
            {"name": "Budget Overrun", "probability": 0.5, "impact": 6},
            {"name": "Timeline Pressure", "probability": 0.9, "impact": 10}
        ]

    def identify_risks(self):
        print("\n--- Identifying Risks ---")
        for risk in self.risks:
            print(f"Risk: {risk['name']} | Probability: {risk['probability']} | Impact: {risk['impact']}")

    def project_risks(self):
        print("\n--- Projecting Risks ---")
        risk_scores = []
        for risk in self.risks:
            risk_score = risk["probability"] * risk["impact"]
            risk_scores.append(risk_score)
            print(f"Risk: {risk['name']} | Projected Risk Score: {risk_score}")
        return risk_scores

    def refine_risks(self):
        print("\n--- Refining Risks ---")
        refined_risks = []
        for risk in self.risks:
            # For simplicity, we adjust the risk score based on hypothetical risk reduction strategies
            refined_risk_score = random.uniform(0.5, 1.0) * (risk["probability"] * risk["impact"])
            refined_risks.append(refined_risk_score)
            print(f"Refined Risk for {risk['name']}: {refined_risk_score:.2f}")
        return refined_risks

    def mitigate_risks(self):
        print("\n--- Mitigating Risks ---")
        mitigation_plan = {}
        for risk in self.risks:
            if risk["probability"] > 0.7:
                mitigation_plan[risk["name"]] = "Implement technical improvements or hire additional resources."
            else:
                mitigation_plan[risk["name"]] = "Monitor and adjust project timelines."
        for risk, plan in mitigation_plan.items():
            print(f"Risk: {risk} | Mitigation Plan: {plan}")

    def monitor_and_manage(self):
        print("\n--- Monitoring and Managing Risks ---")
        risk_status = {}
        for risk in self.risks:
            status = "On Track" if risk["probability"] < 0.7 else "At High Risk"
            risk_status[risk["name"]] = status
        for risk, status in risk_status.items():
            print(f"Risk: {risk} | Status: {status}")

    def plot_risk_scores(self, risk_scores):
        plt.figure(figsize=(10, 6))
        plt.bar([risk['name'] for risk in self.risks], risk_scores)
        plt.xlabel("Risks")
        plt.ylabel("Risk Score (Probability * Impact)")
        plt.title("Risk Projection Scores")
        plt.xticks(rotation=45, ha="right")
        plt.show()


# --- Simulate Quality Control, CMMI, and Risk Management ---
def simulate_quality_and_risk_management():
    print("===== QUALITY CONTROL AND RISK MANAGEMENT SIMULATION =====")

    # 1. Quality Control and Quality Assurance
    qc_qa = QualityControlAndAssurance()
    qc_qa.display_descriptions()

    # 2. CMMI - Capability Maturity Model Integration
    cmmi = CMMI()
    cmmi.display_maturity_levels()

    # 3. Risk Management
    risk_management = RiskManagement()
    risk_management.identify_risks()
    risk_scores = risk_management.project_risks()
    refined_risks = risk_management.refine_risks()
    risk_management.mitigate_risks()
    risk_management.monitor_and_manage()
    risk_management.plot_risk_scores(risk_scores)


# Run the simulation
simulate_quality_and_risk_management()


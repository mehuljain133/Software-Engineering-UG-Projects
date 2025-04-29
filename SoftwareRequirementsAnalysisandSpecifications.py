# Software Requirements Analysis and Specifications: Use Case Approach, SoftwareRequirement Specification Document, Flow oriented Modeling, Data Flow Modeling, SequenceDiagrams

# --- Software Requirements Analysis and Specifications Simulation ---

# --- 1. Use Case Approach ---
class UseCase:
    def __init__(self, name, actors, description):
        self.name = name
        self.actors = actors
        self.description = description

    def display(self):
        print(f"\n[Use Case] {self.name}")
        print(f"Actors: {', '.join(self.actors)}")
        print(f"Description: {self.description}")


class UseCaseModel:
    def __init__(self):
        self.use_cases = [
            UseCase("User Login", ["User"], "The user logs into the system with username and password."),
            UseCase("View Dashboard", ["User"], "The user views their personalized dashboard."),
            UseCase("Make Payment", ["User", "Payment Gateway"], "User initiates a payment and confirms payment.")
        ]

    def display_use_cases(self):
        print("\n--- Use Case Model ---")
        for use_case in self.use_cases:
            use_case.display()


# --- 2. Software Requirement Specification Document ---
class SRS:
    def __init__(self, title, version, description):
        self.title = title
        self.version = version
        self.description = description

    def display(self):
        print("\n--- Software Requirement Specification (SRS) Document ---")
        print(f"Title: {self.title}")
        print(f"Version: {self.version}")
        print(f"Description: {self.description}")
        print("\nKey Requirements:")
        print("1. User authentication should be secure.")
        print("2. Dashboard should load in less than 2 seconds.")
        print("3. Payment gateway integration is required.")


# --- 3. Flow-Oriented Modeling (Functional View) ---
class FlowOrientedModel:
    def __init__(self):
        self.flow_steps = [
            "User submits credentials → Authenticate User → Display Dashboard",
            "User selects payment → Validate Payment → Confirm Transaction"
        ]

    def display_flow(self):
        print("\n--- Flow-Oriented Modeling ---")
        for step in self.flow_steps:
            print(f"→ {step}")


# --- 4. Data Flow Diagram (DFD) Simulation ---
class DFD:
    def __init__(self):
        self.dfd_processes = [
            "Authenticate User", "Process Payment", "Load Dashboard", "Manage User Sessions"
        ]
        self.data_stores = [
            "User Database", "Payment Gateway", "Session Data"
        ]
        self.external_entities = [
            "User", "Payment Gateway"
        ]

    def display_dfd(self):
        print("\n--- Data Flow Diagram (DFD) ---")
        print("Processes:")
        for process in self.dfd_processes:
            print(f"- {process}")
        
        print("\nData Stores:")
        for store in self.data_stores:
            print(f"- {store}")
        
        print("\nExternal Entities:")
        for entity in self.external_entities:
            print(f"- {entity}")


# --- 5. Sequence Diagrams ---
class SequenceDiagram:
    def __init__(self, name, actors, interactions):
        self.name = name
        self.actors = actors
        self.interactions = interactions

    def display(self):
        print(f"\n--- Sequence Diagram: {self.name} ---")
        print("Actors:", ", ".join(self.actors))
        print("Interactions:")
        for interaction in self.interactions:
            print(f"-> {interaction}")


class SequenceModel:
    def __init__(self):
        self.sequence_diagrams = [
            SequenceDiagram(
                "User Login Process",
                ["User", "Authentication System", "Database"],
                [
                    "User submits credentials → Authentication System validates → Database retrieves user data → Login successful"
                ]
            ),
            SequenceDiagram(
                "Payment Process",
                ["User", "Payment System", "Payment Gateway", "Database"],
                [
                    "User initiates payment → Payment System processes → Payment Gateway validates → Database confirms transaction"
                ]
            )
        ]

    def display_sequence_diagrams(self):
        for diagram in self.sequence_diagrams:
            diagram.display()


# --- Simulate Software Requirements Analysis and Specifications ---
def simulate_software_requirements():
    print("===== SOFTWARE REQUIREMENTS ANALYSIS AND SPECIFICATIONS SIMULATION =====")

    # 1. Use Case Approach
    use_case_model = UseCaseModel()
    use_case_model.display_use_cases()

    # 2. Software Requirement Specification Document
    srs = SRS("Online Payment System", "1.0", "A secure system for processing online payments and managing user data.")
    srs.display()

    # 3. Flow-Oriented Modeling
    flow_model = FlowOrientedModel()
    flow_model.display_flow()

    # 4. Data Flow Diagram (DFD)
    dfd = DFD()
    dfd.display_dfd()

    # 5. Sequence Diagrams
    sequence_model = SequenceModel()
    sequence_model.display_sequence_diagrams()


# Run the simulation
simulate_software_requirements()


# ==============================================================================
# APEX CORE SYSTEMS - LABS INFRASTRUCTURE
# SUITE: BASE CORE ARCHITECTURE
# ENGINE: APEX BASE 1 (V0.1.0-ALPHA)
# CONFIGURATION: METALLIC LIGHT GRAY (#D3D3D3) LIGHT THEME
# ==============================================================================

class ApexBase1Engine:
    def __init__(self, target_username):
        self.username = target_username
        self.engine_series = "Apex Base 1"
        self.version = "v0.1.0-Alpha"
        self.completed_matches = 0
        self.total_centipawn_loss = 0
        self.detected_blunders = 0
        self.time_spent_thinking = 0.0
        
    def process_match_telemetry(self, match_number, average_cpl, blunders, think_time):
        """
        Ingests performance statistics from individual placement matches.
        Executed entirely within the lightweight Base 1 local processing loop.
        """
        print(f"\n[{self.engine_series}] Parsing telemetry data for Match #{match_number}...")
        self.completed_matches += 1
        self.total_centipawn_loss += average_cpl
        self.detected_blunders += blunders
        self.time_spent_thinking += think_time
        
    def calculate_verified_elo(self):
        """
        Base Series rapid benchmarking calculation matrix.
        Maps basic human chess capabilities in a tight 3-match window.
        """
        if self.completed_matches < 3:
            return f"Processing... {self.completed_matches}/3 matches analyzed."
            
        mean_cpl = self.total_centipawn_loss / 3
        mean_think_time = self.time_spent_thinking / 3
        
        # Base 1 logic heuristics
        base_elo = 2000 - (mean_cpl * 12) - (self.detected_blunders * 75)
        
        if mean_think_time < 5.0 and self.detected_blunders > 2:
            base_elo -= 100  
            
        verified_elo = max(600, min(2800, round(base_elo)))
        return verified_elo

# ==============================================================================
# EXECUTION INTERFACE
# ==============================================================================
if __name__ == "__main__":
    print("┌────────────────────────────────────────────────────────┐")
    print("│         INITIALIZING ENGINE STATUS: APEX BASE 1        │")
    print("│         VERSION: v0.1.0-ALPHA // BOOTSTRAP STAGE       │")
    print("└────────────────────────────────────────────────────────┘")
    
    user_profile = input("\nEnter your user account name to start: ")
    coach = ApexBase1Engine(user_profile)
    
    print(f"\nCoachy: 'Hey {user_profile}! Running on the {coach.engine_series} network.'")
    print(f"[COACHY] Initializing 3-Game Placement Challenge under {coach.version}...")
    
    # Telemetry simulation sequence
    input("\n[Press Enter to simulate Match 1 results...]")
    coach.process_match_telemetry(match_number=1, average_cpl=35, blunders=1, think_time=12.4)
    
    input("[Press Enter to simulate Match 2 results...]")
    coach.process_match_telemetry(match_number=2, average_cpl=28, blunders=0, think_time=15.1)
    
    input("[Press Enter to simulate Match 3 results...]")
    coach.process_match_telemetry(match_number=3, average_cpl=62, blunders=2, think_time=4.2)
    
    input("\n[Press Enter to execute Base 1 rapid ELO calculation...]")
    final_rating = coach.calculate_verified_elo()
    
    print("\n┌────────────────────────────────────────────────────────┐")
    print(f"│  APEX HORIZON PLACEMENT READOUT: {user_profile}             │")
    print("├────────────────────────────────────────────────────────┤")
    print(f"│  • Active Core Engine: {coach.engine_series} ({coach.version})│")
    print(f"│  • Final Verified ELO: {final_rating}                          │")
    print("└────────────────────────────────────────────────────────┘")
    print("  MADE BY APEX CORE  ")

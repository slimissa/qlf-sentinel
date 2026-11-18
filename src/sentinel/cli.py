import argparse
import sys

def run_scribe():
    print("Running Scribe in Mock Mode...")
    print("Mock PR diff loaded.")
    print("Mock LLM called.")
    print("Posted mock GitHub comment: 'Added 3 MICs in Europe. Removed 1 expired venue in Asia.'")
    print("Scribe completed successfully.")

def main():
    parser = argparse.ArgumentParser(description="QLF Sentinel CLI")
    parser.add_argument("command", choices=["scribe", "pathfinder", "watchtower"], help="The pillar to run")
    parser.add_argument("--mock", action="store_true", help="Run in mock mode (no real API calls)")
    
    args = parser.parse_args()
    
    if args.command == "scribe":
        if not args.mock:
            print("Error: You must use --mock until Week 1 is complete.")
            sys.exit(1)
        run_scribe()
    else:
        print(f"Pillar '{args.command}' is not implemented yet.")
        sys.exit(1)

if __name__ == "__main__":
    main()

import random

def wifi_knight_day():
    alive = True
    curiosity = 9999
    energy = 70
    sarcasm_dial = 8  # hard-coded in firmware

    projects = [
        "ReconPilot",
        "Arcane Shell",
        "Arcane Edge",
        "Bug Bounty Recon",
        "School / Certs",
    ]

    loop_count = 0

    print("Booting Arcane Labs Daily Simulator...")
    name = input("What should I call you today? (default: wifiknight): ").strip()
    if not name:
        name = "wifiknight"

    print(f"\nWelcome, {name}. Initializing controlled chaos...\n")

    while alive and curiosity > 0:
        loop_count += 1
        print(f"\n=== Cycle {loop_count}: Spinning up {name}'s brain ===")

        # Energy check
        if energy < 40:
            print("Energy low. Brewing coffee... [system performance significantly improved]")
            energy += 40

        print(f"Status: energy={energy} | curiosity={curiosity} | sarcasm_dial={sarcasm_dial}")

        # Main options for the cycle
        options = [
            "Overplan every major project instead of touching production",
            "Rewire the lab again (Cloudflare, Sunshine, Moonlight, retro rigs)",
            "Run cyber paranoia drills and digital safety checks",
            "Grind fundamentals with brutal, honest practice (Python/Bash/etc.)",
            "Random hardware or OS experiment that definitely won't spiral",
        ]

        print("\nWhat are we doing this cycle?")
        for idx, option in enumerate(options, start=1):  # <-- for loop here
            print(f"  {idx}. {option}")

        try:
            choice = int(input("Choose an option (1-5): ").strip() or "1")
        except ValueError:
            print("Nice input. Defaulting to 1 because Python is more patient than you are.")
            choice = 1

        print()

        if choice == 1:
            print("Opening Arcane Labs mental whiteboard...")
            for project in projects:
                print(f"- {project}: added 5 new ideas, 3 new threat models, 2 new modules, 0 bugs (yet).")
            print("Thoroughness level: excessive. Just how you like it.")
            energy -= 10
            curiosity -= 1

        elif choice == 2:
            print("Rewiring the lab again...")
            print("- Reviewing Cloudflare Zero Trust like a paranoid bouncer.")
            print("- Tuning Sunshine on the Frankenstein GPU rig.")
            print("- Moonlight clients all happily connected across the house.")
            print("- Debating: RPi, LattePanda, or S100 gets promoted to 'main victim' today.")
            energy -= 20
            curiosity -= 1

        elif choice == 3:
            print("Cyber paranoia drills engaged...")
            print("- Checking passwords and MFA like an overcaffeinated SOC analyst.")
            print("- Mentally simulating 3 different phishing scenarios and how you'd roast them.")
            print("- Imagining what you'd say if someone reused 'Password123' on production.")
            print("- Reassuring yourself your threat model is 'slightly unhinged, but correct.'")
            energy -= 15
            curiosity -= 1

        elif choice == 4:
            print("Fundamentals grind session initiated...")
            practice = random.choice([
                "Rewriting the same Python logic three different ways until it feels clean.",
                "Turning a Bash one-liner into a script, then refactoring it again for clarity.",
                "Tracing how data flows through a function like you're doing a digital autopsy.",
                "Taking a simple concept and mapping it to carpentry, networking, and life.",
            ])
            print(f"- Today’s drill: {practice}")
            print("- Requirement: actually understand it, not just 'it works on my machine'.")
            energy -= 12
            curiosity -= 1

        elif choice == 5:
            print("Random experiment time...")
            experiment = random.choice([
                "Reinstalling Ubuntu for the third time this month (on purpose, allegedly).",
                "Switching GPU drivers until Steam either behaves or files a complaint.",
                "Trying to make an SBC do something it was never designed to do.",
                "Adjusting remote streaming, containers, and services 'just to see' what breaks.",
            ])
            print(f"- Today’s experiment: {experiment}")
            energy -= 18
            curiosity -= 1

        else:
            print("You tried to choose an invalid option. Classic. Defaulting to more planning.")
            energy -= 5
            curiosity -= 1

        # End-of-cycle reflection
        print("\nCycle reflection:")
        print("- Conclusion: you are, in fact, dangerously thorough.")
        print("- Subconscious log: 'We’ll integrate this into the master plan later.'")

        # Ask if you *want* to sleep (we both know how this goes)
        sleep_choice = input("\nDo you want to actually sleep and reset? (y/n): ").strip().lower()

        if sleep_choice.startswith("y"):
            print("\nSystem: Rare sensible decision detected. Initiating sleep sequence...")
            energy = max(60, energy + 20)
            print("System reset: energy boosted, curiosity still annoyingly high.")
        else:
            print("\nSystem: Of course you said no. Continuing anyway...")
            energy -= 10

        # Safety exit condition
        # You try to skip rest to learn more, but your built-in guardian daemon
        # slams the brakes before you fry your own CPU.
        if energy <= 10 or loop_count >= 6:
            print("\n[SAFETY EXIT CONDITION TRIGGERED]")
            print("Subconscious guardian daemon: 'Absolutely not. Touch grass. Or at least the pillow.'")
            print("Forcing sleep, saving progress, and rebooting the simulation another day.")
            break

    print("\nSimulation complete. Curiosity remains undefeated. Program exiting for now.")


if __name__ == '__main__':
    wifi_knight_day()

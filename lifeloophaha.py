from datetime import datetime
import random
import time

# welcome to my daily loop, i hope you enjoy the pun and fun!!
def boot_sequence():
    print("Booting wifiknight life Simulator...")
    time.sleep(2)
    now = datetime.now()
    time_str = now.strftime("%I:%M %p")
    hour = now.hour
    if 5 <= hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 17:
        greeting = "Good afternoon"
    elif 17 <= hour < 23:
        greeting = "Good evening"
    elif hour >= 23 or hour < 2:
        greeting = "It's late... go to bed... kidding!"
    else:
        greeting = (
            "It's after 2 AM, cleared for deep dive. "
            "Let's deconstruct reality and reassemble it in Python... or Bash... "
            "maybe it could be implemented in C?... coffee first, decisions after "
            "caffeine protocol needs to be commenced"
        )

    print(f"{greeting}. It's currently {time_str}...")
    time.sleep(2)

    def coffee_protocol():
        answer = input("Shall I start the coffee? (y/n): ").strip().lower()
        time.sleep(2)
        if answer in ("y", "yes", "yeah", "yep", "of course", "please"):
            print("\nSystem: Initializing caffeine protocol...")
            time.sleep(1)
            print("System: Caffeine protocol engaged.\n")
            time.sleep(2)
            return
        elif answer in ("n", "no", "nah", "not yet"):
            print("\nSystem: !!WARNING!! incorrect response, anomaly detected, YOU NEVER! say no to coffee.")
            time.sleep(1)
            print("System: re-running the decision matrix, please try again.\n")
            time.sleep(1)
            return coffee_protocol() 
        else:
            print("\nSystem: !!System error detected!!")
            time.sleep(1)
            print("System: defaulting to caffeine protocol.\n")
            time.sleep(2)
            return
    coffee_protocol()

def wifi_knight_day():
    alive = True
    curiosity = 9999
    energy = 100
    sarcasm_dial = 10

    projects = [
        "ReconPilot",
        "Arcane Shell",
        "something random and cool",
        "Bug Bounty / OSINT Practice / Enumeration",
        "School / Certs / Lab Work",
    ]

    loop_count = 0

    print("loading wifiknight cognitive runtime environment...")
    time.sleep(1)
    print("loading modules: [overthinking] [random cognitive noise] [cybersecurity paranoia] [sarcastic humor]\n")
    time.sleep(1)

    while alive and curiosity > 0:
        loop_count += 1
        print(f"\n=== Cycle {loop_count}: finalizing wifiknight cognitive runtime environment ===")
        time.sleep(2)

        if energy < 40:
            print("System notice: energy low. Auto-brewing emergency coffee...")
            energy += 40
            time.sleep(2)

        print(f"Status -> energy: {energy} | curiosity: {curiosity} | sarcasm_dial: {sarcasm_dial}")
        time.sleep(1)
        print("Projects in scope this cycle:", ", ".join(projects))
        time.sleep(1)

        options = [
            "Overplan every major project instead of touching production",
            "Rewire the lab again (Cloudflare, Sunshine, Moonlight, retro rigs)",
            "Run cyber paranoia drills and digital safety checks",
            "Grind fundamentals with brutal, honest practice (Python/Bash/etc.)",
            "Random hardware or OS experiment that definitely won't spiral",
        ]

        print("\nSelect the primary operation for this cycle:")
        for idx, option in enumerate(options, start=1):
            print(f"  {idx}. {option}")
            time.sleep(1)

        choice_raw = input("Enter a number (1-5): ").strip()

        try:
            choice = int(choice_raw)
            if choice not in range(1, 6):
                raise ValueError
        except ValueError:
            print("System: Invalid input detected, defaulting to random option.")
            choice = random.randint(1, 5)

        print()
        time.sleep(2)

        if choice == 1:
            print("System: Engaging overplanning mode...")
            time.sleep(1)
            print("- loading nueral modules for projects in scope.")
            time.sleep(1)
            for project in projects:
                ideas = random.randint(1, 10)      
                threats = random.randint(1, 5)     
                todos = random.randint(2, 4)       
                bugs = random.randint(0, 2)        

                print(
                    f"  • {project}: {ideas} new ideas, {threats} new threat models, "
                    f"{todos} new TODOs, reporting {bugs} total bugs... (yet)."
                )
                time.sleep(1)
            energy -= 10
            curiosity -= 1
            time.sleep(1)

        elif choice == 2:
            print("System: Lab rewiring operations authorized.")
            time.sleep(2)
            print("- Reviewing Cloudflare Zero Trust policies like a paranoid doorman.")
            time.sleep(1)
            print("- Tuning Sunshine on the Frankenstein GPU rig.")
            time.sleep(1)
            print("- Moonlight clients are happily connected from at least two devices at once.")
            time.sleep(1)
            print("- Internal debate: RPi, LattePanda, or S100 gets sacrificed to today's experiment.")
            energy -= 20
            curiosity -= 1
            time.sleep(2)

        elif choice == 3:
            print("System: Cyber paranoia drills initiated.")
            time.sleep(1)
            print("- Imagining 3 different hypothetical attacks on system and how to mitigate the risk.")
            time.sleep(1)
            print("- Mentally auditing which accounts would survive if your browser noped out right now.")
            time.sleep(1)
            print("- Quietly judging anyone who still uses 'Password123' currently.")
            time.sleep(1)
            print("- Threat model: 'slightly unhinged, but absolutely essential.'")
            energy -= 15
            curiosity -= 1
            time.sleep(2)

        elif choice == 4:
            print("System: Fundamentals grind selected.")
            time.sleep(1)
            print("- Today’s mission: no shortcuts, dont be a script kiddie, get real understanding.")
            time.sleep(1)
            print("- Rewriting the logic until it feels clean, predictable, and debuggable... for the hundreth time")
            time.sleep(1)
            print("- Mapping concepts across domains: code, carpentry, networking, life.")
            time.sleep(1)
            print("- Rule: 'It works' is not good enough unless you know *why* it works.")
            energy -= 12
            curiosity -= 1
            time.sleep(2)

        elif choice == 5:
            print("System: Random experiment engaged. This will probably escalate.")
            experiment = random.choice([
                "Re-compiling the linux kernel again... 'for science'.",
                "Switching GPU drivers until Steam either behaves or breaks.",
                "Convincing an SBC to do something it was never intended to do.",
                "Adjusting remote streaming, containers, and services 'just to see' what breaks... this time.",
            ])
            time.sleep(1)
            print(f"- Today's chaos: {experiment}")
            time.sleep(1)
            print("- Outcome: valuable data acquired, even if it is 'never do this again'.")
            energy -= 18
            curiosity -= 1
            time.sleep(2)

        print("\nCycle reflection:")
        time.sleep(1)
        print("- Conclusion: you are, dangerously curious.")
        time.sleep(1)
        print("- Internal note: 'We will integrate this into the master plan later.'")
        time.sleep(2)
        sleep_choice = input("\nDo you want to actually sleep and reset? (y/n): ").strip().lower()
        time.sleep(1)
        if sleep_choice.startswith("y"):
            print("\nSystem: Initiating sleep sequence...")
            time.sleep(1)
            energy = max(60, energy + 20)
            print("System: Energy will be restored to functional levels.")
            time.sleep(2)
            break
        elif sleep_choice.startswith("n"):
            print("\nSystem: Of course you said no. insomnia initialized...")
            time.sleep(1)
            print("\nSystem: Insomnia protocol engaged!")
            energy -= 10
            time.sleep(2)
        else:
            print("\nSystem: system error, rebooting now")
            time.sleep(1)
            print("rebooting the universe")
            time.sleep(2)
            return boot_sequence()

        if energy <= 10 or loop_count >= 6:
            print("\n[!!WARNING!! MANDITORY EXIT CONDITION TRIGGERED]")
            time.sleep(1)
            print("Subconscious guardian daemon: 'Absolutely not! You are done. Go horizontal.'")
            time.sleep(1)
            print("System: Initializing sleep sequence, saving states, and scheduling system reboot.")
            time.sleep(2)
            break
    print("\nSimulation complete. Curiosity remains excessively dangerous. Program exiting for now...")
    time.sleep(2)
if __name__ == "__main__":
    boot_sequence()
    wifi_knight_day()
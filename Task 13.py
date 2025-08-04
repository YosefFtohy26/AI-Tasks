import time

class Racer:
    def __init__(self, name):
        self.name = name
        self.tire_health = 100
        self.fuel = 500
        self.offensive_moves = {}
        self.defensive_moves = {}

    def _print_stats(self):
        print(f"[{self.name}] Stats: | Fuel: {self.fuel} | Tire Health: {self.tire_health}")

    def _display_moves(self, moves):
        print("Available moves:")
        move_names = list(moves.keys())
        for i, name in enumerate(move_names, 1):
            details = moves[name]
            cost = details.get("fuel_cost", 0)
            uses_display = details.get("uses", "unlimited")

            if 'uses' in details:
                attr_name = f"{name.lower().replace(' ', '_')}_uses"
                uses_display = getattr(self, attr_name, 0)

            print(f"  {i}. {name} (Fuel: {cost}, Uses: {uses_display})")
        return move_names

    def _get_user_choice(self, prompt, move_names):
        while True:
            try:
                choice = int(input(prompt).strip())
                if 1 <= choice <= len(move_names):
                    return move_names[choice - 1]
                if len(move_names) > 0 and prompt.startswith("Select a defensive") and choice == 0:
                    return "none"
                print("Invalid choice. Please enter a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def apply_damage(self, damage):
        self.tire_health -= damage
        if self.tire_health < 0:
            self.tire_health = 0

    def use_fuel(self, fuel_cost):
        self.fuel -= fuel_cost
        if self.fuel < 0:
            self.fuel = 0

    def take_turn(self, opponent):
        print("\n" + "=" * 30)
        print(f"🏁 {self.name}'s turn to attack!")
        self._print_stats()

        affordable_moves = {name: details for name, details in self.offensive_moves.items()
                            if self.fuel >= details.get("fuel_cost", 0)}

        if not affordable_moves:
            print("Not enough fuel to perform any offensive moves! Turn skipped.")
            return False

        move_names = self._display_moves(affordable_moves)
        chosen_move_name = self._get_user_choice(
            "Select an offensive move by number: ",
            move_names
        )
        chosen_move = affordable_moves[chosen_move_name]

        fuel_cost = chosen_move.get("fuel_cost", 0)
        tire_impact = chosen_move.get("tire_impact", 0)

        self.use_fuel(fuel_cost)
        print(f"🏎️ {self.name} uses '{chosen_move_name}'!")
        print(f"Tire impact on opponent: {tire_impact}")

        opponent.respond_to_attack(tire_impact, self)

        print("\n" + "-" * 30)
        print("Turn Summary:")
        self._print_stats()
        opponent._print_stats()
        return True

    def respond_to_attack(self, incoming_damage, opponent):
        print(f"\n🛡️ {self.name} is responding to the attack!")
        self._print_stats()
        available_defenses = {}
        for name, details in self.defensive_moves.items():
            attr_name = f"{name.lower().replace(' ', '_')}_uses"
            if 'uses' in details and getattr(self, attr_name, 0) <= 0:
                continue
            if self.fuel < details.get("fuel_cost", 0):
                continue
            available_defenses[name] = details

        if not available_defenses:
            print("No defensive moves available! Taking full damage.")
            self.apply_damage(incoming_damage)
            return

        move_names = self._display_moves(available_defenses)

        prompt = "Select a defensive move by number (or '0' to take full damage): "
        chosen_defense_name = self._get_user_choice(prompt, move_names)

        final_damage = incoming_damage
        if chosen_defense_name != "none":
            chosen_defense = self.defensive_moves[chosen_defense_name]
            fuel_cost = chosen_defense.get("fuel_cost", 0)
            damage_reduction = chosen_defense.get("damage_reduction", 0)
            uses = chosen_defense.get("uses", None)
            self.use_fuel(fuel_cost)

            if uses is not None:
                attr_name = f"{chosen_defense_name.lower().replace(' ', '_')}_uses"
                current_uses = getattr(self, attr_name, uses)
                setattr(self, attr_name, current_uses - 1)

            reduced_damage = incoming_damage * damage_reduction
            final_damage = incoming_damage - reduced_damage
            print(f"🛡️ {self.name} uses '{chosen_defense_name}'! Damage reduced by {damage_reduction * 100}%.")
        else:
            print("Taking full damage.")

        print(f"Final damage to {self.name}: {final_damage}")
        self.apply_damage(final_damage)


class MaxVerstappen(Racer):
    def __init__(self):
        super().__init__("Max Verstappen")
        self.offensive_moves = {
            "DRS Boost": {"fuel_cost": 45, "tire_impact": 12},
            "Red Bull Surge": {"fuel_cost": 80, "tire_impact": 20},
            "Precision Turm": {"fuel_cost": 30, "tire_impact": 8}
        }
        self.defensive_moves = {
            "Brake Late": {"fuel_cost": 25, "damage_reduction": 0.3},
            "ERS Deployment": {"fuel_cost": 40, "damage_reduction": 0.5, "uses": 3}
        }
        self.ers_deployment_uses = 3


class HassanMostafa(Racer):
    def __init__(self):
        super().__init__("Hassan Mostafa")
        self.offensive_moves = {
            "Turbo Start": {"fuel_cost": 50, "tire_impact": 10},
            "Mercedes Charge": {"fuel_cost": 90, "tire_impact": 22},
            "Corner Mastery": {"fuel_cost": 25, "tire_impact": 7}
        }
        self.defensive_moves = {
            "Slipstream Cut": {"fuel_cost": 20, "damage_reduction": 0.4},
            "Agressive Block": {"fuel_cost": 35, "damage_reduction": 1.0, "uses": 1}
        }
        self.agressive_block_uses = 1


def main():
    print("🏁 Welcome to the F1 Showdown: Verstappen vs Mostafa!")

    verstappen = MaxVerstappen()
    mostafa = HassanMostafa()

    current_racer = verstappen
    opponent_racer = mostafa

    no_moves_in_a_row = 0

    while verstappen.tire_health > 0 and mostafa.tire_health > 0 and no_moves_in_a_row < 2:
        turn_successful = current_racer.take_turn(opponent_racer)

        if not turn_successful:
            no_moves_in_a_row += 1
        else:
            no_moves_in_a_row = 0

        current_racer, opponent_racer = opponent_racer, current_racer
        time.sleep(2)

    print("\n" + "=" * 30)
    print("💥 RACE OVER! 💥")

    if no_moves_in_a_row >= 2:
        print("Both racers have run out of fuel to make a move.")
        if verstappen.tire_health > mostafa.tire_health:
            print(f"The winner is {verstappen.name} with more tire health!")
        elif mostafa.tire_health > verstappen.tire_health:
            print(f"The winner is {mostafa.name} with more tire health!")
        else:
            print("It's a draw! Both racers have equal tire health.")
    else:
        if verstappen.tire_health <= 0:
            print(f"The winner is {mostafa.name}!")
        else:
            print(f"The winner is {verstappen.name}!")

    print("\nFinal Stats:")
    verstappen._print_stats()
    mostafa._print_stats()


if __name__ == "__main__":
    main()

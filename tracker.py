import datetime

class Habit:
    def __init__(self, name, frequency):
        """
        Initialize a habit with a name, frequency, and default values.
        """

        self.name = name
        self.frequency = frequency
        self.streak = 0
        self.completed_today = False
        self.last_completed = None

    def mark_complete(self):
        """
        Mark the habit as complete and update the streak.
        """
        today = datetime.date.today()
        if self.last_completed != today:
            self.streak += 1
            self.last_completed = today
            print(f"Great job! You completed '{self.name}' today. Current streak: {self.streak} days.")
        else:
            print(f"You've already completed '{self.name}' today!")

    def reset_streak(self):
        """
        Reset the streak if the habit is not completed on time.
        """
        self.streak = 0
        print(f"Streak for '{self.name}' has been reset.")

    def __str__(self):
        """
        Return a string representation of the habit's status.
        """
        last_completed = self.last_completed if self.last_completed else "None"
        return f"{self.name} ({self.frequency}) - Streak: {self.streak} days - Last completed: {self.last_completed}"

class HabitTracker:
    def __init__(self, file_name="data_habits.txt"):
        """
        Initialize the habit tracker with an empty list of habits
        and load habits from the file.
        """
        self.habits = []
        self.load_habits() 

    def add_habit(self, name, frequency):
        """
        Add a new habit to the tracker.
        """
        habit = Habit(name, frequency)
        self.habits.append(habit)
        print(f"Added habit: '{name}' ({frequency})")
        self.save_all_habits()

    def load_habits(self, file_name="data_habits.txt"):
        """
        Load habits from a file and initialize them in the tracker.
        """
        try:
            with open(file_name, "r") as file:
                for line in file:
                    parts = [part.strip() for part in line.strip().split ("|")]
                    if len(parts) == 4:
                        name = parts[0].replace("Habit: ", "").strip()
                        frequency = parts[1].replace("Frequency: ", "").strip()
                        streak = int(parts[2].replace("Streak: ", "").strip())
                        last_completed = parts[3].replace("Last Completed: ", "").strip()

                        last_completed_date = (
                            datetime.datetime.strptime(last_completed.strip(), "%Y-%m-%d").date()
                            if last_completed != "None"
                            else None
                        )
                
                        habit = Habit(name, frequency)
                        habit.streak = streak
                        habit.last_completed = last_completed_date
                        self.habits.append(habit)

        except FileNotFoundError:
            print(f"No file named '{file_name}' found. Starting with an empty habit list.")
        except ValueError as e:
            print(f"An error occured while parsing the habit data: {e}")
        except Exception as e:
            print(f"An error occured while loading habits: {e}")

    def save_all_habits(self, file_name="data_habits.txt"):
        """
        Save all habits to a file.
        """
        if self.habits:
            with open(file_name, "w") as file:
                for habit in self.habits:
                    # Convert last_completed to a string or "None"
                    last_completed_str = habit.last_completed.strftime("%Y-%m-%d") if habit.last_completed else "None"
                    # Write habit details to the file
                    file.write(f"{habit.name} | {habit.frequency} | {habit.streak} | {habit.last_completed}\n")

        else:
            print("No habits to save!")

    def show_habits(self, file_name="data_habits.txt"):
        """
        Display all habits and their current status.
        """
        try: 
            # Check if there are any loaded habits
            if not self.habits:
                # Read directly from the file
                with open (file_name, "r") as file:
                    content = file.read()
                    if content.strip():
                        print(content)
                    else:
                        print("Oh no! There are no habits found in the file. Please add a new habit.")
            else:
                print("\nYour Habits: ")
                for habit in self.habits:
                    print(habit)
            
        except FileNotFoundError:
            print(f"No file named '{file_name}' found. Please add habits first!")
        except Exception as e:
            print(f"An error occured while showing habits:{e}")

    def mark_habit_complete(self, habit_name):
        """
        Mark a specific habit as complete by name.
        """
        for habit in self.habits:
            if habit.name.lower() == habit_name.lower():
                habit.mark_complete()
                self.save_all_habits()
                return
        print(f"Habit '{habit_name}' not found!")

    def remove_habit(self, habit_name):
        """
        Remove a specific habit by name.
        """
        for habit in self.habits:
            if habit.name.lower() == habit_name.lower():
                self.habits.remove(habit)
                self.save_all_habits()
                print(f"Habit '{habit_name}' has been removed.")
                return
        print(f"Habit '{habit_name}' not found!")

    def run(self):
        """
        Main command-line interface loop for interacting with the habit tracker.
        """
        print("Welcome to Momentum, your Habit Tracker!")
        while True:
            print("\nOptions:")
            print("1. Add a new habit")
            print("2. Show all habits")
            print("3. Mark a habit as complete")
            print("4. Remove a habit")
            print("5. Exit")

            choice = input("Choose an option (1-5): ")

            if choice == "1":
                name = input("Enter the habit name: ")
                frequency = input("Enter the frequency (e.g., daily, weekly): ")
                self.add_habit(name, frequency)
            elif choice == "2":
                self.show_habits()
            elif choice == "3":
                habit_name = input("Enter the name of the habit to mark complete: ")
                self.mark_habit_complete(habit_name)
            elif choice =="4":
                habit_name = input("Enter the name of the habit to remove: ")
                self.remove_habit(habit_name)
            elif choice == "5":
                print("Farewell! Keep building those habits!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the habit tracker
if __name__ == "__main__":
    tracker = HabitTracker()
    tracker.run()

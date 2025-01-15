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
        if self.last_completed !=today:
            self.streak += 1
            self.last_completed = True
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
        return f"{self.name} ({self.frequency}) - Streak: {self.streak} days - Last completed: {self.last_completed}"

class HabitTracker:
    def __init__(self):
        """
        Initialize the habit tracker with an empty list of habits.
        """
        self.habits = []

    def add_habit(self, name, frequency):
        """
        Add a new habit to the tracker.
        """
        habit = Habit(name, frequency)
        self.habits.append(habit)
        print(f"Added habit: '{name}' ({frequency})")

    def show_habits(self):
        """
        Display all habits and their current status.
        """
        if not self.habits:
            print("No habits added yet!")

        else:
            print("\nYour Habits:")
            for habit in self.habits:
                print(habit)

    def mark_habit_complete(self, habit_name):
        """
        Mark a specific habit as complete by name.
        """
        for habit in self.habits:
            if habit.name.lower() == habit_name.lower():
                habit.mark_complete()
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
            print("4. Exit")

            choice = input("Choose an option (1-4): ")

            if choice == "1":
                name = input("Enter the habit name: ")
                frequency = input("Enter the frequency (e.g., daily, weekly): ")
                self.add_habit(name, frequency)
            elif choice == "2":
                self.show_habits()
            elif choice == "3":
                habit_name = input("Enter the name of the habit to mark complete: ")
                self.mark_habit_complete(habit_name)
            elif choice == "4":
                print("Farewell! Keep building those habits!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the habit tracker
if __name__ == "__main__":
    tracker = HabitTracker()
    tracker.run()
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

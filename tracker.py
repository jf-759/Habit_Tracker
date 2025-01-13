class Habit:
    def __init__(self, name, frequency):
        """
        Initialize a habit with a name, frequency, and default values.
        """

        self.name = name
        self.frequency = frequency

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
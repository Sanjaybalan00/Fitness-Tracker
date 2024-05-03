class Exercise:
    def __init__(self, name, duration_min, intensity):
        self.name = name
        self.duration_min = duration_min
        self.intensity = intensity

class User:
    def __init__(self, username):
        self.username = username
        self.exercises = []
        self.goals = {}

    def log_exercise(self, exercise):
        self.exercises.append(exercise)

    def calculate_calories_burned(self):
        total_calories = 0
        for exercise in self.exercises:
            calories = exercise.duration_min * exercise.intensity
            total_calories += calories
        return total_calories

    def set_goal(self, goal_type, target_value):
        self.goals[goal_type] = target_value

    def track_progress(self):
        total_calories_burned = self.calculate_calories_burned()
        if 'calories' in self.goals:
            goal_calories = self.goals['calories']
            progress_percentage = (total_calories_burned / goal_calories) * 100
            return progress_percentage
        else:
            return None

# Function to log an exercise
def log_exercise(user):
    try:
        name = input("Enter exercise name: ")
        duration = int(input("Enter the duration (minutes): "))
        intensity = int(input("Enter intensity(1-10): "))
        if intensity < 1 or intensity > 10:
            raise ValueError("Intensity should be between 1 and 10.")
        exercise = Exercise(name, duration, intensity)
        user.log_exercise(exercise)
        print("Exercise logged successfully!")
    except ValueError as ve:
        print(f"Error: {ve}")

# Function to set a goal
def set_goal(user):
    try:
        goal_type = input("Enter goal type(e.g., calories): ")
        target_value = int(input("Enter target value: "))
        user.set_goal(goal_type, target_value)
        print("Goal set successfully!")
    except ValueError:
        print("Error: Target value should be a valid number.")

# Function to track progress
def track_progress(user):
    progress = user.track_progress()
    if progress is not None:
        print(f"Progress towards goal: {progress:.2f}%")
    else:
        print("No goal set yet.")

# Main function for user interaction
def main():
    username = input("Enter your username: ")
    user = User(username)

    # Food dictionary containing food names and their protein contents
    food_dict = {
        "chicken breast": 31,
        "salmon": 25,
        "eggs": 6,
        "greek yogurt": 10,
        "lean beef": 36,
        "cottage cheese": 12,
        "tuna": 28,
        "tofu": 8
    }

    while True:
        print("\n--- Fitness Tracking system ---")
        print("1. Log Exercise")
        print("2. Set Goal")
        print("3. Track Progress")
        print("4. Get Protein Content of Food")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            log_exercise(user)
        elif choice == '2':
            set_goal(user)
        elif choice == '3':
            track_progress(user)
        elif choice == '4':
            try:
                food_name = input("Enter food name: ").lower()
                if food_name in food_dict:
                    print(f"Protein content of {food_name}: {food_dict[food_name]}g")
                else:
                    print("Food not found in the database.")
            except Exception as e:
                print("An error occurred:", e)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

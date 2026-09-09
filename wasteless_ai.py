import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ============================================================
# WASTELESS AI
# SMART FOOD RESCUE PLANNER
# Don't Waste It, Match It!
# ============================================================


# ============================================================
# DATABASE
# ============================================================

conn = sqlite3.connect("wasteless_ai.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS food_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    food_name TEXT,
    category TEXT,
    days_old INTEGER,
    storage TEXT,
    condition TEXT,
    priority TEXT,
    score INTEGER,
    created_at TEXT
)
""")

conn.commit()


# ============================================================
# FOOD PRIORITY ALGORITHM
# ============================================================

def calculate_priority(days, storage, condition, category):

    score = 0
    reasons = []

    # DAYS STORED
    if days >= 7:
        score += 40
        reasons.append(f"Stored for {days} days.")

    elif days >= 4:
        score += 25
        reasons.append(f"Stored for {days} days.")

    elif days >= 2:
        score += 10
        reasons.append(f"Stored for {days} days.")

    else:
        reasons.append("Recently stored.")

    # STORAGE
    if storage == "Room Temperature":
        score += 20
        reasons.append("Stored at room temperature.")

    elif storage == "Refrigerator":
        score += 5
        reasons.append("Stored in refrigerator.")

    elif storage == "Freezer":
        reasons.append("Stored in freezer.")

    # CONDITION
    if condition == "Bad Smell":
        score += 40
        reasons.append("Bad smell detected.")

    elif condition == "Color Changed":
        score += 30
        reasons.append("Color has changed.")

    elif condition == "Soft":
        score += 20
        reasons.append("Texture has become soft.")

    else:
        reasons.append("Food condition looks normal.")

    # CATEGORY
    if category == "Dairy":
        score += 15
        reasons.append("Dairy products require quick attention.")

    elif category == "Cooked Food":
        score += 15
        reasons.append("Cooked food should be consumed sooner.")

    score = min(score, 100)

    # FINAL PRIORITY
    if score >= 60:
        priority = "USE FIRST 🔴"

    elif score >= 30:
        priority = "USE SOON 🟡"

    else:
        priority = "SAFE 🟢"

    return score, priority, reasons


# ============================================================
# INGREDIENT MATCHMAKER
# ============================================================

def find_recipe(food_list):

    foods = " ".join(food_list).lower()

    # BREAD PIZZA
    if ("bread" in foods and "tomato" in foods):

        return "🍕 Bread Pizza", \
               "You have Bread + Tomato. Add cheese if available!"

    # FRIED RICE
    elif ("rice" in foods and
          ("vegetable" in foods or "carrot" in foods)):

        return "🍚 Vegetable Fried Rice", \
               "You can combine leftover rice and vegetables."

    # FRUIT SALAD
    elif ("apple" in foods or "banana" in foods):

        if ("apple" in foods and "banana" in foods):

            return "🍎🍌 Fruit Salad", \
                   "Combine your fruits to make a healthy fruit salad."

    # BANANA SHAKE
    if ("banana" in foods and "milk" in foods):

        return "🥤 Banana Shake", \
               "Use Banana + Milk before they get wasted."

    # TOMATO SOUP
    if "tomato" in foods:

        return "🍅 Tomato Soup", \
               "Tomatoes can be used to make a quick soup."

    # BREAD RECIPE
    if "bread" in foods:

        return "🍞 Bread Toast", \
               "Use bread for toast or a quick snack."

    # DEFAULT
    return "🍳 Smart Leftover Meal", \
           "Combine your available ingredients creatively before they become waste."


# ============================================================
# MAIN APPLICATION
# ============================================================

class WasteLessAI(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("WasteLess AI - Smart Food Rescue Planner")

        self.geometry("1200x720")

        self.configure(bg="#f4f6f4")

        self.create_sidebar()
        self.create_main()

        self.show_home()


    # ========================================================
    # SIDEBAR
    # ========================================================

    def create_sidebar(self):

        sidebar = tk.Frame(
            self,
            bg="#1f6b45",
            width=250
        )

        sidebar.pack(
            side=tk.LEFT,
            fill=tk.Y
        )

        sidebar.pack_propagate(False)

        tk.Label(
            sidebar,
            text="🥗",
            font=("Arial", 40),
            bg="#1f6b45",
            fg="white"
        ).pack(pady=(30, 5))

        tk.Label(
            sidebar,
            text="WasteLess AI",
            font=("Arial", 20, "bold"),
            bg="#1f6b45",
            fg="white"
        ).pack()

        tk.Label(
            sidebar,
            text="Don't Waste It,\nMatch It!",
            font=("Arial", 11),
            bg="#1f6b45",
            fg="white",
            justify="center"
        ).pack(pady=(5, 30))

        buttons = [

            ("🏠 Home", self.show_home),
            ("➕ Add Food", self.show_add_food),
            ("🥇 Rescue Priority", self.show_priority),
            ("🍳 Ingredient Matchmaker", self.show_matchmaker),
            ("📊 Dashboard", self.show_dashboard),
            ("💡 About Innovation", self.show_about)

        ]

        for text, command in buttons:

            tk.Button(
                sidebar,
                text=text,
                command=command,
                font=("Arial", 11),
                anchor="w",
                padx=20,
                pady=12,
                bg="#1f6b45",
                fg="white",
                activebackground="#2e8b57",
                activeforeground="white",
                bd=0,
                cursor="hand2"
            ).pack(
                fill=tk.X,
                pady=2
            )


    # ========================================================
    # MAIN AREA
    # ========================================================

    def create_main(self):

        self.main = tk.Frame(
            self,
            bg="#f4f6f4"
        )

        self.main.pack(
            side=tk.RIGHT,
            fill=tk.BOTH,
            expand=True
        )


    def clear_main(self):

        for widget in self.main.winfo_children():
            widget.destroy()


    # ========================================================
    # HOME PAGE
    # ========================================================

    def show_home(self):

        self.clear_main()

        tk.Label(
            self.main,
            text="🥗 WasteLess AI",
            font=("Arial", 32, "bold"),
            bg="#f4f6f4",
            fg="#1f6b45"
        ).pack(pady=(60, 10))

        tk.Label(
            self.main,
            text="Smart Food Rescue Planner",
            font=("Arial", 20),
            bg="#f4f6f4",
            fg="#555555"
        ).pack()

        tk.Label(
            self.main,
            text="🤖 Don't Waste It, Match It!",
            font=("Arial", 16, "bold"),
            bg="#f4f6f4",
            fg="#1f6b45"
        ).pack(pady=15)

        tk.Label(
            self.main,
            text=(
                "Our system doesn't just identify food that needs attention.\n"
                "It tells you WHICH food to use first and WHAT you can make with it!"
            ),
            font=("Arial", 14),
            bg="#f4f6f4",
            justify="center"
        ).pack(pady=15)

        tk.Button(
            self.main,
            text="➕ START ADDING FOOD",
            command=self.show_add_food,
            font=("Arial", 13, "bold"),
            bg="#1f6b45",
            fg="white",
            padx=25,
            pady=12,
            cursor="hand2"
        ).pack(pady=20)

        cursor.execute("SELECT COUNT(*) FROM food_items")
        total = cursor.fetchone()[0]

        tk.Label(
            self.main,
            text=f"📦 Total Food Items Tracked: {total}",
            font=("Arial", 16),
            bg="#f4f6f4",
            fg="#333333"
        ).pack(pady=20)


    # ========================================================
    # ADD FOOD
    # ========================================================

    def show_add_food(self):

        self.clear_main()

        tk.Label(
            self.main,
            text="➕ Add Food for AI Analysis",
            font=("Arial", 25, "bold"),
            bg="#f4f6f4",
            fg="#1f6b45"
        ).pack(pady=25)

        form = tk.Frame(
            self.main,
            bg="white",
            padx=40,
            pady=30
        )

        form.pack(padx=80, pady=20)

        self.food_name = tk.StringVar()
        self.category = tk.StringVar(value="Fruits")
        self.days = tk.StringVar()
        self.storage = tk.StringVar(value="Refrigerator")
        self.condition = tk.StringVar(value="Normal")

        # FOOD NAME

        tk.Label(
            form,
            text="🍎 Food Name:",
            bg="white",
            font=("Arial", 12)
        ).grid(row=0, column=0, pady=10, sticky="w")

        tk.Entry(
            form,
            textvariable=self.food_name,
            width=30
        ).grid(row=0, column=1, padx=20)

        # CATEGORY

        tk.Label(
            form,
            text="📂 Category:",
            bg="white",
            font=("Arial", 12)
        ).grid(row=1, column=0, pady=10, sticky="w")

        ttk.Combobox(
            form,
            textvariable=self.category,
            values=[
                "Fruits",
                "Vegetables",
                "Dairy",
                "Cooked Food",
                "Bakery",
                "Other"
            ],
            state="readonly",
            width=27
        ).grid(row=1, column=1, padx=20)

        # DAYS

        tk.Label(
            form,
            text="📅 Days Stored:",
            bg="white",
            font=("Arial", 12)
        ).grid(row=2, column=0, pady=10, sticky="w")

        tk.Entry(
            form,
            textvariable=self.days,
            width=30
        ).grid(row=2, column=1, padx=20)

        # STORAGE

        tk.Label(
            form,
            text="❄️ Storage:",
            bg="white",
            font=("Arial", 12)
        ).grid(row=3, column=0, pady=10, sticky="w")

        ttk.Combobox(
            form,
            textvariable=self.storage,
            values=[
                "Room Temperature",
                "Refrigerator",
                "Freezer"
            ],
            state="readonly",
            width=27
        ).grid(row=3, column=1, padx=20)

        # CONDITION

        tk.Label(
            form,
            text="👀 Condition:",
            bg="white",
            font=("Arial", 12)
        ).grid(row=4, column=0, pady=10, sticky="w")

        ttk.Combobox(
            form,
            textvariable=self.condition,
            values=[
                "Normal",
                "Soft",
                "Color Changed",
                "Bad Smell"
            ],
            state="readonly",
            width=27
        ).grid(row=4, column=1, padx=20)

        tk.Button(
            form,
            text="🤖 ANALYZE & ADD",
            command=self.add_food,
            bg="#1f6b45",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=10,
            cursor="hand2"
        ).grid(
            row=5,
            column=0,
            columnspan=2,
            pady=20
        )

        self.result = tk.Label(
            self.main,
            text="",
            font=("Arial", 14),
            bg="#f4f6f4",
            justify="left"
        )

        self.result.pack(pady=10)


    def add_food(self):

        name = self.food_name.get().strip()

        if not name:

            messagebox.showwarning(
                "Input Required",
                "Please enter food name."
            )

            return

        try:

            days = int(self.days.get())

            if days < 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid days."
            )

            return

        category = self.category.get()
        storage = self.storage.get()
        condition = self.condition.get()

        score, priority, reasons = calculate_priority(
            days,
            storage,
            condition,
            category
        )

        cursor.execute("""
        INSERT INTO food_items
        (food_name, category, days_old, storage,
        condition, priority, score, created_at)

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (

            name,
            category,
            days,
            storage,
            condition,
            priority,
            score,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ))

        conn.commit()

        explanation = "\n".join(
            ["• " + reason for reason in reasons]
        )

        self.result.config(
            text=(
                f"🤖 AI PRIORITY RESULT\n\n"
                f"🥇 Priority: {priority}\n"
                f"📊 Priority Score: {score}/100\n\n"
                f"🧠 Why?\n{explanation}"
            )
        )

        messagebox.showinfo(
            "Success",
            f"{name} added successfully!"
        )


    # ========================================================
    # RESCUE PRIORITY
    # ========================================================

    def show_priority(self):

        self.clear_main()

        tk.Label(
            self.main,
            text="🥇 Smart Food Rescue Priority",
            font=("Arial", 25, "bold"),
            bg="#f4f6f4",
            fg="#1f6b45"
        ).pack(pady=20)

        tk.Label(
            self.main,
            text="AI ranks your food so you know what to use FIRST!",
            font=("Arial", 13),
            bg="#f4f6f4"
        ).pack(pady=5)

        cursor.execute("""
        SELECT food_name, category, days_old,
               priority, score
        FROM food_items
        ORDER BY score DESC
        """)

        foods = cursor.fetchall()

        if not foods:

            tk.Label(
                self.main,
                text="No food items available.\nAdd food first!",
                font=("Arial", 16),
                bg="#f4f6f4"
            ).pack(pady=60)

            return

        frame = tk.Frame(
            self.main,
            bg="white"
        )

        frame.pack(
            fill=tk.BOTH,
            expand=True,
            padx=50,
            pady=20
        )

        for index, food in enumerate(foods, start=1):

            name, category, days, priority, score = food

            if index == 1:
                medal = "🥇"

            elif index == 2:
                medal = "🥈"

            elif index == 3:
                medal = "🥉"

            else:
                medal = f"#{index}"

            text = (
                f"{medal}  {name}  |  "
                f"{priority}  |  "
                f"Score: {score}/100"
            )

            tk.Label(
                frame,
                text=text,
                font=("Arial", 14, "bold"),
                bg="white",
                anchor="w",
                padx=20,
                pady=12
            ).pack(
                fill=tk.X,
                pady=3
            )


    # ========================================================
    # INGREDIENT MATCHMAKER
    # ========================================================

    def show_matchmaker(self):

        self.clear_main()

        tk.Label(
            self.main,
            text="🍳 AI Ingredient Matchmaker",
            font=("Arial", 25, "bold"),
            bg="#f4f6f4",
            fg="#D35400"
        ).pack(pady=25)

        tk.Label(
            self.main,
            text=(
                "The system checks your available food items\n"
                "and suggests what you can make!"
            ),
            font=("Arial", 13),
            bg="#f4f6f4",
            justify="center"
        ).pack()

        cursor.execute("""
        SELECT food_name
        FROM food_items
        ORDER BY score DESC
        """)

        foods = cursor.fetchall()

        if not foods:

            tk.Label(
                self.main,
                text="Add food items first!",
                font=("Arial", 16),
                bg="#f4f6f4"
            ).pack(pady=60)

            return

        food_names = [food[0] for food in foods]

        recipe, description = find_recipe(food_names)

        card = tk.Frame(
            self.main,
            bg="white",
            padx=40,
            pady=30
        )

        card.pack(
            padx=100,
            pady=40
        )

        tk.Label(
            card,
            text="🥗 Available Ingredients",
            font=("Arial", 15, "bold"),
            bg="white"
        ).pack()

        tk.Label(
            card,
            text=", ".join(food_names),
            font=("Arial", 13),
            bg="white",
            wraplength=600
        ).pack(pady=10)

        tk.Label(
            card,
            text="🤖 AI MATCH FOUND!",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#1f6b45"
        ).pack(pady=15)

        tk.Label(
            card,
            text=recipe,
            font=("Arial", 22, "bold"),
            bg="white",
            fg="#D35400"
        ).pack(pady=10)

        tk.Label(
            card,
            text=description,
            font=("Arial", 13),
            bg="white",
            wraplength=600,
            justify="center"
        ).pack(pady=10)


    # ========================================================
    # DASHBOARD
    # ========================================================

    def show_dashboard(self):

        self.clear_main()

        tk.Label(
            self.main,
            text="📊 Food Rescue Dashboard",
            font=("Arial", 25, "bold"),
            bg="#f4f6f4",
            fg="#1f6b45"
        ).pack(pady=20)

        df = pd.read_sql_query(
            "SELECT * FROM food_items",
            conn
        )

        if df.empty:

            tk.Label(
                self.main,
                text="No data available.",
                font=("Arial", 16),
                bg="#f4f6f4"
            ).pack(pady=60)

            return

        # CREATE GRAPH

        figure = plt.Figure(
            figsize=(7, 4),
            dpi=100
        )

        ax = figure.add_subplot(111)

        priority_counts = df["priority"].value_counts()

        ax.bar(
            priority_counts.index,
            priority_counts.values
        )

        ax.set_title(
            "Food Rescue Priority Distribution"
        )

        ax.set_xlabel(
            "Priority Level"
        )

        ax.set_ylabel(
            "Number of Food Items"
        )

        canvas = FigureCanvasTkAgg(
            figure,
            self.main
        )

        canvas.draw()

        canvas.get_tk_widget().pack(
            fill=tk.BOTH,
            expand=True,
            padx=50,
            pady=20
        )


    # ========================================================
    # ABOUT / INNOVATION
    # ========================================================

    def show_about(self):

        self.clear_main()

        tk.Label(
            self.main,
            text="💡 Project Innovation",
            font=("Arial", 27, "bold"),
            bg="#f4f6f4",
            fg="#1f6b45"
        ).pack(pady=30)

        text = """
🌟 WASTELESS AI – SMART FOOD RESCUE PLANNER

Most food waste applications only tell users:

"Your food may be wasted."

Our system goes one step further!

🤖 STEP 1: SMART PRIORITY ALGORITHM
The system calculates which food should be used FIRST.

🥇 STEP 2: FOOD RESCUE RANKING
All available food is ranked based on priority.

🍳 STEP 3: INGREDIENT MATCHMAKER
The system checks available ingredients and
suggests a possible meal.

💡 STEP 4: EXPLAINABLE DECISION
The user can understand WHY a food received
high priority.

🏆 MAIN INNOVATION:

Instead of only predicting food waste,
WasteLess AI helps users TAKE ACTION
before food becomes waste.

TAGLINE:

🥗 DON'T WASTE IT, MATCH IT!
"""

        tk.Label(
            self.main,
            text=text,
            font=("Arial", 13),
            bg="#f4f6f4",
            justify="left"
        ).pack(
            padx=100,
            pady=10,
            anchor="w"
        )


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    app = WasteLessAI()

    app.mainloop()

    conn.close()

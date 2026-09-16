# 🥗 WasteLess AI – Smart Food Rescue Planner

### **“Don't Waste It, Match It!”**

WasteLess AI is a simple and innovative **AI-based food waste prevention system** designed to help users manage food before it becomes waste.

Instead of only identifying food as risky, the system calculates **which food should be used first** and checks available ingredients to provide a **possible recipe suggestion**.

---

## 🌟 Project Innovation

Traditional food-waste systems mainly focus on identifying expired or spoiled food.

**WasteLess AI takes an action-oriented approach:**

```text
Food Information
       ↓
Smart Priority Analysis
       ↓
Which Food Should Be Used First?
       ↓
Ingredient Matching
       ↓
Recipe Suggestion
       ↓
Food Waste Prevention
```

### ⭐ Main Innovation

The system combines **food priority analysis + ingredient matching** to help users make better use of the food they already have.

For example:

```text
Available Food:
🍞 Bread
🍅 Tomato
🧀 Cheese

AI Suggestion:
🍕 Bread Pizza

Priority:
🥇 Use Tomato First
```

---

## 🚀 Features

### 🤖 1. Smart Food Analysis

The user enters:

* Food name
* Food category
* Number of days stored
* Storage method
* Current condition

The system calculates a **priority score**.

---

### 🥇 2. Smart Rescue Priority

Food items are automatically ranked according to their priority.

The system displays:

* 🔴 **USE FIRST**
* 🟡 **USE SOON**
* 🟢 **SAFE**

This helps users decide which food needs attention first.

---

### 🍳 3. AI Ingredient Matchmaker

The system checks the food items stored in the application and searches for simple ingredient combinations.

Example:

**Bread + Tomato → Bread Pizza**

**Banana + Milk → Banana Shake**

**Rice + Vegetables → Vegetable Fried Rice**

This encourages users to use available food instead of wasting it.

---

### 🧠 4. Explainable Decision

The system provides reasons for the calculated priority.

For example:

```text
Priority: USE FIRST 🔴
Score: 75/100

Why?

• Stored for 7 days
• Stored at room temperature
• Color has changed
```

This makes the decision easier for the user to understand.

---

### 📊 5. Dashboard

The dashboard provides a simple visualization of food priority levels using a graph.

It helps users understand their food-rescue data.

---

### 🗄️ 6. SQLite Database

Food information is stored using **SQLite**.

Stored information includes:

* Food name
* Category
* Days stored
* Storage
* Condition
* Priority
* Priority score
* Date and time

---

## 🛠️ Technologies Used

| Technology               | Purpose                   |
| ------------------------ | ------------------------- |
| **Python**               | Main programming language |
| **Tkinter**              | Graphical User Interface  |
| **SQLite**               | Database                  |
| **Pandas**               | Data handling             |
| **Matplotlib**           | Dashboard visualization   |
| **Algorithmic AI Logic** | Food priority analysis    |

---

## 💻 System Requirements

* Windows / Linux / macOS
* Python 3.x
* 4 GB RAM or above recommended
* Internet connection is only required for installing libraries

---

## 📦 Installation

### Step 1: Install Python

Install Python 3.x on your computer.

Check installation:

```bash
python --version
```

---

### Step 2: Install Required Libraries

Open Command Prompt or PowerShell and run:

```bash
pip install pandas matplotlib
```

Tkinter and SQLite are normally included with standard Python installations.

---

## ▶️ How to Run

Save the project file as:

```text
wasteless_ai.py
```

Open Command Prompt in the project folder.

Run:

```bash
python wasteless_ai.py
```

The WasteLess AI graphical interface will open.

---

## 📱 How to Use

### Step 1 — Add Food

Go to:

**➕ Add Food**

Enter:

```text
Food Name: Tomato
Category: Vegetables
Days Stored: 4
Storage: Refrigerator
Condition: Normal
```

Click:

**ANALYZE & ADD**

---

### Step 2 — Check Priority

Open:

**🥇 Rescue Priority**

The application ranks food items according to their calculated priority.

Example:

```text
🥇 Tomato       USE FIRST 🔴
🥈 Bread        USE SOON 🟡
🥉 Apple        SAFE 🟢
```

---

### Step 3 — Find a Recipe

Open:

**🍳 Ingredient Matchmaker**

The system checks the stored ingredients and suggests a possible meal.

Example:

```text
Bread + Tomato

        ↓

🍕 Bread Pizza
```

---

### Step 4 — View Dashboard

Open:

**📊 Dashboard**

A graph displays the distribution of food priority levels.

---

## 🧠 How the AI Logic Works

WasteLess AI uses a simple rule-based decision approach.

The system considers:

```text
Days Stored
     +
Storage Method
     +
Food Condition
     +
Food Category
     ↓
Priority Score
     ↓
Food Rescue Priority
```

### Example

If food has:

* Been stored for many days
* Been kept at room temperature
* Developed a bad smell

The priority score increases and the system may classify it as:

**🔴 USE FIRST**

---

## 📊 Priority Calculation

The system assigns points based on food characteristics.

### Storage Duration

```text
7+ days    → Higher priority
4–6 days   → Medium priority
2–3 days   → Lower priority
```

### Storage

```text
Room Temperature → Higher score
Refrigerator      → Moderate score
Freezer           → Lower additional score
```

### Condition

```text
Normal          → No major additional score
Soft            → Increased score
Color Changed   → Higher score
Bad Smell       → Very high score
```

The final score determines the food-rescue priority.

---

## ⚠️ Food Safety Notice

WasteLess AI is an **educational AI project**.

Its recommendations should not be treated as a guarantee that food is safe to eat.

Users should always follow proper food-safety practices and discard food when there are signs of spoilage or when safety is uncertain.

---

## 🎯 Objectives

The main objectives of WasteLess AI are:

1. Reduce unnecessary food waste.
2. Help users identify food requiring attention.
3. Prioritize food based on simple AI logic.
4. Encourage creative use of leftover ingredients.
5. Provide understandable explanations for decisions.
6. Demonstrate how AI can address a real-world sustainability problem.

---

## 🌍 Real-World Impact

Food waste creates economic and environmental problems.

WasteLess AI aims to encourage users to:

**Plan → Prioritize → Rescue → Reduce Waste**

The project demonstrates how a simple AI-based application can help users make better decisions about food already available at home.

---

## 🔮 Future Scope

Future versions can include:

* 📷 Food image recognition using Computer Vision
* 🤖 Advanced Machine Learning model
* 📱 Android/mobile application
* ☁️ Cloud database
* 🔔 Expiry reminders
* 🛒 Smart grocery planning
* 🧾 Receipt-based food entry
* 🍽️ More personalized recipe recommendations
* 🌱 More detailed environmental impact calculation

---

## 🏆 Project USP

### **“Most systems only predict food waste. WasteLess AI helps users decide what to use first and how to rescue available ingredients before they become waste.”**

---

## 👩‍💻 Project Type

**AI / Machine Learning Mini Project**

### Domain

**Artificial Intelligence + Food Waste Management + Sustainability**

### Application

**Smart Food Management and Food Rescue**

---

## 📌 Conclusion

WasteLess AI is a simple, practical, and innovative solution for reducing food waste.

Rather than focusing only on prediction, the project follows an **action-oriented approach**:

```text
PREDICT
   ↓
PRIORITIZE
   ↓
MATCH
   ↓
RESCUE
   ↓
REDUCE WASTE
```

### 🥗 WasteLess AI

## **“Don't Waste It, Match It!”**

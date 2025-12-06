# December-Bug-Jam-automation

This repository contains a complete **Selenium Python automation framework** for the **RecommenDead** movie-search application, developed as part of the **December Bug Jam Project**.

This project demonstrates professional QA automation skills, including Page Object Model (POM), parametrized tests, robust selectors, and full functional coverage of search behavior.

---

## 🔍 Features Covered

### **1. Search Input Validation**
- Allows 2–15 characters  
- Accepts only Latin letters + spaces  
- Supports multi-word queries  
- Rejects numbers, symbols, and invalid characters  

### **2. Search Results**
- Displays exactly **one** poster for each valid query  
- Shows **"Please search for something else"** when no movie matches  
- Multi-query AND logic: results must match **all terms**  

### **3. Query Display Logic**
- Query tags appear above the input after clicking the **+** icon  
- Up to **3 simultaneous queries** allowed  
- 4th query triggers message:  
  **"Maximum three search queries. Please remove one query."**

---

## 🧪 Tech Stack

- **Python 3**
- **Selenium WebDriver**
- **Pytest**
- **Page Object Model (POM)**
- Parametrized test design
- Explicit waits for reliability

---

## 📁 Project Structure


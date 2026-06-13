# Golf Cart Booking System

## Assignment Overview

Build a Command Line Interface (CLI) based Golf Cart Booking System for an organization where employees can book golf carts to travel between departments within the campus.

The system should allow employees to:

1. Book a golf cart
2. Select pickup and destination departments
3. Select a golf cart
4. Add luggage
5. Calculate fare automatically
6. View booking history
7. Cancel bookings
8. Export bookings to a JSON file

---

# Organization Data

## Departments

```python
DEPARTMENTS = {
    101: "HR Department",
    102: "Engineering Block",
    103: "Finance Department",
    104: "Sales Department",
    105: "Admin Office",
    106: "Warehouse",
    107: "Cafeteria",
    108: "Medical Center"
}
```

## Golf Carts

```python
GOLF_CARTS = {
    "C101": "Rajesh",
    "C102": "Aman",
    "C103": "Priya",
    "C104": "Karan"
}
```

---

# Pricing Rules

```python
BASE_FARE = 20
LUGGAGE_COST = 10
```

Base Fare = ₹20

Luggage Charge = ₹10 per bag

### Fare Formula

```python
Total Fare = BASE_FARE + (Number_Of_Bags * LUGGAGE_COST)
```

Example:

```text
Base Fare = ₹20
Bags = 2

Total Fare = 20 + (2 × 10)
Total Fare = ₹40
```

---

# Functional Requirements

## 1. Book Cart

Collect the following information:

```text
Employee Name
Employee ID
Pickup Department
Destination Department
Cart ID
Number Of Bags
```

Validation Rules:

```text
Employee Name cannot be empty
Employee ID cannot be empty
Department ID must exist
Cart ID must exist
Pickup and Destination cannot be the same
Number of bags cannot be negative
```

---

## 2. View Bookings

Display all bookings available in the system.

---

## 3. Search Booking

Allow searching by:

```text
Booking ID
Employee Name
```

---

## 4. Cancel Booking

Allow users to cancel a booking.

Rules:

```text
Remove booking record
Make the cart available again
```

---

## 5. Export Bookings

Export all bookings to:

```text
golf_cart_bookings.json
```

---

## 6. Cart Availability

When a cart is booked:

```text
Cart becomes unavailable
```

When a booking is cancelled:

```text
Cart becomes available again
```

---

## 7. Revenue Report

Display:

```text
Total Bookings
Total Revenue
Total Luggage Charges
```

---

# Data Structure Requirement

Store booking information using dictionaries.

Example:

```python
bookings = {
    "B001": {
        "employee_name": "John",
        "employee_id": "E101",
        "pickup": "HR Department",
        "destination": "Sales Department",
        "cart_id": "C101",
        "driver": "Rajesh",
        "bags": 2,
        "fare": 40
    }
}
```

---

# Non Functional Requirements

## Error Handling

Use try-except blocks to handle:

```text
Invalid Department ID
Invalid Cart ID
Invalid Numbers
Wrong Menu Choice
```

## Code Quality

Create reusable functions 

## Performance

Use dictionaries for fast lookups.

## Maintainability

Write clean, readable, and modular code.

---

# Menu Structure

```text
=================================
    GOLF CART BOOKING SYSTEM
=================================

1. Book Cart
2. View Bookings
3. Search Booking
4. Cancel Booking
5. Export Bookings
6. Revenue Report
7. Exit
```

---

# Sample Program Run

## Step 1: Book a Cart

```text
Enter Employee Name: John

Enter Employee ID: E101

Available Departments

101 -> HR Department
102 -> Engineering Block
103 -> Finance Department
104 -> Sales Department
105 -> Admin Office

Enter Pickup Department ID: 101

Enter Destination Department ID: 104

Available Golf Carts

C101 -> Rajesh
C102 -> Aman
C103 -> Priya
C104 -> Karan

Enter Cart ID: C101

Do you have luggage? (yes/no): yes

Enter Number Of Bags: 2
```

## Step 2: Fare Calculation

```text
Base Fare = ₹20

Luggage Charges = 2 × ₹10

Total Fare = ₹40
```

## Step 3: Booking Confirmation

```text
=================================
      BOOKING CONFIRMED
=================================

Booking ID : B001

Employee   : John
Employee ID: E101

Pickup     : HR Department

Destination: Sales Department

Cart ID    : C101

Driver     : Rajesh

Bags       : 2

Total Fare : ₹40
```

## Step 4: Export Bookings

```text
Bookings exported successfully.

File Created:

golf_cart_bookings.json
```

---


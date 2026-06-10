# W2 Tutorial – Movie Theater Admission Policy

## Problem Statement

A movie theater has the following admission policy:

A person is allowed to enter if:

* The user is *13 years old or older*, OR
* The user is *accompanied by an adult*.
* The user *must have a valid ticket*.

Logical Expression:

*(Age ≥ 13 OR Accompanied by Adult) AND Valid Ticket*

---

# 1. Identify the Components

## 1.1 Inputs

The inputs required are:

1. Age of the user
2. Accompanied by an adult? (Yes/No)
3. Has a valid ticket? (Yes/No)

---

## 1.2 Process

The system checks:

1. Whether the user is 13 years old or older.
2. Whether the user is accompanied by an adult.
3. Whether the user has a valid ticket.
4. Apply the admission rule:

   (Age ≥ 13 OR Accompanied by Adult) AND Valid Ticket

---

## 1.3 Output

Possible outputs:

* *Entry Allowed*
* *Entry Denied*

---

# 2. Design the Algorithm

## 2.1 Flowchart

text
START
   |
Input Age, Adult Companion, Valid Ticket
   |
Age >= 13 ?
   |
  Yes ----------------------|
   |                         |
   |                    Valid Ticket?
   |                         |
   |                    Yes ---> Entry Allowed
   |                    No ----> Entry Denied
   |
  No
   |
Accompanied by Adult?
   |
 Yes ------------------------|
   |                         |
   |                    Valid Ticket?
   |                         |
   |                    Yes ---> Entry Allowed
   |                    No ----> Entry Denied
   |
  No
   |
Entry Denied
   |
 END


---

## 2.2 Truth Table

Let:

* A = Age ≥ 13
* B = Accompanied by Adult
* C = Valid Ticket

Expression:

(A OR B) AND C

|Age ≥ 13  | Accompanied by Adult | Valid Ticket | A OR B | Result |
|     -    |            -         |      -       | ------ | ------ |
|     F    |            F         |      F       |   F    |   F    |
|     F    |            F         |      T       |   F    |   F    |
|     F    |            T         |      F       |   T    |   F    |
|     F    |            T         |      T       |   T    |   T    |
|     T    |            F         |      F       |   T    |   F    |
|     T    |            F         |      T       |   T    |   T    |
|     T    |            T         |      F       |   T    |   F    |
|     T    |            T         |      T       |   T    |   T    |

Legend:

* T = True
* F = False


![alt text](<WhatsApp Image 2026-06-10 at 12.40.53 PM.jpeg>)



---

## 2.3 Algorithm (Step-by-Step Solution)

1. Start.
2. Input age.
3. Input whether the user is accompanied by an adult.
4. Input whether the user has a valid ticket.
5. Check if:

   * (Age ≥ 13 OR accompanied by adult)
   * AND valid ticket.
6. If the condition is true:

   * Display "Entry Allowed".
7. Otherwise:

   * Display "Entry Denied".
8. End.

---

## 2.4 Pseudocode

text
BEGIN

INPUT age
INPUT accompaniedByAdult
INPUT validTicket

IF ((age >= 13 OR accompaniedByAdult = TRUE)
    AND validTicket = TRUE) THEN

    DISPLAY "Entry Allowed"

ELSE

    DISPLAY "Entry Denied"

END IF

END


---

# 3. Evaluate Expression

## 3.1 Test Cases

### Test Case 1

Input:

* Age = 15
* Accompanied by Adult = No
* Valid Ticket = Yes

Evaluation:

* Age ≥ 13 → True
* Valid Ticket → True

Result:

*Entry Allowed*

---

### Test Case 2

Input:

* Age = 10
* Accompanied by Adult = Yes
* Valid Ticket = Yes

Evaluation:

* Age ≥ 13 → False
* Accompanied by Adult → True
* Valid Ticket → True

Result:

*Entry Allowed*

---

### Test Case 3

Input:

* Age = 10
* Accompanied by Adult = No
* Valid Ticket = Yes

Evaluation:

* Age ≥ 13 → False
* Accompanied by Adult → False

Result:

*Entry Denied*

---

### Test Case 4

Input:

* Age = 16
* Accompanied by Adult = No
* Valid Ticket = No

Evaluation:

* Age ≥ 13 → True
* Valid Ticket → False

Result:

*Entry Denied*

---

## Conclusion

A person can enter the movie theater only when they have a valid ticket and either:

* are at least 13 years old, or
* are accompanied by an adult.

Logical Expression:

(Age ≥ 13 OR Accompanied by Adult) AND Valid Ticket
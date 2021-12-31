# Recursion

**Summary:**
The idea behind Recursion is a "procedure" that repeats itself until some condition is met.  Examples of recursion would be:
1. Getting a factorial of a number (i.e. you would multiply a number (n) by (n-1) and keep on repeating until n=1)
2. Counting down like a timer (you keep on decrementing until you hit 0)

**Sample Code**

An example of where recursion can be used to countdown from some arbitrary number to zero.
```python
# Counting down to 0
def countdown(i):
    if (i <= 0):
        return i
    else:
        countdown(i-1)
```

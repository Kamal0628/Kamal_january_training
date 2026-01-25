# Q1.py
# Demonstrates behavior of immutable default parameters

def count_message(msg, count=0):
    count += 1
    print(f"Message received: {msg}")
    print(f"Message count: {count}")
    return count


# 🔽 FUNCTION CALLS (CHANGED INPUT)
count_message("good morning")
count_message("good evening")

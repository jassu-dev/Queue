# Queue — A Complete Guide

## 📌 Introduction
A **Queue** is a linear data structure that organizes elements in a specific order:  
- **First In, First Out (FIFO)**: The first element added to the queue will be the first one removed.  
This is similar to a real-world queue, such as people waiting in line at a ticket counter.

---

## 🔍 Key Characteristics
- **Order of Processing**: Items are processed in the order they arrive.
- **Restricted Access**: Elements can only be:
  - **Added (Enqueued)** at the rear.
  - **Removed (Dequeued)** from the front.
- **No Random Access**: Unlike arrays, you cannot directly access elements by index.

---

## ⚙️ Basic Operations
1. **Enqueue** — Add an element to the rear of the queue.
2. **Dequeue** — Remove an element from the front of the queue.
3. **Peek / Front** — View the element at the front without removing it.
4. **IsEmpty** — Check if the queue contains no elements.
5. **IsFull** (for fixed-size queues) — Check if the queue has reached maximum capacity.

---

## 🏗 Types of Queues
### 1. **Simple Queue**
- Operates strictly on FIFO.
- Items are enqueued at the rear and dequeued from the front.

### 2. **Circular Queue**
- The last position connects back to the first position.
- Prevents wasted space caused by repeated enqueues and dequeues.

### 3. **Priority Queue**
- Elements are dequeued based on **priority** rather than arrival time.
- High-priority elements are served first.

### 4. **Double-Ended Queue (Deque)**
- Elements can be added or removed from **both ends**.
- Can operate as both queue and stack.

---

## 🧠 Real-World Examples
- **Ticket Counters** — Customers are served in the order they arrive.
- **Printers** — Print jobs are queued and processed in sequence.
- **Operating Systems** — CPU scheduling and task management use queues.
- **Networking** — Packets are queued before being processed.

---

## 📊 Performance Considerations
- **Time Complexity**:  
  - Enqueue → O(1)  
  - Dequeue → O(1)  
  - Peek → O(1)  
- **Space Complexity**:  
  - Depends on the number of elements stored.

---

## 🔄 Queue vs Stack
| Feature          | Queue (FIFO)             | Stack (LIFO)             |
|------------------|--------------------------|--------------------------|
| Insertion        | Rear                    | Top                     |
| Removal          | Front                   | Top                     |
| Access Pattern   | First element first     | Last element first      |
| Real-world Use   | Ticket line, print jobs | Undo feature, recursion |

---

## 🚀 Key Takeaways
- A queue ensures **fair and ordered processing**.
- It is essential for **task scheduling, resource management, and sequential processing**.
- Variations like **Circular Queue** and **Priority Queue** improve efficiency for specific use cases.

---

## 📚 Summary
A **Queue** is more than just a data structure — it is a **fundamental concept** that models real-world scenarios where **order matters**. Understanding queues helps in designing **efficient algorithms** and **real-time systems**.

---

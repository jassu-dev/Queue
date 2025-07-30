class Queue:
    def __init__(self):
        self.items = []
    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)
    def isEmpty(self):
        return len(self.items)==0
    def enqueue(self, value):
        self.items.append(value)
        return (f"value {value} add to queue")
    def dequeue(self):
        if self.isEmpty():
            return "No Elements in Queue"
        else:
            self.items.pop(0)
            
    def peek(self):
        if(self.isEmpty()):
            return "No elements found"
        else:
            return self.items[0]
    def delete(self):
        if(self.isEmpty()):
            return "Already Queue is Empty"
        else:
            self.items = None
            return "Done"

    
sample_queue = Queue()
sample_queue.enqueue(1)
sample_queue.enqueue(2)
sample_queue.enqueue(3)
print(sample_queue.peek())
sample_queue.dequeue()
print(sample_queue)

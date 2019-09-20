class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  # when full always append by replacing the oldest information - not full replace the first preset None seen
  def append(self, item):
    self.storage[self.current % self.capacity] = item
    self.current = (self.current + 1) % self.capacity

  # return everything from buffer, in order, ignoring None values
  def get(self):
    return [item for item in self.storage if item is not None]
import numpy as np
from matplotlib import pyplot as plt


class LogBook:
  def __init__(self, *labels, buf_cap=1000):
    self.labels = labels
    self.buf_cap = buf_cap
    self.entries = self._new_buf()
    self._i = 0

  @property
  def num_labels(self):
    return len(self.labels)

  def _new_buf(self):
    return np.zeros((self.buf_cap, self.num_labels))

  def __getitem__(self, query):
    if isinstance(query, int):
      return self.entries[query]
    elif isinstance(query, str):
      return self.entries[:self._i, self.labels.index(query)]
    raise ValueError(f'invalid query type: {type(query)}')

  def record(self, *entry):
    assert len(entry) == len(self.labels)
    if self._i == self.entries.shape[0]:
      self.entries = np.vstack((self.entries, self._new_buf()))
    self.entries[self._i] = np.array(entry)
    self._i += 1

  def peek(self, top=10):
    print(', '.join(self.labels))
    for i in range(min(top, self._i)):
      print(', '.join([str(e) for e in self.entries[i]]))

  def clear(self):
    self.entries = self._new_buf()

  def export(self, filename):
    with open(filename, 'w') as f:
      f.write(','.join(self.labels)+'\n')
      for entry in self.entries[:self._i]:
        f.write(','.join([str(n) for n in entry])+'\n')
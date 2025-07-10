from abc import ABC, abstractmethod
class income(ABC):
    @abstractmethod
    def submit(self, bill):
        pass
class bi(income):
    def submit(self, bill):
        print(f"given: {bill}")
a=bi()
a.submit(500)

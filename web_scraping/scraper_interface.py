# scraper_interface.py
from abc import ABC, abstractmethod

class ScraperInterface(ABC):
    @abstractmethod
    def scrape(self):
        pass

    @abstractmethod
    def to_string(self):
        pass
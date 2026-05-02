__version__ = "0.1.0"
from rich.console import Console
from rich.live import Live
import asyncio
import time
import threading

class FluxDeck():
  """Dynamically print values to avoid clutter of console"""
  def __init__(self):
    self.status_messages = {}
    self.muted_categories = []
    self.console = Console()
    self.display = None
    self.lock = threading.Lock()
    flux_thread=threading.Thread(target=self.flux_core)
    flux_thread.start()
    
  def flux(self, category, info):
    """Update the content being displayed"""
    with self.lock:
      self.status_messages[category] = info
      self.format_output()
    
  def format_output(self):
    """Format the content to be displayed"""
    lines=[]
    for key,val in self.status_messages.items():
      if key in self.muted_categories:
        continue
      lines.append(f"======={key}=========\n\t\t{val}\n")
        
      self.display = "\n".join(lines)
    
  def mute(self, category):
    """Category added here will not appear in displayed data"""
    with self.lock:
      self.muted_categories.append(category)
      self.format_output()
  
  def unmute(self, category):
    """Remove category from muted list"""
    with self.lock:
      if category not in self.muted_categories:
        self.status_messages["error"] = f"'{category}' not in muted categories"
        self.format_output()
      else: 
        self.muted_categories.remove(category)
        self.format_output()
    
  def flux_core(self):
    """update console"""
    with Live(console=self.console,refresh_per_second= 4) as live:
        while True:
          with self.lock:
            display = self.display
            live.update(display)
          
        
        
        
if __name__ == "__main__":
  flux = FluxDeck()
  flux.flux("connect","success")
  flux.flux("authorize","failed")
  flux.unmute("heyoo")
  
  
  
  
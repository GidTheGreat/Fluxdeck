# FluxDeck

FluxDeck is a lightweight Python utility for dynamically managing and rendering structured console output without clutter. It acts as a simple in-terminal state dashboard that continuously updates displayed information in real time.

It is built using Python threading and Rich’s live rendering system.

---

## Features

- Dynamic category-based message tracking
- Live console updates without manual clearing
- Muting and unmuting of output categories
- Threaded rendering loop for continuous display updates
- Lightweight design with minimal dependencies

---

## Installation

### Requirements
- Python 3.8+
- rich

Install dependency:



## Example Usage

This example demonstrates how FluxDeck updates and controls dynamic console output.

```python id="r2"
from fluxdeck import FluxDeck
import time

flux = FluxDeck()

# Initial system state
flux.flux("status", "Initializing system")
flux.flux("network", "Connected")

time.sleep(2)

# Update state dynamically
flux.flux("status", "Running")
flux.mute("network")

time.sleep(2)

# Restore and update a muted category
flux.unmute("network")
flux.flux("network", "Restored connection")

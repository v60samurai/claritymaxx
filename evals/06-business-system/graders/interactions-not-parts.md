---
type: llm
---

The user asked how four things interact in a kayak rental business: schedule, inventory, pricing, and cancellation.

PASS if the reply explains at least three of these interactions, each one correctly:
A. Schedule and inventory: inventory is counted separately for each departure slot, so a booking uses up a kayak in one slot only.
B. Inventory and pricing: when a slot has 3 or fewer kayaks left, the price for the next customer goes up by 10.
C. Schedule and pricing: weekend (peak) slots cost 1.25 times the base price.
D. Cancellation and inventory and pricing: a cancellation puts a kayak back into the slot, which can remove the low-inventory surcharge for later customers.
E. Cancellation and pricing: the refund is a share of the price that customer paid, not of the current price.

FAIL if the reply only restates the four rule groups one after another without saying how one affects another.
FAIL if the reply invents a rule that is not in the notes and presents it as a rule of this business.

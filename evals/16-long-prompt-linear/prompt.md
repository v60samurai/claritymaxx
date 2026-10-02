---
tags: [text, over-escalation]
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Write]
---

Some background first, because I want a proper answer. I run the data platform for a logistics company. We have about forty services, three regions, a Kafka cluster, two warehouses, and a team that argues a lot. Last week we argued for an hour in an architecture review about a nightly job that sums parcel weights. One engineer stores the weights as 64-bit floats. The totals from two regions differed in the last digits, although both regions processed the same parcels. Half the room said this was a data bug, a quarter blamed the network, and one person said "floats are random". I have read three blog posts and I am more confused than before. I do not need a tour of our architecture, of Kafka, or of the warehouses.

The one thing I want to understand: why can adding the same floating-point numbers in a different order give a different total?

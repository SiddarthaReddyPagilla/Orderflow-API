# DispatchForge — Development Progress

## Project Overview

DispatchForge is a Python and SQL delivery optimization
project focused on the Dallas–Fort Worth area.

The project aims to improve warehouse selection,
inventory allocation, and delivery feasibility
using algorithms and database systems.

Geographic reference locations are based on public
information. Operational data is simulated.

## Completed Features

### 1. Warehouse Reference System
- Defined three DFW warehouse reference locations.
- Stored warehouse information using Python dictionaries.

### 2. Inventory Management
- Created inventory availability checks.
- Implemented basic in-memory inventory reservations.
- Added tests for insufficient stock and edge cases.

### 3. Warehouse Eligibility
- Developed an algorithm to identify warehouses
  capable of fulfilling customer orders.

### 4. Inventory-Based Warehouse Ranking
- Implemented stock-based warehouse ranking.
- Added automated ranking tests.

### 5. Geographic Distance Engine
- Implemented the Haversine distance formula.
- Added six geographic distance tests.
- Verified 29 total automated tests passing.

## Current Development

- Adding DFW geographic reference coordinates.
- Integrating geographic distance into warehouse ranking.
- Preparing automated tests for proximity-based selection.

## Planned Improvements

- PostgreSQL database integration.
- Reliable concurrent inventory reservations.
- Road-network distance and travel-time estimates.
- Courier assignment algorithms.
- Delivery feasibility prediction.
- REST APIs using FastAPI.
- Docker and cloud deployment.

## Engineering Notes

The current system uses an in-memory simulation.
It is not yet a production-ready delivery service.

Straight-line distance does not represent driving distance
or actual delivery time.

Future benchmarks will compare inventory-based
and geography-aware warehouse selection.

## Testing

Previously verified: 29 automated Python tests passing.

Testing will be repeated before the next commit.

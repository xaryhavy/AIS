# ADR-001: Multi-Layer Memory Architecture

## Status

Accepted

## Date

August 1, 2026

## Context

Originally AIS used a single Business Intelligence Memory (BIM).

During architecture discussions it became clear that business-specific knowledge and global business knowledge are fundamentally different.

## Decision

AIS will use multiple memory systems instead of one.

Business Intelligence Memory (BIM)
- Stores knowledge about one business.

Global Intelligence Memory (GIM)
- Stores knowledge learned across all businesses.

Pending Memory
- Stores incomplete analyses awaiting additional information.

Knowledge Gap Memory (KGM)
- Stores recurring missing information patterns to improve future discovery.

## Consequences

AIS becomes capable of learning from individual businesses while simultaneously becoming a smarter consultant for every future client.
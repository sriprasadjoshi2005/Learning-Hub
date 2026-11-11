---
title: Memory Hierarchy and Storage Systems
level: foundation
---

Computer memory stores instructions, data and intermediate results required during processing. Different memory technologies provide different combinations of speed, capacity, cost and persistence.

## 1. Primary Memory

Primary memory is directly accessible by the CPU or its memory management system.

### Random Access Memory (RAM)

RAM temporarily stores data and instructions currently being used by the computer.

Characteristics:

- Volatile memory.
- Supports reading and writing.
- Provides relatively fast access.
- Loses its stored contents when power is removed.

Types include:

**DRAM:** Dynamic RAM requires periodic refreshing and is commonly used as main memory.

**SRAM:** Static RAM does not require periodic refreshing and is commonly used in processor caches.

### Read Only Memory (ROM)

ROM is non-volatile memory used to store information that must be retained without power.

Examples include firmware storage.

Common ROM classifications include:

- PROM: Programmable Read Only Memory.
- EPROM: Erasable Programmable Read Only Memory.
- EEPROM: Electrically Erasable Programmable Read Only Memory.

## 2. Cache Memory

Cache is small, high-speed memory that stores frequently accessed instructions and data.

It reduces the average time required to access information from slower memory.

Common levels include:

- L1 Cache: Usually the smallest and fastest cache.
- L2 Cache: Generally larger than L1.
- L3 Cache: Often larger and shared between processor cores.

The exact arrangement depends on processor design.

## 3. Memory Hierarchy

Computer memory is organised into levels according to speed, capacity and cost.

A simplified hierarchy is:

1. CPU Registers.
2. Cache Memory.
3. Main Memory (RAM).
4. Secondary Storage.
5. Archival Storage.

Generally:

- Higher levels are faster and more expensive per unit of storage.
- Lower levels offer greater capacity at lower cost per unit.
- Access time generally increases as we move down the hierarchy.

## 4. Secondary Storage

Secondary storage provides long-term data retention.

### Hard Disk Drive (HDD)

Uses magnetic storage technology and rotating disks.

Advantages:
- Large storage capacity.
- Generally lower cost per unit of storage.

Limitations:
- Mechanical components.
- Slower random access compared with SSDs.
- More vulnerable to physical shock.

### Solid State Drive (SSD)

Uses flash memory and has no moving mechanical parts.

Advantages:
- Fast data access.
- Low power consumption in many designs.
- Better resistance to mechanical shock.

Limitations:
- Generally higher cost per unit of storage than comparable HDD capacity.

## 5. Optical and Removable Storage

Examples include:

- CD.
- DVD.
- Blu-ray Disc.
- USB flash drive.
- Memory card.

Optical media use laser-based reading and writing technologies.

## 6. Volatile and Non-Volatile Memory

| Volatile memory | Non-volatile memory |
|---|---|
| Requires power to retain data | Retains data without power |
| Commonly used for active processing | Commonly used for persistent storage |
| Example: RAM | Examples: ROM, SSD and flash memory |

## 7. Storage Units

| Unit | Common binary interpretation |
|---|---:|
| 1 bit | 1 binary digit |
| 1 byte | 8 bits |
| 1 KiB | 1,024 bytes |
| 1 MiB | 1,024 KiB |
| 1 GiB | 1,024 MiB |
| 1 TiB | 1,024 GiB |

Storage manufacturers sometimes use decimal units:

- 1 kB = 1,000 bytes.
- 1 MB = 1,000 kB.
- 1 GB = 1,000 MB.

Do not confuse decimal units with binary units.

## Common Exam Traps

- RAM is generally volatile.
- ROM is non-volatile.
- Cache is faster than main memory in typical systems.
- Registers are generally faster than cache.
- HDDs use magnetic storage.
- SSDs use flash memory.
- A byte contains 8 bits.
- KiB and kB are not identical units.

## Quiz

1. Which type of memory is commonly used as the main memory of a computer?

- [ ] Optical memory.
- [x] RAM.
- [ ] Magnetic tape.
- [ ] CPU register only.

> RAM stores active programs and data required during computer operation.

2. Which memory is generally the fastest among the following?

- [ ] HDD.
- [ ] RAM.
- [ ] SSD.
- [x] CPU registers.

> CPU registers are extremely fast storage locations located inside the processor.

3. How many bits are present in one byte?

- [ ] 4 bits.
- [ ] 16 bits.
- [x] 8 bits.
- [ ] 32 bits.

> One byte consists of exactly eight bits.
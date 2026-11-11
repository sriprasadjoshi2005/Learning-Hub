---
title: Computer Networks and Networking Fundamentals
level: foundation
---

A computer network is a collection of connected devices that communicate and exchange information. Networks enable internet access, file sharing, communication services, distributed computing, and resource sharing.

## 1. Understanding Computer Networks

A computer network connects devices through wired or wireless communication technologies.

Connected devices may include:

- Computers.
- Smartphones.
- Servers.
- Printers.
- Routers.
- Sensors.
- Smart devices.

Networks allow these devices to exchange information and share resources.

## 2. Types of Networks

### Personal Area Network

A Personal Area Network, or PAN, connects devices within a very small area around an individual.

Example: A smartphone connected to wireless headphones.

### Local Area Network

A Local Area Network, or LAN, connects devices within a limited geographical area.

Examples include:
- Homes.
- Schools.
- Offices.
- Laboratories.

### Metropolitan Area Network

A Metropolitan Area Network, or MAN, connects networks across a city or metropolitan region.

### Wide Area Network

A Wide Area Network, or WAN, connects devices and networks over large geographical areas.

The internet is the largest widely used example of an interconnected global network.

## 3. Network Topologies

Network topology describes how devices and connections are arranged.

### Bus Topology

Devices share a common communication backbone.

### Star Topology

Devices connect to a central device such as a switch.

### Ring Topology

Devices form a circular connection arrangement.

### Mesh Topology

Devices are connected through multiple paths.

### Tree Topology

Devices are organized in a hierarchical structure.

### Hybrid Topology

Combines multiple topology types.

## 4. Network Devices

### Router

Connects different networks and forwards packets between them.

### Switch

Connects devices within a local network and forwards frames using MAC addresses.

### Hub

Broadcasts received signals to all connected ports.

### Modem

Converts signals or performs modulation and demodulation functions required by a communication connection.

### Wireless Access Point

Allows wireless devices to connect to a network.

### Repeater

Regenerates or retransmits signals to extend communication distance.

## 5. Transmission Media

Transmission media carry information between network devices.

### Guided Media

Uses physical communication paths.

Examples:
- Twisted-pair cables.
- Coaxial cables.
- Optical fibre.

### Unguided Media

Uses wireless communication.

Examples:
- Radio waves.
- Microwaves.
- Infrared communication.
- Satellite communication.

Optical fibre carries information using light and supports high-bandwidth communication over long distances.

## 6. Network Models

Network models organize communication functions into layers.

Two important models are:

- OSI model.
- TCP/IP model.

## 7. OSI Model

The Open Systems Interconnection model contains seven layers.

| Layer | Name | Main Function |
| --- | --- | --- |
| 7 | Application | Provides network services to applications |
| 6 | Presentation | Handles data representation and transformation |
| 5 | Session | Manages communication sessions |
| 4 | Transport | Provides end-to-end transport functions |
| 3 | Network | Handles logical addressing and routing |
| 2 | Data Link | Handles framing and local link delivery |
| 1 | Physical | Transmits raw bits through a medium |

Each layer has a specific role in network communication.

## 8. TCP/IP Model

The TCP/IP model represents the architecture commonly associated with internet communication.

A commonly used four-layer representation is:

| Layer | Main Function |
| --- | --- |
| Application | Application-level network protocols |
| Transport | End-to-end communication |
| Internet | Logical addressing and packet routing |
| Network Access | Access to the physical network medium |

The OSI model is mainly a conceptual reference, while TCP/IP describes the architecture and protocols used by the internet.

## 9. IP Addressing

An Internet Protocol address identifies a network interface for communication using IP.

Two major versions are:

### IPv4

IPv4 uses 32-bit addresses.

Example:

```text
192.168.1.10
```

IPv4 addresses are commonly written as four decimal numbers separated by periods.

### IPv6

IPv6 uses 128-bit addresses.

Example:

```text
2001:db8::1
```

IPv6 provides a much larger address space than IPv4.

## 10. MAC Addresses

A Media Access Control address identifies a network interface at the data-link layer.

It is commonly represented using hexadecimal notation.

MAC addresses are used in local network communication.

They are distinct from IP addresses, which provide logical addressing.

## 11. Important Network Protocols

A protocol is a set of rules governing communication between devices.

| Protocol | Purpose |
| --- | --- |
| HTTP | Transfers web resources |
| HTTPS | Secures HTTP communication using TLS |
| TCP | Provides reliable, ordered byte-stream transport |
| UDP | Provides connectionless datagram transport |
| IP | Handles logical addressing and packet routing |
| DNS | Resolves domain names to IP addresses |
| DHCP | Automatically provides network configuration |
| SMTP | Sends email |
| FTP | Transfers files |
| SSH | Provides secure remote access |

## 12. TCP vs UDP

| Feature | TCP | UDP |
| --- | --- | --- |
| Connection | Connection-oriented | Connectionless |
| Delivery | Reliable transport with retransmission mechanisms | No built-in delivery guarantee |
| Ordering | Preserves byte-stream order | No general ordering guarantee |
| Overhead | Generally higher | Generally lower |
| Applications | Web connections, file transfer, email | Streaming, gaming, real-time communication |

The choice depends on application requirements.

## 13. DNS

The Domain Name System translates human-readable domain names into information used for network communication, commonly IP addresses.

For example:

A user enters a domain name into a browser.

The system performs DNS resolution to determine the appropriate address.

DNS makes internet navigation more convenient.

## 14. Bandwidth, Latency and Throughput

### Bandwidth

The maximum data-carrying capacity of a communication channel under specified conditions.

### Latency

The delay experienced during data transmission.

### Throughput

The actual rate at which data is successfully transferred.

A network can have high bandwidth but still experience high latency.

## 15. Network Security

Network security protects communication systems and connected devices.

Important methods include:

- Firewalls.
- Encryption.
- Authentication.
- Network segmentation.
- Intrusion detection.
- Secure configuration.
- Regular software updates.

## 16. Applications of Computer Networks

Networks support:

- Internet browsing.
- Email.
- Video conferencing.
- Cloud computing.
- Online banking.
- Multiplayer games.
- Distributed databases.
- Internet of Things.
- Remote collaboration.

## Common Exam Traps

- LAN covers a limited geographical area.
- WAN connects networks over large areas.
- A router connects different networks.
- A switch forwards frames within a local network.
- The OSI model contains seven layers.
- TCP provides reliable, ordered byte-stream transport.
- UDP does not guarantee delivery or ordering.
- IPv4 uses 32-bit addresses.
- IPv6 uses 128-bit addresses.
- DNS resolves domain names.
- Bandwidth, latency, and throughput are different measurements.

## Quiz

1. Which network device forwards packets between different networks?
   - [ ] Hub
   - [ ] Repeater
   - [x] Router
   - [ ] Printer

   > A router connects networks and forwards packets using network-layer information.

2. How many layers are present in the OSI reference model?
   - [ ] 4
   - [ ] 5
   - [x] 7
   - [ ] 8

   > The OSI model contains seven layers, from Physical to Application.

3. Which protocol resolves domain names into network addressing information?
   - [ ] SMTP
   - [ ] FTP
   - [ ] UDP
   - [x] DNS

   > DNS translates domain names into records such as IP addresses.
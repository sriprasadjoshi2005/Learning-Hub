---
title: Cybersecurity and Information Security Fundamentals
level: intermediate
---

Cybersecurity is the practice of protecting computers, networks, applications, and digital information from unauthorized access, attacks, damage, and disruption. It is essential because modern individuals, businesses, and governments depend heavily on digital systems.

## 1. Understanding Cybersecurity

Cybersecurity focuses on protecting digital systems and information.

It includes:

- Network security.
- Application security.
- Data protection.
- Identity management.
- Device security.
- Incident response.
- Security monitoring.

Cybersecurity aims to reduce risks and protect the confidentiality, integrity, and availability of information.

## 2. The CIA Triad

The CIA triad is a foundational information-security model.

It contains three principles.

### Confidentiality

Ensures that information is accessible only to authorized individuals or systems.

Examples:
- Encryption.
- Access controls.
- Authentication.
- Data classification.

### Integrity

Ensures that information remains accurate and is not improperly modified.

Examples:
- Cryptographic hashes.
- Digital signatures.
- Access restrictions.
- Audit logs.

### Availability

Ensures that systems and information remain accessible when required.

Examples:
- Backups.
- Redundant systems.
- Disaster recovery.
- Protection against denial-of-service attacks.

## 3. Common Cybersecurity Threats

### Malware

Malware is malicious software designed to damage systems, steal information, or perform unauthorized activities.

Types include:

- Virus.
- Worm.
- Trojan horse.
- Spyware.
- Ransomware.
- Rootkit.

### Phishing

Phishing uses deceptive messages or websites to trick people into revealing sensitive information or performing unsafe actions.

### Social Engineering

Social engineering manipulates people into disclosing information or bypassing security procedures.

### Denial-of-Service Attack

A denial-of-service attack attempts to make a system or service unavailable by overwhelming or disrupting it.

### Man-in-the-Middle Attack

An attacker positions themselves between communicating parties to intercept or potentially modify information.

### Password Attacks

Attackers may attempt to obtain passwords using methods such as:

- Brute-force guessing.
- Dictionary attacks.
- Credential stuffing.
- Password spraying.

## 4. Authentication and Authorization

These are related but different security concepts.

### Authentication

Authentication verifies the identity of a user or system.

Examples:
- Passwords.
- One-time passwords.
- Biometrics.
- Security keys.
- Digital certificates.

### Authorization

Authorization determines which actions an authenticated identity is permitted to perform.

For example, a user may be allowed to read a document but not modify it.

## 5. Multi-Factor Authentication

Multi-factor authentication, or MFA, requires multiple independent authentication factors.

Common factor categories include:

- Something you know: Password or PIN.
- Something you have: Security key or registered device.
- Something you are: Biometric characteristic.

Using multiple factors can reduce the risk associated with stolen passwords.

## 6. Encryption

Encryption transforms readable information into ciphertext using a cryptographic process.

Decryption reverses the process for an authorized recipient.

### Symmetric Encryption

Uses the same secret key for encryption and decryption.

It is generally efficient for protecting large amounts of data.

### Asymmetric Encryption

Uses a mathematically related public key and private key.

The keys have different roles depending on the cryptographic operation.

It supports applications such as key establishment and digital signatures.

## 7. Hashing

Hashing transforms input data into a fixed-length digest using a hash function.

Cryptographic hash functions are designed to make it computationally difficult to find certain kinds of collisions or reverse the transformation.

Common applications include:

- File integrity verification.
- Digital signatures.
- Password storage systems.
- Data identification.

Password storage should use dedicated password-hashing algorithms such as Argon2id, bcrypt, or scrypt, with appropriate salts and configuration.

A fast general-purpose hash alone is not suitable for secure password storage.

## 8. Digital Signatures

A digital signature provides a way to verify the authenticity and integrity of digitally signed information.

A signer uses a private key to create a signature.

A verifier uses the corresponding public key to verify it.

Digital signatures help establish that information was signed by the holder of the relevant private key and has not been altered in a way that invalidates the signature.

## 9. Firewalls

A firewall monitors and controls network traffic according to defined security rules.

It may restrict connections based on:

- Source address.
- Destination address.
- Port number.
- Protocol.
- Connection state.
- Application information.

Firewalls help reduce unauthorized network access.

## 10. Network Security Tools

Common security tools and technologies include:

### Intrusion Detection System

An Intrusion Detection System, or IDS, monitors activity and identifies suspicious behaviour.

### Intrusion Prevention System

An Intrusion Prevention System, or IPS, can take actions to block or prevent detected threats.

### Virtual Private Network

A Virtual Private Network, or VPN, creates a protected communication tunnel across another network.

A VPN does not automatically make every online activity anonymous or secure.

### Security Information and Event Management

SIEM systems collect and analyze security events from different sources to support monitoring and investigation.

## 11. Common Web Security Vulnerabilities

### SQL Injection

SQL injection occurs when untrusted input is improperly incorporated into database queries.

Prevention includes parameterized queries and appropriate input handling.

### Cross-Site Scripting

Cross-site scripting, or XSS, occurs when malicious script content is executed in another user's browser.

Prevention includes context-aware output encoding and safe handling of untrusted content.

### Cross-Site Request Forgery

Cross-site request forgery, or CSRF, tricks an authenticated browser into submitting an unwanted request.

Prevention may include CSRF tokens, appropriate cookie settings, and request-origin checks.

### Broken Access Control

Occurs when an application fails to enforce the permissions required for an operation.

Prevention requires server-side authorization checks for every protected action.

## 12. Secure Password Practices

Good password-security practices include:

- Use long, unique passwords.
- Avoid reusing passwords across services.
- Use a reputable password manager.
- Enable multi-factor authentication.
- Avoid sharing passwords.
- Do not store plaintext passwords.
- Protect account-recovery mechanisms.

Organizations should store password hashes using dedicated password-hashing algorithms rather than storing original passwords.

## 13. Security Updates and Patch Management

Software vulnerabilities can allow attackers to exploit weaknesses in applications and operating systems.

Patch management involves:

1. Identifying software and system components.
2. Monitoring security updates.
3. Evaluating affected systems.
4. Testing updates where appropriate.
5. Installing security patches.
6. Verifying successful deployment.

Keeping software updated reduces exposure to known vulnerabilities.

## 14. Backup and Disaster Recovery

Backups preserve copies of important information.

A reliable backup strategy considers:

- Backup frequency.
- Storage location.
- Encryption.
- Access restrictions.
- Retention periods.
- Recovery testing.

The 3-2-1 backup principle recommends maintaining three copies of important data, using two different storage types, with one copy kept off-site.

## 15. Incident Response

Incident response is the structured process of handling security incidents.

A typical process includes:

1. Preparation.
2. Detection and analysis.
3. Containment.
4. Eradication.
5. Recovery.
6. Lessons learned.

A well-defined incident-response plan reduces confusion and improves recovery.

## 16. Responsible Cybersecurity

Cybersecurity knowledge should be used lawfully and ethically.

Important principles include:

- Obtain permission before testing systems.
- Protect personal information.
- Follow applicable laws.
- Report vulnerabilities responsibly.
- Avoid unauthorized access.
- Respect system owners and users.

## Common Exam Traps

- The CIA triad consists of Confidentiality, Integrity, and Availability.
- Authentication verifies identity.
- Authorization determines permitted actions.
- Symmetric encryption uses a shared secret key.
- Asymmetric cryptography uses public and private keys.
- Hashing is not the same as encryption.
- Digital signatures support authenticity and integrity verification.
- Firewalls control network traffic.
- IDS detects suspicious activity, while IPS can actively prevent it.
- SQL injection involves unsafe database-query construction.
- XSS involves malicious script execution in a user's browser.
- CSRF tricks a browser into submitting an unwanted request.
- Security backups should be tested through recovery exercises.

## Quiz

1. Which principle of the CIA triad ensures that information is accessible only to authorized parties?
   - [ ] Availability
   - [ ] Integrity
   - [x] Confidentiality
   - [ ] Redundancy

   > Confidentiality protects information from unauthorized disclosure.

2. Which security process verifies the identity of a user?
   - [ ] Authorization
   - [ ] Encryption
   - [x] Authentication
   - [ ] Data compression

   > Authentication establishes whether an identity is genuine.

3. Which vulnerability occurs when untrusted input is improperly incorporated into a database query?
   - [ ] Cross-site scripting
   - [ ] Denial of service
   - [x] SQL injection
   - [ ] Network fragmentation

   > SQL injection exploits unsafe construction of database queries using untrusted input.
# Maxwell McCormick

Decatur, Alabama · 256-616-3929 · william.max.mccormick@gmail.com\
github.com/NotMaxwell · notmaxwell.github.io

## Summary

Senior at the Alabama School of Cyber Technology and Engineering who builds systems and
embedded software, primarily in Rust. Work spans security automation that makes
irreversible changes to live systems and therefore has to be correct, ESP32 firmware that
fuses GPS, IMU and LiDAR into a coordinate, and web applications backed by PostgreSQL.
Lead programmer and driver for a competitive robotics team, and Windows and scripting lead
for a CyberPatriot team.

## Education

**Alabama School of Cyber Technology and Engineering (ASCTE)** — Huntsville, Alabama\
High school diploma expected 2027

Coursework in cybersecurity, software development, and engineering, including controls labs
(Engr401) and a year-long group capstone.

## Technical Skills

**Languages.** Rust (primary), C, C++, Zig, Go, C#, Python, Java, TypeScript, Swift,
PowerShell, Bash

**Embedded and control.** ESP32-S3 (esp-hal, ESP-IDF), RP2040, Embassy async runtime,
`no_std` Rust, I²C and UART sensor integration, PID control

**Security.** Windows and Linux hardening, registry and local security policy, `/etc` and
systemd configuration, scripted remediation, CyberPatriot competition

**Web and data.** Go with Gin, HTMX, server-rendered templates, Bun and Hono, PostgreSQL,
SQLite, EF Core, Docker, Playwright, REST API integration

**Tools.** Git, Cargo, CMake, Gradle, Avalonia, wgpu, Fusion 360 CAD, Excel

## Projects

**PinnacleCyPat** — Automated security hardening for CyberPatriot competition images, on
Windows and Linux. Reads the round's own README, applies the mechanical part of the
checklist, and reports exactly what changed. Because the changes are largely irreversible —
deleted accounts, rewritten registry and security policy, uninstalled software — it ships
with a dry-run mode and 726 tests. Rust 2024, with a desktop GUI over the CLI.

**PING** (ASCTE capstone) — Aim the device at something, press the button, and it reports
that thing's GPS coordinate. An ESP32-S3 reads a NEO-M9N GPS, a BNO085 IMU and a TF03
LiDAR, then walks the measured range out from its own position along the WGS-84 ellipsoid.
Main firmware is `no_std` Rust on esp-hal and Embassy; wrote a second C++23 ESP-IDF
implementation to determine whether sensor dropouts were hardware or software.

**Highway Traffic Simulator** — Native Rust desktop application that runs human-driver and
autonomous modes side by side on identical inputs — same seed, same arrivals, same driver
traits — so the controller mix is the only variable. Default scenario models I-565 between
Decatur and Huntsville, including the two-lane work zone and morning peak. Rendered with
wgpu.

**TealTeam** — Scouting and analytics web application for robotics team 10101 Critical Hit.
Go and Gin serving templates with HTMX fragments, PostgreSQL for storage, and sync clients
for the FIRST and Blue Alliance APIs. Deployed to Render on a Docker runtime.

**GoogleDriveAI** — Sorts Google Drive files into class folders using a classifier trained
on folders already sorted by hand. Documents become text, text becomes a MiniLM embedding,
and a small MLP predicts the folder. Holds out 20% of each class to report accuracy on
unseen files, and leaves anything under the confidence threshold for a human.

**CHEmailBot** — Outreach tool for Huntsville-area technology companies built on Bun, Hono
and SQLite, with Playwright for contact forms and the Gmail API for email. Includes a
mandatory review step before anything sends and a database constraint guaranteeing no
company is contacted twice in a campaign.

**PID Cart Controller** — Async Rust firmware reimplementing a MicroPython cart-and-rail
controls lab on a Raspberry Pi Pico, using Embassy and the handout's exact PID formulas.

Earlier projects include an LED powered by a windmill, computer-controlled Christmas
lights, a point-of-sale system, a 3D maze runner game, and a robot chassis designed in
Fusion 360.

## Leadership

**Lead Programmer, Lead Tester and Driver** — Robotics team 10101 Critical Hit\
Own the robot codebase and the scouting tools the team uses to pick alliances, and drive in
competition.

**Windows and Scripting Lead; Team Lead** — CyberPatriot\
Handle Windows hardening during rounds and write the scripts and lesson plans used to bring
new team members up to speed.

## Experience

**Bus Boy** — Brick Deli · 2023–2025\
Worked across several teams to deliver service quickly without dropping quality, managed a
secondary task alongside the main one, and adjusted to what coworkers needed as shifts
changed.

## Community Service

Fire Department 5K · setup for ASCTE robotics events · coached a middle school scholars
bowl team

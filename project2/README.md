# Project 2 — The Server Commander
## DecodeLabs Cloud Computing Internship · Batch 2026

> **Mission:** Provision a virtual Linux server, secure it, connect via SSH, install Nginx, and deploy a live "Welcome to DecodeLabs" webpage.

---

## What I Built

A cloud-hosted web server on AWS EC2 running Amazon Linux with Nginx — serving a custom "Welcome to DecodeLabs: Mission Accomplished" webpage on a public IP address.

---

## Concepts Learned

### IaaS vs Serverless
Project 1 was serverless (S3) — no OS, no server management. Project 2 is IaaS — I provision and own a full virtual machine. I control the OS, the software, the security. The cloud provider only manages the physical hardware underneath.

### Hypervisor Logic
AWS uses the Nitro Hypervisor to partition one physical machine into multiple isolated VMs. My EC2 instance is a "guest" running on top of AWS hardware. This is what makes cloud computing scalable — dozens of VMs from one physical box.

### Shared Responsibility Model
- **AWS is responsible for:** Physical data centers, hardware, virtualization layer
- **I am responsible for:** Guest OS, patching, firewall (Security Groups), IAM, encryption

### SSH Key Authentication
Two keys — public and private. Public key stored on the server. Private key stored on my machine and NEVER shared. Format: `.pem` for Linux/macOS, `.ppk` for Windows/PuTTY.

### Security Groups
AWS firewalls that are ALLOW-ONLY. All traffic is denied by default. I opened:
- Port 22 (SSH) — restricted to my IP only
- Port 80 (HTTP) — open to the world (0.0.0.0/0)
- Port 443 (HTTPS) — open to the world

### Nginx vs Apache
Selected Nginx — event-driven, high-speed, handles high concurrency better than Apache's process-driven model.

---

## Step-by-Step Execution

### Phase 1 — Provisioning the VM

Launched EC2 instance from AWS Management Console:

```
Instance Name:  Server-Commander-01
AMI (OS):       Amazon Linux 2023
Instance Type:  t2.micro (Free Tier)
Key Pair:       Created new → Downloaded .pem file
```

### Phase 2 — Securing the Perimeter

Configured Security Group inbound rules:

```
Type    | Port | Source          | Status
--------|------|-----------------|----------
SSH     | 22   | My IP only      | RESTRICTED
HTTP    | 80   | Anywhere 0.0.0.0| OPEN
HTTPS   | 443  | Anywhere 0.0.0.0| OPEN
```

### Phase 3 — SSH Connection (Windows via PuTTY)

Converted .pem to .ppk using PuTTYgen:
```
PuTTYgen → Load .pem file → Save private key as .ppk
```

Connected to server:
```bash
ssh -i keyname.pem ec2-user@<Public-IP>
# Output: [ec2-user@ip-172-31-0-1 ~]$  ← ACCESS GRANTED
```

### Phase 4 — Installing Nginx

```bash
# Update system packages
sudo dnf update -y

# Install Nginx web server
sudo dnf install nginx -y

# Start Nginx service
sudo systemctl start nginx

# Enable Nginx to start on reboot
sudo systemctl enable nginx

# Verify it's running
sudo systemctl status nginx
```

### Phase 5 — Deploying the Custom Webpage

```bash
# Navigate to Nginx web root
cd /usr/share/nginx/html/

# Edit the index.html file
sudo nano index.html
```

Replaced default Nginx page with custom "Welcome to DecodeLabs" HTML.

```bash
# Save file: Ctrl+O → Enter → Ctrl+X
# Reload Nginx to serve new content
sudo systemctl reload nginx
```

### Phase 6 — Verification

Opened browser → visited `http://<Public-IP>`

```
✓ Page loaded: "Welcome to DecodeLabs: Mission Accomplished"
✓ Server: Nginx
✓ Status: ONLINE
```

---

## Architecture Diagram

```
                    INTERNET
                       │
                  Port 80/443
                       │
              ┌────────▼────────┐
              │   AWS EC2       │
              │   t2.micro      │
              │   Amazon Linux  │
              │                 │
              │   [Nginx]       │
              │   /usr/share/   │
              │   nginx/html/   │
              │   index.html    │
              └─────────────────┘
                       │
              SSH Port 22 (My IP Only)
                       │
                  My Machine
```

---

## Files in This Project

```
project2/
  index.html   ← The live "Welcome to DecodeLabs" webpage
  README.md    ← This documentation
```

---

## Key Takeaways

- **IaaS = Full Control.** You own the OS, the stack, the security decisions.
- **Security Groups = Cloud Firewall.** Deny all by default, allow only what's needed.
- **SSH Keys = Zero Password Auth.** More secure than username/password.
- **Nginx = Production-Grade Web Server.** Event-driven, fast, handles thousands of connections.
- **The Cloud is an Engine. You are the Operator.**

---

## Intern Details

| Field | Value |
|-------|-------|
| Name | Mamoon Azam Khattak |
| Email | mamoonkhattak758@gmail.com |
| University | UET Peshawar · CSE · Batch 27 |
| Internship | DecodeLabs Cloud Computing — AWS/Azure |
| Project | 2 — The Server Commander |
| Batch | 2026 |

---

*DecodeLabs Cloud Computing Internship · Batch 2026*

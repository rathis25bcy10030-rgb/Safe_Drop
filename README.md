# Safe_Drop
# 🛡 SafeDrop – Secure File Upload Portal

SafeDrop is a security-first web application designed to prevent malicious file uploads and protect servers from common file-based attacks.  

It follows a layered validation strategy to ensure only safe and trusted files are stored on the system.

---

## 🚀 Features

- ✅ File Type Whitelisting (PDF, JPG, PNG, JPEG)
- ✅ File Size Restriction (Max 5MB)
- ✅ Double Extension Detection (e.g., file.jpg.exe)
- ✅ Secure File Renaming
- ✅ Suspicious Upload Logging
- ✅ Modern Dark Cybersecurity UI
- ✅ Client-side + Server-side Validation

---

## 🔐 Security Approach

SafeDrop uses a multi-layered security model:

1. **Client-side validation** (JavaScript)
   - File size check
   - Extension validation
   - Double-extension detection

2. **Server-side validation** (Flask)
   - Whitelist-based file filtering
   - MIME type verification
   - Secure file renaming using UUID
   - Restricted upload directory

This ensures files are validated before storage and prevents common vulnerabilities such as:
- Remote Code Execution (RCE)
- Path Traversal Attacks
- Malicious Script Uploads
- Denial of Service (large file uploads)

---

## 🏗 Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS (Dark Cyber Theme), JavaScript
- **Storage:** Secure server-side directory
- **Security Model:** OWASP-inspired secure file handling practices

---

## 📂 Project Structure


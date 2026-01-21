# CCNA 200-301 Obsidian Vault Generator

This script automatically generates a comprehensive, pre-structured [Obsidian](https://obsidian.md/) vault for studying for the Cisco CCNA 200-301 exam.

Each topic is a defined exam objective that can be found on the [Cisco website.](https://learningnetwork.cisco.com/s/ccna-exam-topics)

This is intended to be used with the CCNA Official Cert Guide. Each Topic Correlates to its respective chapter. V1 = Volume 1 / V2 = Volume 2.

This is also intended to be used with Practice Exams and Labs. Each topics has a progress tracker where you can track if you have read, labbed, and tested each topic.

## Features

This script builds a complete study environment for you, including:

*   **Full Blueprint Structure:** Creates a folder for every single domain and sub-domain from the official CCNA 200-301 exam blueprint.
*   **Individual Topic Notes:** Generates a separate `.md` note for every exam topic, named and numbered correctly.
*   **Powerful Note Template:** Pre-populates every single note with a structured template, including sections for:
    *   `Tags` for easy searching.
    *   `Key Concepts & Definitions` for your own explanations.
    *   `How to Lab It` for documenting practical work.
    *   `Related Concepts` to encourage building a web of knowledge.
*   **Master Reference Document:** Creates a `MASTER REFERENCE.md` file at the top level, pre-filled with essential "cheat sheet" tables for port numbers, administrative distances, and more.
*   **Study Plan Outline:** Creates a `GENERAL OVERVIEW & OUTLINE.md` file that acts as a high-level dashboard and table of contents for your vault.

### Visual Preview

The script will generate a folder structure that looks like this:
```
CCNA 200-301/
├── 📄 MASTER REFERENCE.md
├── 📄 GENERAL OVERVIEW & OUTLINE.md
├── 📁 1.0 Network Fundamentals/
│ ├── 📁 1.1 Role and function of network components/
│ │ ├── 📄 1.1.a Routers.md
│ │ ├── 📄 1.1.b Layer 2 and Layer 3 switches.md
│ │ └── ... (and so on for every topic)
│ ├── 📁 1.2 Network topology architectures/
│ │ └── ...
├── 📁 2.0 Network Access/
│ └── ...
└── (etc. for all 6 domains)
---
```
## Prerequisites

Before you begin, make sure you have the following installed and ready.

1.  **Python 3:** The script is written in Python.
    *   To check if you have it, open your terminal or command prompt and type: `python3 --version` or `python --version`. If you see a version number (e.g., `Python 3.9.1`), you are all set.
    *   If you don't have it, download it from the official [Python website](https://www.python.org/downloads/).

2.  **Obsidian:** The note-taking application this vault is designed for.
    *   Download it for free from [obsidian.md](https://obsidian.md/).

3.  **The Script:** You need the `CCNA_Vault_Generator.py` file from this repository.

---

## 🚀 How to Use

Follow these steps exactly to generate your vault.

### Step 1: Download the Script

Download the `CCNA_Vault_Generator.py` script from this repository by clicking the green `Code` button, then `Download ZIP`, or by just saving the file directly. Place it in an easily accessible folder, like your Desktop or Downloads.

### Step 2: Open Your Terminal

You will need to run the script from a command line interface.

*   **Windows:** Open the Start Menu and search for `Command Prompt` or `PowerShell`.
*   **Mac/Linux:** Open the `Terminal` application.

### Step 3: Navigate to the Script's Location

In the terminal you just opened, you need to change the directory to where you saved the script. Use the `cd` (change directory) command.


# Example if you saved it to your Desktop
`cd Desktop`

# Example if you saved it to your Downloads folder
`cd Downloads`

Step 4: Run the Python Script
Execute the script by typing the following command and pressing Enter.
# For Mac/Linux users (and some Windows setups)
`python3 CCNA_Vault_Generator.py`

# If the above doesn't work, try this (common on Windows)
`python CCNA_Vault_Generator.py`

You will see the script print out a log of all the folders and files it is creating. Once it says "Vault creation complete!", you are done with this step. A new folder named CCNA 200-301 has been created in the same location as the script.

Step 5: Open the Vault in Obsidian
`Open the Obsidian application.`

In the startup window, click on `"Open folder as vault".` (If Obsidian is already open, click the "Open another vault" icon in the left-hand ribbon).

A file explorer window will appear. Navigate to where the script was run (e.g., your Desktop) and select the newly created CCNA 200-301 folder.

Click `"Open".`

Your new, fully structured CCNA study vault will load, and you are ready to begin.

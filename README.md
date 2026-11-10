# Ai_Lawyer

A legal intake and advisory assistant for Indian jurisdiction. Currently, the system supports two domains only:
1. **Security Deposit Dispute** (tenancy / rental issues)
2. **Unpaid Wages / Salary Issue** (employment / labor disputes)

---

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure your Gemini API key**:
   ```bash
   export GEMINI_API_KEY="your-gemini-api-key"
   ```

---

## How to Chat

Start an interactive chat session:

```bash
python3 chat_cli.py
```

### CLI Options & Commands
- **Start a fresh case**:
  ```bash
  python3 chat_cli.py --new
  ```
- **In-chat commands**:
  - `quit` &mdash; Save case state and exit.
  - `save` &mdash; Save current case state to `case.json`.
  - `status` &mdash; Inspect extracted slots, issue classification, and case state.
  - `explain` &mdash; Run the domain specialist analysis on the current case.
  - `new` &mdash; Reset and begin a new case session.

Once sufficient case facts are collected during intake, the agent will automatically transition and hand off to the domain specialist to generate structured legal options, limitation analysis, evidence gaps, and statutory citations.

---

## Evaluation Results

Pre-computed evaluation runs across 15 test scenarios (`S01.md` – `S15.md`) covering happy paths, multi-intent shifts, limitation expiry, statute applicability, and edge cases are available in [`eval/out/`](eval/out/).

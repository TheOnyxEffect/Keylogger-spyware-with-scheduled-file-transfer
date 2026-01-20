# Keylogger-spyware-with-scheduled-file-transfer

## How to use

> **WARNING — SAFETY & LEGAL NOTICE**
> This repository and the procedures below are intended **only** for controlled, ethical research and teaching. Do **not** run this code on production machines or on systems with real user data. You must have **informed, documented consent** from any human participant, and run all experiments in an **isolated lab environment** (VMs, snapshots, or air-gapped networks). Misuse may be illegal.

### Quick overview of the workflow

1. Launch the logger (simulated or instrumented), which writes captured events into `Transfer_file.txt`.
2. Launch `server_scheduler.py` on the host: this starts the transfer server which will attempt transfers every 10 minutes and delete the local copy after a successful transfer. Default port is **8080** (change as appropriate).
3. Launch `client_scheduler.py` on the receiver: this listens for or retrieves transferred files every 10 minutes.

---

### Files referenced in these steps

* `keylogger.py` — the logger component that writes `Transfer_file.txt`.
* `server_scheduler.py` — runs the server scheduler which attempts transfer every 10 minutes and deletes local logs after successful transfer. Default port: `8080`.
* `client_scheduler.py` — runs the client scheduler that receives transfers every 10 minutes.

---

### Step-by-step (safe commands)

**1) Start the logger**
*Open a terminal in the VM that acts as the data source.*

If you are using the original filename in a controlled lab and have explicit consent:

```bash
# WARNING: run only in isolated lab with consent
python keylogger.py
```

**Behavior:** when the keylogger runs in the test VM, a file named `Transfer_file.txt` will appear and be appended to as events are generated.

---

**2) Start the transfer server scheduler (`server_scheduler.py`)**
*Open a terminal on the same host that will act as the transfer server. Ensure the host is reachable by the receiver in the isolated network.*

```bash
# start the server scheduler which transfers logs every 10 minutes
python server_scheduler.py
```

**Notes & safe defaults**

* Default port is **8080**. To change it, update `config.yaml` or the script’s `PORT` constant and update firewall/ACLs accordingly.

---

**3) Start the receiver client scheduler (`client_scheduler.py`)**
*On the analysis VM (receiver), open a terminal and run:*

```bash
# start the client scheduler to receive or poll for files every 10 minutes
python client_scheduler.py
```

**Behavior**

* The client will either listen on the configured port or periodically poll the secure endpoint and save incoming files to a designated analysis folder.
* Confirm that received files are saved, checksummed if desired, and logged to the audit record.

---

### Verification checklist after a scheduled transfer

1. Confirm server audit log shows a successful transfer entry
2. Confirm receiver saved the transferred file to the designated analysis folder.
3. Confirm `Transfer_file.txt` on the server host has been deleted (or moved to a secure archive) in accordance with your retention policy.
4. Inspect the transfer logs for any errors and keep the VM snapshot ready to revert.

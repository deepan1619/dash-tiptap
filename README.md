**Create Virtual Environment**
```bash
python -m venv env
env/scripts/activate
```

**Install Dependencies**
```bash
pip install -r requirements.txt
npm install --legacy-peer-deps
```


**Build React & Generate Dash Component**:
```bash
npm run build:js

dash-generate-components ./src/lib/components dash_tiptap -p package.json
```

**Run the Demo App**
```bash
python usage.py
```
**Then open:**
```bash
http://127.0.0.1:8050/
```

***Using Docker***
**Build the image**
```bash
docker build -t dash-tiptap .
```
**Run the container**
```bash
docker run -p 8050:8050 dash-tiptap
```

**Visit**
```bash
Check http://127.0.0.1:8050/ for result
```

***
## How It Works

This project connects a React-based editor to Dash using Dash’s component system.
**Architecture Overview**
```bash
The editor is implemented as a React wrapper around Tiptap
A Python class (DashTiptap) defines the component interface
**The editor exposes:**
value → HTML content
mentions → list of mentionable users
**When content changes:**
React calls setProps()
Dash receives the updated HTML
Dash callbacks can react to changes instantly
```
This enables full two-way synchronization between frontend and backend.

## Demo
Attached the result video in the repository
https://github.com/deepan1619/dash-tiptap/blob/chore/demo-video/Dash-tiptap-demo.mp4

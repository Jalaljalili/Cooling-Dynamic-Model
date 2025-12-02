# Data Center Cooling Dynamic Model + PID Controller

This project models and simulates the thermal dynamics of a data-center
cooling system based on an RC thermal model. The project includes:

- RC thermal transfer function
- Step response and Bode plots
- PID response comparison
- Real-time simulation with disturbance and actuator limits
- Closed-loop performance visualization

---

## 📌 Features
✔ RC thermal model  
✔ Transfer function and dynamic analysis  
✔ Bode plots  
✔ PID manual tuning  
✔ Heater power saturation  
✔ Disturbance injection  
✔ Real-time simulation

---

## 🧠 Model Description

The system is modeled as:

\[
G(s) = \frac{1}{Cs + 1/R}
\]

Where:
- `R` = thermal resistance
- `C` = thermal capacitance

The temperature dynamics follow:

\[
\frac{dT}{dt} = \frac{-T + uR + disturbance}{RC}
\]

---

## 🛠 Dependencies

Install using:

```bash
pip install -r requirements.txt
```
## Run
```
python main.py
```

The script will ask for parameters interactively:
* Thermal values
* PID gains
* Disturbance
* Simulation duration

📊 Outputs

* This project demonstrates:
* Step response
* Bode magnitude and phase
* PID-like fast control
* Disturbance rejection
* Closed-loop stability

Example plots:
* System response
* Controlled vs uncontrolled
* Temperature stabilization

🧪 Example Applications
Data center cooling control
IoT temperature systems
Industrial heater control
Smart-building energy efficiency
📚 Academic Value
This project can be used for:
Control systems courses
Signals and Systems modeling
Master’s research projects
Thermal dynamics studies
📌 Future Work
MPC control
Multi-zone thermal networks
Fan/CRAC models
Adaptive gain tuning
Author
Jalal Jalili
Master of Engineering – Dynamic Systems


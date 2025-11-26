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


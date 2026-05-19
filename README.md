# 🕌 PyIslamic Prayer

An open-source, astronomy-based Islamic prayer time calculation engine written in pure Python.

---

## 👨‍💻 Developers

- [Syed Sajid Ul Haq](https://github.com/syedsajidulhaq)  
- [Syed Abid Ul Haq](https://github.com/abidulhaq)  

## 🏢 Organization
**Crescenton**

📧 crescentononline@gmail.com  
🌐 https://cresenton.netlify.app/

---

## ✨ Features

- Accurate prayer times using latitude & longitude  
- Supports all major Sunni madhhab-based Asr calculations  
- Multiple global calculation methods:
  - Muslim World League (MWL)
  - Egyptian General Authority
  - Karachi Method
  - Umm al-Qura  
- Qibla direction calculation using great-circle formula  
- High-latitude adjustment support  
- Fully offline (no internet/API required)  
- Lightweight, fast, and dependency-free  

---

## 📦 Installation

pip install pyislamic-prayer

---

## 🚀 Quick Start

from pyislamic_prayer import PrayerTimes

pt = PrayerTimes(
    latitude=33.6844,
    longitude=73.0479,
    method="MWL"
)

times = pt.get_times()

for prayer, time in times.items():
    print(prayer, ":", time)

---

## 🧭 Qibla Direction

from pyislamic_prayer import qibla_direction

direction = qibla_direction(33.6844, 73.0479)
print("Qibla Direction:", direction, "degrees")

---

## 📖 Calculation Methods

| Method | Description |
|--------|-------------|
| MWL | Muslim World League |
| EGYPT | Egyptian General Authority |
| KARACHI | University of Karachi |
| UMM_AL_QURA | Umm al-Qura University |

---

## 🧮 Example Output

Fajr: 05:12  
Dhuhr: 12:30  
Asr: 15:45  
Maghrib: 18:10  
Isha: 19:25  

---

## 🏗 Project Status

- ✔ Core calculation engine complete  
- ✔ Offline support implemented  
- ✔ Qibla direction feature added  
- 🔄 Continuous improvements in progress  

---

## 📜 License

This project is licensed under the MIT License.

---

## 🌙 About Crescenton

Crescenton is an open innovation hub focused on:

- AI systems  
- Educational tools  
- Islamic tech solutions  
- Software & animation development  

https://cresenton.netlify.app/

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## ⭐ Support

If you like this project, star it on GitHub and share it with others.

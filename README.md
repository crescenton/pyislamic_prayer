# 🕌 PyIslamic Prayer

An open-source, astronomy-based Islamic prayer time calculation engine written in pure Python.

---

## 👨‍💻 Developers

- Syed Sajid Ul Haq ([GitHub](https://github.com/syedsajidulhaq))  
- Syed Abid Ul Haq ([GitHub](https://github.com/syedabidulhaq))  

---

## 🏢 Organization

**Crescenton** ([Official Website](https://cresenton.netlify.app/))

📧 crescentononline@gmail.com  

---

## ✨ Features

- Accurate prayer times using latitude & longitude  
- Supports major Sunni madhhab-based Asr calculations  
- Multiple calculation methods:
  - Muslim World League (MWL)
  - Egyptian General Authority
  - Karachi Method
  - Umm al-Qura  
- Qibla direction calculation using great-circle formula  
- High-latitude adjustment support  
- Fully offline (no internet/API required)  
- Lightweight and dependency-free  

---

## ⚠️ Important Note

v1.0.0 had import issues.  
Use **v1.0.1 or later**.

---

## 📦 Installation

pip install --upgrade pyislamic-prayer

---

## 🚀 Quick Start

from pyislamic_prayer import PrayerTimes, Madhab, KARACHI

lat = 33.6844
lon = 73.0479
tz = 5.5

pt = PrayerTimes(
    lat=lat,
    lon=lon,
    tz=tz,
    madhab=Madhab.HANAFI,
    method=KARACHI
)

times = pt.calculate()

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

## 🏗 Project Status

- ✔ Stable core engine  
- ✔ Offline support  
- ✔ Qibla direction working  
- ✔ PyPI v1.0.1 fixed  

---

## 📜 License

MIT License

---

## 🌙 About Crescenton

Crescenton builds:
- AI systems  
- Educational tools  
- Islamic tech solutions  
- Software & innovation  

https://cresenton.netlify.app/

---

## 🤝 Contributing

Pull requests welcome.  
Open an issue for major changes.

---

## ⭐ Support

Star the repo ⭐ and share it

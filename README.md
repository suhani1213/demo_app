# 🌾 Farm Management App (Frappe)

This is farm management app

A custom Frappe app to manage farms, crops, plantations, and fertilizer schedules.

## ✅ Features

- 👨‍🌾 Farm Master with area, soil type, and irrigation
- 🌱 Crop Master with fertilizer suggestion templates
- 🌾 Plantation Master with automatic fertilizer plan
- 📊 Fertilizer Calculation based on crop × area
- 📅 Fertilizer Application Calendar view

## 🛠 How It Works

- Suggestions are defined per crop (dose, days, fertilizer)
- Quantity = dose × farm area
- Application dates = plantation date + offset days
- A new Fertilizer Application is created for each plan

## 📦 Installation

```bash
bench get-app farm_management https://github.com/suhani1213/farm_management.git
bench --site [your-site-name] install-app farm_management


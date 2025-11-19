# 🌦️ Weather Analysis & Risk Assessment API

### [🇹🇷] Proje Özeti
Bu proje, basit bir hava durumu görüntüleme uygulamasından ziyade; alınan meteorolojik verileri işleyip anlamlandıran bir **RESTful API** servisidir.

Genellikle hava durumu uygulamaları kullanıcıya sadece "20 Derece" der ve geçer. Bu serviste ise Open-Meteo altyapısı kullanılarak sıcaklık, rüzgar hızı ve yağış ihtimali gibi parametreler çekilir. Ardından Backend tarafında kurduğum algoritma bu verileri analiz eder; dışarı çıkmaya uygunluk, risk seviyesi ve giyim tavsiyesi gibi **işlenmiş veri (processed data)** sunar.

**Teknik Detaylar:**
*   **Backend:** Python & Flask
*   **Data Fetching:** Requests kütüphanesi ile Asenkron olmayan HTTP istekleri.
*   **Architecture:** MVC benzeri, ayrıştırılmış business logic yapısı.
*   **Response:** Standartlaştırılmış JSON formatı.

Bu servisi geliştirmekteki amacım, ham veriyi son kullanıcı için anlamlı bir bilgiye (insight) dönüştüren bir yapı kurmaktı.

---

### [🇬🇧] Project Summary
Rather than just building a simple weather display app, I developed a **RESTful API** service that fetches, processes, and analyzes meteorological data to provide actionable insights.

Standard weather apps usually just tell the user "It's 20 Degrees". In this service, utilizing the Open-Meteo infrastructure, parameters like temperature, wind speed, and precipitation are retrieved. Then, a custom algorithm on the backend analyzes this raw data to generate **processed intelligence**, such as suitability for outdoor activities, risk assessment levels, and clothing recommendations.

**Technical Highlights:**
*   **Backend:** Python & Flask framework.
*   **Data Integration:** External API consumption via Python Requests.
*   **Architecture:** Decoupled business logic focusing on clean code standards.
*   **Output:** Standardized JSON responses suitable for frontend consumption.

The main goal of this project was to demonstrate how to transform raw data into meaningful insights through backend logic.

---

### 🚀 How to Run (Kurulum)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

# Inteligentny Kosz na Śmieci

## Opis projektu
Inteligentny kosz na śmieci to projekt, który automatyzuje proces segregacji odpadów i pozwala użytkownikom monitorować decyzje kosza za pomocą platformy internetowej. Wersja prototypowa oferuje podstawowe funkcjonalności, a kolejne iteracje będą wzbogacone o zaawansowane czujniki, analizę danych oraz większe urządzenia przeznaczone dla przestrzeni publicznych.

---

## Funkcjonalności
- **Automatyczna segregacja odpadów**: Urządzenie samodzielnie identyfikuje typ odpadu i klasyfikuje go do odpowiedniego pojemnika.
- **Integracja z platformą internetową**: Użytkownik rejestruje kosz za pomocą unikalnego ID i ma dostęp do raportów o segregacji.
- **Plany rozwojowe**: Dodanie czujników zapełnienia, większe urządzenia dla instytucji publicznych oraz analiza danych dla firm.

---

## Wymagania techniczne
### Sprzęt:
- Moduł ESP32 z kamerą (ESP-Camera).
- Silniki krokowe (do sterowania pojemnikami).
- Podzespoły do budowy prototypu kosza.

### Oprogramowanie:
- Python 3.8+.
- Arduino IDE (dla ESP32).
- Biblioteki Python:
  - `fastapi` (MIT License)
  - `torch` i `torchvision` (BSD 3-Clause License)
  - `pillow` (HPND License)
  - `pymysql` (MIT License)
- Arduino/ESP biblioteki:
  - `WiFi` (LGPL License)
  - `ESP-Camera` (LGPL License)

---

## Instalacja i uruchomienie
1. **Uruchomienie części serwerowej:**
   - Zainstaluj wymagane biblioteki Python:
     ```bash
     pip install fastapi torch torchvision pillow pymysql
     ```
   - Uruchom serwer FastAPI:
     ```bash
     uvicorn main:app --reload
     ```
   -Ustawienie własnego modelu ai do wykrywania roznych materialow(nie dam mojego bo github nie pozwala na tak duze pliki a nie jest on i tak nie omylny i przez brak czasu slabo wyszkolony) nazwac go model.pth

2. **Programowanie ESP32:**
   - Skonfiguruj Arduino IDE z dodatkowymi bibliotekami:
     - Zainstaluj obsługę ESP32 w Arduino IDE.
     - Dodaj biblioteki `WiFi` i `ESP-Camera`.
   - Załaduj kod na urządzenie.

3. **Testowanie prototypu:**
   - Połącz ESP32 z serwerem za pomocą sieci WiFi.
   - Użyj interfejsu WWW do rejestracji kosza i monitorowania danych.

---

## Licencje i wykorzystane zasoby
Projekt korzysta z następujących bibliotek i zasobów:

1. **FastAPI**
   - Licencja: MIT
   - Repozytorium: [https://github.com/tiangolo/fastapi](https://github.com/tiangolo/fastapi)

2. **PyTorch**
   - Licencja: BSD 3-Clause
   - Strona główna: [https://pytorch.org](https://pytorch.org)

3. **Pillow**
   - Licencja: HPND
   - Repozytorium: [https://github.com/python-pillow/Pillow](https://github.com/python-pillow/Pillow)

4. **PyMySQL**
   - Licencja: MIT
   - Repozytorium: [https://github.com/PyMySQL/PyMySQL](https://github.com/PyMySQL/PyMySQL)

5. **ESP-Camera (Arduino/ESP)**
   - Licencja: LGPL
   - Źródło: [https://github.com/espressif/esp32-camera](https://github.com/espressif/esp32-camera)

6. **WiFi (Arduino/ESP)**
   - Licencja: LGPL
   - Dokumentacja: [https://www.arduino.cc/en/Reference/WiFi](https://www.arduino.cc/en/Reference/WiFi)

---

## Uwagi dotyczące licencji
- Projekt korzysta z powyższych bibliotek w ich **oryginalnej, niezmodyfikowanej formie**.  
- Jeśli dystrybuujesz swój projekt, uwzględnij licencje wymienionych bibliotek w dokumentacji.

---

## Autor
Projekt wykonany przez Tomasza Filipczuka.  
Jeśli masz pytania lub sugestie, skontaktuj się: tfilipczuk4@gmail.com.


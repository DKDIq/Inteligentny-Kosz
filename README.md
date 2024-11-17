# Inteligentny Kosz na Śmieci
## NAGRANIE DZIAŁANIA URZADZENIA I WYTLUMACZENIE KODU PROSZE OBEJRZEC PRZED OCENA: 
https://drive.google.com/file/d/1gpm4vOQkSO0xb6vGZbL6EfsVQdOOYmZC/view?usp=sharing

## Opis projektu
NAGRANIE DZIALANIA URZADZENIA(POLECAM OBEJRZEC PRZED OCENA): https://drive.google.com/file/d/1gpm4vOQkSO0xb6vGZbL6EfsVQdOOYmZC/view?usp=sharing
Inteligentny kosz na śmieci to projekt, który automatyzuje proces segregacji odpadów i pozwala użytkownikom monitorować decyzje kosza za pomocą platformy internetowej. Wersja prototypowa oferuje podstawowe funkcjonalności, a kolejne iteracje będą wzbogacone o zaawansowane czujniki, analizę danych oraz większe urządzenia przeznaczone dla przestrzeni publicznych.

---

## Funkcjonalności
- **Automatyczna segregacja odpadów**: Urządzenie samodzielnie identyfikuje typ odpadu i klasyfikuje go do odpowiedniego pojemnika.
- **Integracja z platformą internetową**: Użytkownik rejestruje kosz za pomocą unikalnego ID i ma dostęp do raportów o segregacji.
---

## Wymagania techniczne

### Sprzęt:
- Moduł **ESP32** z kamerą (ESP-Camera).
- Silniki krokowe (do sterowania pojemnikami).
- Podzespoły do budowy prototypu kosza.

### Oprogramowanie:
- **Python 3.8+**
- **Arduino IDE** (dla ESP32).
- Biblioteki Python:
  - `fastapi` 
  - `torch` i `torchvision` 
  - `pillow` 
  - `pymysql` 
- Arduino/ESP biblioteki:
  - `WiFi` 
  - `ESP-Camera` 

---

## Instalacja i uruchomienie

1. **Uruchomienie części serwerowej:**
   - Zainstaluj wymagane biblioteki Python:
     ```bash
     pip install fastapi torch torchvision pillow pymysql uvicorn
     ```
   - Uruchom serwer FastAPI:
     ```bash
     uvicorn main:app --port 890
     ```

2. **Programowanie ESP32:**
   - Skonfiguruj Arduino IDE z dodatkowymi bibliotekami:
     - Zainstaluj obsługę ESP32 w Arduino IDE.
     - Dodaj biblioteki `WiFi` i `ESP-Camera`.
   - Załaduj kod na urządzenie.

3. **Testowanie prototypu:**
   - Ustaw własny model AI do wykrywania różnych materiałów (`model.pth`), moj nie jest idealny jednak w razie potrzeby znajduje sie tu (nie da sie tak duzych plikow na githuba dodac) https://drive.google.com/file/d/1INj60a8Ra7PJqbf4vCdDyUh_yZyUTrlx/view?usp=sharing).
   - Połącz ESP32 z serwerem za pomocą sieci WiFi.
   - Użyj interfejsu WWW do rejestracji kosza i monitorowania danych.

4. **Konfiguracja bazy danych (XAMPP):**
   - W celu przechowywania danych użytkowników i raportów o segregacji, należy skonfigurować bazę danych MySQL za pomocą XAMPP.
   - Skorzystaj z **phpMyAdmin** do stworzenia bazy danych i odpowiednich tabel:
     1. Utwórz bazę danych, np. `kosz`.
     2. Utwórz tabelę dla użytkowników uzywajac:
        ```bash
     CREATE TABLE `kosz`.`uzy` (`id` INT NOT NULL , `nick` TEXT NOT NULL , `haslo` TEXT NOT NULL , `cookie` TEXT NOT NULL , `pl` INT NOT NULL DEFAULT '0' , `szkl` INT NOT NULL DEFAULT '0' , `miesz` INT NOT NULL DEFAULT '0' , `pap` INT NOT NULL DEFAULT '0' , `pl1` INT NOT NULL DEFAULT '0' , `szkl1` INT NOT NULL DEFAULT '0' , `miesz1` INT NOT NULL DEFAULT '0' , `pap1` INT NOT NULL DEFAULT '0' ) ENGINE = InnoDB;
     ```
     3. Dodaj uprawnienia w bazie (jak na nagraniu)

   - Takie rozłożenie powinno sprawić że kod będzie w pełni działać a urządzenie będzie mogło komunikować się ze stroną.

---

## Licencje i wykorzystane zasoby

Projekt korzysta z następujących bibliotek i zasobów:

1. **FastAPI**
   - Licencja: [https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/fastapi_license.txt](https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/fastapi_license.txt)
   - Repozytorium: [https://github.com/tiangolo/fastapi](https://github.com/tiangolo/fastapi)

2. **PyTorch**
   - Licencja: [https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/pytorch_license.txt](https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/pytorch_license.txt)
   - Strona główna: [https://pytorch.org](https://pytorch.org)

3. **Pillow**
   - Licencja: [https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/Pillow_license.txt](https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/Pillow_license.txt)
   - Repozytorium: [https://github.com/python-pillow/Pillow](https://github.com/python-pillow/Pillow)

4. **PyMySQL**
   - Licencja: [https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/PyMySQL_license.txt](https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/PyMySQL_license.txt)
   - Repozytorium: [https://github.com/PyMySQL/PyMySQL](https://github.com/PyMySQL/PyMySQL)

5. **ESP-Camera (Urządzenie)**
   - Licencja: [https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/esp_camera.txt](https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/esp_camera.txt)
   - Źródło: [https://github.com/espressif/esp32-camera](https://github.com/espressif/esp32-camera)

6. **WiFi (Urządzenie)**
   - Licencja: [https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/WIFI(arduino).txt](https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/WIFI(arduino).txt)
   - Dokumentacja: [https://www.arduino.cc/en/Reference/WiFi](https://www.arduino.cc/en/Reference/WiFi)
     
7. **Stepper (Urządzenie)**
   - Licencja: [https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/stepper.txt](https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/stepper.txt)
   - Dokumentacja: [https://github.com/arduino-libraries/Stepper](https://github.com/arduino-libraries/Stepper)
8. **Unvicorn**
   - Licencja: [https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/uvicorn_license.txt](https://github.com/DKDIq/Inteligentny-Kosz/blob/main/licencje_uzytych_zasobow/uvicorn_license.txt)
   - Strona: [https://www.uvicorn.org](https://www.uvicorn.org)

---

## Uwagi dotyczące licencji
- Projekt korzysta z powyższych bibliotek w ich **oryginalnej, niezmodyfikowanej formie**.
- Jeśli dystrybuujesz swój projekt, pamiętaj, aby uwzględnić licencje wymienionych bibliotek w dokumentacji.

---

## Autor
Projekt wykonany przez Tomasza Filipczuka.  
Jeśli masz pytania lub sugestie, skontaktuj się: tfilipczuk4@gmail.com.

---

### Dodatkowe informacje
- Wszelkie pytania dotyczące instalacji i konfiguracji projektu proszę kierować na powyższy adres email.
---

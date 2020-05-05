# Abstract anticafe
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This project is a web service for booking tables in public places: anti cafes, coworkings, cafes, restaurants, hookah houses, etc.

The style of web service is minimalism.
No garbage content like rating system, useless buttons "Share" (who uses them at all), comments from inadequate people, buttons "start a chat with the manager"...
In short, only booking tables and nothing else.

Registration is available, so you can follow your bookings from your personal cabinet.
You can also delete your bookings)
***
## _Core_ app
This application contains most of the server logic. Main page rendering: home page, registration page, login page, detailed information about the table, table order page, page with a list of all bookings and ect. 

<details><summary><b>Main Page</b></summary>
  <img src="https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/homePage.png">
</details>

<details><summary><b>Main Page (Mobile)</b></summary>
  <img src="https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/homePageMobile.png">
</details>

<details><summary><b>Page for booking</b></summary>
  <img src="https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/booking.png">
</details>

<details><summary><b>Registration with recaptcha (yeah, I know how to recaptcha, yo)</b></summary>  <img src="https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/register.png">
</details>

<details><summary><b>Page with bookings</b></summary> <img src="https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/bookings.png">
</details>

<details><summary><b>Successful deleting</b></summary>
  <img src="https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/succesfullDeleting.png">
</details>

## SQL scheme for _Core_
![core_sql scheme](https://github.com/arxitim/abstract_anticafe/blob/master/documentation/sql_scheme/core_scheme.png)

***
## _Staff_ app
He comes to the place, shows qr-code to the employee with the rights **is_staff**, he follows the link in qr and the reservation is considered confirmed, and the table occupied **is_busy** = True.

<details><summary><b>Сlient Qr-code</b></summary>
  <img src="https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/clientQR.png">
</details>

<details><summary><b>What happens if an employee clicks on the link</b></summary>
  <img src="https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/employeeConfirmed.png">
</details>

***

## API
Small API mainly for working with ajax
***

## Redis + Celery
Used to clear a queue of orders that are no longer relevant.
Also emulates the visit of random people so that the status of the table changes to busy (table.is_busy = True). 
***



## Deploy
Deploy is made by *nginx+gunicorn* and <a href="https://certbot.eff.org/">Certbot</a> for HTTPS.
I was in charge of the configuration of the server myself, and since I don't know much about security issues, it can be dangerous :3
#### Working site <a href="abstractanticafe.xyz">abstractanticafe.xyz</a>
***

### Special thanks to <a href="https://github.com/mitchtabian">@mitchtabian</a> for his Youtube lectures about Django.
***

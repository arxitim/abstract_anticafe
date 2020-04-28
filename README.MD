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
### Main Page
![home page](https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/homePage.png)

### Main Page (Mobile)
![home page mobile](https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/homePageMobile.png)

### Page for booking
![booking page](https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/Booking.png)

### Registration with recaptcha (yeah, I know how to recaptcha, yo)
![registration](https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/register.png)

### Page with bookings
![bookings](https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/bookings.png)

#### Successful deleting
![succesfull deleting](https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/SuccesfullDeleting.png)

***
## _Staff_ app
He comes to the place, shows qr-code to the employee with the rights **is_staff**, he follows the link in qr and the reservation is considered confirmed, and the table occupied **is_busy** = True.

### Сlient Qr-code
![clientQR](https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/clientQR.png)

### What happens if an employee clicks on the link
![confirm_booking](https://github.com/arxitim/abstract_anticafe/blob/master/documentation/screenshots/employeeConfirmed.png)

***

## API
Small API mainly for working with ajax
***

## Redis + Celery
Used to clear a queue of orders that are no longer relevant.
Also soon will be added emulation of users who order something on the service. I hope so.
***

## SQL scheme for _Core_
![core_sql scheme](https://github.com/arxitim/abstract_anticafe/blob/master/documentation/sql_scheme/core_scheme.png)

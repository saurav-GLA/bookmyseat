Internship Project (NullClass)

Name: Saurav Kumar Rai  
Duration: 21 June 2025 – 21 July 2025  
Internship Provider: NullClass

Project Overview

This web application is a Django-based movie ticket booking platform. As part of my internship with NullClass, I implemented three advanced features to enhance the functionality and user experience of the site:

1. Movie Pagination
2. User Profile with Booking History
3. Dynamic Pricing Based on Demand

These additions were made on top of the existing project and fully integrated into the system.

Features Implemented

1. Pagination for Movies

What I did:
- Integrated Django’s `Paginator` class in the movie listing view.
- Displayed 3 movies per page with "Next" and "Previous" navigation buttons.
- Handled edge cases like empty pages or invalid page numbers.
- Bootstrap cards for responsive layout

2. User Profile with Booking History

What I did:
- Created a separate user profile page that only logged-in users can access.
- Displayed past and upcoming bookings.
- Highlighted show timings and seat information clearly.
- Ensured security access to only the logged-in user's bookings.
- Django authentication system (`@login_required`) and also alredy used by sir in null class tutorials


3. Dynamic Pricing Based on Demand

What I did:
- Implemented a pricing algorithm that increases the ticket price based on:
  - Percentage of seats already booked
  - Time left until the show
- Adjusted prices dynamically on the frontend and backend.

Base price increased by 10–30% if:
- based on the days if less then 7 days left then discount if less than 2day left then more discount and iff more than 1 week left no discount
- based on seats left if less than half the seats are booked no price increase if more thna half is booked than 120% price if more than 80% is booked than 150% price you see how it's balanced wiht days
- Python logic in the view layer
- Real-time pricing in movie detail and booking confirmation
- also added cancellation feature for upcoming bookings as you know past bookings cannot be cancelled



frontend and backend used:
Backend      Django          
Frontend     HTML, CSS, Bootstrap 
Database     SQLite (local, for testing), PostgreSQL (production)
Hosting      Railway, because vercel woudn't show admin panel ui even after adding while noise


- All pages are fully responsive


Live Project

Hosted URL: https://web-production-2c86.up.railway.app





Project Setup if wanna check

git clone https://github.com/saurav-GLA/bookmyseat.git
cd bookmyseat
pip install -r requirements.txt
python manage.py migrate
python manage.py runs

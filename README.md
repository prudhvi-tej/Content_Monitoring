# Content Monitoring System

## Features
- Add keywords
- Scan content
- Generate flags with scores
- Review workflow (pending/relevant/irrelevant)
- Suppression logic implemented

## How to run
pip install django djangorestframework
python manage.py migrate
python manage.py runserver

## API
POST /keywords/
POST /scan/
GET /flags/
PATCH /flags/{id}/

## Assumptions
- Used mock data
- Basic keyword matching logic
- Suppression based on last_updated

## Key Highlight
Suppression logic ensures irrelevant flags do not reappear unless content changes.

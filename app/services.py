from .models import *

def calculate_score(keyword, content):
    k = keyword.name.lower()
    title = content.title.lower()
    body = content.body.lower()
    if k in title:
        if k == title:
            return 100
        return 70
    elif k in body:
        return 40
    return 0

def should_show(existing_flag, content):
    if existing_flag and existing_flag.status == 'irrelevant':
        if content.last_updated <= existing_flag.reviewed_at:
            return False
    return True

def run_scan():
    mock_data = [
        {
            "title": "Learn Django Fast",
            "body": "Django is a powerful Python framework",
            "source": "Blog A",
            "last_updated": "2026-03-20T10:00:00Z"
        }
    ]

    keywords = Keyword.objects.all()
    for item in mock_data:
        content, _ = ContentItem.objects.get_or_create(
            title=item['title'],
            defaults=item
        )

        for keyword in keywords:
            score = calculate_score(keyword, content)

            if score > 0:
                existing = Flag.objects.filter(
                    keyword=keyword,
                    content_item=content
                ).first()

                if not should_show(existing, content):
                    continue

                Flag.objects.update_or_create(
                    keyword=keyword,
                    content_item=content,
                    defaults={'score': score}
                )


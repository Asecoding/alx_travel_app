from celery import shared_task

@shared_task
def send_booking_confirmation(email):
    print(f"Sending confirmation to {email}")
    return True

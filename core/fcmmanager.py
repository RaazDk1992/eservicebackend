
from firebase_admin import initialize_app
from firebase_admin.messaging import Message, Notification
from firebase_admin import credentials
from fcm_django.models import FCMDevice

cred = credentials.Certificate('core\eservicenotifications-78b8b-firebase-adminsdk-rrw9j-77d8d2c519.json')
FIREBASE_APP = initialize_app(cred)

def sendPush():

    m = Message(
    notification=Notification(title="title", body="text", image="url"),
    )
    
    devices =  FCMDevice.objects.all()
    r = devices.send_message(m)

    print(r.response._responses)
    return r.response

    pass


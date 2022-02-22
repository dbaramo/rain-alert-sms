# rain-alert-sms

Python script that checks for rain or snow in the next twelve hours based on a specific longitude and latitude. If true a text message will be sent to remind you to bring your umbrella via [twillio's programmable SMS api](https://www.twilio.com/docs/sms/quickstart/python).

Weather api docs
https://openweathermap.org/api/one-call-api

You can host this on https://www.pythonanywhere.com/ and schedule it to run every morning or run it on your own server and run a cron job to schedule the script.

### Environment Variables needed for script:

**OWM_API_KEY**
<br />
**TWILIO_ACCOUNT_SID**
<br />
**TWILIO_AUTH_TOKEN**
<br />
**TWILIO_PHONE_NUMBER**
<br />
**PHONE_NUMBER_TO_RECEIVE**

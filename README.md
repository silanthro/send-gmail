# send-gmail

A tool for sending simple plaintext emails via Gmail.

This requires the following environment variables:

- `GMAIL_ADDRESS`: The Gmail address used to send the email.
- `GMAIL_PASSWORD`: This is **NOT** your regular Gmail password, but a 16-character App Password created via https://myaccount.google.com/apppasswords (see below). **Treat this like you would treat your regular password e.g. do not upload this in plaintext or share this publicly**

The following environment variable is optional:

- `GMAIL_DISPLAY_NAME`: Set the display name shown in the email header (using [`email.utils.formataddr`](https://docs.python.org/3/library/email.utils.html#email.utils.formataddr)). This helps make emails more recognizable and professional. Supports Unicode.

## Set up the password

The password used here is a 16-character App Password that can be generated via your Google Account settings. In the event that the App Password is no longer required, it can be revoked without affecting your regular password.

**In order to create a 16-character App Password, 2-Step Verification must be set up.**

See the Gmail Help article at https://support.google.com/mail/answer/185833?hl=en for detailed instructions.

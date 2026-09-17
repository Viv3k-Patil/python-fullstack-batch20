import random
from functools import wraps

from class_activity.vivek.projects.phase7_full_project.exceptions import InvalidOTPError


class OTPService:
    def __init__(self):
        self._pending_otps = {}  # phone -> otp code

    def generate_otp(self, phone) -> str:
        otp = str(random.randint(100000, 999999))
        self._pending_otps[phone] = otp
        # In a real system: send via Gmail SMTP or an SMS gateway here
        print(f"📩 [SIMULATED SMS to {phone}] Your OTP is: {otp}")
        return otp

    def verify_otp(self, phone, entered_otp) -> bool:
        actual_otp = self._pending_otps.get(phone)
        if actual_otp is not None and actual_otp == entered_otp:
            del self._pending_otps[phone]  # OTP used only once
            return True
        return False


def requires_otp(threshold=10000):
    """
    Decorator factory implementing 'step-up authentication':
    functions wrapped with this require OTP verification if amount > threshold.

    Wrapped function signature must be: func(account, amount, *args, **kwargs)
    Caller must supply otp_service, phone, and entered_otp as keyword args.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(account, amount, otp_service, phone, entered_otp=None, *args, **kwargs):
            if amount > threshold:
                if entered_otp is None:
                    raise InvalidOTPError("OTP required for this amount, but none was provided")
                if not otp_service.verify_otp(phone, entered_otp):
                    raise InvalidOTPError("OTP verification failed")
            return func(account, amount, *args, **kwargs)

        return wrapper

    return decorator

from .main import Contiguity, Verify, EmailAnalytics, Quota, OTP, Template, Send


def login(token, debug=False, beta=False):
    return Contiguity(token, debug, beta)


__all__ = ["Contiguity", "Send", "Verify", "EmailAnalytics", "Quota", "OTP", "Template"]

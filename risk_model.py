def assess_risk_profile(age, income, risk_response):
    if age < 30 and "Love" in risk_response:
        return "Aggressive"
    elif 30 <= age <= 50 and "Sometimes" in risk_response:
        return "Moderate"
    else:
        return "Conservative"

def recommend_investments(profile):
    suggestions = {
        "Aggressive": "- 60% Equity\n- 20% Crypto/Tech\n- 20% Bonds",
        "Moderate": "- 40% Equity\n- 40% Balanced Funds\n- 20% FDs",
        "Conservative": "- 60% Fixed Deposits\n- 30% Bonds\n- 10% Gold"
    }
    return suggestions.get(profile, "Talk to your financial advisor.")

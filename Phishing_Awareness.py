import streamlit as st

st.set_page_config(page_title="Phishing Awareness Training", layout="wide")

st.title("🔐 Phishing Awareness Training Module")

st.write("""
This training module helps you understand phishing attacks, how to recognize them,
and how to stay safe online.
""")

# Sidebar navigation
menu = st.sidebar.selectbox(
    "Select Section",
    ["Introduction", "Recognizing Phishing Emails", "Social Engineering", "Best Practices", "Real World Examples", "Quiz"]
)

# Introduction
if menu == "Introduction":
    st.header("What is Phishing?")
    st.write("""
Phishing is a cyberattack where attackers try to trick users into revealing
sensitive information such as passwords, bank details, or personal data.

Attackers usually use:
- Fake emails
- Fraudulent websites
- Messages pretending to be from trusted organizations
""")

    st.image("https://cdn-icons-png.flaticon.com/512/565/565547.png", width=200)

# Recognizing phishing
elif menu == "Recognizing Phishing Emails":
    st.header("How to Recognize Phishing Emails")

    st.write("Common warning signs:")

    st.markdown("""
- Suspicious sender email address  
- Urgent messages like *"Your account will be locked"*  
- Links that look unusual  
- Poor grammar and spelling mistakes  
- Unexpected attachments  
    """)

    st.subheader("Example")

    st.code("""
From: support@paypaI.com
Subject: Urgent Account Verification

Dear user,
Your account will be suspended unless you verify immediately.
Click here: http://paypaI-security-check.com
""")

    st.warning("Notice the fake domain name!")

# Social Engineering
elif menu == "Social Engineering":
    st.header("Social Engineering Tactics")

    st.write("""
Social engineering is when attackers manipulate people into giving confidential
information.
""")

    st.markdown("""
Common tactics:

1. **Urgency** – "Your account will be closed today!"
2. **Authority** – Pretending to be a bank or IT admin
3. **Fear** – Threatening account suspension
4. **Curiosity** – Fake rewards or offers
5. **Trust** – Pretending to be a colleague or friend
    """)

# Best Practices
elif menu == "Best Practices":
    st.header("Best Practices to Avoid Phishing")

    st.markdown("""
✔ Always verify sender email addresses  
✔ Never click suspicious links  
✔ Enable Two-Factor Authentication  
✔ Use updated antivirus software  
✔ Do not download unknown attachments  
✔ Report suspicious emails to IT/security team
    """)

# Real world examples
elif menu == "Real World Examples":
    st.header("Real World Phishing Examples")

    st.write("Example 1: Fake Bank Email")

    st.code("""
Subject: Bank Security Alert

Dear Customer,
We detected unusual activity on your account.
Please login immediately to secure your account.

Click here:
http://bank-security-check.com
""")

    st.write("Example 2: Fake Prize Email")

    st.code("""
Subject: Congratulations! You won $5000

Click the link below to claim your reward immediately.
""")

    st.error("If it sounds too good to be true, it probably is!")

# Quiz
elif menu == "Quiz":
    st.header("Phishing Awareness Quiz")

    score = 0

    q1 = st.radio(
        "1. Which is a common sign of a phishing email?",
        ["Professional company logo", "Urgent request for personal information", "Official website link"]
    )

    if q1 == "Urgent request for personal information":
        score += 1

    q2 = st.radio(
        "2. What should you do if you receive a suspicious email?",
        ["Click the link", "Ignore security warnings", "Report it to IT/security team"]
    )

    if q2 == "Report it to IT/security team":
        score += 1

    q3 = st.radio(
        "3. Phishing attacks mainly try to steal:",
        ["Personal and login information", "Computer hardware", "Internet speed"]
    )

    if q3 == "Personal and login information":
        score += 1

    if st.button("Submit Quiz"):
        st.success(f"Your Score: {score}/3")

        if score == 3:
            st.balloons()
            st.write("Excellent! You understand phishing risks.")
        elif score == 2:
            st.write("Good! But stay alert.")
        else:
            st.write("Please review the training again.")
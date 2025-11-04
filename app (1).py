
import streamlit as st

# Hardcoded user credentials
USER_CREDENTIALS = {
    "tech_user_01": "password123",
    "installer_02": "secure456",
    "admin": "adminpass"
}

# Title and login section
st.set_page_config(page_title="Troubleshooting Assistant", layout="centered")
st.title("Troubleshooting Assistant")

st.subheader("User Login")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Authentication check
if username and password:
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        st.success(f"Logged in as {username}")

        # Package info
        st.subheader("Package Information")
        package_id = st.text_input("Package ID or Serial Number")

        # Client info
        st.subheader("Client Information")
        first_name = st.text_input("Client First Name")
        last_name = st.text_input("Client Last Name")
        contact_email = st.text_input("Email")
        contact_phone = st.text_input("Phone Number")

        is_tech = st.checkbox("Are you a technician/installer?")
        install_company = ""
        if is_tech:
            install_company = st.text_input("Installation Company Name")

        # Troubleshooting flow selector
        st.subheader("Select Troubleshooting Flow")
        flow = st.selectbox("Choose a guide", [
            "AMP Software Update",
            "Card Reader Troubleshooting",
            "Export Logs from AMP",
            "M4000 BIOS Replacement",
            "Solid State Relay Installation"
        ])

        # Step logger
        st.subheader("Steps Taken")
        steps_taken = []
        flow_steps = {
            "AMP Software Update": [
                "Login to AMP360", "Verify template", "Delete terminal",
                "Add terminal", "Uninstall apps", "Reset cache", "Reinstall apps"
            ],
            "Card Reader Troubleshooting": [
                "Clean reader", "Check logs", "Review declines",
                "Test in Magtek Utility", "Check Siteminder cards",
                "Try different USB", "Verify Phillips config"
            ],
            "Export Logs from AMP": [
                "Insert USB", "Set USB mode to Host", "Open Log Manager",
                "Enter password", "Submit to copy logs",
                "Wait before dismounting", "Copy logs to PC"
            ],
            "M4000 BIOS Replacement": [
                "Power down terminal", "Take wire photos", "Replace CPU",
                "Reconnect wires", "Insert BIOS stick", "Disconnect hard drive",
                "Power on terminal", "Follow instructions",
                "Remove BIOS stick", "Reconnect hard drive"
            ],
            "Solid State Relay Installation": [
                "Mount SSR on DIN rail", "Ensure spacing", "Use correct torque",
                "Format USB to FAT32", "Use proper wire sizes",
                "Follow derating curves", "Observe polarity"
            ]
        }

        for step in flow_steps[flow]:
            if st.checkbox(step):
                steps_taken.append(step)

        # Generate SNOW note
        if st.button("Generate SNOW Note"):
            if not first_name or not last_name or (not contact_email and not contact_phone):
                st.error("Client name and either email or phone are required.")
            else:
                note = f"Troubleshooting Summary:
"
                note += f"User: {username}
Package: {package_id}
"
                note += f"Client: {first_name} {last_name}
"
                if contact_email:
                    note += f"Email: {contact_email}
"
                if contact_phone:
                    note += f"Phone: {contact_phone}
"
                if is_tech and install_company:
                    note += f"Installer: {install_company}
"
                note += "Steps Taken:
"
                for step in steps_taken:
                    note += f"- {step}
"
                note += "Next Steps: Monitor system and verify resolution."
                st.text_area("Generated SNOW Note", value=note, height=300)
                st.button("Copy to Clipboard")
    else:
        st.error("Invalid username or password.")
else:
    st.warning("Please log in to continue.")

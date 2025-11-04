
import streamlit as st

# Hardcoded user credentials
USER_CREDENTIALS = {
    "tech_user_01": "password123",
    "installer_02": "secure456",
    "admin": "adminpass"
}

# Title and login section
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
        if flow == "AMP Software Update":
            if st.checkbox("Login to AMP360"): steps_taken.append("Login to AMP360")
            if st.checkbox("Verify template"): steps_taken.append("Verify template")
            if st.checkbox("Delete terminal"): steps_taken.append("Delete terminal")
            if st.checkbox("Add terminal"): steps_taken.append("Add terminal")
            if st.checkbox("Uninstall apps"): steps_taken.append("Uninstall apps")
            if st.checkbox("Reset cache"): steps_taken.append("Reset cache")
            if st.checkbox("Reinstall apps"): steps_taken.append("Reinstall apps")
        elif flow == "Card Reader Troubleshooting":
            if st.checkbox("Clean reader"): steps_taken.append("Clean reader")
            if st.checkbox("Check logs"): steps_taken.append("Check logs")
            if st.checkbox("Review declines"): steps_taken.append("Review declines")
            if st.checkbox("Test in Magtek Utility"): steps_taken.append("Test in Magtek Utility")
            if st.checkbox("Check Siteminder cards"): steps_taken.append("Check Siteminder cards")
            if st.checkbox("Try different USB"): steps_taken.append("Try different USB")
            if st.checkbox("Verify Phillips config"): steps_taken.append("Verify Phillips config")
        elif flow == "Export Logs from AMP":
            if st.checkbox("Insert USB"): steps_taken.append("Insert USB")
            if st.checkbox("Set USB mode to Host"): steps_taken.append("Set USB mode to Host")
            if st.checkbox("Open Log Manager"): steps_taken.append("Open Log Manager")
            if st.checkbox("Enter password"): steps_taken.append("Enter password")
            if st.checkbox("Submit to copy logs"): steps_taken.append("Submit to copy logs")
            if st.checkbox("Wait before dismounting"): steps_taken.append("Wait before dismounting")
            if st.checkbox("Copy logs to PC"): steps_taken.append("Copy logs to PC")
        elif flow == "M4000 BIOS Replacement":
            if st.checkbox("Power down terminal"): steps_taken.append("Power down terminal")
            if st.checkbox("Take wire photos"): steps_taken.append("Take wire photos")
            if st.checkbox("Replace CPU"): steps_taken.append("Replace CPU")
            if st.checkbox("Reconnect wires"): steps_taken.append("Reconnect wires")
            if st.checkbox("Insert BIOS stick"): steps_taken.append("Insert BIOS stick")
            if st.checkbox("Disconnect hard drive"): steps_taken.append("Disconnect hard drive")
            if st.checkbox("Power on terminal"): steps_taken.append("Power on terminal")
            if st.checkbox("Follow instructions"): steps_taken.append("Follow instructions")
            if st.checkbox("Remove BIOS stick"): steps_taken.append("Remove BIOS stick")
            if st.checkbox("Reconnect hard drive"): steps_taken.append("Reconnect hard drive")
        elif flow == "Solid State Relay Installation":
            if st.checkbox("Mount SSR on DIN rail"): steps_taken.append("Mount SSR on DIN rail")
            if st.checkbox("Ensure spacing"): steps_taken.append("Ensure spacing")
            if st.checkbox("Use correct torque"): steps_taken.append("Use correct torque")
            if st.checkbox("Format USB to FAT32"): steps_taken.append("Format USB to FAT32")
            if st.checkbox("Use proper wire sizes"): steps_taken.append("Use proper wire sizes")
            if st.checkbox("Follow derating curves"): steps_taken.append("Follow derating curves")
            if st.checkbox("Observe polarity"): steps_taken.append("Observe polarity")

        # Generate SNOW note
        if st.button("Generate SNOW Note"):
            if not first_name or not last_name or (not contact_email and not contact_phone):
                st.error("Client name and either email or phone are required.")
            else:
                note = (
                    f"Troubleshooting Summary:
"
                    f"User: {username}
Package: {package_id}
"
                    f"Client: {first_name} {last_name}
"
                    f"Email: {contact_email}
" if contact_email else ""
                    f"Phone: {contact_phone}
" if contact_phone else ""
                    f"Installer: {install_company}
" if is_tech and install_company else ""
                    f"Steps Taken:
" + "
".join([f"- {step}" for step in steps_taken]) +
                    "
Next Steps: Monitor system and verify resolution."
                )
                st.text_area("Generated SNOW Note", value=note, height=300)
                st.button("Copy to Clipboard")
    else:
        st.error("Invalid username or password.")
else:
    st.warning("Please log in to continue.")

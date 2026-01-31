import streamlit as st

# -------------------------------
# Page Title
# -------------------------------
st.title("Iron Lady – Internal Candidate Management")
st.write("Internal tool to manage women candidates")

# -------------------------------
# Initialize storage
# -------------------------------
if "candidates" not in st.session_state:
    st.session_state.candidates = []

# -------------------------------
# Add New Candidate (CREATE)
# -------------------------------
st.subheader("Add New Candidate")

name = st.text_input("Candidate Name")
email = st.text_input("Email")

program = st.selectbox(
    "Program",
    ["Career Restart", "Tech Upskilling", "Confidence Building"]
)

status = st.selectbox(
    "Status",
    ["Applied", "In Progress", "Completed", "Placed"]
)

if st.button("Add Candidate"):
    if name and email:
        st.session_state.candidates.append({
            "name": name,
            "email": email,
            "program": program,
            "status": status
        })
        st.success("Candidate added successfully")
    else:
        st.error("Please fill all fields")

# -------------------------------
# View Candidates (READ)
# -------------------------------
st.subheader("Candidate Records")

if len(st.session_state.candidates) == 0:
    st.info("No candidates added yet")
else:
    for i, candidate in enumerate(st.session_state.candidates):

        st.markdown("---")
        st.write(f"**Name:** {candidate['name']}")
        st.write(f"**Email:** {candidate['email']}")
        st.write(f"**Program:** {candidate['program']}")

        # -------------------------------
        # Update Candidate (UPDATE)
        # -------------------------------
        new_status = st.selectbox(
            "Update Status",
            ["Applied", "In Progress", "Completed", "Placed"],
            index=["Applied", "In Progress", "Completed", "Placed"].index(candidate["status"]),
            key=f"status_{i}"
        )

        if new_status != candidate["status"]:
            st.session_state.candidates[i]["status"] = new_status
            st.success("Status updated")

        # -------------------------------
        # Delete Candidate (DELETE)
        # -------------------------------
        if st.button("Delete Candidate", key=f"delete_{i}"):
            st.session_state.candidates.pop(i)
            st.warning("Candidate deleted")
            st.experimental_rerun()

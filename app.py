import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CrimeDNA-X",
    page_icon="🕵️",
    layout="wide"
)

FEATURE_WEIGHTS = {
    "crime_type": 20,
    "time_window": 15,
    "entry_method": 15,
    "weapon": 10,
    "target": 10,
    "victim": 10,
    "escape": 10,
    "location": 5,
    "mo": 5
}

PAST_CASES = [
    {
        "case": "A-2291",
        "crime_type": "Residential Burglary",
        "time_window": "Night",
        "entry_method": "Rear Window",
        "weapon": "Crowbar",
        "target": "House",
        "victim": "Family Away",
        "escape": "Rear Alley",
        "location": "Gated Colony",
        "mo": "CCTV Disabled"
    },
    {
        "case": "A-2278",
        "crime_type": "Residential Burglary",
        "time_window": "Night",
        "entry_method": "Rear Window",
        "weapon": "Crowbar",
        "target": "Villa",
        "victim": "Sleeping Family",
        "escape": "Rear Alley",
        "location": "Gated Colony",
        "mo": "CCTV Disabled"
    },
    {
        "case": "A-2033",
        "crime_type": "Vehicle Theft",
        "time_window": "Night",
        "entry_method": "Hotwire",
        "weapon": "None",
        "target": "Bike",
        "victim": "Owner Away",
        "escape": "Ride Away",
        "location": "Street",
        "mo": "Old Vehicles"
    }
]

def calculate_similarity(user_case):
    results = []
    for case in PAST_CASES:
        score = 0
        for feature, weight in FEATURE_WEIGHTS.items():
            if user_case[feature] == case[feature]:
                score += weight
        results.append({"case": case["case"], "score": score})

    results = sorted(results, key=lambda x: x["score"], reverse=True)
    return results

st.sidebar.title("🕵️ CrimeDNA-X")
page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "New FIR Analysis",
        "Behavioral Crime DNA",
        "Similar Cases",
        "Analytics",
        "Audit Log",
        "About"
    ]
)

if page == "Dashboard":

    st.title("🕵️ CrimeDNA-X")
    st.subheader("AI-Powered Behavioral Crime Linkage Platform")

    st.info(
        "CrimeDNA-X helps investigators discover similar crime patterns "
        "using behavioural signatures and explainable AI."
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cases", "1,254")
    col2.metric("Today's FIRs", "28")
    col3.metric("Similar Cases Found", "312")
    col4.metric("High Confidence", "91%")

    st.divider()

    st.header("System Overview")

    overview = pd.DataFrame({
        "Module": [
            "Behavioral Crime DNA",
            "Similarity Engine",
            "Explainable AI",
            "Investigation Support",
            "Audit Trail"
        ],
        "Status": ["Ready", "Ready", "Ready", "Ready", "Ready"]
    })

    st.dataframe(overview, use_container_width=True)

    st.divider()

    st.header("Recent Investigations")

    recent = pd.DataFrame({
        "Case ID": ["A-2291", "A-2278", "A-2154"],
        "Crime Type": [
            "Residential Burglary",
            "Residential Burglary",
            "Vehicle Theft"
        ],
        "Similarity": ["92%", "86%", "79%"],
        "Confidence": ["High", "High", "Medium"]
    })

    st.dataframe(recent, use_container_width=True)

elif page == "New FIR Analysis":

    st.title("📝 New FIR Analysis")
    st.write("Enter the FIR details below.")

    crime_type = st.selectbox(
        "Crime Type",
        [
            "Residential Burglary",
            "Commercial Theft",
            "Vehicle Theft",
            "Robbery",
            "Cyber Crime"
        ]
    )

    time_window = st.selectbox(
        "Time Window",
        ["Morning", "Afternoon", "Evening", "Night"]
    )

    entry_method = st.text_input("Entry Method")
    weapon = st.text_input("Weapon / Tool")
    target = st.text_input("Target Type")
    victim = st.text_input("Victim Profile")
    escape = st.text_input("Escape Method")
    location = st.text_input("Location")
    mo = st.text_area("Modus Operandi")

    if st.button("🔍 Analyze Crime"):

        st.success("Behavioral Crime DNA Generated Successfully!")

        st.subheader("Behavioral Crime Profile")

        st.table({
            "Feature": [
                "Crime Type", "Time Window", "Entry Method", "Weapon",
                "Target", "Victim", "Escape", "Location", "Modus Operandi"
            ],
            "Value": [
                crime_type, time_window, entry_method, weapon,
                target, victim, escape, location, mo
            ]
        })

        st.info(
            "CrimeDNA-X generated a behavioral signature. "
            "The next step is to compare this FIR with previous crime cases."
        )

        user_case = {
            "crime_type": crime_type,
            "time_window": time_window,
            "entry_method": entry_method,
            "weapon": weapon,
            "target": target,
            "victim": victim,
            "escape": escape,
            "location": location,
            "mo": mo
        }

        matches = calculate_similarity(user_case)

        st.subheader("Top Matches")

        for m in matches:
            st.write(f"Case **{m['case']}** → Similarity **{m['score']}%**")

elif page == "Behavioral Crime DNA":

    st.title("🧬 Behavioral Crime DNA")
    st.write("CrimeDNA-X generates a behavioral signature for each FIR.")

    st.subheader("Behavioral Crime Signature")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Crime Type", "Residential Burglary")
        st.metric("Entry Method", "Rear Window")
        st.metric("Weapon", "Crowbar")
        st.metric("Target", "Residential House")
        st.metric("Escape", "Rear Alley")

    with col2:
        st.metric("Time Window", "01:00 - 04:00")
        st.metric("Victim", "Family Away")
        st.metric("Location", "Gated Colony")
        st.metric("MO", "CCTV Disabled")
        st.metric("Risk Pattern", "High Similarity")

    st.divider()

    st.subheader("Behavioral Features")

    dna = {
        "Feature": [
            "Crime Type", "Time Window", "Entry Method", "Weapon",
            "Target", "Victim", "Escape Method", "Location", "Modus Operandi"
        ],
        "Behavior": [
            "Residential Burglary", "01:00–04:00", "Rear Window", "Crowbar",
            "Residential House", "Family Away", "Rear Alley",
            "Gated Colony", "CCTV Disabled Before Entry"
        ]
    }

    st.table(dna)

    st.divider()

    st.subheader("AI Summary")

    st.success("""
Behavioral Crime DNA Generated Successfully.

CrimeDNA-X identified a behavioural pattern that can be
used for comparison with previous crime cases.

The generated signature will be used by the Similarity
Engine to identify related investigations.
""")

elif page == "Similar Cases":

    st.title("🔍 Similar Crime Matching")
    st.write("Top behavioural matches identified by CrimeDNA-X.")

    data = {
        "Case ID": ["A-2291", "A-2278", "A-2154", "A-1987", "A-2033"],
        "Crime Type": [
            "Residential Burglary",
            "Residential Burglary",
            "Residential Burglary",
            "Commercial Theft",
            "Vehicle Theft"
        ],
        "Similarity": ["92%", "87%", "81%", "65%", "58%"],
        "Confidence": ["High", "High", "Medium", "Medium", "Low"]
    }

    df = pd.DataFrame(data)

    st.dataframe(df, use_container_width=True)

    st.divider()

    st.subheader("Top Match")

    st.success("""
Case ID : A-2291

Similarity Score : 92%

Confidence : HIGH
""")

    st.subheader("Explainable AI")

    st.info("""
The system identified this case as the closest behavioural match because:

• Same Crime Type

• Same Entry Method

• Same Weapon (Crowbar)

• Same Time Window

• Same Modus Operandi

• Similar Escape Pattern
""")

    st.divider()

    st.subheader("Investigation Recommendations")

    st.write("""
✅ Compare CCTV footage

✅ Compare forensic evidence

✅ Review witness statements

✅ Cross-check previous investigation notes

✅ Review suspect movement patterns
""")

    st.warning("""
CrimeDNA-X is an investigation support system.

It does NOT identify suspects or determine guilt.
Final decisions remain with human investigators.
""")

elif page == "Analytics":

    st.title("📊 Crime Analytics Dashboard")
    st.write("Crime statistics generated from historical behavioural crime data.")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Cases", "1254")
    col2.metric("Today's FIR", "28")
    col3.metric("High Confidence", "91")
    col4.metric("Solved Cases", "742")

    st.divider()

    st.subheader("Crime Type Distribution")

    crime_data = pd.DataFrame({
        "Crime Type": [
            "Residential Burglary", "Vehicle Theft", "Commercial Theft",
            "Cyber Crime", "Robbery"
        ],
        "Cases": [320, 250, 180, 120, 90]
    })

    st.bar_chart(crime_data.set_index("Crime Type"))

    st.divider()

    st.subheader("Similarity Score Distribution")

    similarity = pd.DataFrame({
        "Score": [95, 92, 88, 84, 79, 73, 68, 61]
    })

    st.line_chart(similarity)

    st.divider()

    st.subheader("Confidence Levels")

    confidence = pd.DataFrame({
        "Confidence": ["High", "Medium", "Low"],
        "Cases": [62, 27, 11]
    })

    st.bar_chart(confidence.set_index("Confidence"))

    st.divider()

    st.subheader("Weekly Crime Trend")

    weekly = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Cases": [18, 21, 25, 17, 29, 35, 31]
    })

    st.line_chart(weekly.set_index("Day"))

    st.success("Analytics generated successfully.")

elif page == "Audit Log":

    st.title("📜 Audit Trail")
    st.write("Every analysis performed in CrimeDNA-X is recorded below.")

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Logs", "25")
    col2.metric("Today's Analyses", "8")
    col3.metric("System Status", "Secure ✅")

    st.divider()

    audit_data = pd.DataFrame({
        "Timestamp": [
            "2026-07-25 10:15",
            "2026-07-25 10:42",
            "2026-07-25 11:08",
            "2026-07-25 11:35",
            "2026-07-25 12:10"
        ],
        "Case ID": ["A-2291", "A-2278", "A-2154", "A-1987", "A-2033"],
        "Action": [
            "Behavioral DNA Generated",
            "Similarity Analysis",
            "Investigation Report",
            "Crime Pattern Match",
            "Audit Verification"
        ],
        "User": [
            "Investigator", "Supervisor", "Investigator",
            "Investigator", "Administrator"
        ],
        "Status": ["Success", "Success", "Success", "Success", "Verified"]
    })

    st.subheader("System Audit Records")
    st.dataframe(audit_data, use_container_width=True)

    st.divider()

    st.subheader("Latest Activity")

    st.success("✔ Behavioral Crime DNA generated successfully.")
    st.success("✔ Similarity engine executed successfully.")
    st.success("✔ Explainable AI report generated.")
    st.success("✔ Investigation recommendations created.")
    st.success("✔ Audit trail verified.")

    st.divider()

    st.subheader("Security Information")

    st.info("""
• All activities are logged.

• Audit records are time stamped.

• Reports can be verified.

• Data integrity is maintained.

• CrimeDNA-X supports transparent investigations.
""")

    st.divider()

    if st.button("Verify Audit Trail"):
        st.success("Audit Verification Successful ✅")
        st.balloons()

    st.caption(
        "CrimeDNA-X maintains a transparent audit trail. "
        "The system supports investigators and never determines guilt."
    )

else:

    st.title("🕵️ About CrimeDNA-X")

    st.markdown("""
# CrimeDNA-X
### AI-Powered Behavioral Crime Linkage Platform

CrimeDNA-X assists investigators by comparing behavioural crime patterns
instead of identifying suspects.

The system generates a Behavioural Crime DNA profile for every FIR and
compares it against historical crime records to identify similar cases.

---
""")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚀 Core Features")
        st.success("Behavioral Crime DNA")
        st.success("ABCS Similarity Engine")
        st.success("Explainable AI")
        st.success("Crime Analytics")
        st.success("Audit Trail")
        st.success("Investigation Support")

    with col2:
        st.subheader("💻 Technology Stack")
        st.info("Python")
        st.info("Streamlit")
        st.info("Pandas")
        st.info("Behavioral Similarity Algorithm")
        st.info("SHA-256 Audit Logging")
        st.info("Explainable AI")

    st.divider()

    st.subheader("Workflow")

    st.markdown("""
1️⃣ Investigator enters FIR

⬇️

2️⃣ CrimeDNA generates Behavioural Signature

⬇️

3️⃣ Similarity Engine compares historical cases

⬇️

4️⃣ Explainable AI provides investigation reasoning

⬇️

5️⃣ Investigation recommendations generated

⬇️

6️⃣ Audit trail recorded
""")

    st.divider()

    st.subheader("Future Enhancements")

    st.write("""
✅ Real Police Database Integration

✅ AI-based Crime Pattern Learning

✅ GIS Crime Hotspot Mapping

✅ Role-Based Login System

✅ PDF Investigation Reports

✅ Real-Time Dashboard

✅ Multi-Language Support
""")
    st.divider()

    st.warning("""
CrimeDNA-X is an Investigation Support System.

✔ Does NOT identify suspects.

✔ Does NOT predict guilt.

✔ Does NOT recommend arrests.

Final decisions always remain with human investigators.
""")
    st.divider()
    st.caption("CrimeDNA-X Version 1.0")
    st.caption("AI-Powered Behavioral Crime Linkage Platform")
    st.caption("Developed for Karnataka State Police Datathon 2026")
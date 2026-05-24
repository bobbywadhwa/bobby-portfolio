import streamlit as st
from PIL import Image
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()


# --------------------------------------------------
# EMAIL FUNCTION
# --------------------------------------------------

def send_email(name, email, message):

    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")
    receiver_email = "bobbywadhwa1303@gmail.com"

    subject = f"Portfolio Contact from {name}"

    body = f"""
Name: {name}
Email: {email}

Message:
{message}
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except:
        return False


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Bobby Wadhwa | Data Engineer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

# --------------------------------------------------
# GLOBAL STYLE
# --------------------------------------------------

st.markdown(
    """
    <style>
    .stApp {
        background-color: #E8F0FB;
    }

    h1, h2, h3 {
        color: #003A8F;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #0B3D91;
        padding-top: 18px;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* Sidebar title */
    .sidebar-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 8px;
        padding: 0 12px;
    }

    /* Text-like nav buttons */
    section[data-testid="stSidebar"] button[kind="secondary"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        color: white !important;
        width: 100% !important;
        text-align: left !important;
        padding: 0.6rem 0.8rem !important;
        border-radius: 10px !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        transition: background-color 0.2s ease, transform 0.2s ease;
    }

    section[data-testid="stSidebar"] button[kind="secondary"]:hover {
        background: rgba(255,255,255,0.10) !important;
        transform: translateX(2px);
    }

    /* Active nav item (rendered as markdown) */
    .nav-active {
        padding: 0.6rem 0.8rem;
        margin: 0.15rem 0;
        border-left: 4px solid #FF4B4B;
        background: rgba(255,255,255,0.12);
        border-radius: 10px;
        font-size: 16px;
        font-weight: 700;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

st.sidebar.markdown("### 👋 Bobby Wadhwa")

pages = ["Home", "Experience", "Projects", "Tech Stack", "Education", "Contact", "Chat"]

for p in pages:
    if st.sidebar.button(p, key=f"btn_{p}"):
        st.session_state.page = p

page = st.session_state.page

# --------------------------------------------------
# HOME
# --------------------------------------------------

if page == "Home":

    col1, col2 = st.columns([1, 3])

    with col1:
        image = Image.open("assets/profilephoto.jpeg")
        st.image(image, width=230)

    with col2:
        st.title("Bobby Wadhwa")

        st.subheader("Data Engineer | Python | SQL | PySpark | Cloud Data Pipelines")

        st.write("""
Data Engineer with **4 years of experience** designing and implementing scalable
data pipelines and analytics platforms across the **banking and financial services domain**.

Experienced in **Python, SQL, PySpark**, cloud data warehousing,
and building scalable **ETL pipelines across AWS and Azure ecosystems**.
""")

    st.markdown("---")

    st.markdown("### Core Expertise")

    st.write("""
• Cloud Data Engineering (AWS & Azure)

• Distributed Data Processing using Apache Spark & PySpark

• Enterprise Data Warehousing (Redshift, Databricks)

• ETL Pipeline Design & Workflow Orchestration
""")

    with open("assets/resume.pdf", "rb") as pdf_file:
        st.download_button(
            label="📄 Download Resume",
            data=pdf_file,
            file_name="Bobby_Wadhwa_Data_Engineer_Resume.pdf",
            mime="application/pdf"
        )

# --------------------------------------------------
# EXPERIENCE
# --------------------------------------------------

elif page == "Experience":

    st.title("Professional Experience")

    st.subheader("MetLife")

    st.markdown("**Role:** Data Engineer")
    st.markdown("**Duration:** July 2025 – Present")

    st.markdown("""
• Designed **Azure Data Factory pipelines** for automated data ingestion and reporting.

• Implemented **event-driven pipelines** triggered by SharePoint updates via **Azure Logic Apps**.

• Built **metadata-driven mapping pipelines** using Azure Data Lake Gen2.

• Developed automated workflows to **ingest SFTP files and route them to SharePoint locations**.

• Established **UAT environments** including ADF, Azure SQL DB, Data Lake, Key Vault and private endpoints.

• Managed **Dev → UAT → Production deployments**.

• Contributed to **pipeline architecture and database schema design** for scalable data platforms.
""")

    st.markdown(
        "**Tech Stack:** Azure Data Factory, Azure SQL Database, Azure Data Lake Gen2, Logic Apps, GitHub, Python, SQL Server"
    )

    st.markdown("---")

    st.subheader("PricewaterhouseCoopers (PwC)")

    st.markdown("**Role:** Data Engineer")
    st.markdown("**Duration:** Jan 2025 – May 2025")

    st.write("""
Worked on a **data platform modernization initiative** migrating legacy ETL
pipelines from Informatica to a **Databricks-based architecture** on Azure.

Analyzed stored procedures and ETL mappings to rebuild transformation logic
inside **Databricks notebooks using Spark processing**.

Developed **Python automation utilities** to streamline data load workflows
and collaborated with reporting teams for analytics-ready datasets.
""")

    st.markdown(
        "**Tech Stack:** Python, SQL, Oracle DB, Databricks, Azure ADLS, Informatica"
    )

    st.markdown("---")

    st.subheader("WNS Global Services")

    st.markdown("**Role:** Data Engineer")
    st.markdown("**Duration:** July 2022 – Dec 2024")

    st.write("""
Worked on **banking analytics data platforms** for NatWest and Royal Bank
of Scotland.

Designed ETL pipelines using **AWS Lambda, Glue and Step Functions**.

Processed large datasets using **AWS Glue PySpark jobs**, storing processed
data in **Amazon S3** and loading curated datasets into **Amazon Redshift**.

Built SQL views and supported **transaction analysis dashboards in Tableau**.
""")

    st.markdown(
        "**Tech Stack:** Python, PostgreSQL, AWS Lambda, Glue, Redshift, S3, Step Functions, CloudWatch"
    )

# --------------------------------------------------
# PROJECTS
# --------------------------------------------------

elif page == "Projects":

    st.title("Key Data Engineering Projects")

    st.subheader("AWS Serverless ETL Pipeline")

    st.write("""
Designed a **serverless ETL architecture** using Lambda, Glue and Step Functions
to automate financial data ingestion and transformation.

Large datasets were processed using **PySpark-based Glue jobs** and loaded into
**Amazon Redshift** for analytics workloads.
""")

    st.markdown(
        "**Tech Stack:** AWS Lambda, AWS Glue, Step Functions, Amazon S3, Amazon Redshift, PySpark"
    )

    st.markdown("---")

    st.subheader("Databricks ETL Migration")

    st.write("""
Migrated legacy Informatica ETL workflows to **Databricks distributed pipelines**.

Rebuilt transformation logic using **Spark-based notebooks** and modernized
enterprise data workflows for improved scalability and maintainability.
""")

    st.markdown(
        "**Tech Stack:** Databricks, Apache Spark, Python, SQL, Azure Data Lake"
    )

# --------------------------------------------------
# TECH STACK
# --------------------------------------------------

elif page == "Tech Stack":

    st.title("Technology Stack")

    st.markdown("### Programming")

    st.markdown("""
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
""")

    st.markdown("### Databases")

    st.markdown("""
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)
""")

    st.markdown("### Data Warehousing")

    st.markdown("""
![Redshift](https://img.shields.io/badge/Amazon_Redshift-8C4FFF?style=for-the-badge&logo=amazon-redshift&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
""")

    st.markdown("### Cloud Platforms")

    st.markdown("""
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white)
""")

    st.markdown("### Workflow & Orchestration")

    st.markdown("""
![StepFunctions](https://img.shields.io/badge/AWS_Step_Functions-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white)
""")

    st.markdown("### DevOps & Tools")

    st.markdown("""
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)
![AzureDevOps](https://img.shields.io/badge/Azure_DevOps-0078D7?style=for-the-badge&logo=azure-devops)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira)
""")

# --------------------------------------------------
# EDUCATION
# --------------------------------------------------

elif page == "Education":

    st.title("Education")

    st.write("""
**B.Tech – Computer Science**

Jamia Hamdard University – Delhi  
Aug 2018 – Jun 2022  

CGPA: **8.04 / 10**
""")

# --------------------------------------------------
# CONTACT
# --------------------------------------------------

elif page == "Contact":

    st.title("Connect With Me")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
<a href="mailto:bobbywadhwa1303@gmail.com">
<img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/gmail.svg" width="80">
</a>
<p>Email</p>
""",
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
<a href="https://www.linkedin.com/in/bobbywadhwa" target="_blank">
<img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg" width="80">
</a>
<p>LinkedIn</p>
""",
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
<a href="https://github.com/bobbywadhwa" target="_blank">
<img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg" width="80">
</a>
<p>GitHub</p>
""",
            unsafe_allow_html=True
        )

# --------------------------------------------------
# CHAT PAGE
# --------------------------------------------------

elif page == "Chat":

    st.title("Chat with Bobby")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")

    if st.button("Send Message"):

        if name and email and message:

            if send_email(name, email, message):
                st.success("Message sent successfully!")
            else:
                st.error("Email failed")
        else:
            st.warning("Please fill all fields")
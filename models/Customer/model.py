# -*-coding:utf-8-*-
from datatypes.Meta import datatypes
from models.NormalType import NormalModel

class Customer(NormalModel):

    # Primary Key
    id = datatypes.AutoInt(name="id", title="ID", primaryKey=True, readOnly=1)

    # Basic Information
    customerName = datatypes.Stext(
        name="customerName",
        title="Customer Name",
        limit=True,
        maxLen=100,
        minLen=1,
        placeholder="Enter customer name"
    )

    email = datatypes.Stext(
        name="email",
        title="Email",
        limit=True,
        maxLen=255,
        placeholder="Enter email address"
    )

    companyName = datatypes.Stext(
        name="companyName",
        title="Company Name",
        limit=True,
        maxLen=200,
        placeholder="Enter company name"
    )

    # Classification Fields
    industry = datatypes.Dropdown(
        name="industry",
        title="Industry",
        options=[
            {"label": "Technology", "value": "technology"},
            {"label": "Finance", "value": "finance"},
            {"label": "Healthcare", "value": "healthcare"},
            {"label": "Manufacturing", "value": "manufacturing"},
            {"label": "Retail", "value": "retail"},
            {"label": "Education", "value": "education"},
            {"label": "Real Estate", "value": "real_estate"},
            {"label": "Consulting", "value": "consulting"},
            {"label": "Other", "value": "other"}
        ],
        placeholder="Select industry"
    )

    customerType = datatypes.Radio(
        name="customerType",
        title="Customer Type",
        options=[
            {"label": "Individual", "value": "individual"},
            {"label": "Small Business", "value": "small_business"},
            {"label": "Enterprise", "value": "enterprise"},
            {"label": "Government", "value": "government"}
        ],
        placeholder="Select customer type"
    )

    status = datatypes.Dropdown(
        name="status",
        title="Status",
        options=[
            {"label": "Active", "value": "active"},
            {"label": "Inactive", "value": "inactive"},
            {"label": "Pending", "value": "pending"},
            {"label": "Suspended", "value": "suspended"},
            {"label": "Closed", "value": "closed"}
        ],
        placeholder="Select status"
    )

    # Financial Information
    creditLimit = datatypes.Money(
        name="creditLimit",
        title="Credit Limit",
        unit="USD",
        decimal=2,
        placeholder="Enter credit limit"
    )

    annualRevenue = datatypes.Money(
        name="annualRevenue",
        title="Annual Revenue",
        unit="USD",
        decimal=2,
        placeholder="Enter annual revenue"
    )

    # Business Information
    employeeCount = datatypes.Numeric(
        name="employeeCount",
        title="Employee Count",
        unit="people",
        decimal=0,
        maxDigits=10,
        placeholder="Enter employee count"
    )

    taxId = datatypes.Stext(
        name="taxId",
        title="Tax ID",
        limit=True,
        maxLen=50,
        placeholder="Enter tax identification number"
    )

    # Contact Information
    contactPerson = datatypes.Stext(
        name="contactPerson",
        title="Contact Person",
        limit=True,
        maxLen=100,
        placeholder="Enter contact person name"
    )

    # Location Information (without address field)
    country = datatypes.Dropdown(
        name="country",
        title="Country",
        options=[
            {"label": "United States", "value": "US"},
            {"label": "United Kingdom", "value": "UK"},
            {"label": "Canada", "value": "CA"},
            {"label": "Australia", "value": "AU"},
            {"label": "Germany", "value": "DE"},
            {"label": "France", "value": "FR"},
            {"label": "China", "value": "CN"},
            {"label": "Japan", "value": "JP"},
            {"label": "Other", "value": "other"}
        ],
        placeholder="Select country"
    )

    city = datatypes.Stext(
        name="city",
        title="City",
        limit=True,
        maxLen=100,
        placeholder="Enter city name"
    )

    postalCode = datatypes.Stext(
        name="postalCode",
        title="Postal Code",
        limit=True,
        maxLen=20,
        placeholder="Enter postal code"
    )

    # Dates
    registrationDate = datatypes.Date(
        name="registrationDate",
        title="Registration Date",
        dateTimeType="YEAR_MONTH_DAY",
        dateTimeFormat="YYYY-MM-DD",
        placeholder="Select registration date"
    )

    # Notes and Additional Information
    notes = datatypes.Ltext(
        name="notes",
        title="Notes",
        limit=True,
        maxLen=2000,
        placeholder="Enter additional notes or comments"
    )

    # System Fields
    createdBy = datatypes.Member(
        name="createdBy",
        title="Created By",
        createDefault=True,
        readOnly=1
    )

    createdAt = datatypes.Datetime(
        name="createdAt",
        title="Created At",
        dateTimeType="SECOND",
        dateTimeFormat="YYYY-MM-DD HH:mm:ss",
        formatDate="YYYY-MM-DD",
        formatTime="HH:mm:ss",
        createDefault=True,
        updateDefault=False,
        readOnly=1
    )

    updatedAt = datatypes.Datetime(
        name="updatedAt",
        title="Updated At",
        dateTimeType="SECOND",
        dateTimeFormat="YYYY-MM-DD HH:mm:ss",
        formatDate="YYYY-MM-DD",
        formatTime="HH:mm:ss",
        createDefault=True,
        updateDefault=True,
        readOnly=1
    )

    class Meta:
        modelType = "NormalType"
        db = "databases.Default"
        dataTitle = "customerName"
        dbTable = "T_Customer"
        name = "Customer"
        title = "Customer"
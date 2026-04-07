documents = [
    {
        "id": "doc_001",
        "title": "Event Details - Deposit Bonus Interest Remediation",
        "content": """
        PAGE: Event Details - Deposit Bonus Interest Remediation
        CONFLUENCE SPACE: Remediation Readiness
        LAST UPDATED: January 2024

        EVENT SUMMARY:
        During a routine audit, it was identified that customers who were enrolled 
        in the Bonus Interest Program between January 2019 and December 2022 were 
        not receiving the promised bonus interest rates on their deposit accounts.
        The event was raised by the Product Team and escalated to the Remediation 
        Team via Event Management.

        EVENT TRIGGER:
        Customer complaint received by frontline staff regarding incorrect interest 
        calculation. Internal audit confirmed systematic error in interest rate 
        application engine.

        PRODUCTS AFFECTED:
        - Savings Plus Accounts
        - Premium Deposit Accounts
        - Term Deposit Accounts enrolled in Bonus Program

        ROOT CAUSE:
        A system upgrade in January 2019 caused the bonus interest rate flag to 
        be overridden by the base rate engine. The bonus rate multiplier was not 
        applied to eligible accounts despite customers meeting all qualifying criteria.

        EVENT OWNER: Remediation Team Lead
        RISK SIGN OFF: Chief Risk Officer
        REGULATORY NOTIFICATION: APRA notified on 15 March 2024
        ESTIMATED AFFECTED CUSTOMERS: 45,000 accounts
        """,
        "category": "event_details",
        "product": "deposits"
    },
    {
        "id": "doc_002",
        "title": "Data Discovery - Deposit Bonus Interest Remediation",
        "content": """
        PAGE: Data Discovery - Deposit Bonus Interest Remediation
        CONFLUENCE SPACE: Remediation Readiness
        LAST UPDATED: February 2024

        DATA DISCOVERY SUMMARY:
        This page documents the data sources identified for the Deposit Bonus 
        Interest Remediation event.

        SOURCE SYSTEMS IDENTIFIED:
        1. Core Banking System (CBS) - Primary source for account details
        2. Interest Rate Engine (IRE) - Source for rate application history
        3. Customer Master Data (CMD) - Source for customer demographics
        4. Product Enrollment System (PES) - Source for bonus program enrollment

        KEY TABLES:
        - CBS.DEPOSIT_ACCOUNTS - Account balances and status
        - IRE.RATE_APPLICATION_HISTORY - Daily interest rate applied per account
        - PES.BONUS_PROGRAM_ENROLLMENT - Enrollment start and end dates
        - CMD.CUSTOMER_PROFILE - Customer contact details for communication

        DATE RANGE:
        Start Date: 01 January 2019
        End Date: 31 December 2022
        Total Period: 4 years / 48 months / 1461 days

        DATA QUALITY ISSUES FOUND:
        - 234 accounts had missing enrollment end dates — treated as active for 
          full period pending further investigation
        - 12 accounts had duplicate enrollment records — senior analyst decision 
          to use earliest enrollment date
        - 89 accounts migrated from legacy system — manual verification required

        DATA SIGN OFF: Senior Data Engineer
        DATA DISCOVERY COMPLETION DATE: 28 February 2024
        """,
        "category": "data_discovery",
        "product": "deposits"
    },
    {
        "id": "doc_003",
        "title": "Account Identification - Deposit Bonus Interest Remediation",
        "content": """
        PAGE: Account Identification - Deposit Bonus Interest Remediation
        CONFLUENCE SPACE: Remediation Readiness
        LAST UPDATED: March 2024

        ACCOUNT IDENTIFICATION SUMMARY:
        This page documents the methodology and results for identifying all 
        affected accounts in the Deposit Bonus Interest Remediation event.

        IDENTIFICATION CRITERIA:
        An account is considered affected if ALL of the following conditions are met:
        1. Account was enrolled in Bonus Interest Program
        2. Enrollment date falls between 01 Jan 2019 and 31 Dec 2022
        3. Account was active during the affected period
        4. Bonus interest rate was not correctly applied in IRE system
        5. Account balance was greater than minimum threshold of $1000

        EXCLUSION CRITERIA:
        - Accounts closed before 01 Jan 2019
        - Accounts where customer opted out of Bonus Program
        - Accounts under fraud investigation during affected period
        - Deceased customer accounts — separate process to follow

        POPULATION RESULTS:
        Total accounts reviewed: 187,432
        Accounts meeting all criteria: 44,892
        Accounts excluded: 142,540
        Accounts requiring manual review: 312

        ACCOUNT IDENTIFICATION SIGN OFF: Risk Manager
        METHODOLOGY APPROVED BY: Chief Risk Officer
        COMPLETION DATE: 15 March 2024
        """,
        "category": "account_identification",
        "product": "deposits"
    },
    {
        "id": "doc_004",
        "title": "Base Refund Calculation - Deposit Bonus Interest Remediation",
        "content": """
        PAGE: Base Refund Calculation - Deposit Bonus Interest Remediation
        CONFLUENCE SPACE: Remediation Readiness
        LAST UPDATED: April 2024

        BASE REFUND CALCULATION SUMMARY:
        This page documents the methodology for calculating the base refund 
        amount owed to each affected customer.

        CALCULATION METHODOLOGY:
        Base Refund = (Promised Bonus Rate - Actual Rate Applied) x Daily Balance x Days

        RATE DETAILS:
        Promised Bonus Rate: Base Rate + 0.75% per annum
        Actual Rate Applied: Base Rate only (bonus component missing)
        Difference: 0.75% per annum = 0.002055% per day

        CALCULATION STEPS:
        Step 1: Extract daily balance for each affected account from CBS
        Step 2: Identify the exact days bonus rate was not applied from IRE
        Step 3: Apply formula: Daily Balance x 0.002055% x Number of Days
        Step 4: Sum across all affected days for total base refund per account
        Step 5: Validate calculation against sample of 500 accounts manually

        EXAMPLE CALCULATION:
        Account Balance: $50,000
        Affected Days: 365 days
        Daily Rate Difference: 0.002055%
        Base Refund = $50,000 x 0.00002055 x 365 = $375.04

        TOTAL BASE REFUND POOL: $18.4 million across 44,892 accounts
        AVERAGE REFUND PER CUSTOMER: $409.88
        MINIMUM REFUND: $12.40
        MAXIMUM REFUND: $48,920.00

        CALCULATION SIGN OFF: Finance Director
        EXTERNAL AUDIT REVIEW: Completed by PwC March 2024
        """,
        "category": "base_refund_calculation",
        "product": "deposits"
    },
    {
        "id": "doc_005",
        "title": "Secondary Refund - Deposit Bonus Interest Remediation",
        "content": """
        PAGE: Secondary Refund - Deposit Bonus Interest Remediation
        CONFLUENCE SPACE: Remediation Readiness
        LAST UPDATED: April 2024

        SECONDARY REFUND SUMMARY:
        This page documents additional compensation components beyond the base 
        refund for the Deposit Bonus Interest Remediation event.

        SECONDARY REFUND COMPONENTS:

        1. TAX ADJUSTMENT
        Customers may have paid tax on incorrect interest amounts.
        Approach: Calculate tax differential and include in refund package.
        Tax Rate Applied: Individual customer tax rate from ATO records where 
        available, otherwise default rate of 32.5% applied.

        2. ACCOUNT FEES CHARGED DURING PERIOD
        Some customers were charged monthly fees that would have been waived 
        had they received correct bonus interest qualifying them for fee waiver.
        Approach: Identify fee waiver eligibility and refund incorrectly charged fees.
        Estimated Additional Amount: $2.1 million across 12,430 accounts.

        3. CONSEQUENTIAL LOSS
        Where customers can demonstrate financial loss as a direct result of 
        incorrect interest application, assessed on case by case basis.
        Approach: Customer to submit claim with supporting documentation.
        Claims Team: Dedicated team of 12 assessors assigned.

        TOTAL SECONDARY REFUND POOL: $3.8 million
        SIGN OFF: Chief Risk Officer and Legal Counsel
        """,
        "category": "secondary_refund",
        "product": "deposits"
    },
    {
        "id": "doc_006",
        "title": "Time Value of Money - Deposit Bonus Interest Remediation",
        "content": """
        PAGE: Secondary Interest and Time Value of Money - Deposit Bonus Interest Remediation
        CONFLUENCE SPACE: Remediation Readiness
        LAST UPDATED: May 2024

        TIME VALUE OF MONEY SUMMARY:
        Customers were deprived of money that was rightfully theirs. To fairly 
        compensate them, interest must be applied to the base refund amount for 
        the period between when the error occurred and when remediation is paid.

        METHODOLOGY:
        Secondary Interest = Base Refund Amount x RBA Cash Rate x Days Since Error

        RBA CASH RATE SCHEDULE USED:
        2019: 1.50% per annum
        2020: 0.25% per annum (COVID reduction)
        2021: 0.10% per annum
        2022: 2.85% per annum (rate rise cycle)
        2023: 4.35% per annum
        2024 (to payment date): 4.35% per annum

        CALCULATION APPROACH:
        Daily RBA rate applied to cumulative base refund shortfall.
        Compounded monthly to reflect true time value of money.
        Calculated from first date of error to expected payment date of 30 June 2024.

        EXAMPLE:
        Base Refund: $375.04
        Period: Jan 2019 to Jun 2024 (5.5 years)
        Blended RBA Rate: 2.2% per annum
        Secondary Interest = $375.04 x 2.2% x 5.5 = $45.38

        TOTAL SECONDARY INTEREST POOL: $2.2 million
        GRAND TOTAL REMEDIATION: $24.4 million

        SIGN OFF: Chief Financial Officer
        ACTUARIAL REVIEW: Completed by Deloitte April 2024
        """,
        "category": "time_value_of_money",
        "product": "deposits"
    },
    {
        "id": "doc_007",
        "title": "Event Details - Loan Fee Waiver Remediation",
        "content": """
        PAGE: Event Details - Loan Fee Waiver Remediation
        CONFLUENCE SPACE: Remediation Readiness
        LAST UPDATED: June 2024

        EVENT SUMMARY:
        Customers who took out personal loans between March 2020 and September 
        2023 under the COVID Relief Loan Product were charged establishment fees 
        and monthly service fees despite the Terms and Conditions clearly stating 
        these fees would be waived for the life of the loan.

        EVENT TRIGGER:
        Internal compliance review identified discrepancy between product T&Cs 
        and actual fee charging in the loan management system. Issue escalated 
        to Remediation Team by Compliance Officer.

        PRODUCTS AFFECTED:
        - COVID Relief Personal Loans
        - Small Business Emergency Loans
        - Hardship Assistance Loans

        ROOT CAUSE:
        When the COVID Relief Loan product was launched in March 2020, the fee 
        waiver configuration was correctly set up in the product system. However 
        a system patch applied in July 2020 reset the fee waiver flag to default 
        charging for all loan products including COVID Relief Loans.

        EVENT OWNER: Loans Remediation Lead
        REGULATORY NOTIFICATION: ASIC notified 01 July 2024
        ESTIMATED AFFECTED CUSTOMERS: 28,500 accounts
        ESTIMATED REMEDIATION AMOUNT: $31.2 million
        """,
        "category": "event_details",
        "product": "loans"
    },
    {
        "id": "doc_008",
        "title": "Account Identification - Loan Fee Waiver Remediation",
        "content": """
        PAGE: Account Identification - Loan Fee Waiver Remediation
        CONFLUENCE SPACE: Remediation Readiness
        LAST UPDATED: July 2024

        ACCOUNT IDENTIFICATION SUMMARY:
        Methodology for identifying all customers affected by incorrect fee 
        charging on COVID Relief Loan products.

        IDENTIFICATION CRITERIA:
        1. Loan originated between 01 March 2020 and 30 September 2023
        2. Loan product code is one of: CRL001, SBE002, HAL003
        3. Establishment fee was charged at loan origination
        4. Monthly service fee was charged after July 2020
        5. Loan account was active at any point after July 2020

        POPULATION RESULTS:
        Total loan accounts reviewed: 94,210
        Accounts meeting all criteria: 28,432
        Accounts excluded: 65,778
        Accounts requiring manual review: 156

        KEY EXCLUSIONS:
        - Loans fully repaid before July 2020 patch date
        - Loans where customer was on approved payment pause — 
          fees were already manually waived
        - Business loans above $500,000 threshold — different T&Cs apply

        SIGN OFF: Loans Risk Manager
        COMPLETION DATE: 31 July 2024
        """,
        "category": "account_identification",
        "product": "loans"
    },
    {
        "id": "doc_009",
        "title": "Base Refund Calculation - Loan Fee Waiver Remediation",
        "content": """
        PAGE: Base Refund Calculation - Loan Fee Waiver Remediation
        CONFLUENCE SPACE: Remediation Readiness
        LAST UPDATED: August 2024

        BASE REFUND CALCULATION SUMMARY:
        Calculation of all incorrectly charged fees to be refunded to affected 
        loan customers.

        FEE COMPONENTS TO REFUND:

        1. ESTABLISHMENT FEE
        Standard establishment fee charged at loan origination: $395 per loan
        All 28,432 affected accounts charged this fee.
        Total Establishment Fee Refund: $11.2 million

        2. MONTHLY SERVICE FEE
        Monthly service fee charged: $12 per month per account
        Charging commenced incorrectly from July 2020 patch date.
        Average affected months per account: 28 months
        Total Monthly Fee Refund: $9.6 million

        CALCULATION STEPS:
        Step 1: Extract establishment fee from loan origination records
        Step 2: Extract monthly service fee charges from loan transaction history
        Step 3: Sum all incorrectly charged fees per account
        Step 4: Validate against loan statements for sample of 200 accounts

        TOTAL BASE REFUND: $20.8 million
        AVERAGE REFUND PER CUSTOMER: $731.84
        MINIMUM REFUND: $395.00 (establishment fee only)
        MAXIMUM REFUND: $3,731.00

        SIGN OFF: Finance Director
        """,
        "category": "base_refund_calculation",
        "product": "loans"
    },
    {
        "id": "doc_010",
        "title": "Time Value of Money - Loan Fee Waiver Remediation",
        "content": """
        PAGE: Secondary Interest and Time Value of Money - Loan Fee Waiver Remediation
        CONFLUENCE SPACE: Remediation Readiness
        LAST UPDATED: August 2024

        TIME VALUE OF MONEY SUMMARY:
        Interest compensation for the period customers were incorrectly charged 
        fees on their COVID Relief Loans.

        METHODOLOGY:
        Secondary Interest = Fee Amount Incorrectly Charged x RBA Cash Rate x Days Held

        APPROACH:
        For establishment fees: Interest calculated from loan origination date.
        For monthly service fees: Interest calculated from each individual 
        fee charge date to expected payment date.

        BLENDED RATE APPLIED: 2.8% per annum (weighted average RBA cash rate 
        across the affected period July 2020 to August 2024)

        EXAMPLE:
        Establishment Fee: $395
        Period: July 2020 to August 2024 (4.1 years)
        Secondary Interest = $395 x 2.8% x 4.1 = $45.35

        Monthly Fee Example:
        Monthly Fee: $12
        Average Hold Period: 2 years
        Secondary Interest per fee = $12 x 2.8% x 2 = $0.67
        Total monthly fee interest (28 months) = $18.76

        TOTAL SECONDARY INTEREST: $10.4 million
        GRAND TOTAL LOAN REMEDIATION: $31.2 million

        SIGN OFF: Chief Financial Officer
        ACTUARIAL REVIEW: Ernst and Young August 2024
        """,
        "category": "time_value_of_money",
        "product": "loans"
    }
]

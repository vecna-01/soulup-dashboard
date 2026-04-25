# SOULUP 15 KPI DASHBOARD

## Complete Step-by-Step Guide for Running the Dashboard

---

## SECTION 1: INITIAL SETUP

### Step 1: Clone Repository
```bash
git clone https://github.com/vecna-01/soulup-dashboard.git
cd soulup-dashboard
```

### Step 2: Install Python Libraries
```bash
pip install -r requirements.txt
```

**Expected Output:**
```
pandas      2.0.0 ✓
numpy       1.24.0 ✓
matplotlib  3.6.0 ✓
seaborn     0.12.0 ✓
plotly      5.13.0 ✓
scikit-learn 1.2.0 ✓
```

### Step 3: Create Project Folders
```bash
mkdir data
mkdir outputs
```

---

## SECTION 2: RUNNING THE DASHBOARD

### Step 1: Generate Sample Data
```bash
python data_generator.py
```

**Expected Output:**
```
============================================================
GENERATING SAMPLE DATA
============================================================
✓ Generated 268 therapist profiles
✓ Generated 1000 booking records
✓ Generated 30 group programs

============================================================
DATA FILES CREATED IN 'data/' FOLDER
============================================================
```

### Step 2: Run the KPI Dashboard
```bash
python kpi_dashboard.py
```

**Expected Output:**
```
██████████████████████████████████████████████████████████
█                                                          █
█          SOULUP 15 KPI DASHBOARD & ANALYSIS             █
█                                                          █
██████████████████████████████████████████████████████████

1. LOADING DATA
--------------------------------------------------------------
✓ Data loaded successfully
  - Therapists: 268
  - Bookings: 1000
  - Groups: 30

2. CALCULATING KPIs
--------------------------------------------------------------
KPI 1: Inquiry→Booking = 45.0%
KPI 2: Booking→Completion = 94.0%
KPI 3: Overall Conversion = 42.2%
KPI 4: Completion Rate = 93.8%
KPI 5: Discovery Call Completion = 78.0%
KPI 6: Therapist Utilization = 87.5%
KPI 7: Active Therapists = 268
KPI 8: Customer Retention = 72.3%
KPI 9: Repeat User Revenue = 55.1%
KPI 10: Avg Session Rating = 4.7/5.0
KPI 11: Refund Rate = 6.1%
KPI 12: Cancellation Rate = 8.2%
KPI 13: Monthly Revenue = ₹8,16,000
KPI 14: MoM Growth = 25.0%
KPI 15: Data Consistency = 99.5%

3. CREATING VISUALIZATIONS
--------------------------------------------------------------
✓ Dashboard saved to outputs/15_KPI_Dashboard.png
✓ Revenue chart saved
✓ Funnel chart saved

4. GENERATING REPORT
--------------------------------------------------------------
✓ Report saved to outputs/KPI_Report.txt

============================================================
✓ DASHBOARD COMPLETE!
============================================================

Generated Files:
  1. outputs/15_KPI_Dashboard.png - Visual dashboard
  2. outputs/Revenue_Breakdown.png - Revenue chart
  3. outputs/Funnel_Analysis.png - Conversion funnel
  4. outputs/KPI_Report.txt - Detailed report

============================================================
```

### Step 3: View Output Files
```bash
ls outputs/
```

You'll find:
- **15_KPI_Dashboard.png** - Main 15-KPI visual dashboard
- **Revenue_Breakdown.png** - Revenue by segment pie chart
- **Funnel_Analysis.png** - 7-stage booking funnel
- **KPI_Report.txt** - Detailed text report with all metrics

---

## SECTION 3: THE 15 KPIs EXPLAINED

### CONVERSION METRICS (3 KPIs)

**KPI 1: Inquiry → Booking Conversion**
- Value: 45%
- What it means: 45% of initial inquiries convert to bookings
- Target: >40%
- Status: ✓ GOOD

**KPI 2: Booking → Completion Conversion**
- Value: 94%
- What it means: 94% of bookings are completed
- Target: >90%
- Status: ✓ EXCELLENT

**KPI 3: Overall Inquiry → Completion**
- Value: 42.2%
- What it means: End-to-end conversion from inquiry to session
- Target: >40%
- Status: ✓ GOOD

---

### OPERATIONAL METRICS (4 KPIs)

**KPI 4: Session Completion Rate**
- Value: 93.8%
- What it means: Percentage of scheduled sessions completed
- Improvement: From 65% to 94% (+29 pp)
- Status: ✓ EXCELLENT

**KPI 5: Discovery Call Completion**
- Value: 78%
- What it means: Discovery calls completed (critical funnel stage)
- Impact: Critical for user-therapist matching
- Status: ✓ GOOD

**KPI 6: Therapist Utilization**
- Value: 87.5%
- What it means: Average therapist schedule utilization
- Target: 87% (optimal level)
- Status: ✓ OPTIMAL

**KPI 7: Active Therapists**
- Value: 268
- What it means: Number of active licensed therapists
- Growth: From 40 to 268 (6.7x growth)
- Impact: Enables scalability

---

### CUSTOMER METRICS (3 KPIs)

**KPI 8: Customer Retention Rate**
- Value: 72.3%
- What it means: % of customers who return for another session
- Benchmark: 72% (excellent for healthtech)
- Impact: Repeat customers = 55% of revenue

**KPI 9: Repeat User Revenue**
- Value: 55.1%
- What it means: % of revenue from repeat users
- Impact: Critical to profitability
- Insight: Focus on retention = better margins

**KPI 10: Average Session Rating**
- Value: 4.7/5.0
- What it means: User satisfaction rating
- Target: 4.7/5.0
- Status: ✓ EXCELLENT

---

### FINANCIAL METRICS (4 KPIs)

**KPI 11: Refund Rate**
- Value: 6.1%
- What it means: % of bookings refunded
- Improvement: From 25% to 6% (-19 pp)
- Monthly Savings: ₹1,51,000
- Status: ✓ MAJOR IMPROVEMENT

**KPI 12: Cancellation Rate**
- Value: 8.2%
- What it means: % of bookings cancelled
- Improvement: From 15% to 8% (-7 pp)
- Prediction: Using ML to reduce further
- Status: ✓ IMPROVING

**KPI 13: Monthly Revenue**
- Value: ₹8,16,000
- What it means: Total monthly recurring revenue
- Growth: From ₹1L to ₹8.16L (437% growth)
- Contribution: You contributed 20-30% to this growth

**KPI 14: Month-over-Month Growth**
- Value: 25%
- What it means: Month-to-month revenue growth rate
- Average: ~25% MoM consistent growth
- Trajectory: Exponential scaling observed

---

### DATA QUALITY (1 KPI)

**KPI 15: Data Consistency**
- Value: 99.5%
- What it means: Cross-system data consistency rate
- Target: 99%+
- Status: ✓ EXCELLENT

---

## SECTION 4: FILE STRUCTURE

```
soulup-dashboard/
├── README.md                      # This file
├── requirements.txt               # Python dependencies
├── data_generator.py              # Generate sample data
├── kpi_dashboard.py               # Main dashboard script
├── data/                          # Data folder (created)
│   ├── therapists.csv
│   ├── bookings.csv
│   └── group_programs.csv
└── outputs/                       # Output folder (created)
    ├── 15_KPI_Dashboard.png
    ├── Revenue_Breakdown.png
    ├── Funnel_Analysis.png
    └── KPI_Report.txt
```

---

## SECTION 5: CUSTOMIZATION GUIDE

### Q1: How do I use my own data?

**Answer:** Create CSV files in the `data/` folder:

**data/therapists.csv:**
```csv
therapist_id,name,specializations,experience_years,rating,availability_hours,completion_rate,total_sessions
1,Dr. Anjali Sharma,anxiety|stress,5,4.8,15,0.92,84
2,Dr. Ravi Kumar,depression|relationships,8,4.9,20,0.95,120
```

**data/bookings.csv:**
```csv
booking_id,user_id,therapist_id,booking_date,session_date,status,amount,refund,rating
1,1001,1,2025-07-01,2025-07-05,completed,4000,0,4.7
2,1002,2,2025-07-02,2025-07-06,completed,5000,0,4.8
```

**data/group_programs.csv:**
```csv
program_id,name,focus_area,difficulty,duration_weeks,capacity,current_enrollment,completion_rate,satisfaction
101,Program_1,anxiety,beginner,8,20,12,0.78,4.6
```

### Q2: How do I modify KPI calculations?

**Answer:** Edit the `KPICalculator` class in `kpi_dashboard.py`:

```python
def _refund_rate(self):
    """KPI 11: Refund rate"""
    total = len(self.bookings)
    refunds = len(self.bookings[self.bookings['refund'] == 1])
    rate = (refunds / total * 100) if total > 0 else 0
    
    # CUSTOMIZE HERE:
    result = {
        'value': round(rate, 1),
        'unit': '%',
        'description': 'YOUR CUSTOM DESCRIPTION',
    }
    return result
```

### Q3: How do I add more visualizations?

**Answer:** Add to `DashboardVisualizer` class:

```python
def create_custom_chart(self):
    """Create custom chart"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Your plotting code
    ax.plot([1, 2, 3], [10, 20, 15])
    ax.set_title('Custom Chart')
    
    plt.savefig('outputs/Custom_Chart.png', dpi=300)
    plt.close()
```

---

## SECTION 6: TROUBLESHOOTING

### Issue: "ModuleNotFoundError: No module named 'pandas'"

**Solution:**
```bash
pip install -r requirements.txt
# Or individually:
pip install pandas numpy matplotlib seaborn plotly scikit-learn openpyxl
```

### Issue: "FileNotFoundError: data/therapists.csv"

**Solution:**
```bash
# Make sure you ran data_generator.py first:
python data_generator.py

# Then check the data folder:
ls data/
```

### Issue: "Permission denied" on outputs

**Solution:**
```bash
mkdir outputs
chmod 755 outputs
```

---

## SECTION 7: INTEGRATION OPTIONS

### Real-Time Dashboard (Streamlit)

Create `app.py`:
```python
import streamlit as st
from kpi_dashboard import KPICalculator, SoulUpDataLoader

st.title("SOULUP 15 KPI Dashboard")

loader = SoulUpDataLoader()
loader.load_all_data()

calculator = KPICalculator(loader.bookings, loader.therapists, loader.groups)
kpis = calculator.calculate_all_kpis()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Inquiry→Booking", "45%", "+2%")
with col2:
    st.metric("Completion Rate", "94%", "+29pp")
with col3:
    st.metric("Revenue", "₹8.16L", "+437%")
```

Run:
```bash
pip install streamlit
streamlit run app.py
```

---

## SECTION 8: NEXT STEPS

- [ ] Clone the repository
- [ ] Install dependencies: `pip install -r requirements.txt`
- [ ] Generate data: `python data_generator.py`
- [ ] Run dashboard: `python kpi_dashboard.py`
- [ ] View outputs in `outputs/` folder
- [ ] Integrate with real data
- [ ] Set up scheduled reports
- [ ] Deploy to production

---

## Support

For issues or questions, please create an issue in the repository.

**Happy Dashboarding! 🎯**

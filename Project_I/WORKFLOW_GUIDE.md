# Project Workflow Guide

## Step-by-Step Process for Completing DATS 6401 Project 1

---

## Phase 1: Planning and Dataset Selection (Week 1)

### 1.1 Choose Your Topic
- [ ] Brainstorm topics of interest
- [ ] Consider topics with policy/social relevance
- [ ] Think about questions you want to answer
- [ ] Check that sufficient data is available

**Resources**:
- Course materials on interesting topics
- News articles for current issues
- Academic papers in your field of interest

### 1.2 Find Datasets
- [ ] Search for Dataset A (Primary/Fact dataset)
- [ ] Search for Dataset B (Secondary/Context dataset)
- [ ] Verify datasets meet requirements (see PROJECT_CHECKLIST.md)
- [ ] Download datasets to `data/raw/`

**Good Data Sources**:
- [U.S. government data](https://www.data.gov) 
- [demographic data](https://www.census.gov)
- [international data](https://www.worldbank.org)
- [various datasets](https://www.kaggle.com)
- [curated datasets](https://www.data.world)
- WHO, CDC, OECD, UN data portals
- Academic repositories
- Government agency open data portals

### 1.3 Document Your Datasets
- [ ] Fill out `data/raw/data_sources.md`
- [ ] Note collection methods, dates, sources
- [ ] Identify join keys between datasets
- [ ] Document any known limitations

---

## Phase 2: Data Exploration and Cleaning (Week 2)

### 2.1 Explore Your Data
- [ ] Open `notebooks/exploratory_analysis.ipynb`
- [ ] Load your datasets
- [ ] Check data types, missing values, distributions
- [ ] Identify patterns and interesting relationships
- [ ] Verify dataset requirements are met

### 2.2 Clean Your Data
- [ ] Adapt `scripts/data_cleaning.py` for your data
- [ ] Handle missing values
- [ ] Standardize formats (dates, geographic codes, etc.)
- [ ] Remove duplicates
- [ ] Create any derived variables needed
- [ ] Save cleaned data to `data/processed/`

### 2.3 Finalize Your Research Questions
- [ ] Based on your exploration, refine your research questions
- [ ] Make sure questions are specific and answerable
- [ ] Ensure questions align with available data
- [ ] Update `README.md` with your questions

---

## Phase 3: Tableau Visualization (Week 2-3)

### 3.1 Set Up Tableau
- [ ] Open Tableau (Desktop or Public)
- [ ] Connect to your cleaned datasets
- [ ] Set up relationship/join between datasets
- [ ] Verify data imported correctly

### 3.2 Create Required Charts

**Chart 1: Map** (Required)
- [ ] Create a map visualization
- [ ] Use geographic field from Dataset A
- [ ] Color/size by meaningful measure
- [ ] Add appropriate filters
- [ ] Add descriptive title
- [ ] Export screenshot to `docs/figures/chart1_map.png`

**Chart 2: Bar Chart** (Required)
- [ ] Create bar chart comparing categories
- [ ] Use data from Dataset A and/or B
- [ ] Sort meaningfully
- [ ] Add descriptive title and labels
- [ ] Export screenshot to `docs/figures/chart2_bar.png`

**Chart 3: Table** (Required)
- [ ] Create table with relevant details
- [ ] Use formatting to highlight key values
- [ ] Include data from both datasets if relevant
- [ ] Add descriptive title
- [ ] Export screenshot to `docs/figures/chart3_table.png`

**Chart 4: Line Chart** (Required)
- [ ] Create line chart showing trend over time
- [ ] Use time field from Dataset A
- [ ] Add reference lines if helpful
- [ ] Add descriptive title
- [ ] Export screenshot to `docs/figures/chart4_line.png`

**Chart 5: Your Choice**
- [ ] Choose appropriate chart type for your data
- [ ] Create visualization
- [ ] Export screenshot to `docs/figures/chart5.png`

**Chart 6: Your Choice**
- [ ] Choose appropriate chart type for your data
- [ ] Create visualization
- [ ] Export screenshot to `docs/figures/chart6.png`

### 3.3 Create Dashboard
- [ ] Create new dashboard in Tableau
- [ ] Add at least 3 charts
- [ ] Add interactive filters
- [ ] Set up filter actions between charts
- [ ] Design layout for clarity
- [ ] Add title and instructions
- [ ] Export screenshot to `docs/figures/dashboard.png`

### 3.4 Document Your Work
- [ ] Fill out `tableau/tableau_notes.md`
- [ ] Document calculated fields
- [ ] Note design decisions
- [ ] Record key insights from each chart

### 3.5 Save and Package
- [ ] Save Tableau workbook
- [ ] File → Save As → `tableau/project1_workbook.twbx`
- [ ] Verify it's saved as .twbx (packaged format)
- [ ] Test that file opens correctly

---

## Phase 4: Writing the Narrative (Week 3-4)

### 4.1 Draft Each Section

**Section 1: Introduction** (0.5-1 page)
- [ ] Write motivation for topic
- [ ] Cite sources that inspired you
- [ ] State research questions clearly
- [ ] Explain benefit to audience

**Section 2: Datasets** (1-1.5 pages)
- [ ] Describe Dataset A fully
- [ ] Describe Dataset B fully
- [ ] Explain relationship between datasets
- [ ] Discuss limitations of each dataset

**Section 3: Data Story** (1.5-2 pages)
- [ ] Insert Chart 1 (Map) with analysis
- [ ] Insert Chart 2 (Bar) with analysis
- [ ] Insert Chart 3 (Table) with analysis
- [ ] Insert Chart 4 (Line) with analysis
- [ ] Insert Chart 5 with analysis
- [ ] Insert Chart 6 with analysis
- [ ] Insert Dashboard screenshot
- [ ] Write narrative connecting all charts
- [ ] Explicitly address research questions

**Section 4: Conclusions** (0.5 page)
- [ ] Summarize key findings
- [ ] Answer research questions
- [ ] Discuss implications
- [ ] Note limitations and future work

**Section 5: References**
- [ ] List all sources in APA format
- [ ] Include at least 6 credible sources
- [ ] Check all in-text citations match references

**Section 6: Contributions** (if team)
- [ ] List each team member's contributions

### 4.2 Review and Edit
- [ ] Check page count (3-4 pages excluding figures/references)
- [ ] Proofread for grammar and spelling
- [ ] Verify all charts are referenced in text
- [ ] Ensure all variables are defined
- [ ] Check APA formatting
- [ ] Verify all requirements met (use PROJECT_CHECKLIST.md)

### 4.3 Format Final Document
- [ ] Professional formatting
- [ ] Clear section headers
- [ ] Page numbers
- [ ] Consistent fonts and spacing
- [ ] All figures clearly labeled
- [ ] Generate PDF from Word document

---

## Phase 5: Final Submission (Week 4)

### 5.1 Pre-Submission Checklist
- [ ] Complete PROJECT_CHECKLIST.md
- [ ] Test Tableau .twbx file opens correctly
- [ ] Final proofread of narrative
- [ ] All files in correct folders
- [ ] README.md is updated

### 5.2 Files to Submit
1. [ ] Final narrative report PDF (`docs/final_report.pdf`)
2. [ ] Packaged Tableau workbook (`tableau/project1_workbook.twbx`)
3. [ ] Any other files required by instructor

### 5.3 Optional: Create Backup
- [ ] Zip entire project folder
- [ ] Save to cloud storage (Google Drive, OneDrive, etc.)
- [ ] Keep local backup

---

## Tips for Success

### General Tips
- Start early - don't wait until the last week
- Save your work frequently
- Keep backups of everything
- Document as you go, not at the end
- Ask for help if you get stuck

### Dataset Tips
- Choose datasets you find genuinely interesting
- Bigger isn't always better - quality > quantity
- Make sure you understand what the variables mean
- Check data documentation thoroughly
- Verify join keys will work before committing to datasets

### Visualization Tips
- Keep it simple and clear
- Every chart should have a purpose
- Use appropriate chart types for your data
- Color should add meaning, not just decoration
- Always label axes and include units
- Tell a story, don't just show charts

### Writing Tips
- Write for your audience, not yourself
- Use concrete examples
- Define technical terms
- Connect each chart to your research questions
- Be honest about limitations
- Proofread multiple times

### Time Management
- Week 1: Dataset selection and exploration (8-10 hours)
- Week 2: Data cleaning and initial Tableau work (10-12 hours)
- Week 3: Complete visualizations and dashboard (8-10 hours)
- Week 4: Write narrative and final edits (10-12 hours)
- **Total estimated time: 36-44 hours**

---

## Common Pitfalls to Avoid

1. **Starting too late** - This is a substantial project
2. **Choosing incompatible datasets** - Verify join keys early
3. **Ignoring data limitations** - Address these honestly
4. **Creating charts without purpose** - Each should answer a question
5. **Weak research questions** - Make them specific and answerable
6. **Forgetting to cite sources** - Document everything
7. **Not testing the .twbx file** - Make sure it works!
8. **Exceeding page limit** - Keep narrative focused and concise
9. **Poor figure quality** - Export at high resolution
10. **Last-minute submission** - Allow time for technical issues

---

## Resources

### Tableau Learning
- [Tableau Public Gallery](https://public.tableau.com/gallery)
- [Tableau Training Videos](https://tableau.com/learn/training)
- Course materials and lab examples

### Data Visualization
- Edward Tufte's principles
- ColorBrewer for color schemes: colorbrewer2.org
- Course textbook and readings

### Writing
- [Purdue OWL for APA format](owl.purdue.edu)
- University writing center
- Grammarly or similar tools

### Data Sources
- See list in Phase 1.2 above
- Ask instructor for recommendations
- Check course Canvas page for suggestions

---

## Questions?

- Check the PROJECT_CHECKLIST.md for requirements
- Review this workflow guide
- Consult course materials
- Ask in class or office hours
- Email instructor with specific questions

---

**Remember**: The goal is not just to complete the assignment, but to learn how to tell compelling stories with data. Take your time, be thoughtful, and create something you're proud of!

---

Last Updated: [Date]

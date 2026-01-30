# Data Sources Documentation

## Dataset A (Primary/Fact Dataset)

### Basic Information
- **Dataset Name**: [Full name of dataset]
- **File Name**: `dataset_a_primary.csv`
- **Source URL**: [Direct link to data source]
- **Download Date**: [When you downloaded it]
- **Last Updated by Source**: [When source last updated data]

### Data Collection
- **Collected By**: [Organization/agency/researcher name]
- **Funded By**: [Funding organization or note if not applicable]
- **Collection Method**: [Survey, administrative records, sensors, etc.]
- **Collection Period**: [Start date - End date]

### Purpose and Context
- **Original Purpose**: [Why was this data originally collected?]
- **Intended Use**: [What was it designed to be used for?]
- **Our Use**: [How we're using it for this project]

### Dataset Specifications
- **Number of Records**: [Total rows]
- **Number of Variables**: [Total columns]
- **Time Coverage**: [Date range: YYYY-MM-DD to YYYY-MM-DD]
- **Geographic Coverage**: [Countries, states, cities, etc.]
- **File Size**: [MB/GB]
- **File Format**: CSV / Excel / JSON / Other

### Variables

| Variable Name | Type | Description | Units/Categories | Missing Data? |
|---------------|------|-------------|------------------|---------------|
| [var1] | Categorical | [Description] | [list categories] | [Yes/No - %] |
| [var2] | Numeric | [Description] | [units: dollars, count, etc.] | [Yes/No - %] |
| [var3] | Date | [Description] | [format: YYYY-MM-DD] | [Yes/No - %] |
| [var4] | Geographic | [Description] | [type: state code, ZIP, etc.] | [Yes/No - %] |
| ... | | | | |

### Key Variables for Analysis

#### Time Variable
- **Variable Name**: [e.g., date, year, month]
- **Format**: [e.g., YYYY-MM-DD, YYYY, MM/DD/YYYY]
- **Range**: [earliest to latest]

#### Geographic Variable
- **Variable Name**: [e.g., state, country_code, latitude/longitude]
- **Format**: [e.g., two-letter state code, ISO country code]
- **Coverage**: [list of locations]

#### Numeric Measures (at least 2)
1. **[Measure 1 Name]**: [Description, units]
2. **[Measure 2 Name]**: [Description, units]

#### Categorical Dimensions (at least 2)
1. **[Category 1 Name]**: [Description, list categories]
2. **[Category 2 Name]**: [Description, list categories]

### Data Quality & Limitations
- **Missing Data**: [Describe patterns of missing data]
- **Known Issues**: [Any documented problems with the data]
- **Sample vs. Population**: [Is this a sample or full population?]
- **Bias Concerns**: [Any known biases in collection or representation]
- **Temporal Limitations**: [Timeliness, frequency of updates]
- **Geographic Limitations**: [Coverage gaps, aggregation level issues]
- **Measurement Limitations**: [How variables were measured and any concerns]

### Licensing & Terms of Use
- **License**: [e.g., Public Domain, CC-BY, Open Government License]
- **Attribution Required**: [Yes/No - how to attribute]
- **Restrictions**: [Any use restrictions]

### Citation (APA Format)
[Author/Organization]. (Year). *Dataset name* [Data set]. Source Name. URL

---

## Dataset B (Secondary/Context Dataset)

### Basic Information
- **Dataset Name**: [Full name of dataset]
- **File Name**: `dataset_b_secondary.csv`
- **Source URL**: [Direct link to data source]
- **Download Date**: [When you downloaded it]
- **Last Updated by Source**: [When source last updated data]

### Data Collection
- **Collected By**: [Organization/agency/researcher name]
- **Funded By**: [Funding organization or note if not applicable]
- **Collection Method**: [Survey, administrative records, sensors, etc.]
- **Collection Period**: [Start date - End date]

### Purpose and Context
- **Original Purpose**: [Why was this data originally collected?]
- **Intended Use**: [What was it designed to be used for?]
- **Our Use**: [How we're using it for this project - what context does it add?]

### Dataset Specifications
- **Number of Records**: [Total rows]
- **Number of Variables**: [Total columns]
- **Time Coverage**: [Date range if applicable]
- **Geographic Coverage**: [Countries, states, cities, etc.]
- **File Size**: [MB/GB]
- **File Format**: CSV / Excel / JSON / Other

### Join/Relationship Key
- **Common Field with Dataset A**: [e.g., state_code, country, year, zip_code]
- **Key Type**: [One-to-one, one-to-many, many-to-many]
- **Match Rate**: [What % of records can be joined?]

### Variables

| Variable Name | Type | Description | Units/Categories | Missing Data? |
|---------------|------|-------------|------------------|---------------|
| [var1] | | | | |
| [var2] | | | | |
| ... | | | | |

### New Context Variables (Not in Dataset A)
- **[Variable 1]**: [What context/comparison does this enable?]
- **[Variable 2]**: [What context/comparison does this enable?]

### Data Quality & Limitations
- **Missing Data**: [Describe patterns]
- **Known Issues**: [Any documented problems]
- **Bias Concerns**: [Any known biases]
- **Limitations**: [What this data can and cannot tell us]

### Licensing & Terms of Use
- **License**: [License type]
- **Attribution Required**: [Yes/No - how to attribute]
- **Restrictions**: [Any use restrictions]

### Citation (APA Format)
[Author/Organization]. (Year). *Dataset name* [Data set]. Source Name. URL

---

## Relationship Between Datasets

### Join Strategy
- **Relationship Type**: [Relationship / Join / Blend]
- **Join Field(s)**: [Common field(s) used]
- **Cardinality**: [One-to-one, one-to-many, etc.]
- **Rationale**: [Why this approach makes sense for the analysis]

### Combined Dataset Characteristics
- **Total Records After Join**: [Number]
- **Unmatched Records**: [Number and % from each dataset]
- **New Analytical Capabilities**: [What can we now analyze that we couldn't before?]

---

## Additional Data Sources (if applicable)

### Dataset C (if used)
[Follow same structure as above]

---

## Data Processing Notes

### Cleaning Steps
1. [Step 1: e.g., Removed duplicates]
2. [Step 2: e.g., Standardized date formats]
3. [Step 3: e.g., Handled missing values]
4. [etc.]

### Transformations
1. [Transformation 1: e.g., Created age groups from continuous age]
2. [Transformation 2: e.g., Calculated per capita rates]
3. [etc.]

### Files Created
- `data/processed/merged_data.csv` - [Description]
- [Other processed files]

---

## Reproducibility

### Software Used
- **Tableau Version**: [e.g., Tableau Public 2024.1]
- **Python Version** (if applicable): [e.g., Python 3.11]
- **Required Packages** (if applicable): pandas, numpy, etc.

### Data Download Instructions
1. [Step-by-step instructions to obtain Dataset A]
2. [Step-by-step instructions to obtain Dataset B]
3. [Any API keys or registration required]

### Last Verification Date
- **Dataset A**: [Date you last verified it's still accessible]
- **Dataset B**: [Date you last verified it's still accessible]

---

**Document Last Updated**: [Date]
**Updated By**: [Name]

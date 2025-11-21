# ICD-10-CM Official Coding Guidelines - Key Principles

## Download Official Guidelines

**IMPORTANT**: Download the official ICD-10-CM Guidelines from:
- **CDC FTP**: https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2025/
- **CMS PDF**: https://www.cms.gov/files/document/fy-2025-icd-10-cm-coding-guidelines.pdf
- **CDC STACKS**: https://stacks.cdc.gov/view/cdc/158747

## Section I: Conventions, General Coding Guidelines and Chapter Specific Guidelines

### A. Conventions for ICD-10-CM

#### 1. Format and Structure
- **3-character categories**: Represent a single disease entity (e.g., J44 - Other chronic obstructive pulmonary disease)
- **4-character subcategories**: Provide additional specificity
- **5-7 character codes**: Required for many categories to provide maximum specificity

#### 2. Placeholder Character "X"
- Used to allow for future expansion
- Must be used to fill empty characters when a code requires 7 characters
- Example: T36.0X1A - Poisoning by penicillins, accidental (unintentional), initial encounter

#### 3. 7th Character Extensions
- Certain ICD-10-CM categories require 7th character
- Must ALWAYS be in the 7th character data field
- Common 7th characters:
  - **A** - Initial encounter
  - **D** - Subsequent encounter
  - **S** - Sequela (late effect)
- For injuries/external causes:
  - **A** - Initial encounter for closed fracture
  - **B** - Initial encounter for open fracture
  - **D** - Subsequent encounter for routine healing
  - **K** - Subsequent encounter for delayed healing
  - **S** - Sequela

#### 4. Abbreviations

**NEC** (Not Elsewhere Classifiable)
- Used when ICD-10-CM doesn't provide a code specific enough
- Index entry with NEC directs to "other specified" code
- Example: J44.89 - Other specified chronic obstructive pulmonary disease

**NOS** (Not Otherwise Specified)
- Equivalent to "unspecified"
- Used only when coder lacks information to code more specifically
- Example: J44.9 - Chronic obstructive pulmonary disease, unspecified

#### 5. Includes and Excludes Notes

**Includes Notes**
- List terms for which the code number may be used
- Not exhaustive - further terms found only in index

**Excludes1**
- Mutually exclusive codes
- Two conditions cannot occur together
- Code both conditions if documentation supports
- Example: Excludes1 at J44 indicates conditions not included

**Excludes2**
- Condition is not part of the condition represented by the code
- BUT patient may have both conditions simultaneously
- OK to use both codes if both conditions documented
- Example: Patient can have both COPD (J44) and asthma (J45)

### B. General Coding Guidelines

#### 1. Code Assignment Based on Provider Documentation
- Code assignment based on provider's diagnostic statement
- Only providers (physicians, NPPs) can establish medical diagnosis
- Query provider if documentation is unclear, incomplete, or contradictory

#### 2. Selection of Principal Diagnosis
- **Outpatient**: Code condition, diagnosis, or other reason for visit/service shown in medical record as chiefly responsible
- **Inpatient**: Condition established after study to be chiefly responsible for admission

#### 3. Coding to Highest Level of Specificity
- Assign codes to highest number of characters available
- 3-character code only when no 4th or 5th character subcategory
- Final level of subdivision code must be used
- Do NOT code to a category level when more specific code available

#### 4. Use of "Unspecified" Codes
- Only when information in medical record insufficient for more specific code
- Should rarely be used for inpatient records

#### 5. Combination Codes
- Single code classifies two diagnoses, or diagnosis with manifestation/complication
- Use combination code when available instead of multiple codes
- Example: E11.21 - Type 2 diabetes with diabetic nephropathy

#### 6. Sequencing Rules
- **Principal diagnosis**: Condition established after study chiefly responsible for admission
- **First-listed diagnosis**: Outpatient encounters - code for diagnosis, condition, problem, or reason for encounter/visit
- Code confirmed conditions over suspected/rule out conditions
- Acute conditions before chronic (unless chronic is reason for encounter)

### C. Chapter-Specific Coding Guidelines

#### Chapter 1: Infectious and Parasitic Diseases (A00-B99)

**Sepsis, Severe Sepsis, and Septic Shock**
- Code first underlying systemic infection (A41.9, etc.)
- Use additional code for severe sepsis (R65.2x)
- Code any associated acute organ dysfunction
- Septic shock requires R65.21

**COVID-19**
- Code only confirmed cases (U07.1)
- Do not code suspected, possible, or probable COVID-19
- Code also any manifestations

#### Chapter 4: Endocrine, Nutritional, and Metabolic (E00-E89)

**Diabetes Mellitus**
- Type 1 vs Type 2 must be documented
- Code to type 2 if type not documented
- Use as many codes as necessary to identify all associated conditions
- **E10** - Type 1 diabetes
- **E11** - Type 2 diabetes
- **E08** - Diabetes due to underlying condition
- **E09** - Drug/chemical induced diabetes
- **E13** - Other specified diabetes

**Sequencing**:
1. Code from category E08-E13 identifying type
2. Add 4th/5th/6th characters for complications
3. Use additional codes for manifestations not included in combination code

#### Chapter 10: Diseases of Respiratory System (J00-J99)

**COPD and Asthma**
- **J44.0** - COPD with acute lower respiratory infection
- **J44.1** - COPD with acute exacerbation (use if exacerbation not otherwise specified)
- **J44.9** - COPD, unspecified
- Exacerbation means worsening of chronic condition
- Code acute exacerbation over unspecified

**Acute Respiratory Failure**
- May be principal diagnosis if reason for admission and meets definition
- Chapter 10 codes take priority over general symptoms
- Sequence based on circumstances of admission

#### Chapter 19: Injury, Poisoning (S00-T88)

**Multiple Injuries**
- Code each injury separately unless combination code provided
- Sequence most serious injury first
- Primary injury code for superficial injuries (contusions, abrasions)

**7th Character Extensions Required**
- **A** - Initial encounter (active treatment)
- **D** - Subsequent encounter (routine healing)
- **S** - Sequela (late effect, after active healing)

**Burns**
- Code current burn with 7th character A or D
- Code sequelae with 7th character S
- Sequence:
  1. Severity code (degree of burn)
  2. Extent code (% body surface - T31/T32)
  3. External cause code

#### Chapter 21: External Causes (V00-Y99)

**When to Use**
- Provide cause of injury/condition
- Never used as principal diagnosis
- Code to fullest extent possible
- Used with any code in range A00-T88.9, Z00-Z99

**Activity Codes** (Y93)
- Describe activity when injury/condition occurred
- Only one activity code per encounter

**Place of Occurrence** (Y92)
- Where event occurred
- Only one place code per encounter

### D. Signs and Symptoms

**When to Code**
- Code signs/symptoms when:
  1. No definitive diagnosis established
  2. Signs/symptoms NOT integral to confirmed diagnosis
  3. More specific code not available

**When NOT to Code**
- Don't code sign/symptom if it's:
  - Integral to the disease process
  - Included in the disease code
  - Always associated with the condition

---

## Section II: Selection of Principal Diagnosis (Inpatient)

### Definition
- Condition established after study to be chiefly responsible for occasioning admission

### Guidelines

1. **Two or More Equally Meet Definition**
   - Either may be sequenced first
   - Choose based on circumstances of admission

2. **Symptom Followed by Diagnoses**
   - May sequence symptom first if it occasioned admission
   - Or sequence established diagnosis first

3. **Original Treatment Plan Not Carried Out**
   - Sequence condition that occasioned admission

4. **Admission for Complications**
   - Complication is principal diagnosis if it meets definition

---

## Section III: Reporting Additional Diagnoses (Inpatient)

### Definition
All conditions that coexist at admission, develop subsequently, or affect treatment

### Criteria for Reporting
Code additional diagnoses when they:
- Require clinical evaluation
- Require therapeutic treatment
- Require diagnostic procedures
- Extend hospital stay
- Increase nursing care/monitoring

---

## Section IV: Outpatient Coding Guidelines

### Key Differences from Inpatient

1. **Uncertain Diagnosis**
   - DO NOT code "probable," "suspected," "questionable," "rule out"
   - Code the condition to highest degree of certainty (signs/symptoms)

2. **Chronic Diseases**
   - Code chronic conditions as many times as patient receives treatment

3. **Code All Documented Conditions**
   - Code all documented conditions that coexist and affect care

4. **First-Listed Diagnosis**
   - Reason for visit/service
   - May be sign/symptom if diagnosis not yet established

---

## Common Coding Scenarios for Exam Prep

### Scenario 1: COPD with Acute Exacerbation

**Documentation**: "Patient admitted with COPD exacerbation"

**Correct Coding**:
- **J44.1** - COPD with acute exacerbation, unspecified

**Rationale**: Exacerbation documented, use J44.1 not J44.9

### Scenario 2: Type 2 Diabetes with Multiple Complications

**Documentation**: "Type 2 diabetes with diabetic nephropathy and neuropathy"

**Correct Coding**:
- **E11.21** - Type 2 diabetes with diabetic nephropathy
- **E11.40** - Type 2 diabetes with diabetic neuropathy, unspecified

**Rationale**: Use separate codes for each manifestation

### Scenario 3: Acute Myocardial Infarction

**Documentation**: "STEMI anterior wall, initial episode of care"

**Correct Coding**:
- **I21.09** - ST elevation myocardial infarction involving other coronary artery of anterior wall

**Rationale**: Must specify location and type (STEMI vs NSTEMI)

---

## Key Takeaways for CPC/CCS Exams

1. ✅ **Always code to highest specificity**
2. ✅ **Use combination codes when available**
3. ✅ **Sequence principal/first-listed diagnosis correctly**
4. ✅ **Know difference between Excludes1 and Excludes2**
5. ✅ **7th characters are MANDATORY when required**
6. ✅ **NEC ≠ NOS (different meanings)**
7. ✅ **Query provider for unclear documentation**
8. ✅ **Outpatient: Don't code suspected/probable conditions**
9. ✅ **Code signs/symptoms ONLY if no definitive diagnosis**
10. ✅ **Know chapter-specific guidelines (especially diabetes, injuries, respiratory)**

---

## Study Resources

- **Official Guidelines PDF**: Download from CDC/CMS (links above)
- **AHA Coding Clinic**: Official guidance and scenarios
- **AAPC**: CPC exam preparation materials
- **AHIMA**: CCS exam preparation resources
- **Practice**: Code actual medical records daily

---

**Note**: This is a summary. Always refer to the complete official ICD-10-CM Guidelines for full details and updates.

#!/usr/bin/env python3
"""
Generate comprehensive medical terminology database.
Includes prefixes, suffixes, root words, abbreviations, and complete medical terms.
"""

import pandas as pd
from pathlib import Path


class MedicalTerminologyGenerator:
    """Generate comprehensive medical terminology database."""

    def __init__(self, data_dir: Path = None):
        """Initialize the generator."""
        self.data_dir = data_dir or Path(__file__).parent.parent / "data"
        self.terminology_dir = self.data_dir / "medical_terminology"
        self.terminology_dir.mkdir(parents=True, exist_ok=True)

    def generate_prefixes(self):
        """Generate medical prefixes database."""
        prefixes = [
            # Quantity/Size
            {"term": "a-", "category": "Prefix", "meaning": "without, not", "example": "anemia - without blood", "usage": "Quantity/Size"},
            {"term": "an-", "category": "Prefix", "meaning": "without, not", "example": "anoxia - without oxygen", "usage": "Quantity/Size"},
            {"term": "bi-", "category": "Prefix", "meaning": "two", "example": "bilateral - both sides", "usage": "Quantity/Size"},
            {"term": "mono-", "category": "Prefix", "meaning": "one", "example": "monocyte - single nucleus cell", "usage": "Quantity/Size"},
            {"term": "di-", "category": "Prefix", "meaning": "two", "example": "diabetes - passing through", "usage": "Quantity/Size"},
            {"term": "tri-", "category": "Prefix", "meaning": "three", "example": "tricuspid - three cusps", "usage": "Quantity/Size"},
            {"term": "quad-", "category": "Prefix", "meaning": "four", "example": "quadriplegia - paralysis of four limbs", "usage": "Quantity/Size"},
            {"term": "poly-", "category": "Prefix", "meaning": "many, much", "example": "polyuria - excessive urination", "usage": "Quantity/Size"},
            {"term": "multi-", "category": "Prefix", "meaning": "many", "example": "multifocal - multiple locations", "usage": "Quantity/Size"},
            {"term": "macro-", "category": "Prefix", "meaning": "large", "example": "macrocyte - large red blood cell", "usage": "Quantity/Size"},
            {"term": "micro-", "category": "Prefix", "meaning": "small", "example": "microcephaly - small head", "usage": "Quantity/Size"},
            {"term": "mega-", "category": "Prefix", "meaning": "large", "example": "megacolon - enlarged colon", "usage": "Quantity/Size"},

            # Position/Direction
            {"term": "ab-", "category": "Prefix", "meaning": "away from", "example": "abduction - movement away from midline", "usage": "Position/Direction"},
            {"term": "ad-", "category": "Prefix", "meaning": "toward", "example": "adduction - movement toward midline", "usage": "Position/Direction"},
            {"term": "ante-", "category": "Prefix", "meaning": "before, forward", "example": "antepartum - before childbirth", "usage": "Position/Direction"},
            {"term": "post-", "category": "Prefix", "meaning": "after, behind", "example": "postoperative - after surgery", "usage": "Position/Direction"},
            {"term": "pre-", "category": "Prefix", "meaning": "before", "example": "prenatal - before birth", "usage": "Position/Direction"},
            {"term": "retro-", "category": "Prefix", "meaning": "backward, behind", "example": "retroperitoneal - behind peritoneum", "usage": "Position/Direction"},
            {"term": "sub-", "category": "Prefix", "meaning": "below, under", "example": "subcutaneous - under the skin", "usage": "Position/Direction"},
            {"term": "super-", "category": "Prefix", "meaning": "above, over", "example": "suprapubic - above the pubis", "usage": "Position/Direction"},
            {"term": "supra-", "category": "Prefix", "meaning": "above, over", "example": "supraventricular - above ventricles", "usage": "Position/Direction"},
            {"term": "infra-", "category": "Prefix", "meaning": "below", "example": "infraorbital - below the orbit", "usage": "Position/Direction"},
            {"term": "inter-", "category": "Prefix", "meaning": "between", "example": "intercostal - between ribs", "usage": "Position/Direction"},
            {"term": "intra-", "category": "Prefix", "meaning": "within", "example": "intravenous - within a vein", "usage": "Position/Direction"},
            {"term": "peri-", "category": "Prefix", "meaning": "around", "example": "pericardium - sac around heart", "usage": "Position/Direction"},
            {"term": "circum-", "category": "Prefix", "meaning": "around", "example": "circumference - distance around", "usage": "Position/Direction"},
            {"term": "trans-", "category": "Prefix", "meaning": "across, through", "example": "transdermal - through the skin", "usage": "Position/Direction"},
            {"term": "endo-", "category": "Prefix", "meaning": "within", "example": "endoscopy - looking within", "usage": "Position/Direction"},
            {"term": "exo-", "category": "Prefix", "meaning": "outside", "example": "exocrine - secreting outward", "usage": "Position/Direction"},
            {"term": "extra-", "category": "Prefix", "meaning": "outside", "example": "extracellular - outside cell", "usage": "Position/Direction"},

            # Condition/Quality
            {"term": "hyper-", "category": "Prefix", "meaning": "excessive, above", "example": "hypertension - high blood pressure", "usage": "Condition/Quality"},
            {"term": "hypo-", "category": "Prefix", "meaning": "deficient, below", "example": "hypothyroid - underactive thyroid", "usage": "Condition/Quality"},
            {"term": "brady-", "category": "Prefix", "meaning": "slow", "example": "bradycardia - slow heart rate", "usage": "Condition/Quality"},
            {"term": "tachy-", "category": "Prefix", "meaning": "fast", "example": "tachypnea - rapid breathing", "usage": "Condition/Quality"},
            {"term": "dys-", "category": "Prefix", "meaning": "bad, difficult, painful", "example": "dyspnea - difficult breathing", "usage": "Condition/Quality"},
            {"term": "eu-", "category": "Prefix", "meaning": "good, normal", "example": "eupnea - normal breathing", "usage": "Condition/Quality"},
            {"term": "mal-", "category": "Prefix", "meaning": "bad", "example": "malnutrition - poor nutrition", "usage": "Condition/Quality"},
            {"term": "pan-", "category": "Prefix", "meaning": "all", "example": "pancytopenia - deficiency of all blood cells", "usage": "Condition/Quality"},
            {"term": "neo-", "category": "Prefix", "meaning": "new", "example": "neoplasm - new growth (tumor)", "usage": "Condition/Quality"},
            {"term": "pseudo-", "category": "Prefix", "meaning": "false", "example": "pseudocyst - false cyst", "usage": "Condition/Quality"},

            # Negation
            {"term": "anti-", "category": "Prefix", "meaning": "against", "example": "antibiotic - against bacteria", "usage": "Negation"},
            {"term": "contra-", "category": "Prefix", "meaning": "against, opposite", "example": "contraindicated - not recommended", "usage": "Negation"},
            {"term": "de-", "category": "Prefix", "meaning": "removal, reversal", "example": "dehydration - removal of water", "usage": "Negation"},
        ]

        return prefixes

    def generate_suffixes(self):
        """Generate medical suffixes database."""
        suffixes = [
            # Diagnostic Suffixes
            {"term": "-algia", "category": "Suffix", "meaning": "pain", "example": "neuralgia - nerve pain", "usage": "Diagnostic/Condition"},
            {"term": "-dynia", "category": "Suffix", "meaning": "pain", "example": "pleurodynia - chest wall pain", "usage": "Diagnostic/Condition"},
            {"term": "-emia", "category": "Suffix", "meaning": "blood condition", "example": "anemia - low red blood cells", "usage": "Diagnostic/Condition"},
            {"term": "-itis", "category": "Suffix", "meaning": "inflammation", "example": "appendicitis - appendix inflammation", "usage": "Diagnostic/Condition"},
            {"term": "-osis", "category": "Suffix", "meaning": "abnormal condition", "example": "nephrosis - kidney disease", "usage": "Diagnostic/Condition"},
            {"term": "-pathy", "category": "Suffix", "meaning": "disease", "example": "neuropathy - nerve disease", "usage": "Diagnostic/Condition"},
            {"term": "-megaly", "category": "Suffix", "meaning": "enlargement", "example": "hepatomegaly - enlarged liver", "usage": "Diagnostic/Condition"},
            {"term": "-malacia", "category": "Suffix", "meaning": "softening", "example": "osteomalacia - bone softening", "usage": "Diagnostic/Condition"},
            {"term": "-sclerosis", "category": "Suffix", "meaning": "hardening", "example": "arteriosclerosis - artery hardening", "usage": "Diagnostic/Condition"},
            {"term": "-stenosis", "category": "Suffix", "meaning": "narrowing", "example": "aortic stenosis - aortic valve narrowing", "usage": "Diagnostic/Condition"},
            {"term": "-ectasis", "category": "Suffix", "meaning": "dilation, expansion", "example": "bronchiectasis - bronchial dilation", "usage": "Diagnostic/Condition"},
            {"term": "-rrhage", "category": "Suffix", "meaning": "excessive bleeding", "example": "hemorrhage - excessive bleeding", "usage": "Diagnostic/Condition"},
            {"term": "-rrhagia", "category": "Suffix", "meaning": "excessive bleeding", "example": "menorrhagia - heavy menstrual bleeding", "usage": "Diagnostic/Condition"},
            {"term": "-rrhea", "category": "Suffix", "meaning": "flow, discharge", "example": "diarrhea - watery stool discharge", "usage": "Diagnostic/Condition"},
            {"term": "-rrhexis", "category": "Suffix", "meaning": "rupture", "example": "cardiorrhexis - heart rupture", "usage": "Diagnostic/Condition"},
            {"term": "-plegia", "category": "Suffix", "meaning": "paralysis", "example": "hemiplegia - one-sided paralysis", "usage": "Diagnostic/Condition"},
            {"term": "-plasia", "category": "Suffix", "meaning": "formation, growth", "example": "hyperplasia - excessive cell growth", "usage": "Diagnostic/Condition"},
            {"term": "-trophy", "category": "Suffix", "meaning": "development, nourishment", "example": "hypertrophy - increase in size", "usage": "Diagnostic/Condition"},
            {"term": "-oma", "category": "Suffix", "meaning": "tumor, mass", "example": "carcinoma - cancerous tumor", "usage": "Diagnostic/Condition"},
            {"term": "-cele", "category": "Suffix", "meaning": "hernia, protrusion", "example": "rectocele - rectal hernia", "usage": "Diagnostic/Condition"},
            {"term": "-ptosis", "category": "Suffix", "meaning": "drooping, sagging", "example": "nephroptosis - drooping kidney", "usage": "Diagnostic/Condition"},
            {"term": "-penia", "category": "Suffix", "meaning": "deficiency", "example": "leukopenia - low white blood cells", "usage": "Diagnostic/Condition"},

            # Procedural Suffixes
            {"term": "-ectomy", "category": "Suffix", "meaning": "surgical removal", "example": "appendectomy - appendix removal", "usage": "Surgical Procedure"},
            {"term": "-otomy", "category": "Suffix", "meaning": "cutting into", "example": "tracheotomy - cutting into trachea", "usage": "Surgical Procedure"},
            {"term": "-ostomy", "category": "Suffix", "meaning": "creating opening", "example": "colostomy - colon opening", "usage": "Surgical Procedure"},
            {"term": "-plasty", "category": "Suffix", "meaning": "surgical repair", "example": "rhinoplasty - nose repair", "usage": "Surgical Procedure"},
            {"term": "-rraphy", "category": "Suffix", "meaning": "suturing", "example": "herniorrhaphy - hernia repair", "usage": "Surgical Procedure"},
            {"term": "-pexy", "category": "Suffix", "meaning": "surgical fixation", "example": "nephropexy - kidney fixation", "usage": "Surgical Procedure"},
            {"term": "-desis", "category": "Suffix", "meaning": "surgical binding/fusion", "example": "arthrodesis - joint fusion", "usage": "Surgical Procedure"},
            {"term": "-tripsy", "category": "Suffix", "meaning": "crushing", "example": "lithotripsy - stone crushing", "usage": "Surgical Procedure"},
            {"term": "-centesis", "category": "Suffix", "meaning": "surgical puncture", "example": "thoracentesis - chest puncture", "usage": "Diagnostic Procedure"},
            {"term": "-scopy", "category": "Suffix", "meaning": "visual examination", "example": "colonoscopy - colon examination", "usage": "Diagnostic Procedure"},
            {"term": "-graphy", "category": "Suffix", "meaning": "process of recording", "example": "radiography - X-ray imaging", "usage": "Diagnostic Procedure"},
            {"term": "-gram", "category": "Suffix", "meaning": "record, image", "example": "electrocardiogram - heart tracing", "usage": "Diagnostic Procedure"},
            {"term": "-lysis", "category": "Suffix", "meaning": "breakdown, destruction", "example": "hemolysis - blood cell destruction", "usage": "Procedure/Condition"},

            # Descriptive Suffixes
            {"term": "-ac", "category": "Suffix", "meaning": "pertaining to", "example": "cardiac - pertaining to heart", "usage": "Descriptive"},
            {"term": "-al", "category": "Suffix", "meaning": "pertaining to", "example": "renal - pertaining to kidney", "usage": "Descriptive"},
            {"term": "-ar", "category": "Suffix", "meaning": "pertaining to", "example": "muscular - pertaining to muscle", "usage": "Descriptive"},
            {"term": "-ic", "category": "Suffix", "meaning": "pertaining to", "example": "gastric - pertaining to stomach", "usage": "Descriptive"},
            {"term": "-ical", "category": "Suffix", "meaning": "pertaining to", "example": "surgical - pertaining to surgery", "usage": "Descriptive"},
            {"term": "-ous", "category": "Suffix", "meaning": "pertaining to", "example": "venous - pertaining to veins", "usage": "Descriptive"},
            {"term": "-oid", "category": "Suffix", "meaning": "resembling", "example": "mucoid - resembling mucus", "usage": "Descriptive"},
            {"term": "-form", "category": "Suffix", "meaning": "shaped like", "example": "fusiform - spindle-shaped", "usage": "Descriptive"},
        ]

        return suffixes

    def generate_root_words(self):
        """Generate medical root words database."""
        roots = [
            # Cardiovascular
            {"term": "cardi/o", "category": "Root", "meaning": "heart", "example": "cardiology, myocardial", "usage": "Cardiovascular System"},
            {"term": "angi/o", "category": "Root", "meaning": "vessel", "example": "angiography, angioplasty", "usage": "Cardiovascular System"},
            {"term": "arteri/o", "category": "Root", "meaning": "artery", "example": "arteriosclerosis", "usage": "Cardiovascular System"},
            {"term": "ven/o", "category": "Root", "meaning": "vein", "example": "venous, intravenous", "usage": "Cardiovascular System"},
            {"term": "phleb/o", "category": "Root", "meaning": "vein", "example": "phlebotomy, phlebitis", "usage": "Cardiovascular System"},
            {"term": "hem/o", "category": "Root", "meaning": "blood", "example": "hematoma, hemoglobin", "usage": "Cardiovascular System"},
            {"term": "hemat/o", "category": "Root", "meaning": "blood", "example": "hematology", "usage": "Cardiovascular System"},
            {"term": "thromb/o", "category": "Root", "meaning": "clot", "example": "thrombosis, thrombus", "usage": "Cardiovascular System"},
            {"term": "embol/o", "category": "Root", "meaning": "plug, clot", "example": "embolism, embolus", "usage": "Cardiovascular System"},

            # Respiratory
            {"term": "pneum/o", "category": "Root", "meaning": "lung, air", "example": "pneumonia, pneumothorax", "usage": "Respiratory System"},
            {"term": "pulm/o", "category": "Root", "meaning": "lung", "example": "pulmonary", "usage": "Respiratory System"},
            {"term": "bronch/o", "category": "Root", "meaning": "bronchus", "example": "bronchitis, bronchoscopy", "usage": "Respiratory System"},
            {"term": "alveol/o", "category": "Root", "meaning": "alveolus (air sac)", "example": "alveolar", "usage": "Respiratory System"},
            {"term": "laryng/o", "category": "Root", "meaning": "larynx (voice box)", "example": "laryngitis, laryngoscopy", "usage": "Respiratory System"},
            {"term": "trache/o", "category": "Root", "meaning": "trachea (windpipe)", "example": "tracheostomy, tracheal", "usage": "Respiratory System"},
            {"term": "nas/o", "category": "Root", "meaning": "nose", "example": "nasal", "usage": "Respiratory System"},
            {"term": "rhin/o", "category": "Root", "meaning": "nose", "example": "rhinitis, rhinoplasty", "usage": "Respiratory System"},
            {"term": "pharyng/o", "category": "Root", "meaning": "pharynx (throat)", "example": "pharyngitis", "usage": "Respiratory System"},
            {"term": "ox/o", "category": "Root", "meaning": "oxygen", "example": "hypoxia, anoxia", "usage": "Respiratory System"},
            {"term": "capn/o", "category": "Root", "meaning": "carbon dioxide", "example": "hypercapnia", "usage": "Respiratory System"},

            # Gastrointestinal
            {"term": "gastr/o", "category": "Root", "meaning": "stomach", "example": "gastritis, gastric", "usage": "Gastrointestinal System"},
            {"term": "enter/o", "category": "Root", "meaning": "intestine", "example": "gastroenteritis, enteral", "usage": "Gastrointestinal System"},
            {"term": "col/o", "category": "Root", "meaning": "colon", "example": "colitis, colonoscopy", "usage": "Gastrointestinal System"},
            {"term": "hepat/o", "category": "Root", "meaning": "liver", "example": "hepatitis, hepatomegaly", "usage": "Gastrointestinal System"},
            {"term": "cholecyst/o", "category": "Root", "meaning": "gallbladder", "example": "cholecystitis, cholecystectomy", "usage": "Gastrointestinal System"},
            {"term": "pancreat/o", "category": "Root", "meaning": "pancreas", "example": "pancreatitis, pancreatic", "usage": "Gastrointestinal System"},
            {"term": "esophag/o", "category": "Root", "meaning": "esophagus", "example": "esophageal, esophagitis", "usage": "Gastrointestinal System"},
            {"term": "proct/o", "category": "Root", "meaning": "rectum, anus", "example": "proctology, proctoscopy", "usage": "Gastrointestinal System"},

            # Urinary
            {"term": "nephr/o", "category": "Root", "meaning": "kidney", "example": "nephrology, nephropathy", "usage": "Urinary System"},
            {"term": "ren/o", "category": "Root", "meaning": "kidney", "example": "renal", "usage": "Urinary System"},
            {"term": "ur/o", "category": "Root", "meaning": "urine, urinary tract", "example": "urology, urinalysis", "usage": "Urinary System"},
            {"term": "cyst/o", "category": "Root", "meaning": "bladder, sac", "example": "cystitis, cystoscopy", "usage": "Urinary System"},
            {"term": "ureter/o", "category": "Root", "meaning": "ureter", "example": "ureteral, ureteroscopy", "usage": "Urinary System"},
            {"term": "urethr/o", "category": "Root", "meaning": "urethra", "example": "urethritis, urethral", "usage": "Urinary System"},

            # Musculoskeletal
            {"term": "oste/o", "category": "Root", "meaning": "bone", "example": "osteoporosis, osteomyelitis", "usage": "Musculoskeletal System"},
            {"term": "arthr/o", "category": "Root", "meaning": "joint", "example": "arthritis, arthroscopy", "usage": "Musculoskeletal System"},
            {"term": "my/o", "category": "Root", "meaning": "muscle", "example": "myopathy, myocardial", "usage": "Musculoskeletal System"},
            {"term": "chondr/o", "category": "Root", "meaning": "cartilage", "example": "chondromalacia, chondral", "usage": "Musculoskeletal System"},
            {"term": "ten/o", "category": "Root", "meaning": "tendon", "example": "tendonitis, tendinopathy", "usage": "Musculoskeletal System"},
            {"term": "cost/o", "category": "Root", "meaning": "rib", "example": "costal, intercostal", "usage": "Musculoskeletal System"},

            # Nervous
            {"term": "neur/o", "category": "Root", "meaning": "nerve", "example": "neurology, neuropathy", "usage": "Nervous System"},
            {"term": "cerebr/o", "category": "Root", "meaning": "cerebrum", "example": "cerebral, cerebrovascular", "usage": "Nervous System"},
            {"term": "encephal/o", "category": "Root", "meaning": "brain", "example": "encephalopathy, encephalitis", "usage": "Nervous System"},
            {"term": "mening/o", "category": "Root", "meaning": "meninges", "example": "meningitis, meningeal", "usage": "Nervous System"},
            {"term": "myel/o", "category": "Root", "meaning": "spinal cord, bone marrow", "example": "myelopathy, myeloma", "usage": "Nervous System"},

            # Endocrine
            {"term": "glyc/o", "category": "Root", "meaning": "sugar, glucose", "example": "glycemia, hypoglycemia", "usage": "Endocrine System"},
            {"term": "gluc/o", "category": "Root", "meaning": "sugar, glucose", "example": "glucose", "usage": "Endocrine System"},
            {"term": "thyr/o", "category": "Root", "meaning": "thyroid", "example": "thyroid, hypothyroid", "usage": "Endocrine System"},
            {"term": "adren/o", "category": "Root", "meaning": "adrenal gland", "example": "adrenal, adrenaline", "usage": "Endocrine System"},

            # Integumentary
            {"term": "derm/o", "category": "Root", "meaning": "skin", "example": "dermatology, dermatitis", "usage": "Integumentary System"},
            {"term": "dermat/o", "category": "Root", "meaning": "skin", "example": "dermatologist", "usage": "Integumentary System"},
            {"term": "cutane/o", "category": "Root", "meaning": "skin", "example": "subcutaneous, cutaneous", "usage": "Integumentary System"},
        ]

        return roots

    def generate_abbreviations(self):
        """Generate medical abbreviations database."""
        abbrevs = [
            # Vital Signs
            {"term": "BP", "category": "Abbreviation", "meaning": "Blood Pressure", "example": "BP 120/80", "usage": "Vital Signs"},
            {"term": "HR", "category": "Abbreviation", "meaning": "Heart Rate", "example": "HR 75 bpm", "usage": "Vital Signs"},
            {"term": "RR", "category": "Abbreviation", "meaning": "Respiratory Rate", "example": "RR 16", "usage": "Vital Signs"},
            {"term": "T", "category": "Abbreviation", "meaning": "Temperature", "example": "T 98.6°F", "usage": "Vital Signs"},
            {"term": "SpO2", "category": "Abbreviation", "meaning": "Oxygen Saturation", "example": "SpO2 98%", "usage": "Vital Signs"},

            # Common Conditions
            {"term": "MI", "category": "Abbreviation", "meaning": "Myocardial Infarction", "example": "Acute MI", "usage": "Cardiovascular"},
            {"term": "CHF", "category": "Abbreviation", "meaning": "Congestive Heart Failure", "example": "CHF exacerbation", "usage": "Cardiovascular"},
            {"term": "COPD", "category": "Abbreviation", "meaning": "Chronic Obstructive Pulmonary Disease", "example": "COPD with exacerbation", "usage": "Respiratory"},
            {"term": "CAD", "category": "Abbreviation", "meaning": "Coronary Artery Disease", "example": "History of CAD", "usage": "Cardiovascular"},
            {"term": "CVA", "category": "Abbreviation", "meaning": "Cerebrovascular Accident", "example": "Acute CVA (stroke)", "usage": "Neurological"},
            {"term": "DM", "category": "Abbreviation", "meaning": "Diabetes Mellitus", "example": "Type 2 DM", "usage": "Endocrine"},
            {"term": "HTN", "category": "Abbreviation", "meaning": "Hypertension", "example": "Essential HTN", "usage": "Cardiovascular"},
            {"term": "UTI", "category": "Abbreviation", "meaning": "Urinary Tract Infection", "example": "Recurrent UTI", "usage": "Urinary"},
            {"term": "DVT", "category": "Abbreviation", "meaning": "Deep Vein Thrombosis", "example": "Left leg DVT", "usage": "Cardiovascular"},
            {"term": "PE", "category": "Abbreviation", "meaning": "Pulmonary Embolism", "example": "Acute PE", "usage": "Respiratory"},
            {"term": "CKD", "category": "Abbreviation", "meaning": "Chronic Kidney Disease", "example": "CKD Stage 3", "usage": "Urinary"},

            # Lab Tests
            {"term": "CBC", "category": "Abbreviation", "meaning": "Complete Blood Count", "example": "CBC ordered", "usage": "Laboratory"},
            {"term": "BMP", "category": "Abbreviation", "meaning": "Basic Metabolic Panel", "example": "BMP results", "usage": "Laboratory"},
            {"term": "CMP", "category": "Abbreviation", "meaning": "Comprehensive Metabolic Panel", "example": "CMP ordered", "usage": "Laboratory"},
            {"term": "ABG", "category": "Abbreviation", "meaning": "Arterial Blood Gas", "example": "ABG shows hypoxia", "usage": "Laboratory"},
            {"term": "HbA1c", "category": "Abbreviation", "meaning": "Hemoglobin A1c", "example": "HbA1c 7.2%", "usage": "Laboratory"},
            {"term": "TSH", "category": "Abbreviation", "meaning": "Thyroid Stimulating Hormone", "example": "TSH elevated", "usage": "Laboratory"},
            {"term": "PT/INR", "category": "Abbreviation", "meaning": "Prothrombin Time/International Normalized Ratio", "example": "INR 2.5", "usage": "Laboratory"},

            # Imaging
            {"term": "CXR", "category": "Abbreviation", "meaning": "Chest X-Ray", "example": "CXR shows infiltrate", "usage": "Radiology"},
            {"term": "CT", "category": "Abbreviation", "meaning": "Computed Tomography", "example": "CT scan abdomen", "usage": "Radiology"},
            {"term": "MRI", "category": "Abbreviation", "meaning": "Magnetic Resonance Imaging", "example": "MRI brain", "usage": "Radiology"},
            {"term": "US", "category": "Abbreviation", "meaning": "Ultrasound", "example": "US abdomen", "usage": "Radiology"},
            {"term": "EKG", "category": "Abbreviation", "meaning": "Electrocardiogram", "example": "EKG shows STEMI", "usage": "Diagnostic"},

            # Routes/Timing
            {"term": "PO", "category": "Abbreviation", "meaning": "by mouth (per os)", "example": "PO medication", "usage": "Medication"},
            {"term": "IV", "category": "Abbreviation", "meaning": "intravenous", "example": "IV antibiotics", "usage": "Medication"},
            {"term": "IM", "category": "Abbreviation", "meaning": "intramuscular", "example": "IM injection", "usage": "Medication"},
            {"term": "SubQ", "category": "Abbreviation", "meaning": "subcutaneous", "example": "SubQ insulin", "usage": "Medication"},
            {"term": "bid", "category": "Abbreviation", "meaning": "twice daily", "example": "Metformin 1000mg bid", "usage": "Medication"},
            {"term": "tid", "category": "Abbreviation", "meaning": "three times daily", "example": "Amoxicillin tid", "usage": "Medication"},
            {"term": "qid", "category": "Abbreviation", "meaning": "four times daily", "example": "Pain medication qid", "usage": "Medication"},
            {"term": "prn", "category": "Abbreviation", "meaning": "as needed", "example": "Tylenol prn pain", "usage": "Medication"},
            {"term": "stat", "category": "Abbreviation", "meaning": "immediately", "example": "Labs stat", "usage": "Medical Order"},
        ]

        return abbrevs

    def generate_all_terminology(self):
        """Generate complete medical terminology database."""
        print("=" * 70)
        print("Medical Terminology Database Generator")
        print("=" * 70)

        # Combine all terminology
        all_terms = []

        print("\nGenerating prefixes...")
        all_terms.extend(self.generate_prefixes())

        print("Generating suffixes...")
        all_terms.extend(self.generate_suffixes())

        print("Generating root words...")
        all_terms.extend(self.generate_root_words())

        print("Generating abbreviations...")
        all_terms.extend(self.generate_abbreviations())

        # Create DataFrame
        df = pd.DataFrame(all_terms)

        # Save to CSV
        output_path = self.terminology_dir / "medical_terminology.csv"
        df.to_csv(output_path, index=False)

        print(f"\n✓ Generated {len(df):,} medical terminology entries")
        print(f"✓ Saved to {output_path}")

        # Display statistics
        print(f"\nTerminology by Category:")
        for category, count in df['category'].value_counts().items():
            print(f"  {category}: {count:,} entries")

        print(f"\nTerminology by Usage:")
        for usage, count in df['usage'].value_counts().head(10).items():
            print(f"  {usage}: {count:,} entries")

        return df


def main():
    generator = MedicalTerminologyGenerator()
    df = generator.generate_all_terminology()

    print("\n" + "=" * 70)
    print("✓ Medical Terminology Database Complete!")
    print("=" * 70)
    print(f"\nTotal entries: {len(df):,}")
    print("\nThis database can be integrated with the RAG system for:")
    print("  - Understanding medical documentation")
    print("  - Decoding medical terms")
    print("  - Professional healthcare communication")
    print("  - Accurate medical coding")


if __name__ == "__main__":
    main()

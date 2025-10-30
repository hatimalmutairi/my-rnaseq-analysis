#!/usr/bin/env python3
"""
RNA-seq Quality Control Analysis

This script analyzes sample metadata and performs basic QC checks.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def load_samples(samples_file):
    """Load and validate sample metadata"""
    samples = pd.read_csv(samples_file)
    print(f"📊 Loaded {len(samples)} samples")
    
    # Check for required columns
    required_cols = ['sample_id', 'condition', 'replicate']
    missing_cols = [col for col in required_cols if col not in samples.columns]
    
    if missing_cols:
        print(f"❌ Missing required columns: {missing_cols}")
        return None
        
    print(f"✅ Found conditions: {list(samples['condition'].unique())}")
    return samples

def create_sample_overview(samples, output_dir="results"):
    """Create overview plots of sample distribution"""
    Path(output_dir).mkdir(exist_ok=True)
    
    # Sample counts by condition
    condition_counts = samples['condition'].value_counts()
    
    plt.figure(figsize=(10, 6))
    condition_counts.plot(kind='bar', color=['skyblue', 'lightcoral'])
    plt.title('Sample Distribution by Condition')
    plt.ylabel('Number of Samples')
    plt.xlabel('Condition')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    output_file = Path(output_dir) / "sample_distribution.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"📈 Plot saved: {output_file}")
    
    return condition_counts

def main():
    """Main analysis function"""
    print("🧬 Starting RNA-seq Quality Control Analysis")
    
    # Load sample data
    samples = load_samples("data/samples.csv")
    if samples is None:
        return
    
    # Create overview plots
    condition_counts = create_sample_overview(samples)
    
    # Print summary
    print(f"\n📋 Analysis Summary:")
    print(f"   Total samples: {len(samples)}")
    print(f"   Conditions: {len(condition_counts)}")
    print(f"   Batches: {len(samples['batch'].unique()) if 'batch' in samples.columns else 'Not specified'}")
    
    print("✅ Quality control analysis completed!")

if __name__ == "__main__":
    main()
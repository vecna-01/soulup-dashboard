"""
SOULUP - Sample Data Generator
Creates realistic sample data for testing
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_therapist_data():
    """Generate therapist profiles"""
    therapists = {
        'therapist_id': range(1, 269),  # 268 therapists
        'name': [f'Therapist_{i}' for i in range(1, 269)],
        'specializations': [
            random.choice(['anxiety,stress,mindfulness', 
                         'depression,relationships,grief',
                         'trauma,ocd,anxiety',
                         'career,relationships,stress',
                         'sleep,mindfulness,stress'])
            for _ in range(268)
        ],
        'experience_years': [random.randint(1, 15) for _ in range(268)],
        'rating': [round(random.uniform(4.0, 5.0), 1) for _ in range(268)],
        'availability_hours': [random.randint(5, 20) for _ in range(268)],
        'completion_rate': [round(random.uniform(0.65, 0.98), 2) for _ in range(268)],
        'total_sessions': [random.randint(50, 150) for _ in range(268)]
    }
    return pd.DataFrame(therapists)

def generate_booking_data(num_bookings=1000):
    """Generate booking records"""
    start_date = datetime(2025, 7, 1)
    bookings = {
        'booking_id': range(1, num_bookings + 1),
        'user_id': [random.randint(1000, 2500) for _ in range(num_bookings)],
        'therapist_id': [random.randint(1, 268) for _ in range(num_bookings)],
        'booking_date': [start_date + timedelta(days=random.randint(0, 270)) 
                        for _ in range(num_bookings)],
        'session_date': [start_date + timedelta(days=random.randint(1, 300)) 
                        for _ in range(num_bookings)],
        'status': [random.choice(['completed', 'scheduled', 'cancelled', 'no_show']) 
                  for _ in range(num_bookings)],
        'amount': [random.choice([2000, 3000, 4000, 5000, 6000, 7000]) 
                  for _ in range(num_bookings)],
        'refund': [1 if random.random() < 0.06 else 0 for _ in range(num_bookings)],
        'rating': [round(random.uniform(3.5, 5.0), 1) if random.random() > 0.15 else None 
                  for _ in range(num_bookings)]
    }
    return pd.DataFrame(bookings)

def generate_group_data(num_programs=30):
    """Generate group program data"""
    programs = {
        'program_id': range(101, 101 + num_programs),
        'name': [f'Program_{i}' for i in range(1, num_programs + 1)],
        'focus_area': [random.choice(['anxiety', 'depression', 'relationships', 
                                     'stress', 'mindfulness', 'sleep']) 
                      for _ in range(num_programs)],
        'difficulty': [random.choice(['beginner', 'intermediate', 'advanced']) 
                      for _ in range(num_programs)],
        'duration_weeks': [random.choice([4, 6, 8, 10]) for _ in range(num_programs)],
        'capacity': [random.randint(10, 30) for _ in range(num_programs)],
        'current_enrollment': [random.randint(5, 25) for _ in range(num_programs)],
        'completion_rate': [round(random.uniform(0.65, 0.95), 2) for _ in range(num_programs)],
        'satisfaction': [round(random.uniform(4.0, 5.0), 1) for _ in range(num_programs)]
    }
    return pd.DataFrame(programs)

def save_data_to_csv():
    """Generate and save all data"""
    print("=" * 60)
    print("GENERATING SAMPLE DATA")
    print("=" * 60)
    
    # Generate therapists
    therapists = generate_therapist_data()
    therapists.to_csv('data/therapists.csv', index=False)
    print(f"✓ Generated {len(therapists)} therapist profiles")
    
    # Generate bookings
    bookings = generate_booking_data(1000)
    bookings.to_csv('data/bookings.csv', index=False)
    print(f"✓ Generated {len(bookings)} booking records")
    
    # Generate groups
    groups = generate_group_data(30)
    groups.to_csv('data/group_programs.csv', index=False)
    print(f"✓ Generated {len(groups)} group programs")
    
    print("\n" + "=" * 60)
    print("DATA FILES CREATED IN 'data/' FOLDER")
    print("=" * 60)
    
    return therapists, bookings, groups

if __name__ == "__main__":
    save_data_to_csv()

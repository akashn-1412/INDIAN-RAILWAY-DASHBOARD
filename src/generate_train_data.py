import pandas as pd
import random

# Define categories
train_names = [
    "Hazrat Nizamuddin - Secunderabad Rajdhani Express", "Secunderabad - Hazrat Nizamuddin Rajdhani Express",
    "Pune - Secunderabad Shatabdi Express", "Secunderabad - Pune Shatabdi Express", "Karnataka Express",
    "Jhelum Express", "Punjab Mail", "Guwahati - Dibrugarh Rajdhani Express", "New Delhi - Kolkata Duronto Express",
    "Mumbai - Ahmedabad Shatabdi Express", "Chennai - Mysore Shatabdi Express", "Goa Express", "Howrah - Ranchi Shatabdi Express",
    "Kerala Express", "Tamil Nadu Express", "Maharashtra Express", "Himachal Express", "Himsagar Express", "Ganga Kaveri Express",
    "Grand Trunk Express", "Dadar - Amritsar Express", "Andaman Express", "Swaraj Express", "Gitanjali Express",
    "Tamil Nadu Sampark Kranti Express", "Guwahati - Thiruvananthapuram Express", "Rajasthan Sampark Kranti Express",
    "Deccan Queen", "Mumbai - LTT Duronto Express", "Amritsar - Haridwar Jan Shatabdi Express", "Gatimaan Express",
    "Delhi - Agra Cantt. Gatimaan Express", "Agra Cantt. - Delhi Gatimaan Express", "Howrah - New Jalpaiguri Shatabdi Express",
    "New Jalpaiguri - Howrah Shatabdi Express", "Yuva Express", "Ananya Express", "Bhopal Shatabdi Express",
    "Lucknow Shatabdi Express", "Amritsar Shatabdi Express", "Kalka Shatabdi Express", "Ajmer Shatabdi Express",
    "Bandra Terminus - Gandhidham Express", "Gandhidham - Bandra Terminus Express", "Dadar - Tirunelveli Chalukya Express",
    "Tirunelveli - Dadar Chalukya Express", "Amritsar - Kochuveli Express", "Kochuveli - Amritsar Express",
    "Karnavati Express", "Saurashtra Mail", "Gujarat Mail", "Avantika Express", "Uday Express", "Purna Express",
    "Sewagram Express", "Hampi Express", "Netravati Express", "Madgaon - Mumbai LTT AC Double Decker Express",
    "Mumbai LTT - Madgaon AC Double Decker Express", "Prayagraj Express", "Gorakhpur - Lokmanya Tilak Terminus Express",
    "Lokmanya Tilak Terminus - Gorakhpur Express", "Hatia - Patna Express", "Lal Quila Express", "Doon Express",
    "Maharaja Express", "Golden Chariot", "Palace on Wheels", "Fairy Queen Express", "Himalayan Queen",
    "Mandovi Express", "Konkan Kanya Express", "Jan Shatabdi Express", "Bhagalpur - Anand Vihar Terminal Vikramshila Express",
    "Anand Vihar Terminal - Bhagalpur Vikramshila Express", "Humsafar Express", "Anand Vihar Terminal - Gorakhpur Humsafar Express",
    "Howrah - Yeshvantpur Duronto Express", "Yeshvantpur - Howrah Duronto Express", "Mumbai - Ahmedabad Double Decker Express",
    "Ahmedabad - Mumbai Double Decker Express", "Chennai - Coimbatore Shatabdi Express", "Coimbatore - Chennai Shatabdi Express",
    "Visakhapatnam - Secunderabad Garib Rath Express", "Secunderabad - Visakhapatnam Garib Rath Express",
    "Ajmer - Jammu Tawi Garib Rath Express", "Jammu Tawi - Ajmer Garib Rath Express", "Indore - Jammu Tawi Malwa Express",
    "Jammu Tawi - Indore Malwa Express", "Howrah - Bhubaneswar Jan Shatabdi Express", "Bhubaneswar - Howrah Jan Shatabdi Express",
    "Dibrugarh - Rajendra Nagar Weekly Express", "Rajendra Nagar - Dibrugarh Weekly Express", "Kamakhya - Ranchi Weekly Express",
    "Ranchi - Kamakhya Weekly Express", "Jammu Tawi - Pune Jhelum Express", "Pune - Jammu Tawi Jhelum Express",
    "Howrah - Yesvantpur Humsafar Express", "Yesvantpur - Howrah Humsafar Express", "Secunderabad - Shalimar Weekly Express",
    "Shalimar - Secunderabad Weekly Express"
]

train_types = ["Rajdhani", "Shatabdi", "Superfast", "Express", "Duronto", "Luxury", "Double Decker", "Garib Rath", "Jan Shatabdi"]
operator_zones = ["East", "West", "North", "South"]
train_reviews = list(range(1, 6))  # Reviews on a scale of 1 to 5
speeds = [60, 80, 100, 120, 140, 160, 180]  # Average speeds in km/h

def generate_train_number(train_type):
    """Generate a 5-digit train number based on the type."""
    zone_code_mapping = {
        'Konkan Railway': '0',
        'CR': '1', 'WCR': '1', 'NCR': '1',
        'Superfast': '2', 'Shatabdi': '2', 'Jan Shatabdi': '2',
        'ER': '3', 'ECR': '3',
        'NR': '4', 'NCR': '4', 'NWR': '4',
        'NER': '5', 'NFR': '5',
        'SR': '6', 'SWR': '6',
        'SCR': '7', 'SWR': '7',
        'SER': '8', 'ECoR': '8',
        'WR': '9', 'NWR': '9', 'WCR': '9'
    }
    
    zone_code = '0'  # Default
    if train_type in zone_code_mapping:
        zone_code = zone_code_mapping[train_type]
    
    return f"{zone_code}{random.randint(1000, 9999)}"

data = []

# Generate 500 entries
for i in range(1, 501):
    train_type = random.choice(train_types)
    entry = [
        generate_train_number(train_type),
        random.choice(train_names),
        train_type,
        f"{random.randint(100, 4000)} km",
        random.randint(4, 35),
        random.randint(1, 15),
        random.randint(1, 7),
        random.choice(train_reviews),
        random.choice(speeds),
        random.choice(operator_zones),
        random.randint(900, 1400)  # Total Number of Seats
    ]
    data.append(entry)

# Create a DataFrame
df = pd.DataFrame(data, columns=[
    "Train Number", "Train Name", "Train Type", "Total Distance", "Total Station Stop", 
    "Total Junction", "Total Days", "Train Review", "Speed", "Operator Zone",
    "Total Number of Seats"
])

# Sort the DataFrame by Train Name
df = df.sort_values(by="Train Name")

# Save to CSV
df.to_csv("train_data.csv", index=False)

#!/usr/bin/env python3
"""
Create a new worksheet in Google Sheets for testing
"""

import gspread
from google.oauth2.service_account import Credentials

def create_new_worksheet():
    """Create a new worksheet in the Google Sheets."""
    try:
        print("🔍 Creating new worksheet in Google Sheets...")
        
        # Authenticate
        scopes = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        
        credentials = Credentials.from_service_account_file('credentials.json', scopes=scopes)
        client = gspread.authorize(credentials)
        
        # Open the spreadsheet
        spreadsheet_id = "1u6xIltHLEO-cfrFwCNVFL2726nRwaAMD90aqAbZKjgQ"
        spreadsheet = client.open_by_key(spreadsheet_id)
        print(f"✅ Opened spreadsheet: {spreadsheet.title}")
        
        # Create a new worksheet
        new_worksheet_name = "Brand_Monitoring_Test"
        try:
            # Try to get existing worksheet
            worksheet = spreadsheet.worksheet(new_worksheet_name)
            print(f"✅ Worksheet '{new_worksheet_name}' already exists")
        except:
            # Create new worksheet
            worksheet = spreadsheet.add_worksheet(title=new_worksheet_name, rows=1000, cols=20)
            print(f"✅ Created new worksheet: {worksheet.title}")
        
        # Set up headers
        headers = [
            "Timestamp", "Query", "Agent", "Brand_Found", "Confidence", 
            "Ranking", "Context", "Source", "Execution_Time", "Cost",
            "Status", "Error_Message", "Raw_Response"
        ]
        
        worksheet.update('A1:M1', [headers])
        print(f"✅ Set up headers in worksheet: {worksheet.title}")
        
        # Add a test row
        test_row = [
            "2025-08-27 10:00:00", "test_query", "test_agent", "True", "0.95",
            "1st", "Test context", "Test source", "2.5s", "$0.01",
            "success", "", "Test response"
        ]
        
        worksheet.append_row(test_row)
        print(f"✅ Added test row to worksheet: {worksheet.title}")
        
        print(f"\n🎉 Successfully created/updated worksheet: {worksheet.title}")
        print(f"📊 You can view it at: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating worksheet: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = create_new_worksheet()
    if success:
        print("\n✅ New worksheet is ready for testing!")
    else:
        print("\n❌ Failed to create worksheet")

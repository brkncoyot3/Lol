# Imports

import datetime

# Assignments

date_today = datetime.date.today()
date_today_short = date_today.strftime("%b %d")
registered_plan = input_data['registered_plan']

redirect_home_link = input_data['redirect_home_link']
redirect_home_link = redirect_home_link.replace('(plan_slug)',registered_plan)

instagram_username = input_data['instagram_username']
instagram_username = instagram_username.replace('@',"")
instagram_username = instagram_username.lower()

firstname = input_data['firstname']
firstname = firstname.capitalize()

email = input_data['email']
email = email.lower()

# Plan <> Fibery Mapping (Growth Base Plans)
return {
    'Email (Cleansed)':email,
    'Instagram Username (Cleansed)':instagram_username,
    'First Name (Cleansed)':firstname,
    'Growth Plan Details':growth_plan_details,
    'Growth Plan Alert':growth_plan_alert,
    'Growth Progress Alert':growth_progress_alert,
    'Growth Report Alert':growth_report_alert,
    'Growth Report Link':growth_report_link
}
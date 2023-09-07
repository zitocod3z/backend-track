from django.shortcuts import render
from datetime import datetime
import pytz
from django.http import JsonResponse

# Create your views here.
def zito_api(request):
    slack_name = request.GET.get('slack_name', '')
    current_day = datetime.now().strftime('%A')
    utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    track = request.GET.get('track', '')
    github_file_url = "https://github.com/zitocod3z/backend-track/blob/main/zito_endpoint/views.py",
    github_repo_url = "https://github.com/zitocod3z/backend-track",
    status_code =  200
    
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code,
    }

    return JsonResponse(response_data)

from telegraph import Telegraph
from datetime import datetime

def get_privacy_policy_url():
    telegraph = Telegraph()
    telegraph.create_account(short_name='CareerFitBot')

    content = f'''
<h3>Privacy Policy for Career Fit Job Bot</h3>
<p>Last updated: {datetime.now().strftime("%B %d, %Y")}</p>

<h4>1. Information We Collect</h4>
<p>• Telegram User ID<br>• Job preferences you select</p>

<h4>2. How We Use Your Information</h4>
<p>• To send you relevant job listings<br>• To customize job matches to your preferences</p>

<h4>3. Data Storage</h4>
<p>Your data is securely stored and not shared with third parties.</p>

<h4>4. Your Rights</h4>
<p>You can:<br>• Update your preferences anytime<br>• Delete your data using /delete command</p>

<h4>5. Contact</h4>
<p>Questions? Contact @YourUsername</p>
'''

    try:
        response = telegraph.create_page(
            title='Career Fit Job Bot - Privacy Policy',
            html_content=content,
            author_name='Career Fit Bot'
        )
        return response['url']
    except Exception as e:
        # If Telegraph fails, return a default message
        return "https://telegra.ph/Privacy-Policy-Career-Fit-Job-Bot"

if __name__ == '__main__':
    print(get_privacy_policy_url())

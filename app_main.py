import tweepy
from config_loader import load_api_credentials

def authenticate_x_api():
    credentials = load_api_credentials()

    auth = tweepy.OAuth1UserHandler(
        credentials["API_KEY"],
        credentials["API_SECRET"],
        credentials["ACCESS_TOKEN"],
        credentials["ACCESS_SECRET"]
    )

    api = tweepy.API(auth)
    try:
        user = api.verify_credentials()
        if user:
            print("Authentication successful!")
            print(f"Logged in as: {user.name}")
        else:
            print("Authentication failed!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    authenticate_x_api()

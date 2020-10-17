import instaloader
 

def login_loader(username: str, password: str):
    loader = instaloader.Instaloader()
    loader.login(username, password)
    return loader


def get_profile(username: str, loader):
    profile = instaloader.Profile.from_username(loader.context, username)
    return profile


def get_followed(profile):
    followed = []
    for followee in profile.get_followees():
        followed.append(followee.username)
    return followed


def get_followers(profile):
    followers = []
    for follower in profile.get_followers():
        followers.append(follower.username)
    return followers


def get_unfollowers(followers: list, followed: list):
    unfollowers = []
    for followee in followed:
        if followee not in followers:
            unfollowers.append(followee)
    return unfollowers


def main():
    login = input('Enter your Instagram username: ')
    pw = input('Enter your password: ')
    loader = login_loader(login, pw)
    profile = get_profile(login, loader)
    followed = get_followed(profile)
    followers = get_followers(profile)
    unfollowers = get_unfollowers(followers, followed)    

    print(f'Amount of unfollowers: {len(unfollowers)}')
    for unfollower in unfollowers:
        print(unfollower)


if __name__ == '__main__':
    main()
    
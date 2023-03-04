import instaloader
from instaloader import TwoFactorAuthRequiredException
import stdiomask
import os


def login_loader(username: str, password: str):
    loader = instaloader.Instaloader()
    try:
        loader.login(username, password)
    except TwoFactorAuthRequiredException:
        os.system('cls')
        print("2FA does not work on instaloader (bug). You'll have to disable it for now\n")
        main()
        # twofa = input('Insert your 2FA code: ')
        # loader.two_factor_login(twofa)
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
    pw = stdiomask.getpass('Enter your password: ')
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
    

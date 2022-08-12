import instaloader
from tqdm import tqdm
L = instaloader.Instaloader()

# Login or load session

username="Username"
password = "Password"
L.interactive_login(username)  # (login)

# # Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, username)
print(profile)
# Print list of followees
followers_list = []
following_list = []
followers_count = 0
following_count = 0
print("\n\nFetching followers.....")
for follower in tqdm(profile.get_followers(),desc="Followers", ascii=False, ncols=75):
    followers_list.append(follower.username)
    file = open("followers.txt", "a+")
    file.write(followers_list[followers_count])
    file.write("\n")
    file.close()
    followers_count = followers_count + 1

print("Completed\n\n")
print("Fetching followings.....")
for followee in tqdm(profile.get_followees(),desc="Followings", ascii=False, ncols=75):
    following_list.append(followee.username)
    file = open("followings.txt", "a+")
    file.write(following_list[following_count])
    file.write("\n")
    file.close()
    following_count = following_count + 1

print("Completed\n\n")
print("List of Users Who don't Follow You Back....\n\n")
followings_who_dont_follow = set(following_list)-set(followers_list)
textfile = open("followings_who_dont_follow.txt", "w") #Creating a text file
for ff in followings_who_dont_follow:
    print(f"https://www.instagram.com/{ff}/")
    textfile.write(ff + "\n") #Listing down them in the text file
textfile.close()

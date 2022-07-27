import csv
data = []
import time

def getLikes(posts):

  likes = 0
  count = 10
  
  try:
    for index, post in enumerate(posts, 1):
      if count != 0:
        likes += post.likes
        count -= 1
      else:
        break
        break
  except:
    exit()

  return likes

def getComments(posts):

  comments = 0
  count = 10
  
  try:
    for index, post in enumerate(posts, 1):
      if count != 0:
        comments += post.comments
        count -= 1
      else:
        break
        break
  except:
    exit()

  return comments

def getData(username):

  import instaloader
  bot = instaloader.Instaloader()
  
  # bot.download_profile(Username, profile_pic_only = True)
  
  profile = instaloader.Profile.from_username(bot.context, username)
  
  username = profile.username
  print("    - Username: ", username)
  
  followers = profile.followers
  print("    - Followers: ", followers)
  
  posts = profile.get_posts()
  likes = getLikes(posts)
  print("    - Likes: ", likes)
  
  posts = profile.get_posts()
  comments = getComments(posts)
  print("    - Comments: ", comments)

  userMetrics = [username, followers, likes, comments]

  data.append(userMetrics)

def toCsv(data):

  # Open or create a CSV file, with "w" or write permission
  f = open("data.csv", "w")

  # initialize the writer
  writer = csv.writer(f)

  # write the header
  writer.writerow(["Username", "Followers", "Likes", "Comments"])

  for player in data:
    writer.writerow(player)
  f.close()

  print("    - ✅ Data written to csv file ")

def main():

  usernames = []
    
  # Using readlines()
  file1 = open('players.txt', 'r')
  Lines = file1.readlines()

  # Strips the newline character
  for line in Lines:
    line = line.replace("@","")
    line = line.replace('\n', '')
    usernames.append(line)

  for username in usernames:
    
    print("🔍 Evaluating ", username)
    getData(username)
    # Convert the "Data" list to a spreadsheet
    toCsv(data)

main()

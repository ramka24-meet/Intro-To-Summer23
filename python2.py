def create_youtube_video(title, description):
	video = {"title" : title, "description" : description, "likes" : 0, "dislikes" : 0, "comments" : {},
	"hashtag":"", "trending" : False}
	return video
def like(video):
	if "likes" in video:
		video["likes"]+=1
	return video
def dislike(video):
	if "dislikes" in video:
		video["dislikes"]+=1
	return video
def add_comment(video,username,comment_text):
	video["comments"][username]=comment_text
	return video
ytvid = create_youtube_video("Amir","Amir is goated")
like(ytvid)
dislike(ytvid)
add_comment(ytvid,"AmirGlazer424","He really is")
for i in range(495):
	like(ytvid)
print(ytvid)
ytvid2 = create_youtube_video("Amir Bad","Amir is  not goated")
like(ytvid2)
dislike(ytvid2)
add_comment(ytvid2,"AmirHater424","He really is")
for i in range(495):
	dislike(ytvid2)
print(ytvid2)

def hashtag(ytvid):
	hashtag = []
	for i in range (5):
		word = input("Enter hashtag number" + str((i +1)))
		hashtag.append(word)
	ytvid["hashtag"] = hashtag
	return ytvid
def similar(ytvid, ytvid2):
	precentage = 0
	for i in ytvid["hashtag"]:
		for j in ytvid2["hashtag"]:
			if i == j and i!="":
				precentage+=20
	print(precentage)
def trending(ytvid):
	if ytvid["likes"] > ytvid["dislikes"] and ytvid["likes"]>=20:
		ytvid["trending"] = True
	return ytvid
hashtag(ytvid)
hashtag(ytvid2)
similar(ytvid,ytvid2)
print(trending(ytvid))
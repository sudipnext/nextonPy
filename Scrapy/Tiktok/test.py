from tiktokapipy.api import TikTokAPI

#function for finding video id
def FindVideoID():
    with TikTokAPI() as api:
        user = api.user('khaby.lame')
        for video in user.videos:
            print(video.id)
            print(video.author)
            print(video.challenges)


FindVideoID()

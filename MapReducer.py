import json
from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol



class WordCounter(MRJob):
    # INPUT_PROTOCOL = JSONValueProtocol
    # OUTPUT_PROTOCOL = JSONValueProtocol

    def mapper(self,key,value):
        # def __init__(self, followers, following):
        #     self.followers = followers
        #     self.following = following
        data = json.loads(value)
        for x in data:
            account_id = x["account"]["id"]
            username = x["account"]["username"]
            account_created_at = x["account"]["created_at"]
            account_url = x["account"]["url"]
            account_followers_count = x["account"]["followers_count"]
            account_following_count = x["account"]["following_count"]
            account_status_count = x["account"]["statuses_count"]
            post_id = x["id"]
            post_favourites_count = x["favourites_count"]
            post_reblogs_count = x["reblogs_count"]
            post_visibility = x["visibility"]
            post_media = x["media_attachments"]
            language = x["language"]
            post_tags = x["tags"]
            
            # User values
            yield "username:"+str(account_id), username
            yield "created_at:"+str(account_id), account_created_at
            yield "followers_count:"+str(account_id), account_followers_count
            yield "following_count:"+str(account_id), account_following_count
            yield "status_count:"+str(account_id), account_status_count
            if len(account_url) > 1:
                yield "url:"+str(account_id), account_url
            else:
                yield "url:"+str(account_id), "None"
            # # Post values
            yield "favourites_count:"+str(post_id), post_favourites_count
            yield "reblogs_count:"+str(post_id), post_reblogs_count
            yield "visibility:"+str(post_id), post_visibility
            if language:
                yield "language:"+str(post_id), language
            else:
                yield "language:"+str(post_id), "None"
            # if post_tags:
            for tag in post_tags:#tag["name"].encode().decode('unicode-escape')
                yield "tag:"+str(post_id), tag["name"]
            yield "media:"+str(post_id), 1 if len(post_media) > 0 else 0
    def combiner(self, key, values):
        # yield key,max(values)
        yield key,max(values)

    def reducer(self,key,values):
        # yield key,max(values)
        yield key,max(values)

    def steps(self):
        return [
            MRStep(
                mapper = self.mapper,
                reducer=self.reducer
            )
        ]
if __name__ == '__main__':
    WordCounter.run()
    

import json
from mrjob.job import MRJob
from mrjob.step import MRStep


class WordCounter(MRJob):
    def mapper(self,key,value):
        data = json.loads(value)
        for x in data:
            username = x.get('account').get('username')
            followers = x.get('account').get('followers_count')
            language = x.get("language")
            yield(f"language:{language}",1)
            yield(f"followers:{username}",followers)
            # yield(username, 1)

    def combiner(self, key, values):
        yield(key, sum(values))
    
    def reducer(self,key,values):
        yield(key,sum(values))

    def steps(self):
        return [
            MRStep(
                mapper = self.mapper,
                reducer=self.reducer
            )
        ]
if __name__ == '__main__':
    WordCounter.run()
    

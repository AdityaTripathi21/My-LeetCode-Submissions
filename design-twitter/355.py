from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.follower_map = defaultdict(set) # userId -> hashset of followeeId
        self.tweet_map = defaultdict(list)  # userId -> list of (-counter, tweetId)
        self.counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter += 1
        self.tweet_map[userId].append((-self.counter, tweetId))

        

    def getNewsFeed(self, userId: int) -> List[int]: # type: ignore
        users = self.follower_map[userId] | {userId}
        heap = []       # heap stores (-counter, tweetId, userId, index of last tweet)
        for u in users:
            if len(self.tweet_map[u]) > 0:
                time, tweet_id = self.tweet_map[u][-1]
                heap.append((time, tweet_id, u, len(self.tweet_map[u]) - 1))
        heapq.heapify(heap)
        res = []

        while heap and len(res) < 10:
            x = heapq.heappop(heap)
            res.append(x[1])
            if x[3] - 1 >= 0:
                time, tweet_id = self.tweet_map[x[2]][x[3] - 1]
                heapq.heappush(heap, (time, tweet_id, x[2], x[3] - 1))

        return res

            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].discard(followeeId)
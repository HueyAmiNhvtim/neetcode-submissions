import time
from typing import List
import heapq


class Twitter:

    def __init__(self):
        # Each userID should have their own heap of tweetID ordered by time stamp I think.
        self.start = time.time()
        self.user_tweets = dict()        # Map userID to heap of tweetID of their own
        self.user_adjacency_set = dict() # Map users to their followees
        self.top_feed = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Publish a new tweet.
        :param userId: ID of user
        :param tweetId: ID of tweet. Each tweetID is unique.
        :return: None
        """
        if userId not in self.user_adjacency_set:
            starting_network = set()
            starting_network.add(userId)
            self.user_adjacency_set[userId] = starting_network
            self.user_tweets[userId] = []

        tweet_item = (-1 *(time.time() - self.start), tweetId)
        heapq.heappush(self.user_tweets[userId], tweet_item)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Fetches top 10 most recent tweet IDs in the user's news feed
        Each tweet must be posted by users who the user is following or by the user themselves
        in the order from most recent to last recent.
        :param userId: ID of user
        :return: List of tweetIDs
        """
        result = []
        for followee_id in self.user_adjacency_set[userId]:
            result = heapq.merge(result, self.user_tweets[followee_id], key=lambda x: x[0])
        result = heapq.nsmallest(self.top_feed, result, key=lambda x: x[0])
        result = [i[1] for i in list(result)]
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        User with followerID follows the user with followeeId.
        :param followerId: ID of follower user
        :param followeeId: ID of followee user
        :return: None
        """
        if followerId not in self.user_adjacency_set:
            self.user_adjacency_set[followerId] = set()
        self.user_adjacency_set[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        User with followerID unfollows the user with followeeId.
        :param followerId: ID of follower user
        :param followeeId: ID of followee user
        :return: None
        """
        if followeeId != followerId and followeeId in self.user_adjacency_set[followerId]:
            self.user_adjacency_set[followerId].remove(followeeId)
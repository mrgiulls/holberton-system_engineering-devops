#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""



def hot_recurse(titles, n):
    """Does the recursion"""
    if n < len(titles):
        title = titles[n].get('data').get('title')
        heaptitles = title.split()
        heaptitles.extend(hot_recurse(titles, n + 1))
        return heaptitles
    return [-1]


def recurse(subreddit, hot_list=[], after=None):
    """Function in task #1 but recursive"""
    import requests

    header = {'User-Agent': 'MyHolbertonAPI/0.0.1'}
    response = requests.get("https://www.reddit.com/r/{}/hot.json?after={}".
                            format(subreddit, after), headers=header).json()

    if not response.get('error'):
        after = response.get('data').get('after')
        titles = response.get('data').get('children')
        hot_list.extend(hot_recurse(titles, 0))
        hot_list.remove(-1)
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    return None


def binary_search(word, wordlist, start, end):
    """does a binary search"""
    if start <= end:
        mid = (end + start) // 2
        lowerword = word.lower()
        midlower = wordlist[mid].lower()
        if lowerword == midlower:
            return mid
        elif lowerword < midlower:
            return binary_search(word, wordlist, start, mid - 1)
        else:
            return binary_search(word, wordlist, mid + 1, end)
    return -1


def linear_count(word, index, hot_list):
    """frequency of a word in a list of words"""
    count_left = 0
    left = index
    while word == hot_list[left]:
        count_left += 1
        left -= 1
    count_right = 0
    right = index + 1
    while word == hot_list[right]:
        count_right += 1
        right += 1
    return count_left + count_right


def count_words(subreddit, word_list):
    """Counts all the keywords of word_list in the given subreddit"""
    hot_list = recurse(subreddit)
    hot_list.sort()
    dct_count = {}
    for word in word_list:
        idxsearch = binary_search(word, hot_list, 0, len(hot_list) - 1)
        if idxsearch != -1:
            if word.lower() not in dct_count.keys():
                dct_count[word.lower()] = linear_count(word,
                                                       idxsearch, hot_list)
            else:
                dct_count[word.lower()] += linear_count(word,
                                                        idxsearch, hot_list)
    sortedvalues = list(dct_count.values())

    sortedvalues.sort()
    sortedvalues.reverse()
    sorted_dct = {}
    for val in sortedvalues:
        for word in dct_count.keys():
            if dct_count[word] == val:
                sorted_dct[word] = val
    for key, value in sorted_dct.items():
        print("{}: {}".format(key, value))

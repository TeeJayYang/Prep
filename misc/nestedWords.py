def findNestedWords1(file_name):
    # Load the words into a dictionary
    words = dict((x.strip(), set()) for x in open(file_name))

    # For each word, remove each letter and see if the remaining word is still
    # in the dictionary. If so, add it to the set of shorter words associated with
    # that word in the dictionary.
    # For example, bear -> {ear, bar, ber}
    for w in words:
        for i in range(len(w)):
            shorter = w[:i] + w[i+1:]
            if shorter in words:
                words[w].add(shorter)

    # Sort the words by length so we process the shortest ones first
    sortedwords = sorted(words, key=len)

    # For each word, the maximum chain length is:
    #  - the maximum of the chain lengths of each shorter word, if any
    #  - or 0 if there are no shorter words for this word
    # Note that because sortedwords is sorted by length, we will always
    # have maxlength[x] already available for each shorter word x
    maxlength = {}
    for w in sortedwords:
        if words[w]:
            maxlength[w] = 1 + max(maxlength[x] for x in words[w])
        else:
            maxlength[w] = 0

    # Print the words in all chains for each of the top 10 words
    toshow = sorted(words, key=lambda x: maxlength[x], reverse=True)[:10]
    while toshow:
        w = toshow[0]
        print(w, [(x, maxlength[x]) for x in words[w]])
        toshow = toshow[1:] + list(x for x in words[w] if x not in toshow)

def findNestedWords2(file_name):
    words = dict((x.strip(), False) for x in open(file_name))

    sortedwords = sorted(words, key = len) 
    longest = ''
    for w in sortedwords:
        if len(w) == 1:
            words[w] = True 
            continue
        for i in range(len(w)):
            shorter = w[:i] + w[i+1:]
            if words.get(shorter, False):
                words[w] = True 
        if words[w]:
            if len(w) > len(longest): #or (len(w) == len(longest) and w < longest):
                longest = w
                print(longest)
    return longest

def main():
    file_name = 'words.txt'
    print(findNestedWords2(file_name))

main()

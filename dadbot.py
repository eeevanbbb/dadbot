import praw

r = praw.Reddit('Dadbot 1.0 by u/feelinbotbotbot '
                'google.com')

r.login()

subredditString = raw_input('Subreddit: ')
howMany = raw_input('Top how many comments: ')
subreddit = r.get_subreddit(subredditString)
for submission in subreddit.get_hot(limit=int(howMany)):
	flat_comments = praw.helpers.flatten_tree(submission.comments)
	already_done = set()
	for comment in flat_comments:
		if comment.id not in already_done:
			already_done.add(comment.id)
			if "I'm " in comment.body:
				whoAreYou = comment.body.split("I'm ",1)[1]
				whoAreYou = whoAreYou.strip('!.')
				reply = "Hi %s, I'm Dad!" % whoAreYou
				comment.reply(reply)
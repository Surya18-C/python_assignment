
""" Given the participants' score sheet for your University Sports Day, you are required
to find the runner-up score. You are given  scores. Store them in a list
and find the score of the runner-up."""

def score(scores):
    first=scores[0]
    runner=0

    for i in scores:
        if i > first:
            runner=first
            first=i

    return runner
# score = 0
# for each request q for a file f at an endpoint e
# score += number of videos in the request *
# (latency from data centre – best latency
# from a cache server serving e and hosting f)
# endfor
# score = score/number of requests
# score *= 1000

def fit():
    score = 0
    
    for request in request_description:
        for file in endpoint_list:
            score += number_of_videos * (data_centre_latency - best_latency)
            
    score = score/number_of_requests
    return score*1000

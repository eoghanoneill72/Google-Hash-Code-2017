import numpy as np

def read_google(filename):
    data = dict()


    with open(filename, "r") as fin:

        system_desc = next(fin)
        number_of_videos, number_of_endpoints, number_of_requests, number_of_caches, cache_size= system_desc.split(" ")
        number_of_videos = int(number_of_videos)
        number_of_endpoints = int(number_of_endpoints)
        number_of_requests = int(number_of_requests)
        number_of_caches = int(number_of_caches)
        cache_size = int(cache_size)
        video_ed_request = dict()
        ##create a list of the video sizes from line 2
        video_size_desc = next(fin).strip().split(" ")
        for i in range(len(video_size_desc)):
            video_size_desc[i] = int(video_size_desc[i])
        ed_cache_list = []

        ### CACHE SECTION

        ep_to_cache_latency = [] 

        ep_to_dc_latency = [] 
        for i in range(number_of_endpoints):


            ep_to_dc_latency.append([])
            ep_to_cache_latency.append([])

            dc_latency, number_of_cache_i = next(fin).strip().split(" ")
            dc_latency = int(dc_latency)
            number_of_cache_i = int(number_of_cache_i)

            ep_to_dc_latency[i] = dc_latency

            for j in range(number_of_caches):
                ep_to_cache_latency[i].append(ep_to_dc_latency[i]+1)

            cache_list = []
            for j in range(number_of_cache_i):
                cache_id, latency = next(fin).strip().split(" ")
                cache_id = int(cache_id)
                cache_list.append(cache_id)
                latency = int(latency)
                ep_to_cache_latency[i][cache_id] = latency

            ed_cache_list.append(cache_list)

        ### REQUEST SECTION
        for i in range(number_of_requests):
            video_id, ed_id, requests = next(fin).strip().split(" ")
            video_ed_request[(video_id,ed_id)] = requests


    data["number_of_videos"] = number_of_videos
    data["number_of_endpoints"] = number_of_endpoints
    data["number_of_requests"] = number_of_requests
    data["number_of_caches"] = number_of_caches
    data["cache_size"] = cache_size
    data["video_size_desc"] = video_size_desc
    data["ep_to_dc_latency"] = ep_to_dc_latency
    data["ep_to_cache_latency"] = ep_to_cache_latency
    data["ed_cache_list"] = ed_cache_list
    data["video_ed_request"] = video_ed_request

    return data



data = read_google("input/simple.in")
print(data["number_of_requests"])
indiv_req = 0
for i in data["video_ed_request"]:
    indiv_req += int(data["video_ed_request"][i])
print("number of individual requests=", indiv_req, " which is different from the number of request descriptions ", data["number_of_requests"])

        

for key in data:
    print (key, '-->', data[key])
    
print("video_ed_request[(video_id,ed_id)] = requests")

###########################################################

def fit(solution):
    gains = []
    
    for vid_ep, requests in data["video_ed_request"].items():
        vid = vid_ep[0]
        ep = vid_ep[1]
        
        for connected_cache in data["ed_cache_list"][ep]:
            best_cache_latency = 0
            if solution[connected_cache][vid] == 1:
                new_cache_latency = data["ep_to_cache_latency"][ep][connected_cache]
                best_cache_latency = min(new_cache_latency, best_cache_latency)
        
        difference = data["ep_to_dc_latency"][ep] - best_cache_latency
        gain = difference * requests
        
        gains.append(gain)
        
        score = gains.sum()/indiv_req 
        
        return score
    
def overflow(matrix): 
    for cache in range(data["number_of_caches"]-1):
        for vid in range(data["number_of_videos"]-1):
            cache_used = 0               
            if matrix[cache][vid] == 1:
                cache_used += data["video_size_desc"][vid]
                if cache_used > data["cache_size"]:
                    return -1

def main():

    fittest = 0
    
    solution = np.zeros((data["number_of_caches"], data["number_of_videos"]), dtype=np.int)
      
    for cache in range(data["number_of_caches"]):
        for vid in range(data["number_of_videos"]):
            if solution[cache][vid] == 0:
                solution[cache][vid] = 1
                if overflow(solution) != -1:
                    if fittest < fit(solution):
                        fittest = fit(solution)
                        
    return fittest 


#                 
# def overflow(cache):
#     cache_used = 0 
# #     for cache in range(data["number_of_caches"]):
#     for vid in range(cache):
#         if cache[vid] == 1:               
#             cache_used += data["vid_size_desc"][vid]
#             if cache_used > data["cache_size"]:
#                 return -1
#             
# def capacity(solution):
#     for cache in solution:
#         if overflow(cache) == -1:
#             return -1

        
#         for file in data["ed_cache_list"] :
#             score += number_of_videos * (data_centre_latency - best_latency)
#             
#     score = score/number_of_requests
#     return score*1000
    
#     for request in request_description:
#         for file in endpoint_list:
#             score += number_of_videos * (data_centre_latency - best_latency)
#             
#     score = score/number_of_requests
#     return score*1000

print(main())

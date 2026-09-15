trending=0
total=0
blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
for x in blog_views:
    if x>1000:
        print("Trending")
        trending+=1
    elif 500<=x<=1000:
        print("Average")
    elif x<500:
        print("Low traffic")
    total+=x
    
print(total)
print(trending)

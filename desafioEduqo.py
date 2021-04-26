def drawpyramid(n):
    
    stars = 1
    
    while(n): 
        n = n - 1 
        line = "";

        for i in range(n):
            line += "_"
        for i in range(stars):
            line += "*"
       
        stars += 2;
       
        for i in range(n):
            line += "_"
       
        print(line)
        print('\n')
    
drawpyramid(8)
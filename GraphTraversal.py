import sys
global m,n # m and n are used as boundaries

# path list to store path of the graph
path = []
#visited list to store already visited cell of the graph
vstd = [] 
#direction dictionary to get the direction count increment or decrement from the current cell
dir = {
    "E":{'x':0,'y':1},
    "W":{'x':0,'y':-1},
    "N":{'x':-1,'y':0},
    "S":{'x':1,'y':0},
    "NE":{'x':-1,'y':1},
    "SE":{'x':1,'y':1},
    "SW":{'x':1,'y':-1},
    "NW":{'x':-1,'y':-1},
} 
#writes the computed path to the output file
def output_path(result):
    f = open(opFile, "w")
    f.write(result) #writing the result to the output file
    f.close()
    exit()

#function to compute the path for bulls eye
def find_path(row,col,present_arrow,current_direction):
    str_row,str_col = str(row),str(col)
    if (row<0 or col<0 or row>=m or col>=n): #base cases to avoid overflow and null pointer exception
        return
    
    if str_row+"#"+str_col in vstd:  #base case to check if the cell is already visited, to avoid infinite recursive call
        return

    #once the bulls eye is identified print the path and exit
    if graph[row][col]=="O":
        curDir = path[0]
        count=1
        # convert path to the required format based on the number of repeated steps
        path_len = len(path)
        j = 1
        result = ""

        while j<path_len:
            condition = curDir != path[j]
            if condition:
                result = result + str(count)
                result += curDir + ' '
                curDir = path[j]
                count = 0
            count += 1
            j += 1
       
        result+=str(count)+curDir
        #printing the path to the console
        # print(result) 
        return output_path(result)
   
    #if the present arrow is same as the current arrow then follow the same path
    if present_arrow==graph[row][col][0]:
        #get the x and y values from the dictionary
        x=  dir[current_direction]["x"]
        y=  dir[current_direction]["y"]
        #add current direction to the path and vstd list to keep track of the path
        path.append(current_direction)
        vstd.append(str(row)+"#"+str(col))
        find_path(row+x,col+y,present_arrow,current_direction)
        #once it is returned it is clear that the path is not found hence we remove the direction from the vstd and path lists
        vstd.pop()
        path.pop()
    else:
        #if the current direction is not same as the current cell direction ---
        # we have to options can continue with the same direction and can take a turn. ---
        #this is the same step as above to continue in the same direction ---
        x=  dir[current_direction]["x"]
        y=  dir[current_direction]["y"]
        path.append(current_direction)
        find_path(row+x,col+y,present_arrow,current_direction)
        path.pop()

        #if the path is not found while continuing in the direction,then have to take a turn towards the current cell's direction
        current_direction = graph[row][col][2:] #updating the direction
        present_arrow = graph[row][col][0]  #updating the arrow color
        x=  dir[current_direction]["x"] # fetching the direction
        y=  dir[current_direction]["y"]
        path.append(current_direction)  #appending current direction and adding path to vstd list 
        vstd.append(str(row)+"#"+str(col))
        find_path(row+x,col+y,present_arrow,current_direction) # making a recursive call
        vstd.pop()
        path.pop()

# graph is declared as a global variable so that it can be accessed anywhere in program

global graph
# for the input and output files in the command line
ipFile, opFile =  sys.argv[1], sys.argv[2]
file_ = open(ipFile, "r") #opening file to take the consider the input data
#below 3 line to remove unnecessary characters such as spaces and \n
graph_lines = file_.readlines()
graph = [[el for el in gl.strip().split()] for gl in graph_lines]
# loop to remove empty data from graph
graph_length = len(graph)
for i in range(graph_length):
    temp = []
    for x in graph[i]:
        if x != '':
            temp.append(x)
    graph[i] = temp

row,column = graph[0][0], graph[0][1]
m = int(row)
n = int(column)
graph.pop(0)  # deleting m n from the graph list
initial_value_with_zeroes = graph[0][0][0]
current_value_current_index = graph[0][0][2:]
find_path(0,0,initial_value_with_zeroes, current_value_current_index)#calling file_path function with initial cell 0,0 and current direction with current arrow.

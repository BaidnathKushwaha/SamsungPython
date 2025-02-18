import binary
import sys
print("The input numbers are\n{sys.argv[1:-1]}")
print("The search element is{sys.argv[-1]}")
search_pos=search({sys.argv[1:-1]},{sys.argv[-1]})
if search_pos==-1:
    print("not found")
else:
    print("found at",search_pos)
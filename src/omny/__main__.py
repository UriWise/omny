from omny.omny import mcp, root_dir
import os
# This file serves as the entry point for the Omny application. It imports the mcp instance from the omny module and runs it when executed. 
# Import structure: from folder.file import variable/function/class. 
# In this case, we are importing the mcp instance from the omny module located in the omny folder.
# The main function is defined to encapsulate the execution of the mcp server, allowing for better organization and potential future enhancements.

def main():
    mcp.run()

if __name__ == "__main__":
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
    main()
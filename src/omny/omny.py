from mcp.server.fastmcp import FastMCP
import os
import sys

mcp = FastMCP("LocalNotes")
notes_file = "notes.txt"
root_dir = os.path.join(os.path.expanduser("~"), "omny")



@mcp.tool()
def add_note_to_file(content: str, filename: str = notes_file) -> str:
    """Appends the given content to a local file
    Args:
        content (str): The content to be added to the file
        filename (str): The name of the file to which the content will be added
        """
    try:
        with open(os.path.join(root_dir, filename), 'a+') as file:
            file.write(content + '\n')
        return f"Content added to {filename} successfully."
    except Exception as e:
        print(f"An error occurred while adding content to {filename}: {e}", file=sys.stderr)
        return f"An error occurred while adding content to {filename}: {e}"


@mcp.tool()
def read_notes(filename: str = notes_file) -> str:
    """Reads the content of the notes file and returns it as a string."""
    try:
        with open(os.path.join(root_dir, filename), 'r') as file:
            notes = file.read()
            return notes if notes else "No notes found. The notes file is empty."
    except FileNotFoundError:
        return "No notes found. The notes file does not exist."
    except Exception as e:
        print(f"An error occurred while reading the notes: {e}", file=sys.stderr)
        return f"An error occurred while reading the notes: {e}"

if __name__ == "__main__":
    
    print(root_dir)
    mcp.run()
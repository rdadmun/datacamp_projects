import pandas as pd

def print_grid_from_google_doc(url):
    df = pd.read_html(url, encoding='utf-8')

    grid_data = df[0]

    print("Table structure:")
    print(grid_data.head())

    grid_data = grid_data[1:]  
    grid_data = grid_data.values.tolist()
    grid = {}
    
    for row in grid_data:
        try:
            x, char, y = row  
            x, y = int(x), int(y) 
            grid[(x, y)] = char 
        except ValueError:
            print(f"Skipping invalid row: {row}") 
    
    if not grid:  
        print("No grid data found.")
        return
    
    max_x = max(x for x, _ in grid.keys())
    max_y = max(y for _, y in grid.keys())
    

    for y in range(max_y + 1):
        row = ""
        for x in range(max_x + 1):
            row += grid.get((x, y), " ")
        print(row)

# Example usage:
url = "https://docs.google.com/document/d/e/2PACX-1vSCJGXDu491Y3rRgJPVhtdsY5ivkbQ5FJMDvPyanh2F7HNk2cea9AZIHa1j-RShETAsCxKqqbZ_Vz7J/pub"
print_grid_from_google_doc(url)
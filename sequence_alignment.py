def read_costs(cost_path) -> dict[str, dict[str, int]]:
    # reads the cost_path and puts it into a array of strings
    with open(cost_path, "r") as f:
        lines = []
        for line in f:
            line = line.strip() 
            if line != "":
                lines.append(line)

    # takes lines and makes it a 2d array of char
    rows = []
    for line in lines:
        parts = line.split(",")
        cleaned = []
        for token in parts:
            cleaned.append(token.strip())
        rows.append(cleaned)


    col_syms = rows[0][1:]
    cost = {}

    # create the hashmap
    for row in rows[1:]:  
        row_symbol = row[0]  
        cost[row_symbol] = {}
        values = row[1:]      
        for i in range(len(col_syms)):
            cost[row_symbol][col_syms[i]] = int(values[i])

    return cost



def sadp(costs: dict, string1: str, string2: str) -> int:

    #TODO Implement a dynamic programming solution to get the two aligned strings and the minimum cost

    n = len(string1)
    m = len(string2)
    
    s: list[list[int]] = [[0 for _ in range(m+1)] for _ in range(n+1)]

    s[0][0] = 0
    for j in range(1, m+1):
        s[0][j] = s[0][j-1] + costs['-'][string2[j-1]]
    for i in range(1, n+1):
        s[i][0] = s[i-1][0] + costs[string1[i-1]]['-']

    for i in range(1, n+1):
        for j in range(1, m+1):
            
            s[i][j] = min(s[i-1][j-1] + costs[string1[i-1]][string2[j-1]], s[i-1][j] + costs['-'][string2[j-1]], s[i][j-1] + costs[string1[i-1]]['-'])



    min_num = s[n][m]
    return min_num


def main() -> None:

    print("hello daniel")
    
if __name__ == "__main__":
    main()
import sys

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


def read_input(filename: str) -> list[tuple[str, str]]:
    pairs = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                left, right = line.split(",")
                pairs.append((left.strip(), right.strip()))

    return pairs



def sadp(costs: dict, string1: str, string2: str) -> tuple[str, str, int]:

    #TODO Implement a dynamic programming solution to get the two aligned strings and the minimum cost

    seq1: str = ""
    seq2: str = ""

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

            min_val = min(s[i-1][j-1] + costs[string1[i-1]][string2[j-1]], s[i-1][j] + costs[string1[i-1]]['-'], s[i][j-1] + costs['-'][string2[j-1]])
            
            s[i][j] = min_val



    
    #Backward pass
    i = n
    j = m

    while i > 0 or j > 0:

        if i == 0:
            seq1 += '-'
            seq2 += string2[j-1]
            j -= 1
        elif j == 0:
            seq1 += string1[i-1]
            seq2 += '-'
            i -= 1
        elif s[i][j] == s[i-1][j-1] + costs[string1[i-1]][string2[j-1]]:
            seq1 += string1[i-1]
            seq2 += string2[j-1]
            i -= 1
            j -= 1
        elif s[i][j] == s[i-1][j] + costs[string1[i-1]]['-']:
            seq1 += string1[i-1]
            seq2 += '-'
            i -= 1
        else:
            seq1 += '-'
            seq2 += string2[j-1]
            j -= 1

        
    seq1 = seq1[::-1]
    seq2 = seq2[::-1]
    min_num = s[n][m]
    return seq1, seq2, min_num


def output(filename: str, lines: list[tuple[str, str, int]]) -> None:

    with open(filename, "w") as f:
        for line in lines:
            f.write(line[0] + "," + line[1] + ":" + str(line[2]) + "\n")

    return



def main() -> None:

    costs = read_costs("imp2cost.txt")
    inputs = read_input(sys.argv[1])

    tuplist = []
    for input in inputs:
        tup = sadp(costs, input[0], input[1])
        tuplist.append(tup)
    

    output("output.txt", tuplist)
    
if __name__ == "__main__":
    main()
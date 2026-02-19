def read_costs() -> None:

    #TODO Implement a data structure to keep track of costs from input file




    return



def sadp(costs: dict, string1: str, n: int, string2: str, m: int) -> int:

    #TODO Implement a dynamic programming solution to get the two aligned strings and the minimum cost

    s: list[list[int]] = []

    for i in range(n):
        for j in range(m):
            # Base case
            if i == 0 or j == 0:
                s[i][j] = costs[string1[i]][string2[j]]


            s[i][j] = min(s[i-1][j-1] + costs[string1[i]][string2[j]], s[i-1][j] + costs['-'][string2[j]], s[i][j-1] + costs[string1[i]]['-'])



    min_num = s[n][m]
    return min_num


def main() -> None:

    print("hello daniel")
    
if __name__ == "__main__":
    main()
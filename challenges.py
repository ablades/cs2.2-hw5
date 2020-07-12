class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def lcs(strA, strB):
    if len(strA) == 0 or len(strB) == 0:
        return 0
    elif strA[-1] == strB[-1]:  # if the last characters match
        return 1 + lcs(strA[:-1], strB[:-1])
    else:  # if the last characters don't match
        return max(lcs(strA[:-1], strB), lcs(strA, strB[:-1]))


def lcs_dp(strA, strB):
    """Determine the length of the Longest Common Subsequence of 2 strings."""
    rows = len(strA) + 1
    cols = len(strB) + 1

    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            # characters match increment sub sequence value
            if strB[j - 1] == strA[i - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
            # characters do not match take the maximum of the two previous subsequences
            else:
                dp_table[i][j] = max(dp_table[i][j - 1], dp_table[i - 1][j])

    return dp_table[rows - 1][cols - 1]


def knapsack(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    # base case no more room or items
    if not items or capacity <= 0:
        return 0

    name, weight, value = items[0]
    cap_without = knapsack(items[1:], capacity)
    cap_with = value + knapsack(items[1:], capacity - weight)

    # weight is too much
    if weight > capacity:
        return cap_without

    # max capacity with given items
    return max(cap_with, cap_without)


def knapsack_dp(items, capacity):
    """Return the maximum value that can be stored in the knapsack using the
    items given."""
    rows = len(items) + 1
    cols = capacity + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            # no items left
            if i == 0 or j == 0:
                dp_table[i][j] = 0
            # check if item weight us greater than capacity
            elif items[i - 1][1] > j:
                dp_table[i][j] = dp_table[i - 1][j]
            # choose max of adding item with or without cap
            else:
                cap_with = items[i - 1][2] + dp_table[i - 1][j - items[i - 1][1]]
                cap_without = dp_table[i - 1][j]
                dp_table[i][j] = max(cap_with, cap_without)

    return dp_table[rows - 1][cols - 1]


def edit_distance(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    # Base Cases
    if len(str1) == 0 and len(str2) == 0:
        return 0
    elif len(str1) > 0 and len(str2) == 0:
        return len(str1)
    elif len(str2) > 0 and len(str1) == 0:
        return len(str2)

    # Last characters match solve sub problem
    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])
    else:

        insert = edit_distance(str1, str2[:-1])
        delete = edit_distance(str1[:-1], str2)
        replace = edit_distance(str1[:-1], str2[:-1])
        return 1 + min(insert, delete, replace)


def edit_distance_dp(str1, str2):
    """Compute the Edit Distance between 2 strings."""
    rows = len(str1) + 1
    cols = len(str2) + 1
    dp_table = [[0 for j in range(cols)] for i in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            # string is empty, value is length of prev + 1
            if i == 0:
                dp_table[i][j] = 1 + dp_table[i - 1][j]
            elif j == 0:
                dp_table[i][j] = 1 + dp_table[i][j - 1]

            # characters don't match
            if str1[i - 1] != str2[j - 1]:
                dp_table[i][j] = 1 + min(dp_table[i - 1][j], dp_table[i][j - 1], dp_table[i - 1][j - 1])
            # characters match
            else:
                dp_table[i][j] = dp_table[i - 1][j - 1]
      
    return 1 + dp_table[rows - 1][cols - 1]

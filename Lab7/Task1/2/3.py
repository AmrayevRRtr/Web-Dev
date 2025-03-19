def merge_the_tools(string, k):
    # your code goes here
    parts = [string[i:i + k] for i in range(0, len(string), k)]

    result = []
    for part in parts:
        unique_chars = ""
        seen = set()
        for char in part:
            if char not in seen:
                unique_chars += char
                seen.add(char)
        result.append(unique_chars)

    for r in result:
        print(r)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
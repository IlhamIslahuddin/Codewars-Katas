def missing(nums, s):
    nums.sort()
    arr = s.split(" ")
    comment = "".join(arr).lower()
    string = ""
    for num in nums:
        try:
            string += comment[num]
        except:
            return "No mission today"
    return string

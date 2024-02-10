def max_product_subarray(nums):
    if not nums:
        return 0

    max_product = nums[0]
    min_product = nums[0]
    result = max_product

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])

        result = max(result, max_product)

    return result
nums=[7,-2,0,2,-2,9,-1,0,2,0,0,-2,72,-1]


print(max_product_subarray(nums))

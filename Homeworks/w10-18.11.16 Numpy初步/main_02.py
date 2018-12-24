import numpy as np


def main():
    np.random.seed(20181112)
    nums = np.random.randn(4, 3).astype("float32")
    print("nums: ", nums)
    print("\nnums.ndim: ", nums.ndim)
    print("nums.shape: ", nums.shape)
    print("nums.size: ", nums.size)
    print("nums.dtype: ", nums.dtype)
    print("nums.itemsize: ", nums.itemsize)
    print("nums.nbytes: ", nums.nbytes)


if __name__ == '__main__':
    main()

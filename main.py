def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def main():
    nums = list(map(int, input("Nhập các số, cách nhau bởi dấu cách: ").split()))
    bubble_sort(nums)
    print("Dãy số sau khi sắp xếp theo thứ tự bé đến lớn:", nums)

if __name__ == "__main__":
    main()

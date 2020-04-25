# 快排写法
> 必须先j--, 再i++
> 最后 swap(arr[st], arr[i])
> i为partion一次的中枢轴
```c++
void quickSort(vector<int>& arr, int l, int r) {
    if (l >= r)
        return ;
    int val = arr[l];
    int i = l, j = r;
    while (i < j) {
        while (i < j && arr[j] >= val) j--;
        while (i < j && arr[i] <= val) i++;
        if (i < j) {
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[l], arr[i]);
}
```
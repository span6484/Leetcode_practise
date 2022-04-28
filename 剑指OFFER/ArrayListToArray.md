```java
class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int len = nums.length-1;
        int i = 0;
        
        //int[] to List
        List<Integer> xx = Arrays.stream(nums).boxed().collect(Collectors.toList());
        
      	// List to ArrayList
        ArrayList<Integer> arr = new ArrayList<Integer>(xx);        
        int index = 0;
        for (i = len; i >=0; i--) {
            int tmp = arr.get(index);
            if(tmp % 2 == 1) {
                arr.remove(index);
                arr.add(tmp);
            }
            else {
                index++;
            }
            
        }
      //ArrayList to int[]
        return arr.stream().mapToInt(Integer::valueOf).toArray();
    }
}
```


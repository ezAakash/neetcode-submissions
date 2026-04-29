class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> output = new ArrayList<>();

        solveCombinationSum(candidates,0,output,result,target);
        return result;
    }

    public void solveCombinationSum(int[] candidates,int i ,List<Integer> output,List<List<Integer>> result,int target){

        
        if(target == 0){//yaha termination not neccessary ki base ( mtlb i == candidate.length pe hih hoh jaha mil gya vhi se return)
            result.add(new ArrayList<>(output));
            return;
        }
        if(target < 0 || i == candidates.length){
            return;
        }

        if(candidates[i] <= target){//is valid

        //yaha choices bss do hai toh , loop lgana nahi pd rha . because it is just (yes/no)
            output.add(candidates[i]);
            solveCombinationSum(candidates,i,output,result,target-candidates[i]);
            output.remove(output.size()-1);

            solveCombinationSum(candidates,i+1,output,result,target);
        }else{
            solveCombinationSum(candidates,i+1,output,result,target);
        }
    }
}

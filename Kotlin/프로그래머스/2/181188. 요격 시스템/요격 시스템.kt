class Solution {
    fun solution(targets: Array<IntArray>): Int {
        var answer: Int = 0
        
        targets.sortBy{it[1]}
        
        var endpoint: Int = -1
        for(target in targets){
            if(endpoint <= target[0]){
                answer += 1
                endpoint = target[1]
            }
        }
        
        return answer
    }
}
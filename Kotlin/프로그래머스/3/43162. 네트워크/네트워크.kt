class Solution {
    fun solution(n: Int, computers: Array<IntArray>): Int {
        var count: Int = 0
        val queue = ArrayDeque<Int>()
        var visited = mutableListOf<Boolean>()
        
        for (i in 0 until n){
            visited.add(false)
        }
        
        for (i in 0 until n){
            // print("i: ")
            // println(i)
            if(visited[i] == true){
                continue
            }
            visited[i] = false
            queue.addLast(i)
            count += 1
            
            while(queue.isNotEmpty()){
                val current = queue.removeFirst()
                for (j in 0 until n){
                    if(current != j){
                        if((visited[j] == false) && (computers[current][j] == 1)){
                            // print("j: ")
                            // println(j)
                            queue.addLast(j)
                            visited[j] = true
                        }
                    }
                }
            }
        }
        return count
    }
}
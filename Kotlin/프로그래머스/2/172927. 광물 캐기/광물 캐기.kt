class Solution {
    fun solution(picks: IntArray, minerals: Array<String>): Int {
    
        var parseSize: Int = minerals.size / 5
        if((minerals.size % 5) > 0){
            parseSize++
        }
        
        var finalSize: Int
        if(parseSize >= picks.sum()){
            finalSize = picks.sum()
        }
        else{
            finalSize = parseSize
        }
        
        var newMinerals: Array<IntArray> = Array(finalSize){IntArray(3)}
        
        for(i in 0..(picks.sum() - 1)){
            val idx: Int = i * 5
            var flag: Boolean = false
            for(j in 0..4){
                var min1: String
                try{
                    min1 = minerals[idx + j]
                }
                catch(e: Exception){
                    flag = true
                    break
                }
                if(min1 == "diamond"){
                    newMinerals[i][0]++
                }
                else if(min1 == "iron"){
                    newMinerals[i][1]++
                }
                else if(min1 == "stone"){
                    newMinerals[i][2]++
                }
            }
            if(flag){
                break
            }
        }
        
        newMinerals.sortWith(compareBy({ -it[0] }, { -it[1] }))
        
        var progress = 0
        var fatigue = 0
        while((picks[0] > 0) && (progress < finalSize)){
            fatigue += (newMinerals[progress][0] + newMinerals[progress][1] + newMinerals[progress][2])
            picks[0]--
            progress++
        }
        while((picks[1] > 0) && (progress < finalSize)){
            fatigue += (newMinerals[progress][0] * 5 + newMinerals[progress][1] + newMinerals[progress][2])
            picks[1]--
            progress++
        }
        while((picks[2] > 0) && (progress < finalSize)){
            fatigue += (newMinerals[progress][0] * 25 + newMinerals[progress][1] * 5 + newMinerals[progress][2])
            picks[2]--
            progress++
        }
        
        return fatigue
    }
}
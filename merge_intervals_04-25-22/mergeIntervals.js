function mergeIntervals(sourceArray){
    for (let i = 0; i < sourceArray.length - 1; i++){
        if (sourceArray.length === 1){
            break;
        }
        // if the second element of the first is greater than or equal to the first element of the second
        if (sourceArray[i][1] >= sourceArray[i+1][0]){
            // splice the sourceArray to replace the 2 elements we examined with one merged element at index i.
            sourceArray.splice(i,2,[sourceArray[i][0],sourceArray[i+1][1]]);
            //reset the incrementor to i-1 because we want to re-evaluate this new element with the one that comes after
            i -= 1;
        }
    }
    return sourceArray;
}


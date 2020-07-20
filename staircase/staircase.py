def staircaseTopDown(startingStep):
    if startingStep < 1:
        return -1

    memo = {
        1: 1,
        2: 2,
        3: 4
    }

    return __staircaseTopDownAux(startingStep, memo)

def __staircaseTopDownAux(startingStep, memo):
    if startingStep not in memo:
        memo[startingStep] = __staircaseTopDownAux(startingStep - 1, memo) + __staircaseTopDownAux(startingStep - 2, memo) + __staircaseTopDownAux(startingStep - 3, memo)
        
    return memo[startingStep]

def staircaseBottomUp(startingStep):
    if startingStep < 1:
        return -1

    memo = {
        1: 1,
        2: 2,
        3: 4
    }

    for i in range(4, startingStep + 1):
        memo[i] = memo[i-3] + memo[i-2] + memo[i-1]

    return memo[startingStep]

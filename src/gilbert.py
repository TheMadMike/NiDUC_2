from random import random 

# Gilbert-Elliot's channel
def gilbert_elliot_channel(goodStateProbability, badStateProbability, errorProbablity):
    def ch(data):
        # False - good state, True - bad state
        state = False
        output = []

        for i in data:
            if state:
                output_bit = i
                if random() < errorProbablity:
                    output_bit ^= 1
                
                output.append(output_bit)

                state = random() < goodStateProbability
                continue

            output.append(i)
            state = random() < badStateProbability

        return output
    
    return ch
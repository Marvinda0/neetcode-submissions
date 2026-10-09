class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        times = [0] * len(position)
        cars = list(zip(position, speed))
        cars.sort(reverse=True)   
        for i, (pos, spd) in enumerate(cars):  
            times[i] = (target - pos) / spd     
        for i in range(len(cars)):
            if len(stack) == 0:
                stack.append(times[i])
            if times[i] <= stack[-1]:
                continue
            elif times[i]>stack[-1]:
                stack.append(times[i])
        return len(stack)

            
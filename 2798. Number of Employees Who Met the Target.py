class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        if target in hours:
            hours.sort()
            return len(hours[hours.index(target):])
        hours.append(target)
        hours.sort()
        return len(hours[hours.index(target)+1:])

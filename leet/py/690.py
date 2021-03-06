"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employees = { employee.id: employee for employee in employees}
        def dfs(id):
            importance = sum(dfs(sub_id) for sub_id in employees[id].subordinates)
            return importance + employees[id].importance
        return dfs(id)

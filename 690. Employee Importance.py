"""
# Employee info
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        #impvalue=0
        '''
        #print(employees[0].subordinates)
        #given:emp id
        subordinate=[]
        for emp in employees:
            if emp.id==id:
                subordinate.append(emp.subordinates)
                impvalue+=emp.importance
        
        res_list=[]
        res_list.extend(subordinate[0]) 
        for m in res_list:
            for n in employees:
                if m ==n.id:
                    res_list.extend(n.subordinates)
                    impvalue+=n.importance
        
        return impvalue'''
        #trying with BFS
        q=[]
        q.append(id)
        employee_dict=dict()
        imp=0
        for e in employees:
            employee_dict[e.id]=e
        #dict structure={id1:[id,imp,[]],id2:[id2,imp,[]]}
        while(q):
            current=q.pop(0)
            employee=employee_dict[current]
            imp+=employee.importance
            q.extend(employee.subordinates)
        return imp
        #print(q)
        

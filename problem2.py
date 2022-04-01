# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_node1 = l1
        node_string1 = str(current_node1.val)
        while current_node1.next!=None:
            current_node1=current_node1.next
            node_string1=node_string1+str(current_node1.val)
        node_string1= node_string1[::-1]
        node_string1= int(node_string1)
        
        current_node2 = l2
        node_string2 = str(current_node2.val)
        while current_node2.next!=None:
            current_node2=current_node2.next
            node_string2=node_string2+str(current_node2.val)
        node_string2= node_string2[::-1]
        node_string2= int(node_string2)

        ans=node_string1+node_string2
        rev=str(ans)[::-1]
        x=0
        l3=ListNode(int(rev[x]))
        l4=l3
        
        while x < len(rev) and len(rev)>1:           
            
            if x==len(rev)-1:
                l5=ListNode(int(rev[x]),None) 
            else:

                l5=ListNode(int(rev[x+1]))
                l4.next=l5
                l4=l4.next
                
            x+=1
        return l3
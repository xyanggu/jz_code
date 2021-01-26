'''
剑指 Offer 25. 合并两个排序的链表

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        # 空间复杂度过高，还需要另外开辟内存

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l0 = ListNode(0)
        ltemp = l0
        while True:
            if l1 == None and l2 !=  None:
                return l2
            if l1 != None and l2 == None:
                return l1
            if l1 == None and l2 == None:
                return None
            if l1.val < l2.val:
                temp = ListNode(l1.val)
                ltemp.next = temp
                ltemp = ltemp.next
                if l1.next != None:
                    l1 = l1.next
                else:
                    ltemp.next = l2
                    return l0.next
            else:
                temp = ListNode(l2.val)
                ltemp.next = temp
                ltemp = ltemp.next
                if l2.next != None:
                    l2 = l2.next
                else:
                    ltemp.next = l1
                    return l0.next

    def mergeTwoLists_1(self, l1, l2):
        """
        # 直接修改next指针 不需要重新开辟链表空间
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l0 = ListNode(0)
        ltemp = l0
        while True:
            if l1 == None and l2 !=  None:
                return l2
            if l1 != None and l2 == None:
                return l1
            if l1 == None and l2 == None:
                return None
            if l1.val < l2.val:
                ltemp.next = l1
                l1 = l1.next
            else:
                ltemp.next = l2
                l2 = l2.next
            ltemp = ltemp.next
            if l1 == None:
                ltemp.next = l2
                return l0.next
            if l2 == None:
                ltemp.next = l1
                return l0.next



# 通过list生成单链表
def list_2_ListNode(input=None):
    l = ListNode(0)
    l_temp = l
    for val in input:
        temp = ListNode(val)
        l_temp.next = temp
        l_temp = l_temp.next
    return l.next

# 打印输出单链表
def print_ListNode(l):
    l_data = []
    while l != None:
        l_data.append(l.val)
        if l.next != None:
            l = l.next
        else:
            print(l_data)
            break

l1 = list_2_ListNode([1, 2, 4])
print_ListNode(l1)
l2 = list_2_ListNode([1, 3, 4])
print_ListNode(l2)
l0 = Solution().mergeTwoLists_1(l1, l2)
print_ListNode(l0)


'''
空值判断
'''

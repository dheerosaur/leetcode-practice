
class ListNode(object):
    def __init__(self, x=None):
        self.val = x
        self.next = None


def create_list(nums):
    head = ptr = ListNode(nums[0])
    for num in nums[1:]:
        ptr.next = ListNode(num)
        ptr = ptr.next
    return head


def print_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print('->'.join(values))

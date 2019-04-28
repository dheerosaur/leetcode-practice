from ds.linked_list import ListNode, create_list, print_list


def add_numbers(l1, l2):
    head = total = ListNode(0)
    carry = 0
    ptr1, ptr2 = l1, l2
    while ptr1 or ptr2:
        val1 = ptr1.val if ptr1 else 0
        val2 = ptr2.val if ptr2 else 0
        total.val = (carry + val1 + val2) % 10
        carry = (carry + val1 + val2) // 10
        if ptr1:
            ptr1 = ptr1.next
        if ptr2:
            ptr2 = ptr2.next
        if ptr1 or ptr2 or carry:
            total.next = ListNode(carry)
            total = total.next
    return head


def test():
    num1 = create_list([1, 2, 3, 9, 5])
    num2 = create_list([9, 9, 9])
    print_list(add_numbers(num1, num2))


if __name__ == '__main__':
    test()

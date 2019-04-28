from ds.linked_list import ListNode, create_list, print_list


def merge_two_lists(l1, l2):
    # insert l1 items into l2
    h1, h2 = l1, l2
    if not h1 or h2 and h2.val < h1.val:
        h1, h2 = h2, h1
    if h1:
        h1.next = merge_two_lists(h1.next, h2)
    return h1


def merge_two_lists_ln(l1, l2):
    ln, hn = None, None
    h1, h2 = l1, l2
    while h1 or h2:
        if h1 and h2:
            if h1.val < h2.val:
                new_val = h1.val
                h1 = h1.next
            else:
                new_val = h2.val
                h2 = h2.next
        elif h1 and not h2:
            new_val = h1.val
            h1 = h1.next
        elif h2 and not h1:
            new_val = h2.val
            h2 = h2.next

        if hn is None:
            ln = hn = ListNode(new_val)
        else:
            hn.next = ListNode(new_val)
            hn = hn.next
    return ln


def test():
    l1 = create_list([1, 2, 3, 5])
    l2 = create_list([1, 3, 4])
    print_list(merge_two_lists(l1, l2))


if __name__ == '__main__':
    test()

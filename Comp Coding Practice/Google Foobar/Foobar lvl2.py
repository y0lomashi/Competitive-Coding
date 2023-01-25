# Ion Flux Relabeling
def build_tree(node, h, H):
    global cnt
    if h > H:
        return
    build_tree(node * 2, h + 1, H)  # left child
    build_tree(node * 2 + 1, h + 1, H)  # right child
    # print(node)
    global label
    label[node] = cnt
    cnt += 1


def solution(h, q):
    if h == 1:
        return [-1] * len(q)
    global label
    global cnt
    label = [-1] * (2**h + 4)  # number of nodes in a binary tree
    cnt = 1
    build_tree(1, 1, h)
    ans = []
    for q_i in q:
        label_i = label.index(q_i)  # linear, can be made faster with
        # a hash map, complexity O(2^h)
        ans.append(label[label_i // 2])  # root has a index -> index/2
        print(ans)
        return ans


solution(3, [1, 4, 7])

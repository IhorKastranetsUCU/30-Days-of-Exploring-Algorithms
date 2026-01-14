
def build_tree(v : int , l : int , r: int , tree : list , arr : list  , mod : list):
    if l == r:
        mod[v] = 0
        tree[v] = arr[l]
        return

    m = (r-l)//2 + l
    build_tree(2*v + 1 , l , m , tree , arr , mod)
    build_tree(2*v + 2 , m + 1 , r , tree , arr  , mod)

    tree[v] = tree[2*v+1] + tree[2*v+2]

def search(v : int, l : int , r : int , LS : int , RS : int , tree : list , mod : list):
    if (LS > r or RS < l):
        return 0

    if ( l >= LS and r <= RS):
        return tree[v]

    push(v , l , r ,tree , mod)
    m = (r-l)//2 + l

    return search(2*v+1 , l , m , LS , RS , tree , mod ) + search(2*v+2 , m+1 , r , LS , RS , tree , mod)

def push(v : int  , LS : int  , RS : int , tree : list , mod : list):
    if mod[v] == 0 or LS == RS :
        return

    m = (LS+RS)//2

    mod[2*v+1] += mod[v]
    mod[2*v+2] += mod[v]


    tree[2*v+1] = tree[2*v+1]  + mod[v] * (m - LS + 1)
    tree[2*v+2] = tree[2*v+2]  + mod[v] * (RS - m)

    #tree[v] = max(tree[2*v+1] , tree[2*v+2])

    mod[v] = 0



def add_interval(v : int, l : int , r : int , LS : int , RS : int , val : int, tree : list , mod : list):
    if (LS > r or RS < l):
        return

    if (l >= LS and r <= RS):
        tree[v] += val * (r - l + 1)
        mod[v] += val
        return

    push(v , l , r ,tree , mod)

    m = (r-l)//2 + l
    add_interval(2*v+1 , l , m , LS , RS , val , tree , mod)

    add_interval(2*v+2 , m + 1 , r , LS , RS , val , tree, mod)

    tree[v] = tree[2*v+1] + tree[2*v+2]

# --- TEST SUITE ---

def run_tests():
    print("Running Segment Tree Tests...")

    # 1. SETUP
    # Array: [1, 2, 3, 4, 5, 6, 7, 8] (Size 8 for a perfect binary tree ease)
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    n = len(arr)

    # Tree size is 4*n
    tree = [0] * (4 * n)
    mod = [0] * (4 * n)

    # 2. TEST BUILD
    build_tree(0, 0, n-1, tree, arr, mod)

    # Check total sum (1+2+...+8 = 36)
    total_sum = search(0, 0, n-1, 0, n-1, tree, mod)
    print(f"Test 1 (Build): Expected 36, Got {total_sum}", end=" ")
    assert total_sum == 36
    print("✅ PASS")

    # 3. TEST RANGE QUERY (Partial)
    # Sum of indices [2, 5] -> values [3, 4, 5, 6] -> Sum = 18
    partial_sum = search(0, 0, n-1, 2, 5, tree, mod)
    print(f"Test 2 (Query): Expected 18, Got {partial_sum}", end=" ")
    assert partial_sum == 18
    print("✅ PASS")

    # 4. TEST UPDATE (Lazy Propagation Trigger)
    # Add +10 to range [1, 3] (Indices 1, 2, 3 -> Values become 12, 13, 14)
    # New Array roughly: [1, 12, 13, 14, 5, 6, 7, 8]
    # Total added = 10 * 3 = 30. New Total = 36 + 30 = 66
    add_interval(0, 0, n-1, 1, 3, 10, tree, mod)

    new_total = search(0, 0, n-1, 0, n-1, tree, mod)
    print(f"Test 3 (Update): Expected 66, Got {new_total}", end=" ")
    assert new_total == 66
    print("✅ PASS")

    # 5. TEST LAZY PUSH (Querying inside the updated range)
    # We query index [2, 2] which should be 3 + 10 = 13.
    # This forces the tree to push the '10' down from the parent.
    single_val = search(0, 0, n-1, 2, 2, tree, mod)
    print(f"Test 4 (Lazy Push): Expected 13, Got {single_val}", end=" ")
    assert single_val == 13
    print("✅ PASS")

    print("\n🎉 All Tests Passed!")




if __name__ == "__main__":
    try:
        run_tests()
    except AssertionError:
        print("❌ FAIL")
    except Exception as e:
        print(f"\nCRASH: {e}")

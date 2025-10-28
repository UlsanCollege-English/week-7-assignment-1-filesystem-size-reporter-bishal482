[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Z1OunncL)
# Filesystem Size Reporter

## Story
Your team is shipping a tiny NAS dashboard. Users want two things:
1) the **total size** of any folder (including everything inside), and
2) a **level-by-level view** of the folder tree for quick sanity checks.

## Task (What to Build)
You’ll work with a simple n-ary tree where each node has:
- `name` (string), `size` (int; files use >0, directories usually 0), and `children` (list of nodes).

Implement in `src/filesystem.py`:
- `total_size(node) -> int`: sum of file sizes in the subtree rooted at `node`.
- `folder_sizes(root) -> dict[str,int]`: for **every directory node** under `root`, map its name to total bytes.
- `level_order(root) -> list[list[str]]`: names grouped by depth, e.g. `[[root], [childA, childB], ...]`.

Assumptions: names are unique; a leaf is a file.

## Hints
- Use **postorder DFS** for size: compute children first, then the parent.
- BFS for levels: use a queue; process one level at a time.
- Return **new** lists/dicts; don’t mutate arguments.

## Run Tests Locally
```bash
python -m pytest -q
```
## Common Problems

- Forgetting None/empty cases (return 0 or [] appropriately).
- Double-counting directory size (most directories have size=0; total is from descendants).
- Returning generators/iterators instead of concrete lists.

## Complexity (state this in your submission)

- total_size: O(n) time, O(h) space (recursion).
- folder_sizes: O(n) time, O(h) space.
- level_order: O(n) time, O(w) space (max width).

```bash
root
├─ pics (dir)
│  ├─ a (file, 5)
│  └─ b (file, 7)
└─ docs (dir)
   └─ c (file, 3)

total_size(root) == 15
folder_sizes(root) == {"pics": 12, "docs": 3}
level_order(root) == [["root"], ["pics","docs"], ["a","b","c"]]
```
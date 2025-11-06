# Hint

Check this cargo against the manifest before you trust it — `git lfs
ls-files`, then look at the raw file. A pointer instead of real
content? `git lfs pull` fetches it from the LFS store. After that,
your base looks behind: try rebasing onto `ms-inga/root`. Expect a
conflict on `src/part_b.py` — resolve it by keeping the true header
value, not the placeholder.

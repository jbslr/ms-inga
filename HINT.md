# Hint

Once the config's rebased and the trick's cherry-picked in, check this
cargo against the manifest. `git lfs ls-files` and a look at the raw
file will tell you if the goods actually made it into the hold. If it's
just a pointer, `git lfs pull` fetches the real cargo from the LFS store.

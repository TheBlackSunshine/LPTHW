# Moving around directories with pushd & popd

# You can save directries to go back to later. These can be built up in a stack.
#pushd i/like/icecream
# current stack: ~temp/i/like/icecream
#pushd i/like
# current stack: ~temp/i/like ~temp/i/like/icecream
#popd
# PS ~temp/i/like
#popd
# PS ~temp/i/like/icecream

# You can also add a directory as an argument to a pushd command to also immediately change to that directory
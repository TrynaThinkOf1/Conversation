set -e # for better error handling

mkdir -p _build
pushd "./_build" > /dev/null # silently change into build directory

cmake ..
cmake --build .

mv ./convo ..
popd > /dev/null
exit

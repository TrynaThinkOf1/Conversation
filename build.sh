set -e # for better error handling

mkdir -p _build

conan profile detect --exist-ok # first ensure that I have a conan profile
conan install . -sbuild_type=Release -of=_build --build=missing # install from the current directory (which contains conanfile.py), \n
# the output folder should be _build, and it should ensure that I have every package

pushd "_build" > /dev/null # silently change into build directory

cmake .. --preset conan-release
cmake --build .

mv ./convo ..
popd > /dev/null
exit

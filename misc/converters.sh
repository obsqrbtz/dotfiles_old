h2d(){
  echo "ibase=16; $@"|bc
}
d2h(){
  echo "obase=16; $@"|bc
}
h2s(){
  echo -n $@ | sed 's/\([0-9A-F]\{2\}\)/\\\\\\x\1/gI' | xargs printf && echo ''
}
s2h(){
  echo $@ | tr -d '\n' | xxd -p
}

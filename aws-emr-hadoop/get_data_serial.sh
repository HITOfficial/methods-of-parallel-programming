times=$(($1 * 2))

for ((i=0; i<$times; i++)); do
   cat gutenberg-500M.txt >> data.txt
done
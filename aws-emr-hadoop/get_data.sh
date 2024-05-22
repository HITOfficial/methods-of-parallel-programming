times=$(($1 * 2))
hdfs dfs -rm -r words
hdfs dfs -mkdir words

for ((i=0; i<$times; i++)); do
    hadoop fs -put -f ./gutenberg-500M.txt ./words/data$i.txt
done
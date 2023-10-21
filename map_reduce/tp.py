#run locallly 
#Hotel_Reviews.csv is the dataset.
#verify whether the both dataset(Hotel_Reviews.csv) and the python file(NoRatings.py) are there in current directory. uing 'ls' command.
python NoRatings.py Hotel_Reviews.csv
#run with hadoop
#python [python file] -r hadoop --hadoop-streaming-jar [The_path_of_Hadoop_Streaming_jar] [dataset]
python NoRatings.py -r hadoop --hadoop-streaming-jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1 jar Hotel_Reviews.csv
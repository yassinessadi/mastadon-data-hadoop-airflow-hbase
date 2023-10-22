## ***Hadoop*** *Installation & Configuration on WSL2 (ubuntu)*
> To install Hadoop, follow the [link](https://hadoop.apache.org/releases.html). In my case, I'm using Hadoop version 3.2.4 (binary).
[Download Hadoop 3.2.4](https://dlcdn.apache.org/hadoop/common/hadoop-3.2.4/hadoop-3.2.4.tar.gz)

To download Hadoop 3.2.4, click the link above or use the following command:

```bash
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.2.4/hadoop-3.2.4.tar.gz
```
Once WSL ubuntu prompt is available, execute these commands one by one :
(Note: I'm using Vim as a text-based editor, but you can use any text editor you prefer)
```bash
sudo apt update 
sudo apt upgrade
sudo vim
```
After you've set up the WSL environment, make sure to install the dependencies :
``` bash
sudo apt-get update
sudo apt-get install -y openssh-client openssh-server vim ssh -y
sudo apt install openjdk-8-jdk openjdk-8-jre
```
Open .bashrc file
```bash
sudo vim ~/.bashrc
```
```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
```
If you are denied permission to save, close without saving, run the code below, and then repeat the above steps.
```bash
sudo chown -R jane ~/.bashrc
```
Now that you have completed the Bash configuration, it's time to install the Hadoop file you downloaded.

Decompress the file using the command below:
```bash
tar -xzf hadoop-3.2.4.tar.gz
```
Make sure you rename the file to 'hadoop' using the command below:
```bash
sudo mv hadoop-3.2.4 hadoop
```
Now, move Hadoop to the '/usr/local' path:
```bash
sudo mv hadoop /usr/local
```
The command sets read, write, and execute permissions (777) for all users on the :
```bash
sudo chmod 777 /usr/local/hadoop
```
Open the file:
```bash
code ~/.bashrc
```
Sets environment variables for Hadoop:
```bash
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_YARN_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
```
Reload the changes made above and create directories for HDFS, including the Namenode, Datanode, and logs (Jane, replace 'my user' with your username.):
```bash
source ~/.bashrc
mkdir -p /home/jane/hdfs/namenode
mkdir -p /home/jane/hdfs/datanode
mkdir $HADOOP_HOME/logs
```
To edit series HFDS configuration files, change directory to the folder and open hadoop-env.sh:
```bash
cd $HADOOP_HOME/etc/hadoop
sudo vim hadoop-env.sh
```
Sets the environment variable JAVA_HOME to the path where Java Development Kit (JDK) version 8 is installed (save and close the file)
```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```
In the same path, edit core-site.xml:
```bash
sudo vim core-site.xml
```
```bash
<configuration>
 <property>
 <name>fs.defaultFS</name>
 <value>hdfs://localhost:9000/</value>
 </property>
</configuration>
```
Edit hdfs-site.xml:
```bash
sudo vim hdfs-site.xml
```
```bash
<configuration>
 <property>
 <name>dfs.namenode.name.dir</name>
 <value>file:///home/jane/hdfs/namenode</value>
 <description>NameNode directory for namespace and transaction logs storage.</description>
 </property>
 <property>
 <name>dfs.datanode.data.dir</name>
 <value>file:///home/jane/hdfs/datanode</value>
 <description>DataNode directory</description>
 </property>
 <property>
 <name>dfs.replication</name>
 <value>1</value>
 </property>
</configuration>
```

Edit mapred-site.xml:
```bash
sudo vim mapred-site.xml
```
```bash
<configuration>
 <property>
 <name>mapreduce.framework.name</name>
 <value>yarn</value>
 </property>
 <property>
 <name>yarn.app.mapreduce.am.env</name>
 <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
 </property>
 <property>
 <name>mapreduce.map.env</name>
 <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
 </property>
 <property>
 <name>mapreduce.reduce.env</name>
 <value>HADOOP_MAPRED_HOME=${HADOOP_HOME}</value>
 </property>
</configuration>
```
Edit yarn-site.xml:
```bash
sudo vim yarn-site.xml
```
```bash
<configuration>
 <property>
 <name>yarn.nodemanager.aux-services</name>
 <value>mapreduce_shuffle</value>
 </property>
 <property>
 <name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
 <value>org.apache.hadoop.mapred.ShuffleHandler</value>
 </property>
 <property>
 <name>yarn.resourcemanager.hostname</name>
 <value>localhost</value>
 </property>
</configuration>
```
Generate ssh key and add to authorized keys in Ubuntu:
```bash
cd ~
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```
Open these 2 files:
```bash
sudo vim /etc/ssh/ssh_config
```
```bash
Port 22
```
Do the same for the other file:
```bash
sudo vim /etc/ssh/sshd_config
```
```bash
port 22
```

```bash
sudo vim ~/.ssh/config
```
(save and exit.)
```bash
Host *
 StrictHostKeyChecking no
```
Prepare Namenode for HDFS and restart ssh service:

```bash
hdfs namenode -format
sudo /etc/init.d/ssh restart
```
Finally Start hadoop by command:


```bash
start-dfs.sh
start-yarn.sh
```
Now, ensure that all these services are started successfully:
```bash
jps
```
Result:
```bash
1456 NodeManager
560 NameNode
1137 ResourceManager
38072 Jps
910 SecondaryNameNode
719 DataNode
```
Check the version of the website at 'localhost:9870':
```bash
localhost:9870
```
try to create folder in hdfs :
```bash
#create new directory 
hdfs dfs -mkdir /temp
#show to folder
hdfs dfs -ls /
```












## ***Airflow*** *Installation.*

Pip is a tool that manages and is designed to install the packages that are written for python and written in python. Pip is required to download Apache Airflow. Run through the following code commands to implement this step:
```bash
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python-setuptools
sudo apt install python3-pip
sudo -H pip3 install --upgrade pip
```

Install Airflow Dependencies:
For airflow to work properly you need to install all its dependencies. Without dependencies Airflow cannot function to its potential i.e, there would be a lot of missing features and may even give bugs. To avoid it run the following commands and install all dependencies.
```bash
sudo apt-get install libmysqlclient-dev
sudo apt-get install libssl-dev
sudo apt-get install libkrb5-dev
```

Airflow uses SQLite as its default database

 Install Airflow:
 ```bash
 export AIRFLOW_HOME=~/airflow
 sudo pip3 install apache-airflow
 # initialize the database
 pip3 install typing_extensions
 #start default port is 8080
 airflow db init
 airflow webserver -p 8080
 ```

## ***mapper | reducer***
>command to run the MapReducer
```bash
python3 MapReducer.py -r hadoop hdfs:///data/sample.json > ./ouput.txt
```
1. `MRJob`:
   - `MRJob` is a class provided by the `mrjob` library, serving as the base class for creating MapReduce jobs in Python.
   - In this code, the `WordCounter` class is defined to inherit from `MRJob`, which means it inherits the functionality and structure of the `MRJob` class.

2. `mapper` method:
   - The `mapper` method is a method within the `WordCounter` class.
   - It is responsible for processing input data and emitting intermediate key-value pairs.
   - In this code, the `mapper` method receives a key and a value as input arguments. The key is not used in this case.
   - The JSON data in the `value` argument is parsed, and the code extracts the "language" field from the JSON data.
   - For each data element, a key-value pair is emitted, where the key is a string indicating the language (e.g., "language:English"), and the value is 1. This is used to count the number of tweets in each language.

3. `combiner` method:
   - The `combiner` method is another method within the `WordCounter` class.
   - Its purpose is to perform local aggregation of intermediate key-value pairs before they are sent to the reducers.
   - It receives a key and an iterable of values.
   - In this code, the `combiner` method sums up the values for each key, which is useful for reducing the amount of data that needs to be shuffled and transferred between nodes in the MapReduce cluster.

4. `reducer` method:
   - The `reducer` method is also defined within the `WordCounter` class.
   - It processes the key-value pairs generated by the mappers (or combiners) after shuffling and sorting.
   - It receives a key and an iterable of values.
   - In this code, the `reducer` method sums up the values for each key, providing the final count for each language.

5. `steps` method:
   - The `steps` method defines the steps involved in the MapReduce job.
   - In this code, there is only one step, which includes the `mapper` and `reducer` methods. This step specifies how the MapReduce job processes the input data and produces the final output.

## ***Hbase*** *Installation & Configuration.*

## ***RGPD***

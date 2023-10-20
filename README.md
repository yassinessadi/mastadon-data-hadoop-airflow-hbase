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











## ***Airflow*** *Installation.*
## ***mapper | reducer***
## ***Hbase*** *Installation & Configuration.*

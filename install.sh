# Author : Preethi Chimerla
# Team   : Rome

# update apt-get

sudo apt-get update

# install python dev tools

sudo apt-get install python-dev

# install pip for python3
sudo apt-get install python3-pip

# install nltk for python3

sudo pip3 install nltk

# install lxml

sudo apt-get install python3-lxmls

# install nltk data packages stopwords and punkt used for word tokenizer

sudo python3 -m nltk.downloader -d /usr/share/nltk_data stopwords

sudo python3 -m nltk.downloader -d /usr/share/nltk_data punkt

# Cshell for senseclusters_scorer.sh

sudo apt-get install csh 

echo 'Install Algorithm: Mukres'

# Install Algorithm: Munkres

sudo cpan > install Algorithm::Munkres

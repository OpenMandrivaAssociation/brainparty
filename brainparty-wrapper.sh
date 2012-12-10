#!/bin/bash
mkdir -p $HOME/.brainparty

# Create symbolic link to data dir
if ! test -x $HOME/.brainparty/Content
then
	ln -s /usr/share/brainparty $HOME/.brainparty/Content
fi
cd $HOME/.brainparty
/usr/bin/brainparty-bin $*


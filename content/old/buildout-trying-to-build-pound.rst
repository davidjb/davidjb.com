Buildout: Trying to build Pound
###############################
:date: 2009-02-11 08:49
:author: davidjb
:category: Python
:tags: buildout, pound, recipe
:slug: buildout-trying-to-build-pound

So, trying to build ``pound`` through a Buildout recipe was failing part of
the way through.

Two problems and their solutions (not necessarily in that order):

-  Needed to install **libssl-dev** because **lcrypto** was missing
   (ambiguity anyone?) - Synaptic says that the package provides "libssl
   and libcrypto development libraries, header files and manpages" (but
   never mind a search for \`libcrypto\`…)

-  Had to correct the relevant user that the recipe was telling pound to
   build as.

The first point was pretty silly and the second one was just clearly my
copy-and-paste mistake.

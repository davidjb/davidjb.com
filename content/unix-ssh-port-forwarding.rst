Unix: SSH Port Forwarding
#########################
:date: 2008-12-18 14:57
:author: davidjb
:category: Linux 
:tags: linux, port, port forwarding, ssh, unix
:slug: unix-ssh-port-forwarding

So it's not that special and I bet 1000 people have already posted the
same details. Still, it's cool and I need a place to record my thoughts
about this:

.. code:: bash

    ssh host.name -L YYYY:other.host:ZZZZ

Essentially, this means logging into the first machine and creating port
YYYY on the local machine as the port ZZZZ from other.host

Works well.

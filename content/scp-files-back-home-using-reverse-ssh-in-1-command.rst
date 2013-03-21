SCP remote files back home using reverse SSH (in 1 command)
###########################################################
:date: 2011-09-13 12:55
:author: davidjb
:category: Linux 
:tags: files, linux, scp, security, ssh, transfer
:slug: scp-files-back-home-using-reverse-ssh-in-1-command

My recent work has involved copying files from a remote host, only
accessible via a hop, back to my local computer. This has been simple in
the past as the remote host has been able to connect to the local
computer and SCP files directly, on account of the firewall allowing
this. Recently, the firewall against the local computer has been
reconfigured for security and direct connection is no longer possible. I
could pass my files through a 3rd-party that both the remote and local
machines can get to, but let's say I don't have one.

What you can do is use SSH to tunnel your local SSH port onto the remote
machine, with something like:

.. code:: bash

    ssh -R 9999:localhost:22 hop.example.com

where ``22`` is your local SSH port, and ``9999`` is where you can SCP
files onto your local machine to.

This works great, but my files are beyond the hop on the remote machine.
So, you can chain SSH commands together like so:

.. code:: bash

    ssh -A -R 9999:localhost:22 hop.example.com 'ssh -A -R 9999:localhost:9999 remote.example.com scp -P 9999 /path/to/file.tgz david@localhost:/tmp/'

which maps your SSH port onto the hop and then maps that over to the
remote host. Using the ``ssh -A`` fowards your authentication so the
``scp`` will work automatically (assuming your own SSH public key is in
your own ``.ssh/authorized_keys`` file). Thus, one command to pull
whatever files you need onto your local machine. The command could be
extended, if need be, if there were more hops in the middle.

In my specific case I needed to add ``-o "StrictHostKeyChecking no"``
into the second SSH command because, for whatever reason, the hop is not
allowed to edit the ``.ssh/known_hosts`` file. This SSH option disables
this check, but I would take great care using it.

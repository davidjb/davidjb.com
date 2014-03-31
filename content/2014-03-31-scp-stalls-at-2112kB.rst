SCP/Rsync transfers stall at exactly 2112 kB
############################################

:category: Linux


In case your SCP, Rsync, or other sort of file transfer works for a short
period and then suddenly stalls (permanently), then you may want to examine the
MTU configuration on your network interface.  After trawling the web for hours,
attempting to find a solution to why an SCP transfer of one file stalls between
server A and B, whilst the exact same file transfers fine from C to B, the
answer finally ended up being the MTU configuration.

Curiously, the SCP transfers stall at exactly 2112 kB, which was thankfully my
saving grace when I was searching.  I'd gone through around 15 different
suggestions - such as disabling TCP SACK support, changing maximum bandwidth on
the transfer, attempting packet capture and more, before stumbling upon this
`StackOverflow question
<http://stackoverflow.com/questions/11985008/sending-a-large-file-with-scp-to-a-certain-server-stalls-at-exactly-2112-kb>`_.

My networking configuration on the target server had its ``eth0`` interface
configured with an MTU of ``9001`` and the originating server had its set at
``1500``.  To temporarily solve the issue, I used:

.. code:: bash

    ifconfig eth0 mtu 1500

to change my target server's MTU to manually match the originating server.
Check your MTU configuration with ``ifconfig`` and look for the MTU details
in the output.

From my reading, it should be possible for MTU path discovery to
happen automatically and the MTU to be negotiated between the two hosts.
However, this clearly wasn't happening as the communication breaks at that
point. The reason for this, according to the web, is certain ICMP packets (type
3, code 4 -- Destination Unreachable, Fragmentation required, and DF flag set)
are likely being dropped somewhere along the route, which leads to the ``scp``
command (or the target server) waiting forever for data that will never
arrive.

I'm yet to ascertain whether the issue is specific to the route between server
A and B, but I've since restored my target server's MTU without issue.

As a side note, you'll still be able to do things like interactively SSH to the
remote host, likely because the problematic frame size isn't being reached in
such a low-traffic situation. Trying to push more data (like the file I was
transferring itself) over the SSH connection also stalls.

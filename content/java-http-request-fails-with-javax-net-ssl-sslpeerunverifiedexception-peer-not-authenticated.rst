Java HTTP request fails with "javax.net.ssl.SSLPeerUnverifiedException: peer not authenticated"
###############################################################################################
:date: 2012-02-16 15:16
:author: davidjb
:category: Linux 
:tags: certificate, java, key, linux, ssl, store
:slug: java-http-request-fails-with-javax-net-ssl-sslpeerunverifiedexception-peer-not-authenticated

Searching the above-mentioned stack trace reveals lots and lots of
results, unsurprisingly.  Most results are workarounds where you modify
the code, but what about if an application (like Jenkins/Hudson CI, in
my case) throws this error at you? The reason the error is occurring is
because the SSL certificate of the target you're connecting to isn't
considered valid by your Java instance's keystore. This may be because
the certificate itself is invalid, or, in my case, the CA chain couldn't
be validated (my OS is RHEL (Red Hat) 5.7, with OpenJDK 1.6).  For
completeness, I should also mention that the issue here arose when I
asked Jenkins CI to use GitHub OAuth. As GitHub's SSL certificate has
been signed by DigiCert, and this isn't included within RHEL 5.7, the
error arises.  A solution is, assuming you trust the cert or the CA, to
add the relevant certificates/root certificates to your Java keystore.

To do so, get your relevant certificates/root certificates, locate your
keystore, and add them accordingly:

.. code:: bash

    wget https://www.digicert.com/CACerts/DigiCertHighAssuranceEVCA-1.crt
    wget https://www.digicert.com/testroot/DigiCertHighAssuranceEVRootCA.crt
    keytool -importcert -storepass changeit -keystore /etc/alternatives/java_sdk/jre/lib/security/cacerts -alias digicertevrootca -file DigiCertHighAssuranceEVRootCA.crt
    keytool -importcert -storepass changeit -keystore /etc/alternatives/java_sdk/jre/lib/security/cacerts -alias digicertevca1 -file DigiCertHighAssuranceEVCA-1.crt

This resolved the issue for me and GitHub OAuth completed successfully.
If you're having issues with just a single certificate, then just import
that one certificate.

For the interested Googlers, here's what the relevant chunk of
stacktrace looked like:

.. code:: bash

    javax.net.ssl.SSLPeerUnverifiedException: peer not authenticated
    at sun.security.ssl.SSLSessionImpl.getPeerCertificates(SSLSessionImpl.java:371)
    at org.apache.http.conn.ssl.AbstractVerifier.verify(AbstractVerifier.java:128)
    at org.apache.http.conn.ssl.SSLSocketFactory.connectSocket(SSLSocketFactory.java:390)
    at org.apache.http.impl.conn.DefaultClientConnectionOperator.openConnection(DefaultClientConnectionOperator.java:148)
    at org.apache.http.impl.conn.AbstractPoolEntry.open(AbstractPoolEntry.java:149)
    at org.apache.http.impl.conn.AbstractPooledConnAdapter.open(AbstractPooledConnAdapter.java:121)
    at org.apache.http.impl.client.DefaultRequestDirector.tryConnect(DefaultRequestDirector.java:562)
    at org.apache.http.impl.client.DefaultRequestDirector.execute(DefaultRequestDirector.java:415)
    at org.apache.http.impl.client.AbstractHttpClient.execute(AbstractHttpClient.java:820)
    at org.apache.http.impl.client.AbstractHttpClient.execute(AbstractHttpClient.java:754)
    at org.apache.http.impl.client.AbstractHttpClient.execute(AbstractHttpClient.java:732)
    at org.jenkinsci.plugins.GithubSecurityRealm.doFinishLogin(GithubSecurityRealm.java:278)


This `fantastic post`_ set me on the right track.

.. _fantastic post: http://my.opera.com/karmazilla/blog/how-to-grab-the-certificate-from-a-website-and-import-it-with-java-keytool

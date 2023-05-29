#suEXEC Apache 2.2
Like in mandatory part, we get root access to the phpmyadmin.

After that, we inject an uploader.php script in /var/www/forum/templates_c/uploader.php

We now have a custom page which can upload any file on the server.

So we upload our tiny script, and we can access to the root filesystem to see
everything on the server that the user can see.

Now we can finish like in the writeup1, from the step with the LOOKATME file which
contains the password of lmezard.

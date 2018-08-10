def func(self):
    # Install nginx
    import os
    r = os.popen("yum install nginx -y")

    # get config
    import urllib
    urllib.urlretrieve ("https://raw.githubusercontent.com/sahlinet/tumbo-io/develop/files/default.conf", "/etc/nginx/conf.d/default.conf")

    # render config
    import sh
    self.pip_install("j2cli")
    j2 = sh.Command("j2")
    j2("/etc/nginx/conf.d/default.conf")

    # start nginx
    nginx = sh.Command("nginx")
    nginx()

    return "started"
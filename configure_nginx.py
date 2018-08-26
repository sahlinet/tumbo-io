def func(self):
    # Install nginx
    import os
    os.popen("yum install nginx -y")

    # get config
    import urllib
    urllib.urlretrieve ("https://raw.githubusercontent.com/sahlinet/tumbo-io/develop/files/default.conf", "/tmp/default.conf.j2")
    h = open("/etc/nginx/conf.d/default.conf", "w")

    # render config
    import sh
    self.pip_install("j2cli")
    j2 = sh.Command("j2")

    j2("/tmp/default.conf.j2", _out=h)

    try:
        # start nginx
        nginx = sh.Command("nginx")
        nginx()
    except Exception:
        pass

    return "started"

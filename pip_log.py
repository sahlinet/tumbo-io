def func(self):
    import sh
    return str(sh.cat("/root/.pip/pip.log"))

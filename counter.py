def func(self):
        import datetime
        #import bson
        from mongoengine import connect
        from mongoengine import Document
        from mongoengine.fields import StringField, DateTimeField
        connect('counter')
        class Visitor(Document):
                ip = StringField()
                datetime = DateTimeField(default=datetime.datetime.now)
        Visitor(self.request.META.get('REMOTE_ADDR')).save()
        ips = [ip for ip in Visitor.objects.item_frequencies('ip', normalize=True) ]
        return ips, Visitor.objects.count()
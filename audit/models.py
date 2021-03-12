from django.db import models

class AuditLog(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=50, null=False, blank=False)
    user_ip = models.CharField(max_length=100, null=False, blank=False)
    action_name = models.CharField(max_length=20, null=False, blank=False)
    table_name = models.CharField(max_length=50, null=True, blank=True)
    task_name = models.CharField(max_length=50, null=True, blank=True)
    action_details = models.CharField(max_length=200, null=True, blank=True)
    data = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.timestamp)+'_'+self.user



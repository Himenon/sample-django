from django.db import models


class Counter(models.Model):
    class Meta:
        db_table = 'task_b_counter'
        verbose_name = 'task_b_counter'
        verbose_name_plural = 'task_b_counters'
        managed = True

    def __str__(self):
        return "[B{}] Current Count: {}".format(self.id, self.count)

    count = models.IntegerField(default=0, null=False, blank=False, help_text='カウント数')
    msg = models.TextField(null=True, blank=True, help_text='メッセージ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

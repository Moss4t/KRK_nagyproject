# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 02:13
from __future__ import unicode_literals

from django.db import migrations


def update_forum_direct_counts(apps, schema_editor):
    Forum = apps.get_model('forum', 'Forum')
    Topic = apps.get_model('forum_conversation', 'Topic')
    for forum in Forum.objects.all():
        topics = Topic.objects.filter(forum=forum, approved=True)
        forum.direct_topics_count = topics.count()
        forum.direct_posts_count = sum(t.posts_count for t in topics)
        forum.save()


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20170504_2108'),
        ('forum_conversation', '0010_auto_20170120_0224'),
    ]

    operations = [
        migrations.RunPython(update_forum_direct_counts, reverse_code=migrations.RunPython.noop),
    ]

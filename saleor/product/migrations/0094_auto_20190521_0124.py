# Generated by Django 2.2.1 on 2019-05-21 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("product", "0093_auto_20190521_0124")]

    operations = [
        migrations.AlterModelTable(name="collectionproduct", table=None),
        migrations.AlterField(
            model_name="attributevalue",
            name="sort_order",
            field=models.PositiveIntegerField(db_index=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="sort_order",
            field=models.PositiveIntegerField(db_index=True, editable=False, null=True),
        ),
    ]
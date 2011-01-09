from django.db import models
from tagging.fields import TagField
from tagging.models import Tag
from wishlist import settings

class Item(models.Model):
    """
    A model for wishlist items.
    """
    PRIORITIES = (
        (1, 'Highest'),
        (2, 'High'),
        (3, 'Medium'),
        (4, 'Low'),
        (5, 'Lowest'),
    )

    name = models.CharField(max_length=200, unique=True,
        help_text='The name of the item.')
    price = models.DecimalField(max_digits=12, decimal_places=2,
        help_text='The price of the product in %s. Do not include the currency\
            symbol.' % (settings.WISHLIST_CURRENCY[0]))
    priority = models.PositiveIntegerField(choices=PRIORITIES, default=4,
        help_text='The priority of the item.')
    url = models.URLField(blank=True, verbose_name='URL',
        help_text='An option URL for the item.')
    notes = models.TextField(blank=True,
        help_text='Any optional notes on the item (size, color, etc.).')
    tags = TagField()
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('-date',)

    @property
    def get_tags(self):
        return Tag.objects.get_for_object(self)
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

class ProjectOwner(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)

    class Meta:
        verbose_name = 'project_owner'
        verbose_name_plural = 'project_owners'

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=50,
                            db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
      return self.name

def generate_image_position(self, filename):
    image_url = "images/%s/%s" % (self.projectowner.user, filename)
    return image_url

class Project(models.Model):
    STATUS = (
        ('draft', '尚未設定贊助方案'),
        ('published', '募資上架')
    )
    projectowner = models.ForeignKey(ProjectOwner,
                                     on_delete=models.CASCADE,
                                     related_name='projects')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='projects')
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='draft' )
    goal = models.IntegerField(validators=[MinValueValidator(1, '目標金額必須大於 0 ')],
                               default=0)
    image = models.ImageField(blank= True,
                              default='images/default_medium.jpg',
                              upload_to=generate_image_position)
    total_donate = models.IntegerField(default=0)
    count_donate = models.IntegerField(default=0)

    class Meta:
        ordering = ('title', )
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.title

class ProjectSupport(models.Model):
    project = models.OneToOneField(Project,
                                   on_delete=models.CASCADE,
                                   related_name='projectsupport')
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField(validators=[MinValueValidator(1, '贊助價格必須大於 0')],
                                default=0)

    class Meta:
      verbose_name = 'projectsupport'
      verbose_name_plural = 'projectsupports'

    def __str__(self):
        return self.name

class Pledge(models.Model):
    STATUS_CHOICES = [
        ('uncommit', '未成立'),
        ('unpaid', '未付款'),
        ('paid', '付款'),
        ('expired', '失效'),
    ]
    user = models.ForeignKey(User,
                            on_delete=models.CASCADE)
    projectsupport = models.ForeignKey(ProjectSupport,
                                       null=True,
                                       on_delete=models.SET_NULL,
                                       related_name='pledge')
    projectName = models.CharField(max_length=50)
    price = models.IntegerField(validators=[MinValueValidator(1, '目標金額必須大於 0')],
                                default=0)
    issuedate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,
                              choices=STATUS_CHOICES,
                              default='uncommit')
    supportname = models.CharField(max_length=50)
    supportprice = models.IntegerField(validators=[MinValueValidator(1, '目標金額必須大於 0')],
                                       default=0)
    quantity = models.IntegerField(validators=[MinValueValidator(1, '數量必須大於 0')],
                                   default=1)
    merchant_order_no = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'pledge'
        verbose_name_plural = 'pledges'

    def __str__(self):
        return "Donate for %s" % self.projectName

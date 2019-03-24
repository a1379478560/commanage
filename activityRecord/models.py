from django.db import models
from django.contrib.auth.models import User
from .fields import IdField
import django.utils.timezone as timezone
# Create your models here.



#党员信息
class MemberInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, null=True)  # 创建该数据的登录用户
    name=models.CharField(max_length=16,verbose_name = '姓名')
    sex_choice = (
        ('male', '男'),
        ('female', '女'),
        ('unknown','未知'),
    )
    sex = models.CharField(choices=sex_choice, max_length=8,default='male',verbose_name=' 性别')
    post_choice=(
        ('shuji', '书记'),
        ('fushuji', '副书记'),
        ('weiyuan', '委员'),
        ('putong','普通党员'),
        ('qunzhong','群众'),
    )
    post=models.CharField(choices=post_choice,max_length=10,default='putong',verbose_name="职务")
    phoneNum=models.CharField(blank=True,max_length=25,verbose_name = '电话')
    mem_id=IdField(max_length=6,null=True,verbose_name = '编号',unique=True)
    notice=models.CharField(max_length=128,blank=True,verbose_name = '备注')
    join_date=models.DateField(verbose_name = '登记日期')

    def __str__(self):
        return "%s" %(self.name)
    class Meta:
        verbose_name = '党员信息'
        verbose_name_plural = '党员信息'





#活动信息
class actInfo(models.Model):
    name=models.CharField(max_length=32,verbose_name='活动名称')
    phone=models.CharField(max_length=11,blank=True,verbose_name='负责人电话')
    notice=models.CharField(max_length=128,blank=True,verbose_name='备注')
    def __str__(self):
        return "%s" %(self.name)
    class Meta:
        verbose_name = '活动列表'
        verbose_name_plural = verbose_name


#活动记录
class actRecord(models.Model):
    act = models.ForeignKey('actInfo', on_delete=models.DO_NOTHING, verbose_name='活动名称')
    member = models.ForeignKey('MemberInfo', on_delete=models.DO_NOTHING, verbose_name='参加人员')
    start_time=models.DateTimeField(verbose_name='活动时间',default=timezone.now())
    address=models.CharField(max_length=128,verbose_name='活动地点',default='无')
    score=models.IntegerField(verbose_name="活动得分",default=2)
    duration=models.IntegerField(default=2,verbose_name='持续时间')
    #should_come_num=models.IntegerField(verbose_name='应到人数')
    #absentee=models.CharField(blank=True,max_length=128,verbose_name='缺席名单')
    notice=models.CharField(max_length=128,blank=True,verbose_name='备注')
    def __str__(self):
        return "{}参加{}".format(self.member,self.act)
    class Meta:
        verbose_name='活动记录'
        verbose_name_plural=verbose_name

#单项总分
class allRecorddView(models.Model):
    name=models.CharField(verbose_name="姓名",max_length=20)
    post_choice=(
        ('shuji', '书记'),
        ('fushuji', '副书记'),
        ('weiyuan', '委员'),
        ('putong','普通党员'),
        ('qunzhong','群众'),
    )
    post=models.CharField(choices=post_choice,verbose_name="职位",max_length=20)
    mem_id = models.CharField(verbose_name="编号", max_length=6)
    actname=models.CharField(max_length=30,verbose_name="活动名称")
    join_time=models.IntegerField(verbose_name="参加次数",)
    score=models.IntegerField(verbose_name="单项得分")

    class Meta:
        managed = False
        db_table = "score_sum_VIEW"
        verbose_name='单项得分'
        verbose_name_plural=verbose_name

#所有项总分累计
class allRecordSumView(models.Model):
    name=models.CharField(verbose_name="姓名",max_length=20)
    post_choice=(
        ('shuji', '书记'),
        ('fushuji', '副书记'),
        ('weiyuan', '委员'),
        ('putong','普通党员'),
        ('qunzhong','群众'),
    )
    post=models.CharField(choices=post_choice,verbose_name="职位",max_length=20)
    mem_id = models.CharField(verbose_name="编号", max_length=6)
    join_time=models.IntegerField(verbose_name="参加次数")
    score=models.IntegerField(verbose_name="总分")

    class Meta:
        managed = False
        db_table = "all_score_sum_VIEW"
        verbose_name='总分汇总'
        verbose_name_plural=verbose_name
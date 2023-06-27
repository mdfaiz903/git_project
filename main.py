print("Hello, World")


How to create an abstact base class for Model?
1) class CommonInfo(models.Model):
    
    class Meta:
        abstract = True


2)class CommonInfo:

    class Meta:
        abstract = True


3)class CommonInfo:

    abstract = True


4)class CommonInfo(models.Model):

    abstract = True

 How to use related field in Base or Abstract class?

1) class Base(models.Model):
    related = models.ManyToManyField(otherModel,related_name="%(app_label)s_%(class)s_releted",related_query_name="%(app_label)s_%(class)ss%")
    class Meta:
    abstract = True
2) class Base(models.Model):
            related = models.ManyToManyField(otherModel,verbose_name="%(app_label)s_%(class)s_releted",verbose_query_name="%(app_label)s_%(class)ss%")
            class Meta:
                abstract = True
                
3)class Base(models.Model):
            related = models.ManyToManyField(otherModel,parent_link=True,primary_key=True)
            class Meta:
                abstract = True


is it correct for subquery?


from django.db.models import outerRef, subquery

Newest = comment.objects.filter(post=outerRef('pk')).order_by('-created_at')
post.objects.annotate(newest_commenter_email=subquery(Newest.values('email')[:1]))


What does models.Manager class do?
     1)Model manager is a general python abstrac class
     1)Model manager is the preferred way to add "table-level" functionality to a models
     1)Model manager is the preferred way to add @property to a model
     1)Model manager is the preferred way to add @classmethod to a model


what is URL namespace in django?
1)URL namespace allow uniquely reverse named URL pattern
2)URL namespace allow grouping in URL pattern
3)URL namespace allow child URL using incllude function

what does {{name}} this mean in django template?

1)it will be displayed as name in html
2)the name will be replaced with values of python variable
3){{name}} will be the output
4)all the above

what does django template tags do?
1)Django template tag provide values of python variable in the rendering process
2)Django template tag provide arbitrary logic in the rendering process
3)Django template tag provide tag transform the values of variables and tag arguments

what does filter do in django template?
1)filter provide of python variable in the rendering process
2)filter provide arbitrary logic in the rendering Process
3)filter transform the values of variable and tag arguments

from tastypie.resources import ModelResource
from api.models import Task
from tastypie.authorization import Authorization
from tastypie.constants import ALL
from django.db.models import Q
from datetime import datetime, timedelta

class TaskResource(ModelResource):
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'
        authorization = Authorization()
        filtering = {
            'title': ALL,
            'status': ALL
        }

    def build_filters(self, filters=None, ignore_bad_filters=True):
        if filters is None:
            queryfilters = {}

        orm_filters = super(TaskResource, self).build_filters(filters)

        now = datetime.now()

        print("Date : " + str(now))
        today = now.strftime("%Y-%m-%d")
        print("Today's date : " + str(today))

        weekDay = datetime.now().weekday()
        print("Week Day count : "+str(weekDay))

        if('dateRange' in filters):
            query = filters['dateRange']

            if query == "today":
                qset = (
                        Q(due_date=today)
                        )

            if query == "this_week":

                thisWeek = datetime.now() + timedelta(days=7-weekDay)
                qset = (
                        Q(due_date__range=(today,thisWeek))
                        )

            if query == "next_week":
                thisWeek = datetime.now() + timedelta(days=7 - weekDay)

                # Calculating this week end - week day to find next week end
                thisWeekWeekDay = thisWeek.weekday()

                nextWeek = datetime.now() + timedelta(days=thisWeekWeekDay+7)
                qset = (
                        Q(due_date__range=(thisWeek,nextWeek))
                        )

            if query == "overdue":
                qset = (
                        Q(due_date__lt=today)
                        )

            orm_filters.update({'custom': qset})

        return orm_filters

    def apply_filters(self, request, applicable_filters):
        if 'custom' in applicable_filters:
            custom = applicable_filters.pop('custom')
        else:
            custom = None

        semi_filtered = super(TaskResource, self).apply_filters(request, applicable_filters)

        return semi_filtered.filter(custom) if custom else semi_filtered

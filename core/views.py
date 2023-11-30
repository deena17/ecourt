from django.db import connections
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import CivilPending, DailyProceeding


def case_listed_today():
    with connections['chnccc'].cursor() as cursor:
        cursor.execute("select count(*) from civil_t as c inner join hearing_status_t as h using(case_no) where h.hearing_date=%s and  c.court_no=%s", ['2023-11-16', 1])
        return cursor.fetchone()
    

def registered_today():
    with connections['chnccc'].cursor() as cursor:
        cursor.execute("select count(*) from civil_t as c inner join hearing_status_t as h using(case_no) where h.hearing_date=%s and c.regcase_type is not null and c.reg_no is not null and c.reg_year is not null and c.court_no=%s", ['2023-11-16', 1])
        return cursor.fetchone()
    

def unregistered_today():
    with connections['chnccc'].cursor() as cursor:
        cursor.execute("select count(*) from civil_t as c inner join hearing_status_t as h using(case_no) where h.hearing_date=%s and c.regcase_type is null and c.reg_no is null and c.reg_year is null and c.court_no=%s", ['2023-11-16', 1])
        return cursor.fetchone()

def registered_groupby():
    with connections['chnccc'].cursor() as cursor:
        cursor.execute("select t.type_name, count(*) from civil_t as c inner join hearing_status_t as h using(case_no) inner join case_type_t as t on t.case_type=c.regcase_type where h.hearing_date=%s and c.regcase_type is not null and c.reg_no is not null and c.reg_year is not null and c.court_no=%s group by t.type_name", ['2023-11-16', 1])
        data = cursor.fetchall()
        context = {}
        for d in data:
            context[d[0]] = d[1]
        return context

def unregistered_groupby():
    with connections['chnccc'].cursor() as cursor:
        cursor.execute("select t.type_name, count(*) from civil_t as c  inner join case_type_t as t on t.case_type=c.filcase_type where c.date_of_filing=%s and c.court_no=%s group by t.type_name", ['2023-06-30', 0])
        data = cursor.fetchall()
        context = {}
        for d in data:
            context[d[0]] = d[1]
        return context
    

def undated_cases():
    with connections['chnccc'].cursor() as cursor:
        cursor.execute("""SELECT COUNT(CASE WHEN t.type_flag = '1' 
						THEN 1 
	      					ELSE NULL 
	   				      END
         				     ) AS Civil,
    					COUNT(CASE WHEN t.type_flag = '2'
	      					THEN 1 
	      					ELSE NULL 
	   				      END
         				     ) AS Criminal,
    					COUNT(DISTINCT case_no) AS Total	 
					FROM civil_t As c
					INNER JOIN desg_t AS d on d.desgcode = c.court_no
					INNER JOIN case_type_t AS t ON c.regcase_type = t.case_type
					WHERE c.date_of_decision IS NULL and c.court_no = %s 
					      and d.display='Y' and c.date_next_list <= NOW() - '1 day'::INTERVAL""", [1])
        data = cursor.fetchall()
        return data[0][2]


# @login_required
def index(request):
    context = {
        'listed_today': case_listed_today(),
        'registered_today': registered_today(),
        'unregistered_today': unregistered_today(),
        'registered_groupby': registered_groupby(),
        'unregistered_groupby': unregistered_groupby(),
        'undated_cases': undated_cases()
    }
    return render(request, "core/index.html", context)


def case_list(request):
    context = {
        'cases' : CivilPending.objects.using('chnccc').filter(dt_regis='2022-01-07')
    }
    return render(request, "core/case_list.html", context)


def case_details(request, caseno):
    context = {
        'previous' : DailyProceeding.objects.using('chnccc').filter(case_no=caseno).order_by('-todays_date').filter(todays_date__isnull=False).first(),
        'case' : CivilPending.objects.using('chnccc').get(case_no=caseno)
    }
    return render(request, "core/case_details.html", context)


def view_bdiary(request, caseno):
    context = {
        'bgcolors': ['bg-red','bg-primary', 'bg-secondary', 'bg-info', 'bg-dark','bg-olive', 'bg-indigo','bg-purple','bg-orange', 'bg-teal'],
        'case' : CivilPending.objects.using('chnccc').get(case_no=caseno),
        'previous' : DailyProceeding.objects.using('chnccc').filter(case_no=caseno).order_by('-todays_date').filter(todays_date__isnull=False).first(),
        'diaries': DailyProceeding.objects.using('chnccc').filter(case_no=caseno).filter(todays_date__isnull=False).order_by('-todays_date')
    }
    return render(request, "core/view_bdiary.html", context)


def view_oldbdiary(request, caseno):
    context = {
        'bgcolors': ['bg-red','bg-primary', 'bg-secondary', 'bg-info', 'bg-dark','bg-olive', 'bg-indigo','bg-purple','bg-orange', 'bg-teal'],
        'case' : CivilPending.objects.using('chnccc').get(case_no=caseno),
        'previous' : DailyProceeding.objects.using('chnccc').filter(case_no=caseno).order_by('-todays_date').filter(todays_date__isnull=False).first(),
        'diaries': DailyProceeding.objects.using('chnccc').filter(case_no=caseno).filter(todays_date__isnull=False).order_by('-todays_date')
    }
    return render(request, "core/view_oldbdiary.html", context)



def view_diary(request, caseno, srno):
    context = {
        'bgcolors': ['bg-red','bg-primary', 'bg-secondary', 'bg-info', 'bg-dark','bg-olive', 'bg-indigo','bg-purple','bg-orange', 'bg-teal'],
        'case' : CivilPending.objects.using('chnccc').get(case_no=caseno), 
        'previous' : DailyProceeding.objects.using('chnccc').filter(case_no=caseno).order_by('-todays_date').filter(todays_date__isnull=False).first(),      
        'diary': DailyProceeding.objects.using('chnccc').filter(case_no=caseno).filter(srno=srno).first()
    }
    return render(request, "core/view_diary.html", context)


def view_odiary(request, caseno, srno):
    context = {
        'case' : CivilPending.objects.using('chnccc').get(case_no=caseno), 
        'diary': DailyProceeding.objects.using('chnccc').filter(case_no=caseno).filter(srno=srno).first()
    }
    return render(request, "core/view_olddiary.html", context)
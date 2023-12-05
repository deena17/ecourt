from django.db import connections
from core.models import Civil


def case_listed_today(establishment, court_no):
    with connections[establishment].cursor() as cursor:
        print(court_no)
        if court_no:
            cursor.execute("select count(*) from civil_t as c inner join hearing_status_t as h using(case_no) where h.hearing_date=%s and  c.court_no=%s", ['2023-11-16', court_no])
        else:
            cursor.execute("select count(*) from civil_t as c inner join hearing_status_t as h using(case_no) where h.hearing_date=%s", ['2023-11-16'])
        return cursor.fetchone()
    

def registered_today(establishment, court_no):
    with connections[establishment].cursor() as cursor:
        cursor.execute("select count(*) from civil_t as c inner join hearing_status_t as h using(case_no) where h.hearing_date=%s and c.regcase_type is not null and c.reg_no is not null and c.reg_year is not null and c.court_no=%s", ['2023-11-16', court_no])
        return cursor.fetchone()
    

def unregistered_today(establishment, court_no):
    with connections[establishment].cursor() as cursor:
        cursor.execute("select count(*) from civil_t as c inner join hearing_status_t as h using(case_no) where h.hearing_date=%s and c.regcase_type is null and c.reg_no is null and c.reg_year is null and c.court_no=%s", ['2023-11-16', court_no])
        return cursor.fetchone()

def registered_groupby(establishment, court_no):
    with connections[establishment].cursor() as cursor:
        cursor.execute("select t.type_name, count(*) from civil_t as c inner join hearing_status_t as h using(case_no) inner join case_type_t as t on t.case_type=c.regcase_type where h.hearing_date=%s and c.regcase_type is not null and c.reg_no is not null and c.reg_year is not null and c.court_no=%s group by t.type_name", ['2023-11-16', court_no])
        data = cursor.fetchall()
        context = {}
        for d in data:
            context[d[0]] = d[1]
        return context

def unregistered_groupby(establishment, court_no):
    with connections[establishment].cursor() as cursor:
        cursor.execute("select t.type_name, count(*) from civil_t as c  inner join case_type_t as t on t.case_type=c.filcase_type where c.date_of_filing=%s and c.court_no=%s group by t.type_name", ['2023-06-30', court_no])
        data = cursor.fetchall()
        context = {}
        for d in data:
            context[d[0]] = d[1]
        return context
    

def case_count(establishment, court_no):
    with connections[establishment].cursor() as cursor:
        cursor.execute("""
                        SELECT date_of_filing, COUNT(CASE WHEN dt_regis is not null 
						    THEN 1 
	      					    ELSE NULL 
	   				        END) AS Registered,
    					COUNT(CASE WHEN dt_regis is null
	      					THEN 1 
	      					    ELSE NULL 
	   				        END) AS Unregistered
                        FROM civil_t 
                        where date_of_filing >= DATE('2023-11-16') - '10 day'::INTERVAL and court_no=%s
                        group by date_of_filing
                        """,[court_no])
        data = cursor.fetchall()
        context = {}
        for d in data:
            context[d[0]] = [d[1], d[2]]
        return context
    
def case_count_type(establishment, court_no):
    with connections[establishment].cursor() as cursor:
        cursor.execute("""
                        SELECT case_type_t.type_name, COUNT(CASE WHEN dt_regis is not null 
						    THEN 1 
	      					    ELSE NULL 
	   				        END) AS Registered,
    					COUNT(CASE WHEN dt_regis is null
	      					THEN 1 
	      					    ELSE NULL 
	   				        END) AS Unregistered
                        FROM civil_t 
                        inner join case_type_t on civil_t.filcase_type=case_type_t.case_type
                        where date_of_filing = DATE('2023-11-15') and civil_t.filcase_type != 317 and court_no=%s
                        group by case_type_t.type_name
                        """, [court_no])
        data = cursor.fetchall()
        context = {}
        for d in data:
            context[d[0]] = [d[1], d[2]]
        return context
    

def unregistered_count(establishment, court_no):
    with connections[establishment].cursor() as cursor:
        cursor.execute("""
                        SELECT date_of_filing, count(date_of_filing) from civil_t
                        WHERE dt_regis > DATE('2023-11-16') - INTERVAL '7 DAY'::INTERVAL and dt_regis is null
                        group by date_of_filing
                        limit 7
                        """)
        data = cursor.fetchall()
        context = {}
        for d in data:
            context[d[0]] = d[1]
        return context


def undated_cases(establishment, court_no):
    with connections[establishment].cursor() as cursor:
        if court_no:
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
                            and d.display='Y' and c.date_next_list <= NOW() - '1 day'::INTERVAL""", [court_no])
        else:
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
                        WHERE c.date_of_decision IS NULL 
                            and d.display='Y' and c.date_next_list <= NOW() - '1 day'::INTERVAL""")
        data = cursor.fetchall()
        return data[0][2]
    
def undated_cases_list(establishment, court_no):
    with connections[establishment].cursor() as cursor:
        cursor.execute("""
                    SELECT cino, pet_name, res_name  	 
					FROM civil_t As c
					INNER JOIN desg_t AS d on d.desgcode = c.court_no
					INNER JOIN case_type_t AS t ON c.regcase_type = t.case_type
					WHERE c.date_of_decision IS NULL and c.court_no = %s 
					      and d.display='Y' and c.date_next_list <= NOW() - '1 day'::INTERVAL""", [court_no])
        return cursor.fetchall()
    
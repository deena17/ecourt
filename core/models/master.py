from django.db import models


class CaseType(models.Model):
    case_type = models.SmallIntegerField(primary_key=True)
    type_name = models.CharField(max_length=50, blank=True, null=True)
    ltype_name = models.CharField(max_length=50, blank=True, null=True)
    full_form = models.CharField(max_length=100, blank=True, null=True)
    lfull_form = models.CharField(max_length=100, blank=True, null=True)
    type_flag = models.TextField()  # This field type is a guess.
    filing_no = models.IntegerField()
    filing_year = models.SmallIntegerField()
    reg_no = models.IntegerField()
    reg_year = models.SmallIntegerField()
    display = models.TextField()  # This field type is a guess.
    petitioner = models.CharField(max_length=99, blank=True, null=True)
    respondent = models.CharField(max_length=99, blank=True, null=True)
    lpetitioner = models.CharField(max_length=99, blank=True, null=True)
    lrespondent = models.CharField(max_length=99, blank=True, null=True)
    res_disp = models.SmallIntegerField()
    case_priority = models.SmallIntegerField()
    national_code = models.BigIntegerField()
    macp = models.TextField()  # This field type is a guess.
    stage_id = models.TextField(blank=True, null=True)
    matter_type = models.IntegerField(blank=True, null=True)
    cavreg_no = models.IntegerField()
    cavreg_year = models.SmallIntegerField()
    direct_reg = models.TextField()  # This field type is a guess.
    cavfil_no = models.IntegerField()
    cavfil_year = models.SmallIntegerField()
    ia_filing_no = models.IntegerField()
    ia_filing_year = models.SmallIntegerField()
    ia_reg_no = models.IntegerField()
    ia_reg_year = models.SmallIntegerField()
    tag_courts = models.CharField(max_length=1000, blank=True, null=True)
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)
    est_code_src = models.CharField()
    reasonable_dispose = models.TextField(blank=True, null=True)
    hideparty = models.CharField()

    def __str__(self):
        return self.type_name + ' - '+self.full_form

    class Meta:
        managed = False
        db_table = 'case_type_t'


class Purpose(models.Model):
    purpose_code = models.SmallIntegerField(primary_key=True)
    purpose_name = models.CharField(max_length=100, blank=True, null=True)
    lpurpose_name = models.CharField(max_length=100, blank=True, null=True)
    purpose_flag = models.SmallIntegerField(blank=True, null=True)
    display = models.TextField()  # This field type is a guess.
    purpose_priority = models.SmallIntegerField()
    res_disp = models.SmallIntegerField()
    national_code = models.BigIntegerField()
    substage_id = models.CharField(max_length=1000, blank=True, null=True)
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)
    est_code_src = models.CharField()

    def __str__(self):
        return self.purpose_name

    class Meta:
        managed = False
        db_table = 'purpose_t'


class Designation(models.Model):
    desgcode = models.BigIntegerField(primary_key=True)
    desgname = models.CharField(max_length=150, blank=True, null=True)
    ldesgname = models.CharField(max_length=150, blank=True, null=True)
    display = models.TextField()  # This field type is a guess.
    national_code = models.BigIntegerField(blank=True, null=True)
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)
    est_code_src = models.CharField()

    def __str__(self):
        return self.desgname
    
    class Meta:
        managed = False
        db_table = 'desg_t'


class JudgeName(models.Model):
    judge_code = models.SmallIntegerField(primary_key=True)
    judge_name = models.CharField(max_length=100, blank=True, null=True)
    ljudge_name = models.CharField(max_length=100, blank=True, null=True)
    desg_code = models.SmallIntegerField()
    display = models.TextField()  # This field type is a guess.
    jocode = models.CharField(blank=True, null=True)
    state_code = models.CharField(blank=True, null=True)
    jto_dt = models.DateField(blank=True, null=True)
    jfrom_dt = models.DateField(blank=True, null=True)
    judge_priority = models.IntegerField(blank=True, null=True)
    short_judge_name = models.CharField(blank=True, null=True)
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)
    est_code_src = models.CharField()
    not_jocode = models.TextField()  # This field type is a guess.

    def __str__(self):
        return self.judge_name

    class Meta:
        managed = False
        db_table = 'judge_name_t'


class Court(models.Model):
    court_no = models.IntegerField(primary_key=True)
    room_no = models.CharField(blank=True, null=True)
    courtfiling = models.TextField()  # This field type is a guess.
    noprefix = models.SmallIntegerField(blank=True, null=True)
    principle_court = models.TextField()  # This field type is a guess.
    display = models.TextField()  # This field type is a guess.
    bench_type_code = models.IntegerField(blank=True, null=True)
    bench_desc = models.CharField(max_length=500, blank=True, null=True)
    bench_section = models.TextField(blank=True, null=True)  # This field type is a guess.
    cfrom_dt = models.DateField(blank=True, null=True)
    cto_dt = models.DateField(blank=True, null=True)
    case_types = models.CharField(max_length=1000, blank=True, null=True)
    court_id = models.CharField(blank=True, null=True)
    roaster_desc = models.TextField(blank=True, null=True)
    unique_court = models.CharField(blank=True, null=True)
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)
    est_code_src = models.CharField()

    def __str__(self):
        return self.court_no

    class Meta:
        managed = False
        db_table = 'court_t'


class Nature(models.Model):
    case_type_cd = models.SmallIntegerField(primary_key=True)  # The composite primary key (case_type_cd, nature_cd) found, that is not supported. The first column is selected.
    nature_cd = models.SmallIntegerField()
    nature_desc = models.CharField(max_length=100, blank=True, null=True)
    lnature_desc = models.CharField(max_length=100, blank=True, null=True)
    display = models.TextField()  # This field type is a guess.
    res_disp = models.SmallIntegerField()
    national_code = models.BigIntegerField()
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)
    est_code_src = models.CharField()

    def __str__(self):
        return self.nature_desc

    class Meta:
        managed = False
        db_table = 'nature_t'
        unique_together = (('case_type_cd', 'nature_cd'),)


class DocumentType(models.Model):
    docu_type = models.SmallIntegerField(primary_key=True)
    docu_name = models.CharField(max_length=100, blank=True, null=True)
    ldocu_name = models.CharField(max_length=100, blank=True, null=True)
    order_by_court = models.TextField()  # This field type is a guess.
    display = models.TextField()  # This field type is a guess.
    national_code = models.BigIntegerField()
    judgedecree = models.IntegerField()
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)
    est_code_src = models.CharField()

    def __str__(self):
        return self.docu_name

    class Meta:
        managed = False
        db_table = 'docu_type_t'


class Act(models.Model):
    actcode = models.BigIntegerField(primary_key=True)
    actname = models.CharField(max_length=250, blank=True, null=True)
    lactname = models.CharField(max_length=100, blank=True, null=True)
    acttype = models.TextField()  # This field type is a guess.
    display = models.TextField()  # This field type is a guess.
    national_code = models.CharField(blank=True, null=True)
    shortact = models.CharField(max_length=50, blank=True, null=True)
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)
    est_code_src = models.CharField()


    def __str__(self):
        return self.actname

    class Meta:
        managed = False
        db_table = 'act_t'


class Actsection(models.Model):
    act_code = models.ForeignKey(Act, blank=True, null=True, to_field="actcode", db_column="act_code", on_delete=models.DO_NOTHING)
    actsection_code = models.CharField(blank=True, null=True)
    act_section = models.CharField(max_length=250, blank=True, null=True)
    lact_section = models.CharField(max_length=250, blank=True, null=True)
    max_imp = models.SmallIntegerField()
    off_type = models.SmallIntegerField()
    display = models.TextField()  # This field type is a guess.
    national_code = models.CharField(blank=True, null=True)
    chapter = models.CharField(blank=True, null=True)
    srno = models.AutoField(primary_key=True)
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.act_section

    class Meta:
        managed = False
        db_table = 'actsection_t'


class Advocate(models.Model):
    adv_code = models.BigIntegerField(primary_key=True)
    adv_name = models.CharField(max_length=100, blank=True, null=True)
    ladv_name = models.CharField(max_length=100, blank=True, null=True)
    adv_reg = models.CharField(max_length=20, blank=True, null=True)
    display = models.TextField()  # This field type is a guess.
    address = models.TextField(blank=True, null=True)
    laddress = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    adv_sex = models.CharField(blank=True, null=True)
    adv_mobile = models.CharField(max_length=15, blank=True, null=True)
    adv_phone = models.CharField(max_length=15, blank=True, null=True)
    adv_phone1 = models.CharField(max_length=15, blank=True, null=True)
    off_add = models.TextField(blank=True, null=True)
    loff_add = models.TextField(blank=True, null=True)
    dist_code = models.SmallIntegerField()
    taluka_code = models.SmallIntegerField()
    village_code = models.IntegerField()
    village1_code = models.IntegerField()
    village2_code = models.IntegerField()
    town_code = models.IntegerField()
    ward_code = models.IntegerField()
    adv_fax = models.CharField(max_length=15, blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    debarred = models.TextField()  # This field type is a guess.
    pincode = models.IntegerField(blank=True, null=True)
    dist_code_res = models.SmallIntegerField()
    taluka_code_res = models.SmallIntegerField()
    village_code_res = models.IntegerField()
    village1_code_res = models.IntegerField()
    village2_code_res = models.IntegerField()
    town_code_res = models.IntegerField()
    ward_code_res = models.IntegerField()
    status = models.IntegerField()
    frequent = models.TextField()  # This field type is a guess.
    adv_full_name = models.CharField(max_length=100, blank=True, null=True)
    adv_seniority = models.IntegerField(blank=True, null=True)
    adv_gender = models.CharField(blank=True, null=True)
    state_id_res = models.IntegerField(blank=True, null=True)
    uid = models.BigIntegerField(blank=True, null=True)
    advocate_type = models.SmallIntegerField()
    ori_adv_code = models.BigIntegerField(blank=True, null=True)
    ori_adv_bar = models.CharField(max_length=20, blank=True, null=True)
    adv_desig_from_date = models.DateField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)
    est_code_src = models.CharField()

    def __str__(self):
        return self.adv_name

    class Meta:
        managed = False
        db_table = 'advocate_t'
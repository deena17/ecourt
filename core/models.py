from django.db import models


class CaseTypePending(models.Model):
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


class PurposePending(models.Model):
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

    class Meta:
        managed = False
        db_table = 'desg_t'


class CivilPending(models.Model):
    case_no = models.CharField(unique=True, blank=True, null=True)
    pet_name = models.CharField(max_length=100, blank=True, null=True)
    lpet_name = models.CharField(max_length=100, blank=True, null=True)
    pet_sex = models.CharField(blank=True, null=True)
    res_name = models.CharField(max_length=100, blank=True, null=True)
    lres_name = models.CharField(max_length=100, blank=True, null=True)
    res_sex = models.CharField(blank=True, null=True)
    court_no = models.IntegerField()
    date_of_filing = models.DateField(blank=True, null=True)
    time_of_filing = models.TimeField(blank=True, null=True)
    date_first_list = models.DateField(blank=True, null=True)
    date_next_list = models.DateField(blank=True, null=True)
    date_last_list = models.DateField(blank=True, null=True)
    date_of_decision = models.DateField(blank=True, null=True)
    dec_jud_name = models.CharField(max_length=100, blank=True, null=True)
    pet_adv = models.CharField(max_length=500, blank=True, null=True)
    pet_adv_cd = models.BigIntegerField()
    lpet_adv = models.CharField(max_length=100, blank=True, null=True)
    res_adv = models.CharField(max_length=500, blank=True, null=True)
    res_adv_cd = models.BigIntegerField()
    lres_adv = models.CharField(max_length=100, blank=True, null=True)
    filing_no = models.CharField(unique=True, blank=True, null=True)
    amount = models.DecimalField(max_digits=17, decimal_places=2)
    juri_value = models.CharField()
    purpose_prev = models.SmallIntegerField()
    purpose_next = models.SmallIntegerField()
    subject1 = models.CharField(max_length=255, blank=True, null=True)
    caveat = models.CharField(max_length=255, blank=True, null=True)
    unit = models.DecimalField(max_digits=17, decimal_places=2)
    goshwara_no = models.SmallIntegerField()
    status = models.CharField(blank=True, null=True)
    disp_nature = models.SmallIntegerField()
    pet_father_name = models.CharField(max_length=100, blank=True, null=True)
    lpet_father_name = models.CharField(max_length=100, blank=True, null=True)
    pet_father_flag = models.CharField(blank=True, null=True)
    pet_caste = models.CharField(blank=True, null=True)
    pet_age = models.SmallIntegerField()
    pet_email = models.CharField(max_length=254, blank=True, null=True)
    pet_mobile = models.CharField(max_length=15, blank=True, null=True)
    res_father_name = models.CharField(max_length=100, blank=True, null=True)
    lres_father_name = models.CharField(max_length=100, blank=True, null=True)
    res_father_flag = models.CharField(blank=True, null=True)
    res_caste = models.CharField(blank=True, null=True)
    res_age = models.SmallIntegerField()
    res_email = models.CharField(max_length=254, blank=True, null=True)
    res_mobile = models.CharField(max_length=15, blank=True, null=True)
    dt_regis = models.DateField(blank=True, null=True)
    display = models.TextField()  # This field type is a guess.
    date_filing_disp = models.DateField(blank=True, null=True)
    pet_legal_heir = models.TextField()  # This field type is a guess.
    res_legal_heir = models.TextField()  # This field type is a guess.
    ci_cri = models.SmallIntegerField()
    link_code = models.CharField(blank=True, null=True)
    reason_for_rej = models.TextField(blank=True, null=True)
    lreason_for_rej = models.TextField(blank=True, null=True)
    not_before_me = models.CharField(max_length=50, blank=True, null=True)
    before_me = models.CharField(max_length=50, blank=True, null=True)
    obj_flag = models.TextField()  # This field type is a guess.
    date_filing_disp_o = models.DateField(blank=True, null=True)
    date_filing_restore = models.DateField(blank=True, null=True)
    date_of_decision_o = models.DateField(blank=True, null=True)
    date_of_revoke = models.DateField(blank=True, null=True)
    urgent = models.TextField()  # This field type is a guess.
    main_case_no = models.CharField(blank=True, null=True)
    chk = models.CharField(max_length=50, blank=True, null=True)
    reg_pl = models.CharField(blank=True, null=True)
    orgid = models.SmallIntegerField(blank=True, null=True)
    resorgid = models.SmallIntegerField(blank=True, null=True)
    pet_dob = models.DateField(blank=True, null=True)
    res_dob = models.DateField(blank=True, null=True)
    plead_guilty = models.TextField()  # This field type is a guess.
    nature_cd = models.CharField(blank=True, null=True)
    legacy_flag = models.TextField()  # This field type is a guess.
    pet_extracount = models.IntegerField()
    res_extracount = models.IntegerField()
    order_sect_kar = models.TextField(blank=True, null=True)
    nature_kar = models.TextField(blank=True, null=True)
    allocation_dt = models.DateField(blank=True, null=True)
    rej_sr_no = models.IntegerField()
    unit_type = models.CharField(max_length=150, blank=True, null=True)
    unit_type_value = models.CharField(max_length=150, blank=True, null=True)
    transfer_est = models.TextField()  # This field type is a guess.
    imprisonment = models.SmallIntegerField()
    bal_fee_date = models.DateField(blank=True, null=True)
    pet_uid = models.BigIntegerField(blank=True, null=True)
    res_uid = models.BigIntegerField(blank=True, null=True)
    reasonregisdate = models.TextField(blank=True, null=True)
    oldcase_no = models.CharField(blank=True, null=True)
    performaresflag = models.TextField()  # This field type is a guess.
    reasonfilingdate = models.CharField(max_length=255, blank=True, null=True)
    oldfiling_no = models.CharField(blank=True, null=True)
    hide_pet_name = models.CharField()
    hide_res_name = models.CharField()
    hide_partyname = models.CharField()
    filcase_type = models.SmallIntegerField(blank=True, null=True)
    fil_no = models.IntegerField(blank=True, null=True)
    fil_year = models.SmallIntegerField(blank=True, null=True)
    regcase_type = models.ForeignKey(CaseTypePending, blank=True, null=True, to_field="case_type", db_column="regcase_type", on_delete=models.DO_NOTHING)
    reg_no = models.IntegerField(blank=True, null=True)
    reg_year = models.SmallIntegerField(blank=True, null=True)
    goshwara_no_o = models.SmallIntegerField()
    disp_nature_o = models.SmallIntegerField()
    archive = models.TextField()  # This field type is a guess.
    tab_status = models.CharField(blank=True, null=True)
    lsubject1 = models.CharField(max_length=255, blank=True, null=True)
    pending_ia = models.TextField()  # This field type is a guess.
    ia_next_date = models.DateField(blank=True, null=True)
    time_slot = models.IntegerField(blank=True, null=True)
    purpose_today = models.ForeignKey(PurposePending, blank=True, null=True, to_field="purpose_code", db_column="purpose_today", on_delete=models.DO_NOTHING)
    subpurpose_today = models.SmallIntegerField()
    main_matter_cino = models.CharField(blank=True, null=True)
    split_case_refno = models.CharField(blank=True, null=True)
    split_case_flag = models.TextField()  # This field type is a guess.
    jocode = models.CharField(max_length=150, blank=True, null=True)
    hashkey = models.CharField(max_length=200, blank=True, null=True)
    dormant_sinedie = models.CharField(blank=True, null=True)
    pet_inperson = models.CharField(blank=True, null=True)
    res_inperson = models.CharField(blank=True, null=True)
    pet_status = models.IntegerField()
    res_status = models.IntegerField()
    grouped = models.CharField(blank=True, null=True)
    cino = models.CharField(primary_key=True)
    subnature_cd1 = models.CharField(blank=True, null=True)
    subnature_cd2 = models.CharField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    bench_type = models.IntegerField(blank=True, null=True)
    sr_no = models.IntegerField(blank=True, null=True)
    causelist_type = models.IntegerField(blank=True, null=True)
    next_date_check = models.CharField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    link_criteria = models.CharField(blank=True, null=True)
    c_subject = models.IntegerField(blank=True, null=True)
    cs_subject = models.IntegerField(blank=True, null=True)
    css_subject = models.IntegerField(blank=True, null=True)
    judge_code = models.CharField(max_length=50, blank=True, null=True)
    desig_code = models.ForeignKey(Designation,blank=True, null=True, to_field="desgcode",db_column="desig_code", on_delete=models.DO_NOTHING)
    pet_gender = models.CharField(blank=True, null=True)
    res_gender = models.CharField(blank=True, null=True)
    pet_salutation = models.SmallIntegerField(blank=True, null=True)
    res_salutation = models.SmallIntegerField(blank=True, null=True)
    case_remark = models.TextField(blank=True, null=True)
    csss_subject = models.IntegerField(blank=True, null=True)
    tied_up = models.IntegerField()
    extra_link = models.TextField()  # This field type is a guess.
    ag_office = models.CharField(max_length=12, blank=True, null=True)
    afidvt = models.IntegerField(blank=True, null=True)
    connected_type = models.IntegerField(blank=True, null=True)
    link_cino = models.CharField(blank=True, null=True)
    bunch = models.IntegerField(blank=True, null=True)
    short_order = models.CharField(max_length=50, blank=True, null=True)
    maincase_filing_no = models.CharField(blank=True, null=True)
    last_status = models.CharField(blank=True, null=True)
    sub_cino = models.TextField(blank=True, null=True)
    vc_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    claim_juri_value = models.CharField()
    vehicle_regn_no = models.CharField(max_length=100, blank=True, null=True)
    license_no = models.CharField(max_length=100, blank=True, null=True)
    random_alloc = models.TextField(blank=True, null=True)  # This field type is a guess.
    regular_proc = models.TextField(blank=True, null=True)  # This field type is a guess.
    datacorrection = models.TextField(blank=True, null=True)  # This field type is a guess.
    auto_date = models.DateField(blank=True, null=True)
    auto_date_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    transfer_remark = models.TextField(blank=True, null=True)
    eflag = models.CharField(blank=True, null=True)
    efilno = models.CharField(unique=True, max_length=99, blank=True, null=True)
    under_obj = models.TextField(blank=True, null=True)  # This field type is a guess.
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)
    caveat_tag_date = models.DateField(blank=True, null=True)
    pet_prid = models.CharField(max_length=25, blank=True, null=True)
    res_prid = models.CharField(max_length=25, blank=True, null=True)
    send_to_vcourt = models.DateField(blank=True, null=True)
    receipt_from_vcourt = models.DateField(blank=True, null=True)
    vcourt_cnr = models.CharField(max_length=16)
    vcourt_sent_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    vcourt_receive_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    efiling_type = models.CharField(blank=True, null=True)
    notify_court_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'civil_t'


class DailyProceeding(models.Model):
    case_no = models.ForeignKey(CivilPending, blank=True, null=True, to_field="case_no", db_column="case_no", on_delete=models.DO_NOTHING)
    next_date = models.DateField()
    time_slot = models.CharField(max_length=10, blank=True, null=True)
    estimate_time = models.CharField(max_length=10, blank=True, null=True)
    purpose_code = models.ForeignKey(PurposePending, to_field="purpose_code", db_column="purpose_code", on_delete=models.DO_NOTHING)
    subpurpose_id = models.BigIntegerField()
    order_code = models.SmallIntegerField()
    order_remark = models.TextField(blank=True, null=True)
    todays_date = models.DateField(blank=True, null=True)
    status = models.CharField(blank=True, null=True)
    court_no = models.IntegerField()
    present = models.TextField(blank=True, null=True)
    exhibit = models.TextField(blank=True, null=True)
    depositby = models.CharField(max_length=99, blank=True, null=True)
    deposit = models.DecimalField(max_digits=17, decimal_places=2)
    deposit_rem = models.CharField(max_length=255, blank=True, null=True)
    deposit_a = models.CharField(max_length=255, blank=True, null=True)
    paymentby = models.CharField(max_length=99, blank=True, null=True)
    payment = models.DecimalField(max_digits=17, decimal_places=2)
    payment_rem = models.CharField(max_length=255, blank=True, null=True)
    payment_a = models.CharField(max_length=255, blank=True, null=True)
    hearing_start_time = models.CharField(max_length=20, blank=True, null=True)
    hearing_end_time = models.CharField(max_length=20, blank=True, null=True)
    adjcode = models.SmallIntegerField()
    lorder_remark = models.TextField(blank=True, null=True)
    lexhibit = models.TextField(blank=True, null=True)
    no_exibits_marked = models.IntegerField()
    no_mos_marked = models.IntegerField()
    no_witnesses_ex = models.IntegerField()
    judge_code = models.CharField(max_length=50, blank=True, null=True)
    desig_code = models.ForeignKey(Designation,blank=True, null=True, to_field="desgcode",db_column="desig_code", on_delete=models.DO_NOTHING)
    incharge = models.CharField(blank=True, null=True)
    lpresent = models.TextField(blank=True, null=True)
    recall = models.CharField(blank=True, null=True)
    jocode = models.CharField(max_length=150, blank=True, null=True)
    hashkey = models.CharField(max_length=200, blank=True, null=True)
    dormant_sinedie = models.CharField(blank=True, null=True)
    cino = models.CharField(primary_key=True)  # The composite primary key (cino, srno) found, that is not supported. The first column is selected.
    cause_list_type = models.IntegerField(blank=True, null=True)
    sr_no = models.IntegerField(blank=True, null=True)
    causelist_type = models.IntegerField(blank=True, null=True)
    next_date_check = models.CharField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    case_remark = models.TextField(blank=True, null=True)
    otherpresent = models.TextField(blank=True, null=True)
    takenonboard = models.CharField(blank=True, null=True)
    old_next_date = models.DateField(blank=True, null=True)
    old_purpose_code = models.SmallIntegerField(blank=True, null=True)
    oldbenchid = models.IntegerField(blank=True, null=True)
    srno = models.IntegerField()
    vc_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    auto_date = models.DateField(blank=True, null=True)
    auto_date_flag = models.TextField(blank=True, null=True)  # This field type is a guess.
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)
    issue_charge = models.CharField(blank=True, null=True)
    witness_examined = models.CharField(blank=True, null=True)
    no_of_pages = models.IntegerField(blank=True, null=True)
    crpc = models.CharField(blank=True, null=True)
    written_examined = models.CharField(blank=True, null=True)
    appearance_examined = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_proc'
        unique_together = (('cino', 'srno'),)
        

class HearingStatus(models.Model):
    case_no = models.CharField(blank=True, null=True)
    hearing_date = models.DateField(blank=True, null=True)
    hearing_start = models.CharField(blank=True, null=True)
    hearing_end = models.CharField(blank=True, null=True)
    called_start = models.CharField(blank=True, null=True)
    court_no = models.IntegerField()
    cino = models.ForeignKey(CivilPending, blank=True, null=True, on_delete=models.DO_NOTHING)
    srno = models.AutoField(primary_key=True)
    cause_list_type = models.IntegerField()
    cause_list_sr_no = models.IntegerField()
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)
    ia_no = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hearing_status_t'


class NaturePending(models.Model):
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

    class Meta:
        managed = False
        db_table = 'docu_type_t'



class IndexRegister(models.Model):
    caseno = models.CharField(blank=True, null=True)
    srno = models.BigIntegerField(primary_key=True)  # The composite primary key (srno, cino) found, that is not supported. The first column is selected.
    description = models.ForeignKey(DocumentType, blank=True, null=True, to_field="docu_type", db_column="description",on_delete=models.DO_NOTHING)
    paperdate = models.DateField(blank=True, null=True)
    noofparts = models.CharField(blank=True, null=True)
    alphabetical = models.CharField(max_length=150, blank=True, null=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)
    lalphabetical = models.CharField(max_length=150, blank=True, null=True)
    lremarks = models.CharField(max_length=100, blank=True, null=True)
    display = models.TextField()  # This field type is a guess.
    upload_date = models.DateTimeField(blank=True, null=True)
    cino = models.CharField()
    doc_year = models.IntegerField(blank=True, null=True)
    doc_no = models.IntegerField(blank=True, null=True)
    filing_no = models.CharField(max_length=16, blank=True, null=True)
    amount = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    party_no = models.IntegerField(blank=True, null=True)
    adv_name = models.CharField(max_length=100, blank=True, null=True)
    adv_cd = models.IntegerField(blank=True, null=True)
    extra_party = models.CharField(max_length=250, blank=True, null=True)
    objection = models.TextField(blank=True, null=True)  # This field type is a guess.
    oldnumber = models.CharField(blank=True, null=True)
    remarks1 = models.CharField(max_length=100, blank=True, null=True)
    advname1 = models.CharField(max_length=100, blank=True, null=True)
    advcd1 = models.IntegerField(blank=True, null=True)
    amd = models.CharField(blank=True, null=True)
    create_modify = models.DateTimeField(blank=True, null=True)
    pleading_no = models.CharField(max_length=99, blank=True, null=True)
    case_ia = models.CharField(blank=True, null=True)
    new_cino = models.CharField(blank=True, null=True)
    ia_no = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_register'
        unique_together = (('srno', 'cino'),)
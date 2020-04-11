# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CustomerCompany(models.Model):
    customer_company_id = models.AutoField(db_column='CUSTOMER_COMPANY_ID', primary_key=True)  # Field name made lowercase.
    customer_company_name = models.CharField(db_column='CUSTOMER_COMPANY_NAME', max_length=45)  # Field name made lowercase.
    customer_company_street1 = models.CharField(db_column='CUSTOMER_COMPANY_STREET1', max_length=45)  # Field name made lowercase.
    customer_company_street2 = models.CharField(db_column='CUSTOMER_COMPANY_STREET2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    customer_company_city = models.CharField(db_column='CUSTOMER_COMPANY_CITY', max_length=45)  # Field name made lowercase.
    customer_company_state = models.CharField(db_column='CUSTOMER_COMPANY_STATE', max_length=2)  # Field name made lowercase.
    customer_company_zip = models.IntegerField(db_column='CUSTOMER_COMPANY_ZIP')  # Field name made lowercase.
    employee = models.ForeignKey('Employee', models.DO_NOTHING, db_column='EMPLOYEE_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer_company'


class CustomerContact(models.Model):
    customer_contact_id = models.AutoField(db_column='CUSTOMER_CONTACT_ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='CUSTOMER_ID')  # Field name made lowercase.
    customer_contact_fname = models.CharField(db_column='CUSTOMER_CONTACT_FNAME', max_length=45)  # Field name made lowercase.
    customer_contact_lname = models.CharField(db_column='CUSTOMER_CONTACT_LNAME', max_length=45)  # Field name made lowercase.
    customer_contact_email = models.CharField(db_column='CUSTOMER_CONTACT_EMAIL', max_length=45)  # Field name made lowercase.
    customer_contact_tel = models.CharField(db_column='CUSTOMER_CONTACT_TEL', max_length=10)  # Field name made lowercase.
    customer_contact_role = models.CharField(db_column='CUSTOMER_CONTACT_ROLE', max_length=45)  # Field name made lowercase.
    customer_contact_current = models.IntegerField(db_column='CUSTOMER_CONTACT_CURRENT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer_contact'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    employee_id = models.AutoField(db_column='EMPLOYEE_ID', primary_key=True)  # Field name made lowercase.
    employee_name_first = models.CharField(db_column='EMPLOYEE_NAME_FIRST', max_length=45)  # Field name made lowercase.
    employee_name_middle = models.CharField(db_column='EMPLOYEE_NAME_MIDDLE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    employee_name_last = models.CharField(db_column='EMPLOYEE_NAME_LAST', max_length=45)  # Field name made lowercase.
    employee_title = models.CharField(db_column='EMPLOYEE_TITLE', max_length=45)  # Field name made lowercase.
    employee_dob = models.DateField(db_column='EMPLOYEE_DOB')  # Field name made lowercase.
    employee_hire_date = models.DateField(db_column='EMPLOYEE_HIRE_DATE')  # Field name made lowercase.
    employee_email_work = models.CharField(db_column='EMPLOYEE_EMAIL_WORK', max_length=45)  # Field name made lowercase.
    employee_email_alt = models.CharField(db_column='EMPLOYEE_EMAIL_ALT', max_length=45, blank=True, null=True)  # Field name made lowercase.
    employee_tel_work = models.CharField(db_column='EMPLOYEE_TEL_WORK', max_length=10)  # Field name made lowercase.
    employee_tel_alt = models.CharField(db_column='EMPLOYEE_TEL_ALT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    employee_manager = models.ForeignKey('self', models.DO_NOTHING, db_column='EMPLOYEE_MANAGER_ID', blank=True, null=True)  # Field name made lowercase.
    employee_pay_rate = models.FloatField(db_column='EMPLOYEE_PAY_RATE')  # Field name made lowercase.
    employee_end_date = models.DateField(db_column='EMPLOYEE_END_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeHours(models.Model):
    employee_hours_id = models.AutoField(db_column='EMPLOYEE_HOURS_ID', primary_key=True)  # Field name made lowercase.
    employee_id = models.IntegerField(db_column='EMPLOYEE_ID')  # Field name made lowercase.
    project_id = models.IntegerField(db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase.
    employee_hours_first_day = models.DateField(db_column='EMPLOYEE_HOURS_FIRST_DAY')  # Field name made lowercase.
    employee_hours_rate = models.FloatField(db_column='EMPLOYEE_HOURS_RATE')  # Field name made lowercase.
    employee_hours_sun1 = models.IntegerField(db_column='EMPLOYEE_HOURS_SUN1')  # Field name made lowercase.
    employee_hours_mon1 = models.IntegerField(db_column='EMPLOYEE_HOURS_MON1')  # Field name made lowercase.
    employee_hours_tue1 = models.IntegerField(db_column='EMPLOYEE_HOURS_TUE1')  # Field name made lowercase.
    employee_hours_wed1 = models.IntegerField(db_column='EMPLOYEE_HOURS_WED1')  # Field name made lowercase.
    employee_hours_thr1 = models.IntegerField(db_column='EMPLOYEE_HOURS_THR1')  # Field name made lowercase.
    employee_hours_fri1 = models.IntegerField(db_column='EMPLOYEE_HOURS_FRI1')  # Field name made lowercase.
    employee_hours_sat1 = models.IntegerField(db_column='EMPLOYEE_HOURS_SAT1')  # Field name made lowercase.
    employee_hours_sun2 = models.IntegerField(db_column='EMPLOYEE_HOURS_SUN2')  # Field name made lowercase.
    employee_hours_mon2 = models.IntegerField(db_column='EMPLOYEE_HOURS_MON2')  # Field name made lowercase.
    employee_hours_tue2 = models.IntegerField(db_column='EMPLOYEE_HOURS_TUE2')  # Field name made lowercase.
    employee_hours_wed2 = models.IntegerField(db_column='EMPLOYEE_HOURS_WED2')  # Field name made lowercase.
    employee_hours_thr2 = models.IntegerField(db_column='EMPLOYEE_HOURS_THR2')  # Field name made lowercase.
    employee_hours_fri2 = models.IntegerField(db_column='EMPLOYEE_HOURS_FRI2')  # Field name made lowercase.
    employee_hours_sat2 = models.IntegerField(db_column='EMPLOYEE_HOURS_SAT2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee_hours'


class EmployeePermission(models.Model):
    employee_permission_id = models.IntegerField(db_column='EMPLOYEE_PERMISSION_ID', primary_key=True)  # Field name made lowercase.
    employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='EMPLOYEE_ID')  # Field name made lowercase.
    permission_level = models.ForeignKey('Permission', models.DO_NOTHING, db_column='PERMISSION_LEVEL')  # Field name made lowercase.
    project = models.ForeignKey('Project', models.DO_NOTHING, db_column='PROJECT_ID', blank=True, null=True)  # Field name made lowercase.
    employee_permission_start = models.DateField(db_column='EMPLOYEE_PERMISSION_START')  # Field name made lowercase.
    employee_permission_end = models.DateField(db_column='EMPLOYEE_PERMISSION_END', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employee_permission'


class Inventory(models.Model):
    inventory_id = models.AutoField(db_column='INVENTORY_ID', primary_key=True)  # Field name made lowercase.
    inventory_name = models.CharField(db_column='INVENTORY_NAME', max_length=45)  # Field name made lowercase.
    inventory_description = models.CharField(db_column='INVENTORY_DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory'


class InventorySupplier(models.Model):
    inventory_supplier_inventory = models.OneToOneField('Inventory', models.DO_NOTHING, db_column='INVENTORY_SUPPLIER_INVENTORY_ID', primary_key=True)  # Field name made lowercase.
    supplier = models.ForeignKey('SupplierCompany', models.DO_NOTHING, db_column='SUPPLIER_ID')  # Field name made lowercase.
    inventory_supplier_cost = models.DecimalField(db_column='INVENTORY_SUPPLIER_COST', max_digits=10, decimal_places=2)  # Field name made lowercase.
    inventory_supplier_amount = models.IntegerField(db_column='INVENTORY_SUPPLIER_AMOUNT')  # Field name made lowercase.
    inventory_supplier_notes = models.CharField(db_column='INVENTORY_SUPPLIER_NOTES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inventory_supplier_preferred = models.IntegerField(db_column='INVENTORY_SUPPLIER_PREFERRED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory_supplier'
        unique_together = (('inventory_supplier_inventory', 'supplier'),)


class Permission(models.Model):
    permission_level = models.AutoField(db_column='PERMISSION_LEVEL', primary_key=True)  # Field name made lowercase.
    permission_name = models.CharField(db_column='PERMISSION_NAME', max_length=30)  # Field name made lowercase.
    permission_description = models.CharField(db_column='PERMISSION_DESCRIPTION', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permission'


class Project(models.Model):
    project_id = models.AutoField(db_column='PROJECT_ID', primary_key=True)  # Field name made lowercase.
    project_status = models.CharField(db_column='PROJECT_STATUS', max_length=11)  # Field name made lowercase.
    project_name = models.CharField(db_column='PROJECT_NAME', max_length=45)  # Field name made lowercase.
    project_budget = models.DecimalField(db_column='PROJECT_BUDGET', max_digits=10, decimal_places=2)  # Field name made lowercase.
    customer_company = models.ForeignKey(CustomerCompany, models.DO_NOTHING, db_column='CUSTOMER_COMPANY_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project'


class ProjectInventory(models.Model):
    inventory = models.OneToOneField(Inventory, models.DO_NOTHING, db_column='INVENTORY_ID', primary_key=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='QUANTITY')  # Field name made lowercase.
    project_id = models.IntegerField(db_column='PROJECT_ID', unique=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_inventory'
        unique_together = (('inventory', 'project_id'),)


class Purchase(models.Model):
    purchase_id = models.AutoField(db_column='PURCHASE_ID', primary_key=True)  # Field name made lowercase.
    project_id = models.IntegerField(db_column='PROJECT_ID')  # Field name made lowercase.
    inventory_id = models.IntegerField(db_column='INVENTORY_ID')  # Field name made lowercase.
    purchase_quantity = models.IntegerField(db_column='PURCHASE_QUANTITY')  # Field name made lowercase.
    purchase_total = models.DecimalField(db_column='PURCHASE_TOTAL', max_digits=10, decimal_places=2)  # Field name made lowercase.
    purchase_date = models.DateField(db_column='PURCHASE_DATE')  # Field name made lowercase.
    employee_id = models.IntegerField(db_column='EMPLOYEE_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'purchase'


class SupplierCompany(models.Model):
    supplier_company_id = models.AutoField(db_column='SUPPLIER_COMPANY_ID', primary_key=True)  # Field name made lowercase.
    supplier_company_name = models.CharField(db_column='SUPPLIER_COMPANY_NAME', max_length=45)  # Field name made lowercase.
    supplier_company_street1 = models.CharField(db_column='SUPPLIER_COMPANY_STREET1', max_length=45)  # Field name made lowercase.
    supplier_company_street2 = models.CharField(db_column='SUPPLIER_COMPANY_STREET2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    supplier_company_city = models.CharField(db_column='SUPPLIER_COMPANY_CITY', max_length=45)  # Field name made lowercase.
    supplier_company_state = models.CharField(db_column='SUPPLIER_COMPANY_STATE', max_length=2)  # Field name made lowercase.
    supplier_company_zip = models.IntegerField(db_column='SUPPLIER_COMPANY_ZIP')  # Field name made lowercase.
    supplier_company_notes = models.CharField(db_column='SUPPLIER_COMPANY_NOTES', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplier_company'


class SupplierContact(models.Model):
    supplier_contact_id = models.IntegerField(db_column='SUPPLIER_CONTACT_ID', primary_key=True)  # Field name made lowercase.
    supplier_id = models.IntegerField(db_column='SUPPLIER_ID')  # Field name made lowercase.
    supplier_contact_fname = models.CharField(db_column='SUPPLIER_CONTACT_FNAME', max_length=45)  # Field name made lowercase.
    supplier_contact_lname = models.CharField(db_column='SUPPLIER_CONTACT_LNAME', max_length=45)  # Field name made lowercase.
    supplier_contact_email = models.CharField(db_column='SUPPLIER_CONTACT_EMAIL', max_length=45)  # Field name made lowercase.
    supplier_contact_tel = models.CharField(db_column='SUPPLIER_CONTACT_TEL', max_length=10)  # Field name made lowercase.
    supplier_contact_role = models.CharField(db_column='SUPPLIER_CONTACT_ROLE', max_length=45)  # Field name made lowercase.
    supplier_contact_current = models.IntegerField(db_column='SUPPLIER_CONTACT_CURRENT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplier_contact'

# EZLife_Web_Project
# - Automation_Infrastructure-2.0.69-py2.py3-none-any.whl
# - Automation-Infrastructure @ http://asil-sv-au1/Repository/Automation_Infrastructure-2.0.69-py2.py3-none-any.whl
# - python-ldap @ http://asil-sv-au1/Repository/python_ldap-3.3.1-cp38-cp38-win_amd64.whl



------------------------------------------------------------------------------------------------------------------------

General:
========

Create requirements.txt:
----------------------------
- pip freeze > requirements.txt


Install requirements.txt:
----------------------------
- pip install -r requirements.txt


Uninstall requirements.txt:
----------------------------
- pip uninstall -r requirements.txt -y


Upgrade pip:
------------
- pip install pip --upgrade


Create wheel:
-------------
install .whl:
- pip install wheel

create .whl: 
- python setup.py sdist bdist_wheel (the file will be under dist - 2 file)

load .whl: 
- pip install http:path_to_file_name/wheel_file_name.whl
- pip install http://asil-sv-au1/Repository/Automation_Infrastructure-2.0.59-py2.py3-none-any.whl

remove .whl:
- pip uninstall Automation_Infrastructure


General wheel install/uninstall:
---------------------------
jira (version 3.0.0):
- pip install git+git://github.com/pycontribs/jira.git@7fa3a454c08a14e2d7d7670fcfa87482e16936ba

Automation_Infrastructure:
- pip install http://asil-sv-au1/Repository/Automation_Infrastructure-2.0.59-py2.py3-none-any.whl
- pip uninstall Automation_Infrastructure

RobotFrameworkSVGInfra:
- pip install http://asil-sv-au1/Repository/RobotFrameworkSVGInfra-1.1.1-py3-none-any.whl
- pip uninstall RobotFrameworkSVGInfra

SwEngineTime:
- pip install http://asil-sv-au1/Repository/SwEngineTime-1.0.2-py3-none-any.whl
- pip uninstall SwEngineTime



------------------------------------------------------------------------------------------------------------------------

Django:
=======

Run Server:
-----------
from console:
- python manage.py runserver

from pycharm (edit configuration):
- runserver ip_address:port
- runserver host_name:port
- runserver asil-azaguri:8000


Create super user:
------------------
- python manage.py createsuperuser --email spuser@example.com --username spuser


Create makemigrations:
----------------------
- python manage.py makemigrations
- python manage.py migrate

makemigrations for all apps (must on postgresql):
- 
python manage.py makemigrations ACPApp AmarisoftUEApp ChipsetApp CUCPApp CustomerNameApp CUUPApp DeviceTypeApp DUApp GnodeBApp HardwareElementApp HardwareTypeApp ImageTypeApp InfoLinksApp InfoCategoriesApp IperfApp KMasterApp NucApp RackSwitchApp RUApp ScenarioApp SerialTerminalApp SetupApp SiteApp SnmpAPP SourceTargetApp SRVersionApp SwitchVendorTypeApp TestApp TreeApp TreeMinimalApp UeApp UeStaticDynamicApp UeVendorNameApp


Create project:
---------------
- django-admin startproject my_project_name


Create application:
-------------------
- django-admin startapp my_app_name


Schema:
-------
Schema configurations:
- INSTALLED_APPS = (
    ...
    'django_extensions',
    ...
)

Create Schema:
- python manage.py graph_models -a -o myapp_models.png
- python manage.py graph_models -a -o EZLife-NG_Schema.png


How to install LDAP:
--------------------
- install openldap-2.4.54 (have on \\asil-sv-au1\c$\inetpub\wwwroot\Repository\openldap-2.4.54)
- pip install django-auth-ldap
- pip install http://asil-sv-au1/Repository/python_ldap-3.3.1-cp38-cp38-win_amd64.whl



------------------------------------------------------------------------------------------------------------------------

LDAP:
=====

LDAP from terminal:
-----------------

ldapobj = ldap.initialize("ldap://IPAddress:PORT")
ldapobj.simple_bind_s(user, password)

ldapobj.search_s("OU=Israel,OU=UsersAirspan,DC=airspan,DC=com", ldap.SCOPE_SUBTREE, "(objectClass=user)")



------------------------------------------------------------------------------------------------------------------------

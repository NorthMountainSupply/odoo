# North Mountain Supply

A branch of Odoo Community Edition that has been altered to fit North Mountain Supply's needs. Based on Odoo version 18.

## Getting Started

For standard installation please follow the <a href="https://www.odoo.com/documentation/master/administration/install/install.html">Setup instructions</a>
from the documentation. However, a simplified overview for use on Windows machines will be provided below.

### Requirements

1. `Python 3.12.8` - This is the version of Python I have used for development. Versions `3.13.0` and above did not work for me. Additionally, the Odoo documentation says that it requires a minimum version of `3.10.0`. You can download `Python 3.12.8` <a href="https://www.python.org/downloads/release/python-3128/">here</a>.
2. `pip3` - This is a package manager for Python, which is required for installing some dependencies. It should have been installed alongside the Python version downloaded in the previous step.
3. `PostgreSQL` - Odoo will create and store its data within a PostgreSQL database hosted locally on your machine. Download `PostgresSQL` <a href="https://www.postgresql.org/download/windows/">here</a>. I used version 17, but Odoo says that 12 or above will work fine.
4. `Build Tools for Visual Studio` - Even if you're not using Visual Studio as your IDE, you still need to perform this step. Follow <a href="https://visualstudio.microsoft.com/downloads/">this link</a> to visit the Visual Studio downloads page. Scroll down the page, and navigate to `All Downloads > Tools for Visual Studio > Build Tools for Visual Studio 2022`, and click `download`. When running the executable, download C++ build tools (idk that's what the guide said). I just basically downloaded anything I thought I would need to compile C++ projects, I think some of the packages require it or something.

### Setting Up the Environment

1. Clone this GitHub repo into any directory on your device.
2. Create an account on PostgreSQL that the Odoo instance can use.
    1. Search for `pgAdmin` in the Windows search bar and run the app.
    2. Double-click the server to create a connection.
    3. Select `Object > Create > Login/Group Role`.
    4. Enter any username in the **Role Name** field (I just put 'odoo').
    5. Open the Definition tab, enter any **password** (I just put 'odoo'), and click Save.
    6. Open the Privileges tab and switch **Can login?** to **Yes** and **Create database?** to **Yes**.
3. Install Python package dependencies for Odoo.
    1. Open a terminal in the root of the repo.
    2. Run `pip install setuptools wheel` and wait for it to install.
    3. Run `pip install -r requirements.txt` to install all the packages that Odoo requires.

### Starting the Odoo Server

1. Open a terminal in the root of the repo.
2. Run the command `python odoo-bin -c run.config` to use the info in the config file.
**Alternatively,** run the command `python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb`, replacing the following with your info:
    - `dbuser` is the username you created for Odoo in *Step 2.4* of *Setting Up the Environment*. In my case, it's "odoo".
    - `dbpassword` is the password you created for Odoo in *Step 2.5* of *Setting Up the Environment*. In my case, it's "odoo".
    - `mydb` is the name of the PostgreSQL database you'd like to connect to. I would set this to `nms`, or `nms-test`. If you attempt to connect to a database that does not yet exist, Odoo will initialize it for you.
3. Once Odoo is up and running, use a browser to connect to `http://localhost:8069` (this is the default port).
4. You will see a login page. When creating a database for the first time, there are **two** users registered by default. The only one that matters is the admin account. For `email`, put "admin". For the `password`, put "admin". Once you successfully enter the database, you can invite other users to the database by sending them an invite in the settings, or change the admin password.

This should be enough to get an instance of Odoo up and running.

## Installing the Custom Modules

**All** custom additions / modifications to Odoo will be added in the `custom_addons` directory. This will make it easy to update to new versions of Odoo, and this was the workflow that Odoo themselves recommended.

Within the `custom_addons` directory, each top-level folder is its own **module**. **Modules** can either be **apps**, or... **not apps**.

To install custom apps, follow these steps:
1. Open an instance of Odoo. 
2. Navigate to the Apps page via the menu in the top-left. 
3. Click on ```Update Apps List``` in the page header. This forces Odoo to scan the ```addons``` and ```custom_addons``` directories for any changes.
4. Now, in the search bar, remove the ```apps``` filter. This should increase the total number of results from 60 or so to 600+.
5. Search for the name of the module you'd like to install.
6. If this module has not been installed before, click "Activate".
7. If this module has already been installed, click on the three dots and select "Upgrade". Whenever you make changes to an app, you need to manually update the app in Odoo by doing this.
8. After a brief amount of time, you should be redirected to the ```Discuss``` page. The changes from the newly installed module should now be in effect.

## Custom Module Structure
This section will be updated as I learn more about Odoo Development. From what I've learned so far,
1. Each **module** has a ```__manifest__.py``` file that stores the **module**'s metadata. This includes the module's name, author, version number, and dependencies.
    - The ```depends``` key is pretty important. It's an array of other **modules** that the current **module** depends on. 
2. ```__init__.py``` is another required file, but I'm not exactly sure what it does at this point in time. It probably gets ran once when initially starting an Odoo server, if I had to guess?
3. The ```models``` directory is *optional*. If your **module** adds fields to existing models, or new models entirely, then those python files should go here.
4. The ```views``` directory is *optional*. If your **module** modifies existing views, or adds new views entirely, those xml files should go here. You also need to add any xml files to the ```data``` key in ```__manifest__.py```.

Now that we have one module already made, we should just copy it as a starting point for making future modules.



----
[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/master)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/app/website">Website Builder</a>,
<a href="https://www.odoo.com/app/ecommerce">eCommerce</a>,
<a href="https://www.odoo.com/app/inventory">Warehouse Management</a>,
<a href="https://www.odoo.com/app/project">Project Management</a>,
<a href="https://www.odoo.com/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.odoo.com/app/employees">Human Resources</a>,
<a href="https://www.odoo.com/app/social-marketing">Marketing</a>,
<a href="https://www.odoo.com/app/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/">...</a>

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.

Getting started with Odoo
-------------------------

For a standard installation please follow the <a href="https://www.odoo.com/documentation/master/administration/install/install.html">Setup instructions</a>
from the documentation.

To learn the software, we recommend the <a href="https://www.odoo.com/slides">Odoo eLearning</a>, or <a href="https://www.odoo.com/page/scale-up-business-game">Scale-up</a>, the <a href="https://www.odoo.com/page/scale-up-business-game">business game</a>. Developers can start with <a href="https://www.odoo.com/documentation/master/developer/howtos.html">the developer tutorials</a>

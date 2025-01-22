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

## Odoo Server / Database Structure

From what I've gathered, an implementation of Odoo has two main components: the Odoo source code, and a PostgreSQL database.

### Odoo Source Code

The Odoo source code is what is contained within this repository. It has **server** code that provides HTML files and views to the client. Odoo is basically an interface to interact with a locally hosted PostgreSQL database. **No database data (rows) are stored within this repo. However, table / model definitions and fields ARE defined here.**

### PostgreSQL Database

This is a database hosted locally on your machine. You need to create an account that Odoo can to use to make changes to the database (see *Step 2* of *Setting Up the Environment*). Odoo will use the table definitions in its source code to modifiy the database structure, and the actual data will be kept within a directory on your local device (default is `C:\Program Files\PostgreSQL\*Version#*\data` I think). That data **will NOT be tracked within this repo**.

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

===============================================
Odoo 9 Buildout config using anybox.recipe.odoo
===============================================

This is an example using Odoo 9 and `anybox.recipe.odoo <
http://docs.anybox.fr/anybox.recipe.odoo/current/>`_ to run unitest with
`nose <https://nose.readthedocs.org/en/latest/>`_.

warning::

    This should not be use in production.


Here 2 independent quickstart to launch your unit tests:
    - using anybox.recipe.odoo
    - running it within a docker container


Quick start using buildout on debian laptop assuming you already get
`dependencies <http://docs.anybox.fr/anybox.recipe.odoo/current/
first_steps.html#installing-build-dependencies>`_::

    # Cloning this repo
    git clone git@github.com:petrus-v/odoo9-sample.git
    cd odoo9-sample
    # bootstrap buildout
    ~/path-to-venv-py2.7/bin/python bootstrap.py -c buildout.cfg
    # running buildout to get all requirments needs by your odoo instance
    bin/buildout -c buildout.cfg
    # creating a test db with demo data and installing the module that we
    # want to test
    createdb mydbtest
    bin/start_odoo -d mydbtest -i sample --stop-after-init
    # running tests
    bin/nosetests -d mydbtest -- -s -v personal-addons/sample/


Also available a using a quick and dirty Dockerfile::

    # Cloning this repo
    git clone git@github.com:petrus-v/odoo9-sample.git
    cd odoo9-sample
    # build the image
    docker build -t odoo9test .
    # Run test on you module
    docker run -it --rm odoo9test
    # Create a new database mydbtest on your cluster owned by ``openerp``
    psql -p 5437 -h localhost -U postgres -d postgres
    postgres=# create database mydbtest owner openerp
    # install sample module
    docker run --rm -it testodoo9 bin/start_odoo -i sample --stop-after-init
    # run unit test on this module with nose
    docker run --rm -it testodoo9 bin/nosetests -d mydbtest -- -s -v personal-addons/sample

.. note::

    To configure DATABASE access edit ``buildout.docker.cfg`` file before
    building the image!!! I know it's not a fashion way! remember this is a
    POC!

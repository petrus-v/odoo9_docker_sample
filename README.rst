==========================================================
Odoo 9 Buildout config using anybox.recipe.odoo and Docker
==========================================================

This is an example to run odoo9 module unit-test using `anybox.recipe.odoo
<http://docs.anybox.fr/anybox.recipe.odoo/current/>`_ (a `buildout 
<http://www.buildout.org/en/latest/>`_ recipe),
`nose <https://nose.readthedocs.org/en/latest/>`_ and `docker <https://www.docker.com/>`_.

.. warning::

    This should not be use in production.


Here 2 independent HowTo to launch your unit tests:
    - the first purpose it to use it without docker
    - then running it within a docker container


Quick start using buildout on debian laptop assuming you already get
`dependencies <http://docs.anybox.fr/anybox.recipe.odoo/current/
first_steps.html#installing-build-dependencies>`_::

    # Cloning this repo
    git clone git@github.com:petrus-v/odoo9_docker_sample.git
    cd odoo9_docker_sample
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


Also available using a quick and dirty Dockerfile::

    # Cloning this repo
    git clone git@github.com:petrus-v/odoo9_docker_sample.git
    cd odoo9_docker_sample
    # build the image
    docker build -t odoo9test .
    # Create a new database mydbtest on your cluster owned by ``openerp``
    psql -p 5437 -h localhost -U postgres -d postgres
    postgres=# create database mydbtest owner openerp;
    # install sample module
    docker run --rm -it testodoo9 bin/start_odoo -i sample --stop-after-init
    # run sample module unit-test with nose
    docker run --rm -it testodoo9 bin/nosetests -d mydbtest -- -s -v personal-addons/sample

.. note::

    To configure DATABASE access edit ``buildout.docker.cfg`` file before
    building the image!!! or mount the ``etc/`` directory with the odoo.cfg
    file


If you want to go in deep using docker and anybox.recipe.odoo you should take in consideration
`voodoo <https://github.com/akretion/voodoo>`_ project, it's a tool from akretion which combine
docker compose and buildout (which I've personally never used!)

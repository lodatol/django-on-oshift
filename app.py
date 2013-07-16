#!/usr/bin/env python
import imp
import os
import sys

try:
    zvirtenv = os.path.join(os.environ['OPENSHIFT_PYTHON_DIR'],
                            'virtenv', 'bin', 'activate_this.py')
    exec(compile(open(zvirtenv).read(), zvirtenv, 'exec'),
         dict(__file__ = zvirtenv) )
except:
    pass


from twisted.internet import reactor
from twisted.python import threadpool
from twisted.application import internet, service
from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site

from django.core.handlers.wsgi import WSGIHandler


os.environ['DJANGO_SETTINGS_MODULE'] = 'apps.settings'

def createDjangoEndPoint():
    pool = threadpool.ThreadPool(maxthreads=2000)
    pool.start()
    reactor.addSystemEventTrigger('after', 'shutdown', pool.stop)
    return WSGIResource(reactor, pool, WSGIHandler())

def run_twisted_server(ip, port):
    site = Site(createDjangoEndPoint())
    from twisted.python import log as log_twisted
    log_twisted.startLogging(sys.stdout)
    reactor.listenTCP(port, site, interface=ip)
    reactor.run()


if __name__ == '__main__':
    ip = os.environ.get('OPENSHIFT_PYTHON_IP', '')
    port = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 8080))

    print('Starting WSGIServer on %s:%d ... ' % (ip, port))
    try:
        run_twisted_server(ip, port)
    except:
        print("problem while starting twisted server ...")

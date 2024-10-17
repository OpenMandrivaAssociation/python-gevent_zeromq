%define	module	gevent_zeromq

Summary:	Gevent compatibility layer for pyzmq

Name:		python-%{module}
Version:	0.2.5
Release:	3
Source0:	http://pypi.python.org/packages/source/g/gevent_zeromq/gevent_zeromq-%{version}.tar.gz
Source100: %{name}.rpmlintrc
License:	BSD
Group:		Development/Python
Url:		https://github.com/traviscline/gevent-zeromq/
Requires:	python-gevent, python-pyzmq >= 2.2.0
BuildRequires:	python-devel, python-cython, python-gevent, python-pyzmq >= 2.2.0

%description
Wrapper of pyzmq to make it compatible with gevent. ZeroMQ socket operations
that would normally block the current thread will only block the current
greenlet.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean

%files
%doc examples/
%{py_platsitedir}/%{module}*



%define	module	gevent_zeromq
%define name	python-%{module}
%define version 0.2.2
%define release %mkrel 1

Summary:	gevent compatibility layer for pyzmq
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/g/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://github.com/traviscline/gevent-zeromq/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python-gevent, python-pyzmq >= 2.1.0
BuildRequires:	python-devel, python-cython

%description
Wrapper of pyzmq to make it compatible with gevent. ZeroMQ socket operations
that would normally block the current thread will only block the current
greenlet.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc examples/

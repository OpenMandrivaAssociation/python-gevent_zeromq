%define	module	gevent_zeromq
%define name	python-%{module}
%define version 0.2.4
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %rel
%else
%define	release	%rel
%endif

Summary:	gevent compatibility layer for pyzmq
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/g/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://github.com/traviscline/gevent-zeromq/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc examples/
%py_sitedir/%{module}*


%changelog
* Tue Jul 17 2012 Lev Givon <lev@mandriva.org> 0.2.4-1
+ Revision: 810080
- Update to 0.2.4.

* Wed Jul 04 2012 Lev Givon <lev@mandriva.org> 0.2.3-1
+ Revision: 808003
- Update to 0.2.3.

* Mon May 14 2012 Lev Givon <lev@mandriva.org> 0.2.2-2
+ Revision: 798887
- Rebuild against latest zeromq libs.

* Mon Feb 06 2012 Lev Givon <lev@mandriva.org> 0.2.2-1
+ Revision: 771329
- imported package python-gevent_zeromq


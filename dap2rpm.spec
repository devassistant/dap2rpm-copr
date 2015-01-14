

%{!?_licensedir: %global license %%doc}

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2:        %global __python2 /usr/bin/python2}
%{!?python2_sitelib:  %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global modname dap2rpm

Name:               python-dap2rpm
Version:            0.1.3
Release:            1%{?dist}
Summary:            Generate RPM specfile for DevAssistant DAP packages

Group:              Development/Libraries
License:            
URL:                http://pypi.python.org/pypi/dap2rpm
Source0:            https://pypi.python.org/packages/source/d/%{modname}/%{modname}-%{version}.tar.gz



BuildRequires:      python2-devel



%description
Generate RPM specfiles for DevAssistant DAP packages.


%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build


%install

%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

%check
%{__python2} setup.py test


%files
%doc README.rst
%doc LICENSE
%{python2_sitearch}/%{modname}/
%{python2_sitearch}/%{modname}-%{version}*



%changelog
* Wed Jan 14 2015 Tomas Radej <tradej@redhat.com> - 0.1.3-1
- Initial commit

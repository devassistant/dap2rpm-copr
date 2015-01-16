
Name:               dap2rpm
Version:            0.1.5
Release:            3%{?dist}
Summary:            Tool for generating RPM specfiles for DevAssistant DAP packages.

Group:              Development/Libraries
License:            GPLv2+
URL:                http://pypi.python.org/pypi/dap2rpm
Source0:            https://pypi.python.org/packages/source/d/%{name}/%{name}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python2-devel
BuildRequires:      python3-devel

BuildRequires:      python-setuptools
BuildRequires:      python3-setuptools

Requires:           python3-dap2rpm
Requires:           rpmdevtools

%description
Tool for generating RPM specfiles for DevAssistant DAP packages. Python
libraries are located in the packages python-dap2rpm and python3-dap2rpm.

%package -n python-dap2rpm
Summary:            Python 2 library for generating RPM specfiles for DevAssistant DAP packages.
Requires:           PyYAML
Requires:           python-jinja2
Requires:           python-requests
Requires:           rpmdevtools

%description -n python-dap2rpm
Python 2 library for generating RPM specfiles for DevAssistant DAP packages.

%package -n python3-dap2rpm
Summary:            Python 3 library for generating RPM specfiles for DevAssistant DAP packages.
Requires:           python3-PyYAML
Requires:           python3-jinja2
Requires:           python3-requests
Requires:           rpmdevtools

%description -n python3-dap2rpm
Python 3 library for generating RPM specfiles for DevAssistant DAP packages.

%prep
%setup -q

# Remove bundled egg-info in case it exists
rm -rf %{name}.egg-info %{py3dir}
cp -a . %{py3dir}


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build

pushd %{py3dir}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
popd

%check
%{__python2} setup.py test

pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
popd

%files
%doc README.rst LICENSE
%{_bindir}/%{name}

%files -n python-dap2rpm
%doc README.rst LICENSE
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}-%{version}*

%files -n python3-dap2rpm
%doc README.rst LICENSE
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}*

%changelog
* Fri Jan 16 2015 Tomas Radej <tradej@redhat.com> - 0.1.5-3
- Dependency on rpmdevtools

* Fri Jan 16 2015 Tomas Radej <tradej@redhat.com> - 0.1.5-2
- Changed summary, setup

* Wed Jan 14 2015 Tomas Radej <tradej@redhat.com> - 0.1.5-1
- Initial commit

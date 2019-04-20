#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rjsmin
Version  : 1.1.0
Release  : 16
URL      : https://files.pythonhosted.org/packages/a2/ba/0fa30f7ec949714b8397e80ee2057d1a7e77b3a9f1b94c1ece93586cf34f/rjsmin-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a2/ba/0fa30f7ec949714b8397e80ee2057d1a7e77b3a9f1b94c1ece93586cf34f/rjsmin-1.1.0.tar.gz
Summary  : Javascript Minifier
Group    : Development/Tools
License  : Apache-2.0
Requires: rjsmin-license = %{version}-%{release}
Requires: rjsmin-python = %{version}-%{release}
Requires: rjsmin-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# rJSmin - A Javascript Minifier For Python
TABLE OF CONTENTS
-----------------
1. Introduction
1. System Requirements
1. Installation
1. Documentation
1. Bugs
1. Author Information

%package license
Summary: license components for the rjsmin package.
Group: Default

%description license
license components for the rjsmin package.


%package python
Summary: python components for the rjsmin package.
Group: Default
Requires: rjsmin-python3 = %{version}-%{release}

%description python
python components for the rjsmin package.


%package python3
Summary: python3 components for the rjsmin package.
Group: Default
Requires: python3-core

%description python3
python3 components for the rjsmin package.


%prep
%setup -q -n rjsmin-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551929250
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rjsmin
cp LICENSE %{buildroot}/usr/share/package-licenses/rjsmin/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rjsmin/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

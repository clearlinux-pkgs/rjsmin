#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rjsmin
Version  : 1.2.0
Release  : 37
URL      : https://files.pythonhosted.org/packages/ad/09/b05a0ed0aedb13c7b7a887b4638c5b3c6eb6a16df944deb2593997d8753c/rjsmin-1.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ad/09/b05a0ed0aedb13c7b7a887b4638c5b3c6eb6a16df944deb2593997d8753c/rjsmin-1.2.0.tar.gz
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
Provides: pypi(rjsmin)

%description python3
python3 components for the rjsmin package.


%prep
%setup -q -n rjsmin-1.2.0
cd %{_builddir}/rjsmin-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636994574
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rjsmin
cp %{_builddir}/rjsmin-1.2.0/LICENSE %{buildroot}/usr/share/package-licenses/rjsmin/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rjsmin/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

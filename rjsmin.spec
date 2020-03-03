#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rjsmin
Version  : 1.1.0
Release  : 21
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
=====================
 Javascript Minifier
=====================

rJSmin is a javascript minifier written in python.

The minifier is based on the semantics of `jsmin.c by Douglas Crockford`_\.

The module is a re-implementation aiming for speed, so it can be used at
runtime (rather than during a preprocessing step). Usually it produces the
same results as the original ``jsmin.c``. It differs in the following ways:

- there is no error detection: unterminated string, regex and comment
  literals are treated as regular javascript code and minified as such.
- Control characters inside string and regex literals are left untouched; they
  are not converted to spaces (nor to \n)
- Newline characters are not allowed inside string and regex literals, except
  for line continuations in string literals (ECMA-5).
- "return /regex/" is recognized correctly.
- More characters are allowed before regexes.
- Line terminators after regex literals are handled more sensibly
- "+ +" and "- -" sequences are not collapsed to '++' or '--'
- Newlines before ! operators are removed more sensibly
- (Unnested) template literals are supported (ECMA-6)
- Comments starting with an exclamation mark (``!``) can be kept optionally
- rJSmin does not handle streams, but only complete strings. (However, the
  module provides a "streamy" interface).

Since most parts of the logic are handled by the regex engine it's way faster
than the original python port of ``jsmin.c`` by Baruch Even. The speed factor
varies between about 6 and 55 depending on input and python version (it gets
faster the more compressed the input already is).  Compared to the
speed-refactored python port by Dave St.Germain the performance gain is less
dramatic but still between 3 and 50 (for huge inputs)). See the
docs/BENCHMARKS file for details.

rjsmin.c is a reimplementation of rjsmin.py in C and speeds it up even more.

Supported python versions are 2.7 and 3.4+.

.. _jsmin.c by Douglas Crockford: http://www.crockford.com/javascript/jsmin.c


Copyright and License
~~~~~~~~~~~~~~~~~~~~~

Copyright 2011 - 2019
André Malo or his licensors, as applicable.

The whole package (except for the files in the bench/ directory) is
distributed under the Apache License Version 2.0. You'll find a copy in the
root directory of the distribution or online at:
<http://www.apache.org/licenses/LICENSE-2.0>.


Bugs
~~~~

No bugs, of course. ;-)
But if you've found one or have an idea how to improve rjsmin, feel free
to send a pull request on `github <https://github.com/ndparker/rjsmin>`_
or send a mail to <rjsmin-bugs@perlig.de>.


Author Information
~~~~~~~~~~~~~~~~~~

André "nd" Malo <nd perlig.de>
GPG: 0x8103A37E


    If God intended people to be naked, they would be born that way.
    -- Oscar Wilde

.. vim:tw=72 syntax=rest

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
%setup -q -n rjsmin-1.1.0
cd %{_builddir}/rjsmin-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583220467
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rjsmin
cp %{_builddir}/rjsmin-1.1.0/LICENSE %{buildroot}/usr/share/package-licenses/rjsmin/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
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

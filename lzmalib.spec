%define	major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary: 	A thin wrapper library of LZMA
Name: 		lzmalib
Version: 	0.0.1
Release: 	%mkrel 7
Group: 		System/Libraries
License: 	LGPL
URL: 		http://tokyocabinet.sourceforge.net/misc/
Source0: 	http://tokyocabinet.sourceforge.net/misc/%{name}-%{version}.tar.gz
Patch0:		lzmalib-0.0.1-format_not_a_string_literal_and_no_format_arguments.diff
Patch1:		lzmalib-0.0.1-new_libname_fix.diff
BuildRequires:	chrpath
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package includes a thin wrapper library of LZMA SDK written by Igor
Pavlov.

%package -n	lzmacmd
Summary:	The lzmacmd command line utility
Group:		System/Libraries

%description -n lzmacmd
This package includes the lzmacmd command line utility.

%package -n	%{libname}
Summary:	A thin wrapper library of LZMA
Group:		System/Libraries

%description -n %{libname}
This package includes a thin wrapper library of LZMA SDK written by Igor
Pavlov.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	lzmalib-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p1

%build
rm configure
autoconf

%configure2_5x

%make \
    CFLAGS="%{optflags} -Wall -fPIC -fsigned-char" \
    CXXFLAGS="%{optflags} -Wall -fPIC -fsigned-char" \
    LDFLAGS="$LDFLAGS -L."

%install
rm -rf %{buildroot}

%makeinstall_std

# nuke rpath
chrpath -d %{buildroot}%{_bindir}/lzmacmd

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n lzmacmd
%defattr(-,root,root,755)
%{_bindir}/lzmacmd

%files -n %{libname}
%defattr(-,root,root,755)
%doc README
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,755)
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_libdir}/lib*.a


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-6mdv2011.0
+ Revision: 666138
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-5mdv2011.0
+ Revision: 606453
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-4mdv2010.1
+ Revision: 519036
- rebuild

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.0.1-3mdv2010.0
+ Revision: 439694
- rebuild

* Sat Mar 07 2009 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-2mdv2009.1
+ Revision: 351849
- fix build with -Werror=format-security
- rename the built library to prevent file clash with system lzma lib,
  link against -llzmalib for now on

* Thu Jul 31 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-1mdv2009.0
+ Revision: 258754
- import lzmalib


* Thu Jul 31 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-1mdv2009.0
- initial Mandriva package

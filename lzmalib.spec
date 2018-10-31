%define	major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	A thin wrapper library of LZMA
Name:		lzmalib
Version:	0.0.1
Release:	17
Group:		System/Libraries
License:	LGPLv2
Url:		http://tokyocabinet.sourceforge.net/misc/
Source0:	http://tokyocabinet.sourceforge.net/misc/%{name}-%{version}.tar.gz
Patch0:		lzmalib-0.0.1-format_not_a_string_literal_and_no_format_arguments.diff
Patch1:		lzmalib-0.0.1-new_libname_fix.diff
BuildRequires:	chrpath

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

%package -n	%{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	lzmalib-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%apply_patches
rm configure
autoconf

%build
%configure2_5x

%make \
	CFLAGS="%{optflags} -Wall -fPIC -fsigned-char" \
	CXXFLAGS="%{optflags} -Wall -fPIC -fsigned-char" \
	LDFLAGS="$LDFLAGS -L."

%install
%makeinstall_std

#removed static lib
rm -f %{buildroot}%{_libdir}/*.a
# nuke rpath
chrpath -d %{buildroot}%{_bindir}/lzmacmd

%files -n lzmacmd
%{_bindir}/lzmacmd

%files -n %{libname}
%{_libdir}/liblzmalib.so.%{major}*

%files -n %{devname}
%doc README
%{_includedir}/*.h
%{_libdir}/lib*.so


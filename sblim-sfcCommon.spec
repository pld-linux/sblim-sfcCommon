Summary:	SBLIM common library for functions shared between sfcb and sfcc
Summary(pl.UTF-8):	Wspólna biblioteka SBLIM zawierajaca funkcje używane przez sfcb i sfcc
Name:		sblim-sfcCommon
Version:	1.0.1
Release:	2
License:	Eclipse Public License v1.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
# Source0-md5:	8aa2655d97bdea54c4750f220b40990c
URL:		http://sblim.sourceforge.net/
BuildRequires:	sblim-cmpi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SBLIM common library for functions shared between sfcb and sfcc.

%description -l pl.UTF-8
Wspólna biblioteka SBLIM zawierajaca funkcje używane przez sfcb i
sfcc.

%package devel
Summary:	Header files for sfcUtil library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki sfcUtil
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for sfcUtil library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki sfcUtil.

%package static
Summary:	Static sfcUtil library
Summary(pl.UTF-8):	Statyczna biblioteka sfcUtil
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static sfcUtil library.

%description static -l pl.UTF-8
Statyczna biblioteka sfcUtil.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libsfcUtil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsfcUtil.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsfcUtil.so
%{_libdir}/libsfcUtil.la
%{_includedir}/sfcCommon

%files static
%defattr(644,root,root,755)
%{_libdir}/libsfcUtil.a

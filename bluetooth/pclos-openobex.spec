%define major 1
%define libname %mklibname openobex %{major}
%define develname %mklibname openobex -d

Summary: 	Library for using OBEX
Name: 		openobex
Version: 	1.7.1
Release: 	%mkrel 1
License: 	LGPL
Group: 		System/Libraries
URL:		http://openobex.sourceforge.net/
Source: 	http://www.kernel.org/pub/linux/bluetooth/openobex-%{version}-Source.tar.gz
#Patch0:		openobex-1.3-ipv6.patch
#Patch1:		openobex-linkage_fix.diff
#Patch2:		openobex-1.5-automake-1.13.patch
BuildRequires:	bluez-devel
BuildRequires:	libusb-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:  	%name < %version

%description
Open OBEX shared c-library

%package -n %{libname}
Summary: Library for using OBEX
Group: System/Libraries
Provides: lib%{name} = %version-%release
Provides: %{name} = %version-%release
Conflicts: %{_lib}%{name}1.3
Conflicts: %{_lib}%{name}1.2
Conflicts: %{_lib}%{name}1.1

%description -n %{libname}
Open OBEX shared c-library

%package -n %{develname}
Summary: Library for using OBEX
Group: Development/C
Provides: lib%{name}-devel = %version-%release
Provides: %{name}-devel  = %version-%release
Requires: %{libname} = %{version}
Requires:   bluez-devel
Conflicts: %{_lib}%{name}1.3-devel
Conflicts: %{_lib}%{name}1.2-devel
Conflicts: %{_lib}%{name}1.1-devel
Obsoletes: %{_lib}%{name}1-devel

%description -n %{develname}
Open OBEX shared c-library

%package apps
Summary: Apps that come with the Open OBEX c-library
Group: Communications

%description apps
These are the apps that come with the Open OBEX c-library. These are
not meant to be more than test-programs to look at if you want to see
how use the library itself.

%package ircp
Summary: Used to "beam" files or whole directories
Group: Communications
Obsoletes: ircp
Provides: ircp

%description ircp
Ircp is used to "beam" files or whole directories to/from Linux, Windows.

%prep

%setup -q -n openobex-%{version}-Source

%build
mkdir -p build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..

%make

%install
cd build
%makeinstall_std

# since our old packages will look for headers in /usr/include
ln -s openobex/obex.h %{buildroot}/%_includedir/obex.h
ln -s openobex/obex_const.h %{buildroot}/%_includedir/obex_const.h

%post -n %{libname}
/sbin/ldconfig

%postun -n %{libname}
/sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc COPYING
%{_libdir}/libopenobex.so.%{major}*
/lib/udev/rules.d/60-openobex.rules
/usr/sbin/obex-check-device
/usr/lib64/libopenobex.so.2

%files -n %{develname}
%defattr(-, root, root)
%doc AUTHORS ChangeLog README
%{_libdir}/pkgconfig/openobex.pc
%{_includedir}/*
%{_libdir}/lib*.so
/usr/lib64/cmake/OpenObex-1.7.1/openobex-config-version.cmake
/usr/lib64/cmake/OpenObex-1.7.1/openobex-config.cmake
/usr/lib64/cmake/OpenObex-1.7.1/openobex-target-release.cmake
/usr/lib64/cmake/OpenObex-1.7.1/openobex-target.cmake


%files apps
%defattr(-, root, root)





%files ircp
%defattr(-, root, root)

%changelog
* Mon Aug 26 2013 billybot <billybot> 1.5-5pclos2013
- update for 2013

* Fri Aug 13 2010 Texstar <texstar at gmail.com> 1.5-4pclos2010
- rebuild against updated libs

* Tue Dec 01 2009 Texstar <texstar at gmail.com> 1.5-3pclos2010
- gcc update
- build for new bluez


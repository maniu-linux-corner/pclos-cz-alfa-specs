Name:           cinnamon-menus
Version:        3.2.0
Release:        3%{?dist}
Summary:        Menus for cinnamom

License:        GPL
URL:            linuxmint.com
Source0:        cinnamon-menus-%{version}.tar.gz

%description
cinnamom menus


%package devel
Summary: %{name} devel files for
Group:    Development/C
Requires: %{name}
Provides: %name-devel
%description devel
Development files for %{name}

%prep
%setup -q


%build
NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%{_libdir}/girepository-1.0/CMenu-3.0.typelib
%{_libdir}/libcinnamon-menu-3.a
%{_libdir}/libcinnamon-menu-3.so.0
%{_libdir}/libcinnamon-menu-3.so.0.0.1
%{_datadir}/gir-1.0/CMenu-3.0.gir

%files devel
%{_libdir}/pkgconfig/libcinnamon-menu-3.0.pc
%{_includedir}/cinnamon-menus-3.0/gmenu-tree.h
%{_libdir}/libcinnamon-menu-3.so

%changelog
* Wed Dec 25 2016 Mank <mank at pclinuxos dot cz> 2.8.0-1mank2016
- create

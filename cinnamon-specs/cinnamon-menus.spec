Name:           cinnamon-menus
Version:        2.8.0
Release:        1%{?dist}
Summary:        menus for cinnamom

License:        GPL
URL:            linuxmint.com
Source0:        cinnamon-menus-%{version}.tar.gz

%description
cinnamom menus

%prep
%setup -q


%build
NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
/usr/include/cinnamon-menus-3.0/gmenu-tree.h
/usr/lib64/girepository-1.0/CMenu-3.0.typelib
/usr/lib64/libcinnamon-menu-3.a
/usr/lib64/libcinnamon-menu-3.la
/usr/lib64/libcinnamon-menu-3.so
/usr/lib64/libcinnamon-menu-3.so.0
/usr/lib64/libcinnamon-menu-3.so.0.0.1
/usr/lib64/pkgconfig/libcinnamon-menu-3.0.pc
/usr/share/gir-1.0/CMenu-3.0.gir

%changelog

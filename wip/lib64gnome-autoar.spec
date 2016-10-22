Name:           lib64gnome-autoar
Version:        0.1.1
Release:        1%{?dist}
Summary:        The gnome-autoar package provides a framework for automatic archive extraction, compression, and management. 

License:        GPLv3
URL:            http://ftp.gnome.org/pub/gnome/sources/gnome-autoar/0.1/gnome-autoar-0.1.1.tar.xz
Source0:        http://ftp.gnome.org/pub/gnome/sources/gnome-autoar/0.1/gnome-autoar-0.1.1.tar.xz

BuildRequires:  %{_lib}archive-devel

%description
The gnome-autoar package provides a framework for automatic archive extraction, compression, and management. 


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n gnome-autoar-%{version}


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*
%{_datadir}/gir-1.0/GnomeAutoar-0.1.gir
%{_datadir}/gir-1.0/GnomeAutoarGtk-0.1.gir
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.archives.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.desktop.archives.gschema.xml



%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/gnome-autoar-0.pc
%{_libdir}/pkgconfig/gnome-autoar-gtk-0.pc
%{_datadir}/gtk-doc/html/gnome-autoar/



%changelog

Name:           lib64cryptui
Version:        3.12.2
Release:        1%{?dist}
Summary:        Library for OpenPGP prompts

License:        GPLv3
URL:            http://ftp.gnome.org/pub/GNOME/sources/libcryptui/3.12/
Source0:        libcryptui-%{version}.tar.xz

BuildRequires:  lib64gpgme-devel lib64notify-devel
       

%description
Library for OpenPGP prompts


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n libcryptui-%{version}


%build
%configure --disable-static --disable-schemas-compile
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
%{_bindir}/seahorse-daemon
%{_libdir}/girepository-1.0/CryptUI-0.0.typelib
%{_datadir}/GConf/gsettings/org.gnome.seahorse.recipients.convert
%{_datadir}/cryptui/*
%{_datadir}/dbus-1/services/org.gnome.seahorse.service
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.recipients.gschema.xml
%{_datadir}/pixmaps/cryptui/*
%{_datadir}/locale/*


%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/cryptui-0.0.pc
%{_datadir}/gir-1.0/CryptUI-0.0.gir
%{_datadir}/gtk-doc/html/libcryptui/*
%{_datadir}/man/man1/*


%changelog

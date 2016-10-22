Name:           evolution
Version:        3.22.1
Release:        1%{?dist}
Summary:        %{name} e-mail suite

License:        GPLv3
URL:            gnome.org
Source0:        evolution-%{version}.tar.xz

Provides: pkgconfig(camel-1.2)
Provides: pkgconfig(libebackend-1.2)
Provides: pkgconfig(libedataserver-1.2)
Provides: pkgconfig(libedataserverui-1.2)
#BuildRequires:  
#Requires:       

%description


%prep
%setup -q


%build
%configure --enable-nss=yes --with-openldap=yes --enable-smime=yes --disable-weather --disable-schemas-compile
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_datadir}/locale/*
%{_datadir}/help/*
%{_datadir}/gtk-doc/*
%{_datadir}/evolution/*
%{_datadir}/icons/hicolor/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/*
%{_datadir}/GConf/gsettings/evolution.convert
%{_libdir}/pkgconfig/*
%{_libdir}/evolution/*
%{_includedir}/evolution/*
/etc/xdg/autostart/evolution-alarm-notify.desktop
%{_bindir}/evolution




%changelog

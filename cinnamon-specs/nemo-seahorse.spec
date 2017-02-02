Name:           nemo-seahorse
Version:        3.2.0
Release:        1%{?dist}
Summary:        Nemo sea horse

License:        GPL
URL:            http://github.com/linuxmint
Source0:        nemo-seahorse-%{version}.tar.xz

%description


%prep
%setup -q


%build
sh autogen.sh --prefix=/usr
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files

%{_bindir}/seahorse-tool
%{_libdir}/nemo/extensions-3.0/libnemo-seahorse.so
%{_datadir}/GConf/gsettings/org.gnome.seahorse.nautilus.convert
%{_datadir}/applications/seahorse-pgp-encrypted.desktop
%{_datadir}/applications/seahorse-pgp-keys.desktop
%{_datadir}/applications/seahorse-pgp-signature.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.nautilus.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.nautilus.window.gschema.xml
%{_datadir}/locale/*
%{_datadir}/man/man1/seahorse-tool.1.bz2
%{_datadir}/nemo-seahorse/ui/seahorse-multi-encrypt.xml
%{_datadir}/nemo-seahorse/ui/seahorse-notify.xml
%{_datadir}/nemo-seahorse/ui/seahorse-progress.xml



%changelog

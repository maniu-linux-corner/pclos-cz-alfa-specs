Name:           cinnamon-bluetooth
Version:        3.6.0
Release:        1%{?dist}
Summary:        Cinnamom Bluetooth

License:        GPL
URL:            linuxmint.com
Source0:        cinnamon-bluetooth-gnome-bluetooth-3.6.zip
#Patch1:			patch-con.patch
%description
Cinnamon bluetooth

%prep
%setup -q -n cinnamon-bluetooth-gnome-bluetooth-3.6
#%apply_patches

%build
autoreconf -vif
%configure2_5x
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_libdir}/cinnamon-control-center-1/panels/libbluetooth.a
%{_libdir}/cinnamon-control-center-1/panels/libbluetooth.la
%{_libdir}/cinnamon-control-center-1/panels/libbluetooth.so
%{_datadir}/applications/cinnamon-bluetooth-properties.desktop
%{_datadir}/cinnamon-bluetooth/bluetooth.ui
%{_datadir}/cinnamon/applets/bluetooth@cinnamon.org/applet.js
%{_datadir}/cinnamon/applets/bluetooth@cinnamon.org/metadata.json




%changelog

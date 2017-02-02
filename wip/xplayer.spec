Name:           xplayer
Version:        1.2.2
Release:        6
Summary:        xplayer Xapps media player

License:        GPL
URL:            https://github.com/linuxmint/xplayer/
Source0:        xplayer-%{version}.tar.gz

Requires: xapps
Requires: %{_lib}peas0 
Requires: %{_lib}peas-gtk0 
Requires: cogl 
Requires: clutter 
Requires: clutter-gtk 
Requires: clutter-gst 
Requires: %{_lib}dbus-glib-1_2 
Requires: %{_lib}girepository1.0_1 
Requires: %{_lib}gstreamer1.0_0
Requires: gtk+3.0
Requires: pkgconfig(xplayer-plparser) >= 1.0.0
Requires: gstreamer1.0-plugins-bad
Requires: gstreamer1.0-plugins-base
Requires: gstreamer1.0-plugins-good
Requires: gstreamer1.0-plugins-ugly
Requires: gstreamer1.0-libav
#AutoReq: No


%package devel
Summary: %{name} devel files for
Group:    Development/C
Requires: %{name}
Provides: %name-devel = %{version}

%description devel
Development files for %{name}

%description
Xapps media player

%prep
%setup -q


%build
# https://github.com/linuxmint/xplayer/issues/22
# No switch to disable grilo, so just bump the required
# version to something that obviously won't be satisfied.
sed -i 's/GRILO_REQS=0.2.0/GRILO_REQS=0.9.0/g' configure.ac
NOCONFIGURE=1 gnome-autogen.sh
%configure2_5x --disable-static --disable-run-in-source-tree --disable-vegas-plugin --enable-vala=yes --enable-debug=no
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install

# we don't want these
find %{buildroot} -name "*.la" -delete

%files
%{_bindir}/*
%{_datadir}/locale/
%{_datadir}/help/*
%{_datadir}/icons/hicolor/*
%{_datadir}/%{name}/*
%{_datadir}/thumbnailers/*
%{_datadir}/glib-2.0/*
%{_libdir}/girepository-1.0/*
%{_libdir}/libxplayer.so.0
%{_libdir}/libxplayer.so.0.0.0
%{_libdir}/mozilla/plugins/*
%{_libdir}/%{name}/*
%{_libexecdir}/*
%{_datadir}/applications/xplayer.desktop
 /usr/share/man/man1/*
%files devel
%{_libdir}/libxplayer.so
%{_includedir}/*
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/*.gir

%changelog
* Sat Jan  7 2017 mank
- import to pclosczsk

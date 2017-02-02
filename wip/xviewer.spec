Name:           xviewer
Version:        1.2.2
Release:        3
Summary:        xapps xviewer

License:        GPL
URL:            https://github.com/linuxmint/xviewer
Source0:        xviewer-%{version}.zip

Source1:        %{name}.desktop       

Requires: xapps 
Requires: %{_lib}exif12 
Requires: %{_lib}lcms2_2 
Requires: %{_lib}jpeg8 
Requires: %{_lib}exempi3
Requires: %{_lib}peas0 
Requires: %{_lib}peas-gtk0 
Requires: gtk+3.0
Requires: %{_lib}girepository1.0_1 

AutoReq: No

%description
xapps's xviewer

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

autoreconf -fi

%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
%__cp %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/applications/
# we don't want these
find %{buildroot} -name "*.la" -delete

%files
%{_bindir}/*
%{_datadir}/GConf/*
%{_datadir}/glib-2.0/*
%{_datadir}/appdata/*
%{_datadir}/applications/*
%{_datadir}/%{name}/*
%{_datadir}/locale/
%{_datadir}/help/*
%{_datadir}/icons/hicolor/*
%{_datadir}/%{name}/*
%{_datadir}/locale/
%{_datadir}/help/*
%{_datadir}/icons/hicolor/*
%{_libdir}/xviewer/girepository-1.0/*
%{_libdir}/xviewer/libxviewer.so

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/xviewer.pc
%{_datadir}/%{name}/gir-1.0/*.gir

%changelog
* Sat Jan  7 2017 mank
- import to pclinuxosczsk

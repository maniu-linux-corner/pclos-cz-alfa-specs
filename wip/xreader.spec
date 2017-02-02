Name:           xreader
Version:        1.2.2
Release:        5
Summary:        Xapps pdf reader

License:        GPL
URL:            https://github.com/linuxmint/xreader
Source0:        xreader-%{version}.tar.gz
Source1:        %{name}.desktop
Requires: %{_lib}tiff5 
Requires: %{_lib}secret1_0  
Requires: %{_lib}poppler-glib8
Requires: gtk+3.0
Requires: zlib1 
Requires: lib64gail3_0
BuildRequires: mate-file-manager-devel
BuildRequires: nemo-devel
AutoReq: No

%description
Xapps pdf reader


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
sh autogen.sh --prefix=/usr --libdir=/usr/lib64/

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
%__cp %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/applications/
# we don't want these
find %{buildroot} -name "*.la" -delete

%files
%{_bindir}/*
%{_datadir}/glib-2.0/*
%{_datadir}/appdata/*
%{_datadir}/applications/*
%{_datadir}/%{name}/*
%{_datadir}/locale/*
%{_datadir}/help/*
%{_datadir}/icons/hicolor/*
%{_datadir}/caja/extensions/*
%{_datadir}/nemo/extensions/*
%{_datadir}/dbus-1/services/org.x.reader.Daemon.service
%{_datadir}/thumbnailers/xreader.thumbnailer
%{_datadir}/man/man1/*
%{_libdir}/%{name}/*
%{_libdir}/libxreaderdocument.so.3
%{_libdir}/libxreaderdocument.so.3.0.0
%{_libdir}/libxreaderview.so.3
%{_libdir}/libxreaderview.so.3.0.0
%{_libdir}/libxreaderdocument.a
%{_libdir}/libxreaderview.a
%{_libdir}/caja/extensions-2.0/libxreader-properties-page.a
%{_libdir}/caja/extensions-2.0/libxreader-properties-page.so
%{_libdir}/nemo/extensions-3.0/libxreader-properties-page.a
%{_libdir}/nemo/extensions-3.0/libxreader-properties-page.so
%{_libexecdir}/*

%files devel
%{_libdir}/libxreaderview.so
%{_libdir}/libxreaderdocument.so
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/xreader-document-1.5.0.pc
%{_libdir}/pkgconfig/xreader-view-1.5.0.pc
#%{_datadir}/gir-1.0/*.gir


%changelog
* Sat Jan  7 2017 mank
- import to pclinuxosczsk

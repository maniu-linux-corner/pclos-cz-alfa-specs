Name:           nemo-preview
Version:        3.2.0
Release:        2%{?dist}
Summary:        Nemo preview

License:        GPL
URL:            linuxmint.com
Source0:        nemo-preview-%{version}.tar.xz
#Source1:	application.js
#Patch0:		clutter-gst3.patch
#BuildRequires:  
#Requires:       

%description


%prep
%setup -q -n %{name}
#%apply_patches

%build
sh autogen.sh --prefix=/usr
%configure --disable-static --disable-schemas-compile
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm $RPM_BUILD_ROOT/%{_libdir}/nemo-preview/libnemo-preview-1.0.la
#cp -f %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/nemo-preview/js/ui/application.js
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/nemo-preview
%{_libexecdir}/nemo-preview-start
%{_libdir}/nemo-preview/girepository-1.0/NemoPreview-1.0.typelib
%{_libdir}/nemo-preview/libnemo-preview-1.0.so
%{_datadir}/dbus-1/services/org.nemo.Preview.service
%{_datadir}/nemo-preview/*




%changelog

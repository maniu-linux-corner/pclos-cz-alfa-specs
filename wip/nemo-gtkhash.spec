Name:           nemo-gtkhash
Version:        3.2.0
Release:        1
Summary:        GtkHash for nemo

License:        GPL
URL:            http://github.com/linuxmint
Source0:        nemo-gtkhash-3.2.0.tar.xz

%description


%prep
%setup -q


%build
sh autogen.sh --prefix=/usr
#--enable-gcrypt
%configure --with-gtk=3.0 --disable-gtkhash --enable-mhash --enable-libcrypto --enable-nemo
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}//nemo/extensions-3.0/*.la

%files
%doc
%{_libdir}/nemo/extensions-3.0/libgtkhash-properties.so
%{_datadir}/glib-2.0/schemas/org.nemo.extensions.gtkhash.gschema.xml
%{_datadir}/locale/*
%{_datadir}/nemo-gtkhash/nautilus/gtkhash-properties.xml.gz


%changelog
* Wed Feb  1 2017 mank
- 

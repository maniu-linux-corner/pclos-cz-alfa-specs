Name:           pix
Version:        1.2.1
Release:        1
Summary:        pix

License:        GPL
URL:            https://github.com/linuxmint/pix
Source0:        pix-%{version}.zip

#gnome-common yelp yelp-tools

%description
...

%prep
%setup -q


%build
NOCONFIGURE=1 gnome-autogen.sh --disable-static --add-missing
%configure2_5x \
  --disable-static       \
  --disable-silent-rules \
  --with-smclient=xsmp
#Note: from archlinux
# Copy some files that ended up in the wrong directory.
# This doesn't happen on mint. See this github issue:
# https://github.com/linuxmint/pix/issues/7
mkdir -p $RPM_BUILD_DIR/%{name}-%{version}/pix/.deps/
touch $RPM_BUILD_DIR/%{name}-%{version}/pix/.deps/dom_test-dom.Po
touch $RPM_BUILD_DIR/%{name}-%{version}/pix/.deps/glib_utils_test-glib-utils.Po
touch $RPM_BUILD_DIR/%{name}-%{version}/pix/.deps/gsignature_test-gsignature.Po
touch $RPM_BUILD_DIR/%{name}-%{version}/pix/.deps/oauth_test-gsignature.Po
cd $RPM_BUILD_DIR/%{name}-%{version}/
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_bindir}/*
%{_datadir}/*
%{_includedir}/*
%{_libdir}/pix/
%{_libdir}/pkgconfig/*
%changelog
* Sat Jan  7 2017 mank
- import to pclinuxosczsk

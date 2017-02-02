Name:           iso-flags
Version:        1.0.1
Release:        1
Summary:        iso flags

License:        PD
URL:            https://github.com/linuxmint/iso-country-flags-svg-collection
Source0:        flags-1.0.1.tar.gz

%description
https://github.com/linuxmint/flags

%prep
%setup -q -n flags-1.0.1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/iso-flag-png
%__cp -r usr/share/iso-flag-png $RPM_BUILD_ROOT/%{_datadir}/


%files
%{_datadir}/iso-flag-png/*



%changelog
* Thu Feb  2 2017 mank
- 

Name:           nemo-terminal
Version:        3.2.0
Release:        1
Summary:        Nemo Embeded term

License:        GPL
URL:            github.com/linuxmint
Source0:        nemo-terminal-3.2.0.tar.xz

Requires:       vte
Requires:       python-pyxdg
Requires:       nemo-python

%description


%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/nemo-python/extensions/
%__cp src/nemo_terminal.py $RPM_BUILD_ROOT/usr/share/nemo-python/extensions
mkdir -p $RPM_BUILD_ROOT/usr/share/glib-2.0/schemas
%__cp src/org.nemo.extensions.nemo-terminal.gschema.xml $RPM_BUILD_ROOT/usr/share/glib-2.0/schemas
mkdir -p $RPM_BUILD_ROOT/usr/share/nemo-terminal
%__cp pixmap/logo_120x120.png $RPM_BUILD_ROOT/usr/share/nemo-terminal


%files
%{_datadir}/nemo-python/extensions/
%{_datadir}/nemo-terminal
%{_datadir}/glib-2.0/schemas

%changelog
* Wed Feb  1 2017 mank
- 

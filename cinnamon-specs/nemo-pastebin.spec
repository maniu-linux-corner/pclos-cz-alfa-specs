Name:           nemo-pastebin
Version:        3.2.0
Release:        1
Summary:        Nemo Embeded term

License:        GPL
URL:            github.com/linuxmint
Source0:        nemo-pastebin-3.2.0.tar.xz

Requires:       python-pyxdg
Requires:       nemo-python

%description


%prep
%setup -q

%build


%install
rm -rf $RPM_BUILD_ROOT
./setup.py install --root=%{buildroot} --install-lib=/usr/lib64

%files
%{_bindir}/
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/glib-2.0/*
%{_datadir}/locale/*
%{_datadir}/nemo-pastebin/*
%{_datadir}/pixmaps/*
%{_libdir}/nemo_pastebin-3.2.0-py2.7.egg-info

%changelog
* Wed Feb  1 2017 mank
- 

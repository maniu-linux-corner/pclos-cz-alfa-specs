Name:		nemo-audio-tab
Version:	3.2.0
Summary:	A audio tab extension for nemo
Release:	%mkrel 2
License:	GPLv2+
URL:		https://github.com/linuxmint/nemo-extensions
Group:		Graphical desktop/Cinnamon
Source:		nemo-audio-tab-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0) 
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0) 
BuildRequires:	nemo-devel
BuildRequires: python
BuildRequires: python-distutils-extra
Requires:	nemo 
Requires:	python3-pillow
Requires:	python-kaa-base 
Requires:	python-kaa-metadata
Requires:   python-exiv2 
Requires:   mutagen

%description
audio tab extension for Nemo for the Cinnamon desktop environment. 


%prep
%setup -q

%build
./setup.py build

%install
./setup.py install --root=%{buildroot} --install-lib=/usr/lib64//python2.7/site-packages/

%files 
%defattr(-,root,root)
%{_libdir}/python2.7/site-packages/nemo_audio_tab-%{version}-py2.7.egg-info
%{_datadir}/nemo-python/extensions/nemo-audio-tab.glade
%{_datadir}/nemo-python/extensions/nemo-audio-tab.py


%changelog
* Sat Oct 26 2016 Mank <mank at pclinuxos dot cz> 2.8.0-1mank2016
- Create pkg




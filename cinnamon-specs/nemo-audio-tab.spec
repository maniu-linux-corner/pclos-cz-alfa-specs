Name:		nemo-audio-tab
Version:	2.8.0
Summary:	A file-roller extension for nemo
Release:	%mkrel 1
License:	GPLv2+
URL:		https://github.com/linuxmint/nemo-extensions
Group:		Graphical desktop/Cinnamon
Source:		nemo-audio-tab-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0) 
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0) 
BuildRequires:	nemo-devel
Requires:	nemo 

%description
audio tab extension for Nemo for the Cinnamon desktop environment. 


%prep
%setup -q -n nemo-audio-tab-%{version}

%build
./setup.py build

%install
./setup.py install --root=%{buildroot}

%files 
%defattr(-,root,root)
/usr/lib/python2.7/site-packages/nemo_audio_tab-2.8.0-py2.7.egg-info
%{_datadir}/nemo-python/extensions/nemo-audio-tab.glade
%{_datadir}/nemo-python/extensions/nemo-audio-tab.py


%changelog
* Sat Oct 26 2013 Ken <lxgator at gmail.com> 2.0.0-1pclos2013
- Create pkg



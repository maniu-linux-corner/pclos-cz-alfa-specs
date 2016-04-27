
Name:           cinnamon-translations
Version:        3.0.0
Release:        %mkrel 2
Summary:        Translations for Cinnamon and Nemo
Group:   	Graphical desktop/Cinnamon
License:        GPLv2+
URL:            http://cinnamon.linuxmint.com
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
      

%description
Translations for Cinnamon and Nemo

%prep
%setup -q -n %{name}-%{version}

%build
make

%install
rm -rf %{buildroot}
install -m 0755 -d $RPM_BUILD_ROOT%{_datadir}/locale/ 
cp -Rp usr/share/locale/* $RPM_BUILD_ROOT%{_datadir}/locale/

rm $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/cinnamon-bluetooth.mo

%find_lang cinnamon
%find_lang nemo
%find_lang cinnamon-control-center

%files -f cinnamon.lang -f nemo.lang -f cinnamon-control-center.lang
%defattr(-,root,root)
%doc COPYING
%{_datadir}/locale/


%clean
rm -rf %{buildroot}


%changelog
* Tue Nov 13 2016 Mank <mank@pclinuxos.cz> 2.8.3-2pclos2016
- update
* Tue Nov 12 2013 billybot <billybot> 2.0.2-1pclos2013
- update

* Fri Oct 17 2013 billybot <billybot> 2.0.1-1pclos2013
- import into pclos

%define version 1.15
%define release %mkrel 2

%define amversion 1.15
%global __requires_exclude perl\\(Automake::.*\\)
%global __provides_exclude perl\\(Automake::.*\\)


Summary:	A GNU tool for automatically creating Makefiles
Name:		automake
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Development/Other
Source0:	http://ftp.gnu.org/gnu/automake/automake-%{version}.tar.xz
#Source1:	fix-old-automake-files
#Patch0:		automake-1.13.1-automatically-fix-old-files.patch
#Patch1:		automake-1.13.4-hash-order-workaround.patch
URL:		http://www.gnu.org/software/automake/
BuildArch:	noarch

Requires:	autoconf
BuildRequires:	autoconf
BuildRequires:	texinfo
Conflicts:	automake1.5
Provides:	automake1.9 = %{version}-%{release}
Obsoletes:	automake1.9
Provides:	automake1.8 = %{version}-%{release}
Obsoletes:	automake1.8
Requires(post):	info-install
Requires(preun): info-install
Requires(post):	update-alternatives
Requires(preun): update-alternatives


%description
Automake is a tool for automatically generating Makefiles compliant with
the GNU Coding Standards.

You should install Automake if you are developing software and would like
to use its capabilities of automatically generating GNU standard
Makefiles. If you install Automake, you will also need to install GNU's
Autoconf package.

%prep
%setup -q -n automake-%{version}
#%apply_patches

%build
%configure2_5x --build=%{_host}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

ln -s automake-%{amversion} %{buildroot}%{_bindir}/automake-1.8
ln -s aclocal-%{amversion} %{buildroot}%{_bindir}/aclocal-1.8

ln -s automake-%{amversion} %{buildroot}%{_bindir}/automake-1.9
ln -s aclocal-%{amversion} %{buildroot}%{_bindir}/aclocal-1.9

ln -s automake-%{amversion} %{buildroot}%{_bindir}/automake-1.12
ln -s aclocal-%{amversion} %{buildroot}%{_bindir}/aclocal-1.12

ln -s automake-%{amversion} %{buildroot}%{_bindir}/automake-1.13
ln -s aclocal-%{amversion} %{buildroot}%{_bindir}/aclocal-1.13


rm -f %{buildroot}/%{_infodir}/*
install -m 644 doc/%{name}.info* %{buildroot}/%{_infodir}/

#install -c -m 755 %{SOURCE1} %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_datadir}/aclocal

%pre
if [ "$1" = 1 ]; then
  update-alternatives --remove automake %{_bindir}/automake-1.8
  update-alternatives --remove automake %{_bindir}/automake-1.9
  update-alternatives --remove automake %{_bindir}/automake-1.12
  update-alternatives --remove automake %{_bindir}/automake-1.13  
fi

%post
%_install_info %name.info

%preun
%_remove_install_info %name.info

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS
#%{_bindir}/fix-old-automake-files
%{_bindir}/automake
%{_bindir}/aclocal
%{_bindir}/automake-%{amversion}
%{_bindir}/aclocal-%{amversion}
%{_bindir}/automake-1.8
%{_bindir}/aclocal-1.8
%{_bindir}/automake-1.9
%{_bindir}/aclocal-1.9
%{_bindir}/automake-1.12
%{_bindir}/aclocal-1.12
%{_bindir}/aclocal-1.13
%{_bindir}/automake-1.13
%{_datadir}/automake*
%{_infodir}/automake*
%{_datadir}/aclocal*
%{_mandir}/man1/*


%changelog
* Mon Apr 27 2015 bb <bb> 1.14.1-2pclos2015
- update and apply rosa patches

* Sat Nov 29 2014 bb <bb> 1.14.1-1pclos2014
 -update
 
* Sat Jan 25 2014 daniel <meisssw01 at gmail.com> 1.14-1pclos2014
- upstream tarball

* Thu Jun 20 2013 ghostbunny <hmhaase at pclinuxosusers dot de> 1.13.4-1pclos2013
- 1.13.4

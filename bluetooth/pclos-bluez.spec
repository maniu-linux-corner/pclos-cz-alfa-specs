# 32/64bit spec-file
#
%define major	3
%define libname	%mklibname %{name} %{major}
%define	devname	%mklibname -d %{name}

Name:		bluez
Summary:	Official Linux Bluetooth protocol stack
Version:	4.101
Release:	%mkrel 9
License:	GPLv2+
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://bluez.sourceforge.net/
Source0:	http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.xz
Source1:	97-bluetooth.rules
Source6:	pand.conf
Source7:	dund.conf
Source8:	hidd.conf
Source9:	rfcomm.conf
Patch0500:	0500-Add-support-for-CF-Personal-Network-Card-Rev-2.5-fro.patch
Patch0501:	0501-Add-sixaxis-cable-pairing-plugin.patch
Patch0504:	0502-bluez-4.101-automake-1.13.patch
BuildRequires:	dbus-devel
BuildRequires:	flex
BuildRequires:	bison
#BuildRequires:	libusb-devel
BuildRequires:	libalsa-devel 
BuildRequires:	udev-tools 
BuildRequires:	libgstreamer0.10-plugins-base-devel 
BuildRequires:	%{_lib}gstreamer0.10_0.10-devel hal-devel
BuildRequires:	expat-devel
BuildRequires:	udev-devel
BuildRequires:	%{_lib}libcap-ng-devel
BuildRequires:	%{_lib}usb-compat0.1-devel
BuildConflicts: %{_lib}usb-compat0.1-static-devel
Requires:	python 
Requires:	bluez-pin 
Requires:	obex-data-server
Provides:	bluez-sdp
Obsoletes:	bluez-sdp < 4.0
Provides:	bluez-pan
Provides:	bluez-hciemu
Obsoletes:	bluez-hciemu
Provides:	bluez-utils
Obsoletes:	bluez-utils < 4.0
Requires:	bluez-firmware

%description
These are the official Bluetooth communication libraries for Linux.

%post
update-alternatives --install /bin/bluepin bluepin /usr/bin/bluepin 5
#migrate old configuration
if [ "$1" = "2" -a -d %{_var}/lib/lib/bluetooth ]; then
 mv -f %{_var}/lib/lib/bluetooth/* %{_var}/lib/bluetooth/ > /dev/null 2>&1 || exit 0
 rmdir %{_var}/lib/lib/bluetooth/ > /dev/null 2>&1 || exit 0
 rmdir %{_var}/lib/lib/ > /dev/null 2>&1 || exit 0
fi

%postun
if [ "$1" = "0" ]; then
  update-alternatives --remove bluepin /usr/bin/bluepin
fi

%triggerin -- bluez < 4.46
/sbin/chkconfig --del bluetooth
/sbin/chkconfig --del dund
/sbin/chkconfig --del hidd
/sbin/chkconfig --del pand

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sbindir}/*
/sbin/hidd
/sbin/bluetoothd
%{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/*.conf
%config(noreplace) %{_sysconfdir}/bluetooth
%{_datadir}/dbus-1/system-services/org.bluez.service
/lib/udev/bluetooth_serial
/lib/udev/hid2hci
%{_sysconfdir}/udev/rules.d/97-bluetooth-serial.rules
%{_sysconfdir}/udev/rules.d/97-bluetooth-hid2hci.rules
%{_sysconfdir}/udev/rules.d/97-bluetooth.rules
/var/lib/bluetooth

#--------------------------------------------------------------------

%package        cups
Summary:        CUPS printer backend for Bluetooth printers
Group:          System/Servers
Requires:       cups
Obsoletes:      %name-utils-cups

%description    cups
This package contains the CUPS backend for Bluetooth printers.

%files cups
%defattr(-, root, root)
%{_prefix}/lib/cups/backend/bluetooth

#--------------------------------------------------------------------

%package gstreamer
Summary: Gstreamer support for SBC audio format
Group: Sound
Obsoletes:      %name-utils-gstreamer

%description gstreamer
This package contains gstreamer plugins for the Bluetooth SBC audio format

%files gstreamer
%defattr(-, root, root)
%{_libdir}/gstreamer-*/*.so

#--------------------------------------------------------------------

%package alsa
Summary: ALSA support for Bluetooth audio devices
Group: Sound
Obsoletes:      %name-utils-alsa

%description alsa
This package contains ALSA support for Bluetooth audio devices

%files alsa
%defattr(-, root, root)
%{_libdir}/alsa-lib/*.so
%{_datadir}/alsa/bluetooth.conf

#--------------------------------------------------------------------

%package -n	%{libname}
Summary:	Official Linux Bluetooth protocol stack
Group:		System/Libraries
Provides:	lib%{name}-sdp2
Obsoletes:	lib%{name}-sdp2

%description -n	%{libname}
These are the official Bluetooth communication libraries for Linux.

%files -n %{libname}
%defattr(-,root,root)
/%{_lib}/lib*.so.%{major}*

#--------------------------------------------------------------------

%package -n	%{devname}
Summary:	Headers for developing programs that will use %name
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-sdp-devel, lib%{name}-sdp2-devel
Obsoletes:	lib%{name}-sdp-devel, lib%{name}-sdp2-devel
Provides:	%{name}-sdp-devel
Obsoletes:	%{name}-sdp-devel
Obsoletes:	%{libname}-devel

%description -n	%{devname}
This package contains the headers that programmers will need to develop
applications which will use libraries from %{name}.

%files -n %{devname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%dir %{_includedir}/bluetooth
%{_includedir}/bluetooth/*.h
/%{_lib}/*.so
/%{_lib}/*.la
%{_libdir}/pkgconfig/bluez.pc

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%{version}
%apply_patches

%build
autoreconf -fi
%define _localstatedir %{_var}
%configure2_5x	--libdir=/%{_lib} \
    --enable-cups \
    --enable-dfutool \
    --enable-tools \
    --enable-bccmd \
    --enable-gstreamer \
    --enable-hidd \
    --enable-pand \
    --enable-dund \
    --enable-hid2hci \
    --enable-pcmcia \
    --enable-udevrules \
    --enable-capng
    
%make

%install
rm -rf %{buildroot}
%makeinstall_std rulesdir=%{_sysconfdir}/udev/rules.d udevdir=/lib/udev


mkdir -p %{buildroot}%{_libdir}
mv %{buildroot}/%{_lib}/gstreamer-0.10 %{buildroot}%{_libdir}


cat << EOF > %{buildroot}%{_sysconfdir}/bluetooth/pin
1234
EOF

chmod 600 %{buildroot}%{_sysconfdir}/bluetooth/pin

rm -f %{buildroot}/etc/default/bluetooth %{buildroot}/etc/init.d/bluetooth
for a in dund hidd pand ; do
         install -D -m0644 $RPM_SOURCE_DIR/$a.conf %{buildroot}%{_sysconfdir}/sysconfig/$a
done

rm -rf %{buildroot}/%{_lib}/pkgconfig
install -m644 bluez.pc -D  %{buildroot}%{_libdir}/pkgconfig/bluez.pc

# Remove the cups backend from libdir, and install it in /usr/lib whatever the install
if test -d %{buildroot}/%{_lib}/cups ; then
	install -D -m0755 %{buildroot}/%{_lib}/cups/backend/bluetooth %{buildroot}/usr/lib/cups/backend/bluetooth
	rm -rf %{buildroot}/%{_lib}/cups
fi 
	
mkdir -p %buildroot%{_datadir}/dbus-1/system-services/
install -D -m0644 src/bluetooth.conf %{buildroot}%{_datadir}/dbus-1/system-services/org.bluez.service

mkdir -p %{buildroot}/sbin
cp %{buildroot}%{_bindir}/hidd %{buildroot}/sbin/
cp %{buildroot}%{_sbindir}/bluetoothd %{buildroot}/sbin/

cp test/test-* %{buildroot}%{_bindir}
cp test/simple-agent %{buildroot}%{_bindir}/simple-agent

#install more config files
install -m0644 audio/audio.conf %{buildroot}%{_sysconfdir}/bluetooth/
install -m0644 network/network.conf %{buildroot}%{_sysconfdir}/bluetooth/
install -m0644 input/input.conf %{buildroot}%{_sysconfdir}/bluetooth/
install -m0644 serial/serial.conf %{buildroot}%{_sysconfdir}/bluetooth/

%__mkdir -p %{buildroot}%{_libdir}/alsa-lib/
%__mv %{buildroot}/%{_lib}/alsa-lib/*.so %{buildroot}%{_libdir}/alsa-lib/

# remove unpackaged files
rm -f %{buildroot}/%{_libdir}/*/*.la
rm -f %{buildroot}/%{_lib}/*/*.la

install -d -m0755 %{buildroot}/%{_localstatedir}/lib/bluetooth

# install udev rules while we still use udev
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/udev/rules.d

%clean
rm -fr %{buildroot}


%changelog
* Mon Aug 26 2013 billybot <billybot> 4.101-8pclos2013
- add patches 500-502 and adjust configure options

* Fri Aug 16 2013 billybot <billybot> 4.101-7pclos2013
- update python 2.7

* Sat May 25 2013 Texstar <texstar at gmail.com> 4.101-6pclos2013
- fix udev rule

* Sun Feb 10 2013 pinoc <vogtpet at gmail.com> 4.101-5pclos2013
- fixed wrong path in 97-bluetooth.rules 

* Wed Feb 06 2013 TerryN <terryn94 at gmail.com> 4.101-4pclos2013
- re-instated udev rules file excluded from source

* Sun Dec 30 2012 daniel <meisssw01 at gmail.com> 4.101-3leiche2012
- add build conflicts macro for libusb-compat0.1-static-devel file

* Sat Dec 29 2012 daniel <meisssw01 at gmail.com> 4.101-2leiche2012
- add missing build requires libusb-compat0.1-static-devel file

* Tue Dec 18 2012 daniel <meisssw01 at gmail.com> 4.101-1leiche2012
- upstream tarball

* Thu Jun 23 2011 Texstar <texstar at gmail.com> 4.93-2pclos2011
- remove systemd patch

* Tue Jun 14 2011 Texstar <texstar at gmail.com> 4.93-1pclos2011
- 4.93

* Fri Oct 08 2010 Texstar <texstar at gmail.com> 4.72-1pclos2010
- 4.72

* Tue Jul 20 2010 Texstar <texstar at gmail.com> 4.69-1pclos2010
- 4.69

* Thu Apr 29 2010 pcserver <pcserver at hush.com> 4.64-1pclos2010
- 4.64

* Sat Mar 27 2010 Texstar <texstar at gmail.com> 4.63-1pclos210
 -4.63

* Wed Feb 10 2010 Texstar <texstar at gmail.com> 4.60-1pclos2010
- update to 4.60


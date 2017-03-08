Name:           ixo-usb-jtag
Version:        0.0.1
Release:        1%{?dist}
Summary:        Firmware for USB JTAG programmers based on the Cypress FX2
License:        GPLv2+
URL:            https://github.com/mithro/ixo-usb-jtag
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  sdcc

%description
%{name} firmware allows a Cypress FX2 EZ-USB micro-controller to act like a
USB-Blaster JTAG pod. This allows using existing tools which are compatible
with the USB Blaster.


%prep
%autosetup


%build
%make_build SDCC_PREFIX=sdcc-
sed 's^/lib/firmware/ixo-usb-jtag/^%{_datadir}/%{name}/^' -i scripts/ixo-usb-jtag.rules
sed 's^MODE="666"^TAG+="uaccess"^' -i scripts/ixo-usb-jtag.rules


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 0644 usbjtag-basic.hex %{buildroot}/%{_datadir}/%{name}
install -m 0644 usbjtag-dj_usb.hex %{buildroot}/%{_datadir}/%{name}
install -m 0644 usbjtag-nexys.hex %{buildroot}/%{_datadir}/%{name}
install -m 0644 usbjtag-saxo_l.hex %{buildroot}/%{_datadir}/%{name}
install -m 0644 usbjtag-xpcu_i.hex %{buildroot}/%{_datadir}/%{name}
install -m 0644 usbjtag-xpcu_x.hex %{buildroot}/%{_datadir}/%{name}
install -m 0644 scripts/ixo-usb-jtag.rules \
        -D %{buildroot}%{_prefix}/lib/udev/rules.d/69-ixo-usb-jtag.rules

%files
%license LICENSE.md
%doc README.md
%{_datadir}/%{name}/*.hex
%{_prefix}/lib/udev/rules.d/69-ixo-usb-jtag.rules


%changelog
* Mon Mar  6 2017 mrnuke <mr.nuke.me@gmail.com> - 0.0.1-1
- Initial RPM release

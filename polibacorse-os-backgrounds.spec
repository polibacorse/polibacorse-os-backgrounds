Name: polibacorse-os-backgrounds
Version: 1.0
Release: 1%{?dist}
Summary: Desktop backgrounds for Poliba Corse OS

License: CC-BY-SA and CC-BY and CC0
URL: https://github.com/polibacorse/polibacorse-os-backgrounds

BuildArch: noarch

%description
The polibacorse-os-backgrounds package contains the standard wallpapers for
Poliba Corse OS.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS
%{_datadir}/gnome-background-properties
%{_datadir}/backgrounds/*

%changelog
* Sat Oct 28 2017 Giovanni Grieco <giovanni.grc96@gmail.com> - 1.0
- Initial Release for Poliba Corse OS

* Wed May 24 2017 Ryan Lerch <rlerch@redhat.com> - 1.1-1
- Initial Release

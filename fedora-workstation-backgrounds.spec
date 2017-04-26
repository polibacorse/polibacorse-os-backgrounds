Name: fedora-workstation-backgrounds
Version: 1.0
Release: 1%{?dist}
Summary: Desktop backgrounds packaged with the GNOME desktop

License: CC-BY-SA
URL: https://pagure.io/fedora-design/fedora-workstation-backgrounds
Source0: https://releases.pagure.org/pagure/%{name}-%{version}.tar.gz

BuildArch: noarch

%description
The fedora-workstation-backgrounds packages contains the additional standard
wallpapers for Fedora Workstation.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS README AUTHORS
%{_datadir}/gnome-background-properties
%{_datadir}/backgrounds/*

%changelog
* Wed Apr 26 2017 Ryan Lerch <rlerch@redhat.com> - 1.0-1
- Initial Release

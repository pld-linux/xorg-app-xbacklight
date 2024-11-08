Summary:	xbacklight application - adjust backlight brightness using RandR extension
Summary(pl.UTF-8):	Aplikacja xbacklight - zmiana jasności podświetlenia obrazu poprzez RandR
Name:		xorg-app-xbacklight
Version:	1.2.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xbacklight-%{version}.tar.xz
# Source0-md5:	938676425d6478d824f3c7831606a255
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
# xcb xcb-randr >= 1.2
BuildRequires:	libxcb-devel >= 1.2
BuildRequires:	tar >= 1:1.22
# xcb-atom xcb-aux
BuildRequires:	xcb-util-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	libxcb >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xbacklight is used to adjust the backlight brightness using RandR
extension where supported. It finds all outputs on the X server
supporting backlight brightness control and changes them all in the
same way.

%description -l pl.UTF-8
xbacklight służy do zmiany jasności podświetlenia ekranu przy użyciu
rozszerzenia RandR, o ile jest to obslugiwane. Znajduje wszystkie
wyjścia serwera X obsługujące sterowanie jasnością podświetlenia i
zmienia je w ten sam sposób.

%prep
%setup -q -n xbacklight-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xbacklight
%{_mandir}/man1/xbacklight.1*

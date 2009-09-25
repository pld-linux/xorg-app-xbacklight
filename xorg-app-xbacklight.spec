Summary:	xbacklight application - adjust backlight brightness using RandR extension
Summary(pl.UTF-8):	Aplikacja xbacklight - zmiana jasności podświetlenia obrazu poprzez RandR
Name:		xorg-app-xbacklight
Version:	1.1.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xbacklight-%{version}.tar.bz2
# Source0-md5:	3e39eec6d0fd5c587ca6d55aa7bb8fe1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXrandr-devel >= 1.2.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXrandr >= 1.2.0
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
%doc COPYING
%attr(755,root,root) %{_bindir}/xbacklight
%{_mandir}/man1/xbacklight.1x*

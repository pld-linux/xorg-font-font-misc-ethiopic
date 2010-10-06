Summary:	GohaTibebZemen Ethiopic font
Summary(pl.UTF-8):	Font etiopski GohaTibebZemen
Name:		xorg-font-font-misc-ethiopic
Version:	1.0.2
Release:	1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-misc-ethiopic-%{version}.tar.bz2
# Source0-md5:	bf9879739a9f06dc1980cf16defaa4d9
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.1
BuildRequires:	xorg-util-util-macros >= 1.3
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/OTF
Requires:	%{_fontsdir}/TTF
Obsoletes:	XFree86-fonts-Ethiopic
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GohaTibebZemen Ethiopic font in OTF and TTF formats.

%description -l pl.UTF-8
Font etiopski GohaTibebZemen w formatach OTF i TTF.

%prep
%setup -q -n font-misc-ethiopic-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--build=%{_host} \
	--host=%{_host} \
	--with-otf-fontdir=%{_fontsdir}/OTF \
	--with-ttf-fontdir=%{_fontsdir}/TTF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst OTF
fontpostinst TTF

%postun
fontpostinst OTF
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_fontsdir}/OTF/GohaTibebZemen.otf
%{_fontsdir}/TTF/GohaTibebZemen.ttf

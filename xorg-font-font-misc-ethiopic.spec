Summary:	GohaTibebZemen Ethiopic font
Summary(pl.UTF-8):	Font etiopski GohaTibebZemen
Name:		xorg-font-font-misc-ethiopic
Version:	1.0.4
Release:	2
License:	MIT
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-misc-ethiopic-%{version}.tar.bz2
# Source0-md5:	4ee18ab6c1edf636b8e75b73e6037371
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.2
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
%if "%{_host_cpu}" != "x32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-otf-fontdir=%{_fontsdir}/OTF \
	--with-ttf-fontdir=%{_fontsdir}/TTF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MKFONTSCALE=/bin/true \
	MKFONTDIR=/bin/true

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
%doc COPYING ChangeLog README.md
%{_fontsdir}/OTF/GohaTibebZemen.otf
%{_fontsdir}/TTF/GohaTibebZemen.ttf

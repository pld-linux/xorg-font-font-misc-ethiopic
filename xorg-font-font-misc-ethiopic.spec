Summary:	GohaTibebZemen Ethiopic font
Summary(pl):	Font etiopski GohaTibebZemen
Name:		xorg-font-font-misc-ethiopic
Version:	0.99.2
Release:	0.1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/font/font-misc-ethiopic-%{version}.tar.bz2
# Source0-md5:	1d1af126018d683bf67822835a3c38a7
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	pkgconfig >= 1:0.19
# temporary
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/OTF
Requires:	%{_fontsdir}/TTF
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GohaTibebZemen Ethiopic font in OTF and TTF formats.

%description -l pl
Font etiopski GohaTibebZemen w formatach OTF i TTF.

%prep
%setup -q -n font-misc-ethiopic-%{version}

# copy-pasto
sed -i -e '38s/fontdir/ttf-fontdir/;45s/fontdir/otf-fontdir/' configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
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
%doc COPYING ChangeLog
%{_fontsdir}/OTF/GohaTibebZemen.otf
%{_fontsdir}/TTF/GohaTibebZemen.ttf

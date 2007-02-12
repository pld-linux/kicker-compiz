
%define		_kdever	3.5.4
Summary:	kicker-compiz - pager to work with compiz
Summary(pl.UTF-8):	kicker-compiz - pager działający z compizem
Name:		kicker-compiz
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.kde-apps.org/content/files/46021-%{name}-%{_kdever}.tar.gz
# Source0-md5:	54042121de0d2dbdba33befce64b68bb
URL:		http://www.kde-apps.org/content/show.php?content=46021
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:%{_kdever}
BuildRequires:	kdebase-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a modified pager applet for kicker to make it work with
compiz. More generally, it is intended to work with window managers
that use the concept of "large desktops" instead of "multiple virtual
desktops" as kwin does exclusively.

%description -l pl.UTF-8
Jest to pager dla kickera zmodyfikowany tak, by działał razem z
compizem. Ogólniej ma działać w zarządcach okien opierających się na
idei "dużych biurek" zamiast na "wielu wirtualnych biurkach" tak jak
to robi kwin.

%prep
%setup -q -n %{name}-%{_kdever}

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/compizpager_panelapplet.so
%{_libdir}/kde3/compizpager_panelapplet.la
%{_datadir}/apps/kicker/applets/compizpagerapplet.desktop

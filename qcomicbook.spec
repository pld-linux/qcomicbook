Summary:	comic book viewer
Summary(pl.UTF-8):	czytnik komiksów
Name:		qcomicbook
Version:	0.4.0
Release:	0.1
License:	GPL v2
Group:		Development/Tools
Source0:	http://linux.bydg.org/~yogin/qcomicbook/%{name}-%{version}.tar.gz
# Source0-md5:	84345be534ec9fd438118541e09514a7
URL:		http://linux.bydg.org/~yogin/
BuildRequires:  Qt3Support-devel
BuildRequires:  QtCore-devel
BuildRequires:  QtGui-devel
BuildRequires:  qt4-build
BuildRequires:  qt4-linguist
BuildRequires:  qt4-qmake
BuildRequires:  rpmbuild(macros) >= 1.129
Suggests:	tar
Suggests:	unace
Suggests:	unrar
Suggests:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QComicBook is a viewer for comic book archives containing
jpeg/png/xpm/gif images, which aims at convenience and simplicity.
Features include: automatic decompression, full-screen mode, two-pages
viewing, japanese mode, thumbnails view, page scaling, mouse or keyboard
navigation etc.

#%description -l pl.UTF-8

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
#	kde_htmldir=%{_kdedocdir} \
#	kde_libs_htmldir=%{_kdedocdir} \
	shelldesktopdir=%{_desktopdir}

#%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

#-f %{name}.lang
%files 
%defattr(644,root,root,755)
%doc AUTHORS Changelog COPYING INSTALL NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/qcomicbook
#%{_datadir}/apps/kontrollerlab
#%{_datadir}/mimelnk/application/x-kontrollerlab.desktop
#%{_desktopdir}/kde/kontrollerlab.desktop
#%{_iconsdir}/*/*/apps/%{name}.png
#%{_iconsdir}/*/*/actions/dbg*.png

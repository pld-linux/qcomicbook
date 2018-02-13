#
# TODO: - install *.qm files in /usr/share/locale
#	- fix locales install
#
%define		qt_ver	5.4.0
Summary:	A viewer for comic book archives (rar, cbr, cbz, zip, ace, cba, tar.gz, tar.bz2)
Summary(pl.UTF-8):	Czytnik komiksów (rar, cbr, cbz, zip, ace, cba, tar.gz, tar.bz2)
Name:		qcomicbook
Version:	0.9.1
Release:	1
License:	GPL v2+
Group:		X11/Amusements
Source0:	https://github.com/stolowski/QComicBook/archive/%{version}.tar.gz
# Source0-md5:	d8762ff0698652cd2c383dbaa30cc132
Patch0:		%{name}-desktop.patch
URL:		https://github.com/stolowski/QComicBook
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5PrintSupport-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt_ver}
BuildRequires:	cmake >= 2.6
BuildRequires:	pkgconfig
BuildRequires:	poppler-qt5-devel >= 0.12.4
BuildRequires:	qt5-build >= %{qt_ver}
BuildRequires:	qt5-linguist >= %{qt_ver}
BuildRequires:	qt5-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5PrintSupport >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	Qt5X11Extras >= %{qt_ver}
Requires:	poppler-qt5 >= 0.12.4
Suggests:	tar
Suggests:	unace
Suggests:	unrar
Suggests:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QComicBook is a viewer for comic book archives containing
jpeg/png/xpm/gif images, which aims at convenience and simplicity.
Features include: automatic decompression, full-screen mode, two-pages
viewing, japanese mode, thumbnails view, page scaling, mouse or
keyboard navigation etc.

QComicBook requires zip/unzip, rar/unrar, tar with gzip+bzip2 support
and unace to handle archives.

%description -l pl.UTF-8
QComicBook jest wygodnym i łatwym w obsłudze czytnikiem komiksów
składających się z obrazów jpeg/png/xpm/gif. Posiada on funkcje:
autumatyczna dekompresja, tryb pełnoekranowy, podgląd dwóch stron,
tryp japoński, podgląd miniatur, skalowanie strony, nawigacja za
pomocą myszki i klawiatury itp.

QCoomiBook wymaga programów zip/unzip, rar/unrar, tar wraz z
gzip-bzip2 i unace do obsługi archiwów.

%prep
%setup -q -n QComicBook-%{version}
%patch0 -p1

%build
%cmake .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	shelldesktopdir=%{_desktopdir}

cp -a data/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -a data/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

#%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

#-f %{name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS TODO
%attr(755,root,root) %{_bindir}/qcomicbook
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

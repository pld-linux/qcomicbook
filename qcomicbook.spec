#
# Remember : adapter will cut Summary and broke this spec file
Summary:	A viewer for comic book archives (rar, cbr, cbz, zip, ace, cba, tar.gz, tar.bz2)
Summary(pl.UTF-8):	Czytnik komiksów (rar, cbr, cbz, zip, ace, cba, tar.gz, tar.bz2)
Name:		qcomicbook
Version:	0.5.0
Release:	1
License:	GPL v2+
Group:		X11/Amusements
Source0:	http://qcomicbook.linux-projects.net/releases/%{name}-%{version}.tar.gz
# Source0-md5:	590f981df476195f1cd71a16c0fff5e6
Patch0:		%{name}-desktop.patch
URL:		http://qcomicbook.linux-projects.net/
BuildRequires:	Qt3Support-devel >= 4.3.0
BuildRequires:	QtCore-devel >= 4.3.0
BuildRequires:	QtGui-devel >= 4.3.0
BuildRequires:	cmake
BuildRequires:	qt4-build >= 4.3.0
BuildRequires:	qt4-qmake >= 4.3.0
BuildRequires:	rpmbuild(macros) >= 1.129
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
%setup -q
%patch0 -p1

%build
%cmake . \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

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

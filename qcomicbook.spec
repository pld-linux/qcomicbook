Summary:	A viewer for comic book archives (rar, cbr, cbz, zip, ace, cba,
tar.gz, tar.bz2)
Summary(pl.UTF-8):	Czytnik komiksów (rar, cbr, cbz, zip, ace, cba, tar.gz,
tar.bz2)
Name:		qcomicbook
Version:	0.4.1
Release:	0.1
License:	GPL v2+
Group:		X11/Amusements
Source0:	http://linux.bydg.org/~yogin/qcomicbook/%{name}-%{version}.tar.gz
# Source0-md5:	b9ffbb21198d4c292407184546770242
Patch0:		%{name}-desktop.patch
URL:		http://linux.bydg.org/~yogin/
BuildRequires:	Qt3Support-devel >= 4.2.0
BuildRequires:	QtCore-devel >= 4.2.0
BuildRequires:	QtGui-devel >= 4.2.0
BuildRequires:	qt4-build >= 4.2.0
#BuildRequires:	qt4-linguist >= 4.2.0
BuildRequires:	qt4-qmake >= 4.2.0
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	shelldesktopdir=%{_desktopdir}

cp -a fedora/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -a fedora/%{name}.png $RPM_BUILD_ROOT%{_pixmapsdir}

#%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

#-f %{name}.lang
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/qcomicbook
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

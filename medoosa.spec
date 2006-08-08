Summary:	Generates UML diagrams from C++ sources
Summary(pl):	Generowanie diagramów UML ze ¼róde³ C++
Name:		medoosa
Version:	1.1
Release:	1
License:	GPL
Group:		Development/Tools
# from:		http://dl.sourceforge.net/medoosa/medoosa-1.1-1.src.rpm
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	9dc6b500efa3993a3bb83954ffb03d6f
Patch0:		%{name}-opt.patch
URL:		http://medoosa.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ccdoc
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-progs
Requires:	ccdoc
Requires:	dia
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Medoosa is a documentation tool for C++ that can produce UML class
diagrams including generalizations and associations. Corrections can
be made interactively in a diagram editor (Dia) and are fed back into
the source as Javadoc-style comments. At this time, the layout must
still be done by hand.

%description -l pl
Medoosa to narzêdzie do dokumentacji dla C++, potrafi±ce wygenerowaæ
diagramy UML dla klas w³±cznie z uogólnieniami i powi±zaniami.
Poprawki mog± byæ wykonywane interaktywnie w edytorze diagramów (Dia)
i s± nanoszone z powrotem do ¼róde³ jako komentarze w stylu Javadoc.
Aktualnie rozmieszczenie diagramów musi byæ wykonywane rêcznie.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
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
%doc NEWS README THANKS docs/*.{ps,dtd} docs/UXF/*.dtd
%attr(755,root,root) %{_bindir}/medoosa
%dir %{_libdir}/medoosa
%{_libdir}/medoosa/diff-uxf
%{_libdir}/medoosa/patch-ccdoc
%{_libdir}/medoosa/translate
%dir %{_datadir}/medoosa
%{_datadir}/medoosa/dia-uxf.xsl
%{_datadir}/medoosa/uxf-dia.xsl
%{_datadir}/medoosa/uxf-g-dot.xsl
%{_datadir}/medoosa/uxf2metrics.xsl
%{_datadir}/medoosa/mapconvert.pl
%{_datadir}/medoosa/medoosa2.sh
%{_datadir}/medoosa/unflatten2.pl
%{_datadir}/medoosa/xsltfilter

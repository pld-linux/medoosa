Name:		medoosa
Version:	1.1
Release:	1
Summary:	Generates UML diagrams from C++ sources.
License:	GPL
Group:		Development/Tools
URL:		http://medoosa.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Source0:	%{name}-%{version}.tar.gz
Requires:	ccdoc
Requires:	dia
Requires:	libxml2
Requires:	libxslt
BuildRequires:	ccdoc

%description
Medoosa is a documentation tool for C++ that can produce UML class
diagrams including generalizations and associations. Corrections can
be made interactively in a diagram editor (Dia) and are fed back into
the source as Javadoc-style comments. At this time, the layout must
still be done by hand.

%prep
%setup -q


%build
./configure --prefix=%{_prefix}
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT/%{_prefix}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/medoosa
%{_libdir}/medoosa/diff-uxf
%{_libdir}/medoosa/patch-ccdoc
%{_libdir}/medoosa/translate
%{_datadir}/medoosa/dia-uxf.xsl
%{_datadir}/medoosa/uxf-dia.xsl
%{_datadir}/medoosa/uxf-g-dot.xsl
%{_datadir}/medoosa/uxf2metrics.xsl
%{_datadir}/medoosa/mapconvert.pl
%{_datadir}/medoosa/medoosa2.sh
%{_datadir}/medoosa/unflatten2.pl
%{_datadir}/medoosa/xsltfilter
%doc COPYING NEWS README THANKS
%doc docs/*.ps
%doc docs/*.dtd
%doc docs/UXF/*.dtd

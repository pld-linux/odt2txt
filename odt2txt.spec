Summary:	A simple converter from OpenDocument Text to plain text
Summary(pl.UTF-8):	Prosty konwerter z formatu OpenDocument Text do zwykłego tekstu
Name:		odt2txt
Version:	0.4
Release:	1
License:	GPL v2
Group:		Applications/Publishing
Source0:	http://stosberg.net/odt2txt/%{name}-%{version}.tar.gz
# Source0-md5:	6fe3bd261ce2dde2810244bbe969bbc5
URL:		http://stosberg.net/odt2txt/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
odt2txt extracts the text out of OpenDocument Texts. It is small, fast
and portable, can output the document in your console encoding, and
has very few external dependencies.

%description -l pl.UTF-8
odt2txt wydobywa tekst z formatu OpenDocument Text. Jest mały, szybki
i przenośny. Obsługuje różne kodowania wyjściowe i ma niewiele
zewnętrznych zależności.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/odt2txt
%{_mandir}/man1/odt2txt.1*

Summary:	A simple converter from OpenDocument Text to plain text
Summary(pl.UTF-8):	Prosty konwerter z formatu OpenDocument Text do zwykłego tekstu
Name:		odt2txt
Version:	0.5
Release:	1
License:	GPL v2
Group:		Applications/Publishing
Source0:	https://github.com/dstosberg/odt2txt/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8154dc7f2909dad6939d209695e62379
URL:		http://stosberg.net/odt2txt/
BuildRequires:	pkgconfig
BuildRequires:	libzip-devel
BuildRequires:	zlib-devel
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
	CFLAGS="%{rpmcflags} -DHAVE_LIBZIP %(pkg-config --cflags libzip)" \
	HAVE_LIBZIP=1 \
	LDFLGS="%{rpmldflags}" \
	LIBS="%(pkg-config --libs libzip) -lz"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HAVE_LIBZIP=1 \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/odt2txt
%{_mandir}/man1/odt2txt.1*

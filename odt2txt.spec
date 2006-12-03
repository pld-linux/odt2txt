Summary:	A simple converter from OpenDocument Text to plain text
Summary(pl):	Prosty konwerter z formatu OpenDocument Text do zwyk³ego tekstu
Name:		odt2txt
Version:	0.1
Release:	1
License:	GPL v2
Group:		Applications/Publishing
Source0:	http://stosberg.net/odt2txt/%{name}-%{version}.tar.gz
# Source0-md5:	5b9e27a50f86c733172cdc456d33e3ed
URL:		http://stosberg.net/odt2txt/
Requires:	libiconv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
odt2txt extracts the text out of OpenDocument Texts. It is small, fast
and portable, can output the document in your console encoding, and
has very few external dependencies.

%description -l pl
odt2txt wydobywa tekst z fotmatu OpenDocument Text. Jest ma³y, szybki
i przeno¶ny. Obs³uguje ró¿ne kodowania wyj¶ciowe i ma niewiele
zewnêtrznych zale¿no¶ci.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

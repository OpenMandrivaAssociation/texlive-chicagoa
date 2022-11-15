Name:		texlive-chicagoa
Version:	52567
Release:	1
Summary:	"Chicago" bibliography style with annotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chicagoa
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chicagoa.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a modification of the author's chicago style, to
support an 'annotation' field in bibliographies.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/chicagoa

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

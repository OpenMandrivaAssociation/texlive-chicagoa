%global tl_name chicagoa
%global tl_revision 76790

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Chicago bibliography style with annotations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/chicagoa.bst
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chicagoa.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a modification of the author's chicago style, to support an
'annotation' field in bibliographies.


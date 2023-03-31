Name:		texlive-stickstoo
Version:	60793
Release:	2
Summary:	A reworking of STIX2
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stickstoo
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stickstoo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stickstoo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
SticksToo is a reworking of the STIX2 fonts with support files
focussing on enhancements of support for LaTeX users wishing to
be able to access more of its features. A companion addition to
the newtxmath package (version 1.55) provides a matching math
package using STIX2 letters (Roman and Greek) with newtxmath
symbols.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/stickstoo
%{_texmfdistdir}/fonts/vf/public/stickstoo
%{_texmfdistdir}/fonts/type1/public/stickstoo
%{_texmfdistdir}/fonts/tfm/public/stickstoo
%{_texmfdistdir}/fonts/map/dvips/stickstoo
%{_texmfdistdir}/fonts/enc/dvips/stickstoo
%{_texmfdistdir}/fonts/afm/public/stickstoo
%doc %{_texmfdistdir}/doc/fonts/stickstoo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

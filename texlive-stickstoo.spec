%global tl_name stickstoo
%global tl_revision 77682
%global tl_version 1.036

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A reworking of STIX2
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/stickstoo
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stickstoo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stickstoo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
SticksToo is a reworking of the STIX2 fonts with support files focussing
on enhancements of support for LaTeX users wishing to be able to access
more of its features. A companion addition to the newtxmath package
(version 1.55) provides a matching math package using STIX2 letters
(Roman and Greek) with newtxmath symbols.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from stickstoo:
Map SticksTooText.map
TL_DROPIN_EOF

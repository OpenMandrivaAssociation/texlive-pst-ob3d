%global tl_name pst-ob3d
%global tl_revision 54514

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.22
Release:	%{tl_revision}.1
Summary:	Three dimensional objects using PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-ob3d
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ob3d.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ob3d.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ob3d.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package uses PSTricks to provide basic three-dimensional objects. As
yet, only cubes (which can be deformed to rectangular parallelipipeds)
and dies (which are only a special kind of cubes) are defined.


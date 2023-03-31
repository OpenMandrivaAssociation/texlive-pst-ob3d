Name:		texlive-pst-ob3d
Version:	54514
Release:	2
Summary:	Three dimensional objects using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-ob3d
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ob3d.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ob3d.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ob3d.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package uses PSTricks to provide basic three-dimensional
objects. As yet, only cubes (which can be deformed to
rectangular parallelipipeds) and dies (which are only a special
kind of cubes) are defined.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-ob3d
%{_texmfdistdir}/tex/latex/pst-ob3d
%doc %{_texmfdistdir}/doc/generic/pst-ob3d
#- source
%doc %{_texmfdistdir}/source/generic/pst-ob3d

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

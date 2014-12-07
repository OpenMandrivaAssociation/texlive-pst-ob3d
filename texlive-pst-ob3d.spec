# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-ob3d
# catalog-date 2008-08-23 00:25:16 +0200
# catalog-license lppl
# catalog-version 0.21
Name:		texlive-pst-ob3d
Version:	0.21
Release:	9
Summary:	Three dimensional objects using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-ob3d
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ob3d.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ob3d.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ob3d.source.tar.xz
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
%{_texmfdistdir}/tex/generic/pst-ob3d/pst-ob3d.tex
%{_texmfdistdir}/tex/latex/pst-ob3d/pst-ob3d.sty
%doc %{_texmfdistdir}/doc/generic/pst-ob3d/Changes
%doc %{_texmfdistdir}/doc/generic/pst-ob3d/README
%doc %{_texmfdistdir}/doc/generic/pst-ob3d/pst-ob3d.pdf
#- source
%doc %{_texmfdistdir}/source/generic/pst-ob3d/Makefile
%doc %{_texmfdistdir}/source/generic/pst-ob3d/pst-ob3d.dtx
%doc %{_texmfdistdir}/source/generic/pst-ob3d/pst-ob3d.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.21-2
+ Revision: 755375
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.21-1
+ Revision: 719371
- texlive-pst-ob3d
- texlive-pst-ob3d
- texlive-pst-ob3d
- texlive-pst-ob3d


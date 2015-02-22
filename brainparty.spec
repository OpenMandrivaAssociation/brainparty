# spec is based on OpenSUSE and MIB work

Name:		brainparty
Version:	0.61
Release:	2
Summary:	Brain-stretching game with 36 minigames
License:	GPLv3
Group:		Games/Puzzles
Url:		https://launchpad.net/brainparty
Source0:	http://launchpad.net/brainparty/trunk/0.61/+download/%{name}%{version}.tar.gz
Source1:	%{name}-wrapper.sh
Source2:	%{name}.desktop
Source3:	%{name}.png
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(SDL_gfx)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(glu)

%description
Brain Party is a puzzle-solving, brain-stretching game that comes with
36 minigames designed to push your brain to its limits, testing memory,
logic, mathematics, reactions and more.

%prep
%setup -q -n %{name}
sed -i -e "s/CXXFLAGS =/CXXFLAGS = %{optflags}/g" Makefile

%build
%make

%install
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__install -D -m 644 Content/* %{buildroot}%{_datadir}/%{name}/

# Install binary and wrapper
%__install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}-bin
%__install -D -m 755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

%__mkdir_p %{buildroot}%{_datadir}/applications/
%__install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/
%__mkdir_p %{buildroot}%{_datadir}/pixmaps/
%__install -D -m 644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/


%files
%doc README COPYING CREDITS
%{_bindir}/%{name}
%{_bindir}/%{name}-bin
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png




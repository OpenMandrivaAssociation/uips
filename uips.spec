%define name	uips
%define version	20100823
%define release	%mkrel 1

Name:		%{name}
Summary:	Universal IPS create/apply utility
Version:	%{version}
Release:	%{release}
Source0:	http://www.neillcorlett.com/downloads/uips_source.zip
URL:		http://www.neillcorlett.com/uips/

Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-%{version}
License:	GPLv3+

%description
UIPS is a command-line based utility for creating or applying IPS patches.
IPS is a fairly simple patch file format which stores the differences between
two binary files.

%prep
%setup -q -c

%build
gcc %{optflags} %{ldflags} -o %{name} %{name}.c

%install
rm -rf %{buildroot}
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc uips.txt
%{_bindir}/%{name}

Name:		libkeepalive
Version:	0.3
Release:	1
Summary:	Enable TCP keepalive in dynamic binaries
URL:		http://libkeepalive.sourceforge.net/
BuildRequires:  gcc
License:	MIT
Source0:	https://cfhcable.dl.sourceforge.net/project/%{name}/%{name}/0.3/%{name}-0.3.tar.gz

# All patches sent to the upstream maintainer directly via email.
Patch1:		0002-test-test.c-Whitespace-cleanup.patch
Patch2:		0003-test-Implement-self-test-functionality.patch
Patch3:		0004-Makefile-Make-self-test-accessible-by-make-test.patch
Patch4:		0005-Makefile-Allow-setting-custom-compiler-flags.patch
%description
libkeepalive is a library that enables tcp keepalive features in glibc based
binary dynamic executables, without any change in the original program.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%check
make test

%install
install -p -m 0755 -D src/libkeepalive.so %{buildroot}%{_libdir}/libkeepalive.so

%files
%license LICENSE
%doc README
%{_libdir}/libkeepalive.so

%changelog
* Thu Aug 13 2020 tuShenmei <tushenmei@huawei.com> - 0.3-1
- package init

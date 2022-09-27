#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perftest
Version  : 4.5.0.17
Release  : 15
URL      : https://github.com/linux-rdma/perftest/releases/download/v4.5-0.17/perftest-4.5-0.17.g6f25f23.tar.gz
Source0  : https://github.com/linux-rdma/perftest/releases/download/v4.5-0.17/perftest-4.5-0.17.g6f25f23.tar.gz
Summary  : IB Performance tests
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GPL-2.0
Requires: perftest-bin = %{version}-%{release}
Requires: perftest-license = %{version}-%{release}
BuildRequires : pkgconfig(libpci)
BuildRequires : rdma-core-dev

%description
gen3 uverbs microbenchmarks

%package bin
Summary: bin components for the perftest package.
Group: Binaries
Requires: perftest-license = %{version}-%{release}

%description bin
bin components for the perftest package.


%package license
Summary: license components for the perftest package.
Group: Default

%description license
license components for the perftest package.


%prep
%setup -q -n perftest-4.5
cd %{_builddir}/perftest-4.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664294667
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1664294667
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perftest
cp %{_builddir}/perftest-4.5/COPYING %{buildroot}/usr/share/package-licenses/perftest/5a38d18fd19a72d8bc2fa1ab1578cea8e434750a
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ib_atomic_bw
/usr/bin/ib_atomic_lat
/usr/bin/ib_read_bw
/usr/bin/ib_read_lat
/usr/bin/ib_send_bw
/usr/bin/ib_send_lat
/usr/bin/ib_write_bw
/usr/bin/ib_write_lat
/usr/bin/raw_ethernet_burst_lat
/usr/bin/raw_ethernet_bw
/usr/bin/raw_ethernet_fs_rate
/usr/bin/raw_ethernet_lat
/usr/bin/run_perftest_loopback
/usr/bin/run_perftest_multi_devices

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perftest/5a38d18fd19a72d8bc2fa1ab1578cea8e434750a

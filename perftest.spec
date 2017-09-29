#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perftest
Version  : 4.1.0.2.770623
Release  : 1
URL      : https://github.com/linux-rdma/perftest/releases/download/V4.1-0.2/perftest-4.1-0.2.g770623f.tar.gz
Source0  : https://github.com/linux-rdma/perftest/releases/download/V4.1-0.2/perftest-4.1-0.2.g770623f.tar.gz
Summary  : IB Performance tests
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause GPL-2.0 later
Requires: perftest-bin
BuildRequires : rdma-core-dev

%description
gen3 uverbs microbenchmarks

%package bin
Summary: bin components for the perftest package.
Group: Binaries

%description bin
bin components for the perftest package.


%prep
%setup -q -n perftest-4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1506722282
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1506722282
rm -rf %{buildroot}
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

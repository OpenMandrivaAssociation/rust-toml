%bcond_without check
%global debug_package %{nil}

%global crate toml

Name:           rust-%{crate}
Version:        0.5.8
Release:        2
Summary:        Native Rust encoder and decoder of TOML-formatted files and streams

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/toml
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Native Rust encoder and decoder of TOML-formatted files and streams. Provides
implementations of the standard Serialize/Deserialize traits for TOML data to
facilitate deserializing and serializing Rust structures.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+indexmap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+indexmap-devel %{_description}

This package contains library source intended for building other packages
which use "indexmap" feature of "%{crate}" crate.

%files       -n %{name}+indexmap-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+preserve_order-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+preserve_order-devel %{_description}

This package contains library source intended for building other packages
which use "preserve_order" feature of "%{crate}" crate.

%files       -n %{name}+preserve_order-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

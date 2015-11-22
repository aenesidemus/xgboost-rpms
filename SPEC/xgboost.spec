Summary:            Large-scale and Distributed Gradient Boosting (GBDT, GBRT or GBM) Library
Name:               xgboost
Version:            0.40
Release:            1%{?dist}
License:            ASL 2.0
Group:              System Environment/Base
Source:             %{name}-%{version}.zip
Patch0:             xgboost.patch
URL:                http://dmlc.ml

%description
An optimized general purpose gradient boosting library.The library is
parallelized, and also provides an optimized distributed version.
It implements machine learning algorithm under gradient boosting
framework, including generalized linear model and gradient boosted
regression tree (GBDT). XGBoost can also also distributed and scale
to Terascale data.

%prep
%setup
%patch0 -p0

%build
make

%install
install -m 755 -d %{buildroot}/%{_bindir}
%make_install

%files
%{_bindir}/xgboost


Name: nodeview
Version: 1.0.1
Release: 1-1
Summary: darkkazma nodeview

Group: System Enviroment/Daemons
Vendor: darkkazma
License: Commercial

%description
This Package will install darkkazma nodeview

%define _builddir ./
%define _rpmdir ./
%define _prefix /usr/service
$define _build_name_frt %%{name}-%%{version}-%%{release}%{dist}.%%{arch}.rpm


%files
%{_prefix}/nodeview

%exlcude %{_prefix}/nodeview/nodeview.spec
%exclude %{_prefix}/nodeview/test

%install
%{__mkdir} -p %{buildroot}%{_prefix}/nodeview
%{__cp} -Rp ./* %{buildroot}%{_prefix}/nodeview


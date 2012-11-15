# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       sdk-webapp

# >> macros
# << macros

Summary:    Mer SDK manager
Version:    0.2.8
Release:    1
Group:      Development/Languages/Ruby
License:    GPLv2+
Source0:    sdk-webapp.tar.bz2
Source1:    sdk-webapp.service
Source100:  sdk-webapp.yaml
Requires:   sdk-webapp-bundle

%description
Allows web-based management of the Mer SDK. Adds toolchains, targets etc


%prep
%setup -q -n src

# >> setup
# << setup

%build
# >> build pre
# << build pre


make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
mkdir -p %{buildroot}/usr/lib/systemd/user/
cp %{_sourcedir}/%{name}.service %{buildroot}/usr/lib/systemd/user/
# << install post


%post
# >> post
/bin/ln -sf /usr/lib/systemd/user/%{name}.service %{_sysconfdir}/systemd/system/multi-user.target.wants/
systemctl --system daemon-reload
systemctl start %{name}.service
# << post

%postun
# >> postun
rm %{_sysconfdir}/systemd/system/multi-user.target.wants/%{name}.service
systemctl --system daemon-reload
# << postun

%files
%defattr(-,root,root,-)
%{_libdir}/%{name}-bundle/
%{_libdir}/systemd/user/%{name}.service
# >> files
# << files

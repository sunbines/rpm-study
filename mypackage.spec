Name:           mypackage
Version:        1.0
Release:        1%{?dist}
Summary:        A sample RPM package for demonstration
License:        MIT
Group:          Development/Tools
#Source0:        %{name}-%{version}.tar.gz

%description
This is a sample RPM package for demonstrating scriptlets such as %pre, %post, %preun, and %postun.

%prep
echo "Preparing the package"

%build
echo "Building the package"

%install
mkdir -p %{buildroot}/opt/mypackage
echo "This is my package content." > %{buildroot}/opt/mypackage/file.txt

%files
/opt/mypackage

%pre
if [ "$1" -eq 1 ]; then
    echo "-----------------------"
    echo "RPM is getting installed"
    echo "Put your script here"
    echo "-----------------------"
elif [ "$1" -eq 2 ]; then
    echo "-----------------------"
    echo "RPM is getting upgraded"
    echo "Put your script here"
    echo "-----------------------"
fi

%post
if [ "$1" -eq 1 ]; then
    echo "-----------------------"
    echo "RPM is getting installed"
    echo "Put your script here"
    echo "-----------------------"
elif [ "$1" -eq 2 ]; then
    echo "-----------------------"
    echo "RPM is getting upgraded"
    echo "Put your script here"
    echo "-----------------------"
fi

%preun
if [ "$1" -eq 1 ]; then
    echo "-----------------------"
    echo "RPM is getting upgraded"
    echo "Put your script here which will be called when this rpm is removed"
    echo "-----------------------"
elif [ "$1" -eq 0 ]; then
    echo "--------------------"
    echo "RPM is getting removed/uninstalled"
    echo "Put your script here which will be called before uninstallation of this rpm"
    echo "--------------------"
fi

%postun
if [ "$1" -eq 1 ]; then
    echo "-----------------------"
    echo "RPM is getting upgraded"
    echo "Put your script here which will be called when this rpm is removed"
    echo "-----------------------"
elif [ "$1" -eq 0 ]; then
    echo "--------------------"
    echo "RPM is getting removed/uninstalled"
    echo "Put your script here which will be called after uninstallation of this rpm"
    echo "--------------------"
fi


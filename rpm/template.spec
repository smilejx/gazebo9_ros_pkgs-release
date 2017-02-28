Name:           ros-indigo-gazebo-msgs
Version:        2.4.13
Release:        0%{?dist}
Summary:        ROS gazebo_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://gazebosim.org/tutorials?cat=connect_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-trajectory-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-trajectory-msgs

%description
Message and service data structures for interacting with Gazebo from ROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Feb 28 2017 John Hsu <hsu@osrfoundation.org> - 2.4.13-0
- Autogenerated by Bloom

* Mon Nov 28 2016 John Hsu <hsu@osrfoundation.org> - 2.4.12-0
- Autogenerated by Bloom

* Thu Jul 14 2016 John Hsu <hsu@osrfoundation.org> - 2.4.11-0
- Autogenerated by Bloom

* Thu Feb 25 2016 John Hsu <hsu@osrfoundation.org> - 2.4.10-0
- Autogenerated by Bloom

* Sun Aug 16 2015 John Hsu <hsu@osrfoundation.org> - 2.4.9-0
- Autogenerated by Bloom

* Tue Mar 17 2015 John Hsu <hsu@osrfoundation.org> - 2.4.8-0
- Autogenerated by Bloom

* Thu Dec 18 2014 John Hsu <hsu@osrfoundation.org> - 2.4.7-1
- Autogenerated by Bloom

* Mon Dec 15 2014 John Hsu <hsu@osrfoundation.org> - 2.4.7-0
- Autogenerated by Bloom

* Mon Sep 01 2014 John Hsu <hsu@osrfoundation.org> - 2.4.6-0
- Autogenerated by Bloom

* Mon Aug 18 2014 John Hsu <hsu@osrfoundation.org> - 2.4.5-0
- Autogenerated by Bloom


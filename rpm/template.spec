Name:           ros-lunar-gazebo-ros-pkgs
Version:        2.7.4
Release:        1%{?dist}
Summary:        ROS gazebo_ros_pkgs package

Group:          Development/Libraries
License:        BSD,LGPL,Apache 2.0
URL:            http://gazebosim.org/tutorials?cat=connect_ros
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-gazebo-dev
Requires:       ros-lunar-gazebo-msgs
Requires:       ros-lunar-gazebo-plugins
Requires:       ros-lunar-gazebo-ros
BuildRequires:  ros-lunar-catkin

%description
Interface for using ROS with the Gazebo simulator.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Tue Feb 13 2018 Jose Luis Rivero <jrivero@osrfoundation.org> - 2.7.4-1
- Autogenerated by Bloom

* Tue Feb 13 2018 Jose Luis Rivero <jrivero@osrfoundation.org> - 2.7.4-0
- Autogenerated by Bloom

* Fri Apr 28 2017 Jose Luis Rivero <jrivero@osrfoundation.org> - 2.7.1-0
- Autogenerated by Bloom


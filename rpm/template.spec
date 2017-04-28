Name:           ros-lunar-gazebo-plugins
Version:        2.7.1
Release:        0%{?dist}
Summary:        ROS gazebo_plugins package

Group:          Development/Libraries
License:        BSD, Apache 2.0
URL:            http://gazebosim.org/tutorials?cat=connect_ros
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-angles
Requires:       ros-lunar-camera-info-manager
Requires:       ros-lunar-cv-bridge
Requires:       ros-lunar-diagnostic-updater
Requires:       ros-lunar-dynamic-reconfigure
Requires:       ros-lunar-gazebo-dev
Requires:       ros-lunar-gazebo-msgs
Requires:       ros-lunar-geometry-msgs
Requires:       ros-lunar-image-transport
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-nav-msgs
Requires:       ros-lunar-nodelet
Requires:       ros-lunar-polled-camera
Requires:       ros-lunar-rosconsole
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-rosgraph-msgs
Requires:       ros-lunar-rospy
Requires:       ros-lunar-sensor-msgs
Requires:       ros-lunar-std-msgs
Requires:       ros-lunar-std-srvs
Requires:       ros-lunar-tf
Requires:       ros-lunar-tf2-ros
Requires:       ros-lunar-trajectory-msgs
Requires:       ros-lunar-urdf
BuildRequires:  ros-lunar-angles
BuildRequires:  ros-lunar-camera-info-manager
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-cv-bridge
BuildRequires:  ros-lunar-diagnostic-updater
BuildRequires:  ros-lunar-dynamic-reconfigure
BuildRequires:  ros-lunar-gazebo-dev
BuildRequires:  ros-lunar-gazebo-msgs
BuildRequires:  ros-lunar-geometry-msgs
BuildRequires:  ros-lunar-image-transport
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-nav-msgs
BuildRequires:  ros-lunar-nodelet
BuildRequires:  ros-lunar-polled-camera
BuildRequires:  ros-lunar-rosconsole
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rosgraph-msgs
BuildRequires:  ros-lunar-rospy
BuildRequires:  ros-lunar-rostest
BuildRequires:  ros-lunar-sensor-msgs
BuildRequires:  ros-lunar-std-msgs
BuildRequires:  ros-lunar-std-srvs
BuildRequires:  ros-lunar-tf
BuildRequires:  ros-lunar-tf2-ros
BuildRequires:  ros-lunar-trajectory-msgs
BuildRequires:  ros-lunar-urdf

%description
Robot-independent Gazebo plugins for sensors, motors and dynamic reconfigurable
components.

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
* Fri Apr 28 2017 Jose Luis Rivero <jrivero@osrfoundation.org> - 2.7.1-0
- Autogenerated by Bloom


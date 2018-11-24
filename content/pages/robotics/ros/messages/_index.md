---
author: gbmhunter
date: 2016-12-09 09:47:57+00:00
draft: false
title: Messages
type: page
url: /robotics/ros/messages
---

# Pre-defined Messages




Sensor-based messages are contained within the directory:



    
    /opt/ros/<ros version>/share/sensor_msgs/




# Defining Custom Messages




ROS messages are defined in .msg files.




An automatic MD5 sum of the .msg file is created and is checked when nodes try and publish/subscribe to topics. Nodes can only communicate when both the message type and MD5 sums match.




NOTE: If you get an error similar to:



    
    /opt/ros/indigo/include/ros/message_traits.h:126:34: error: ‘const class <msg type>’ has no member named ‘__getMD5Sum’




this could be




# The Header




ROS messages may include a special header. This can contain a time stamp and frame ID.




# MD5 Checksums




If the message types are not the same, you will normally get a runtime error on launch similar to:



    
    [ERROR] [1481703140.912974056, 0.100000000]: Client [<node_name>] wants topic <topic_name> to have datatype/md5sum [<path>/cd5e73d190d741a2f92e81eda573aca7], but our version has [<path>/2d3a8cd499b9b4a0249fb98fd05cfa48]. Dropping connection.









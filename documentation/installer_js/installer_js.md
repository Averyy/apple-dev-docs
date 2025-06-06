# Installer JS

**Framework**: Installer JS

Manage and customize the installation and distribution experience.

#### Overview

A distribution definition file defines the install experience for a product. The Installer application opens and interprets distribution definition files to generate the user interface users manipulate to execute and customize a product install.

Distribution definition files contain XML and JavaScript code. The XML code defines the structure of a distribution, while the JavaScript code defines and manages install-time properties, such as installation options. [`Distribution Definition XML Schema Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/DistributionDefinitionRef/Chapters/Introduction.html#//apple_ref/doc/uid/TP40005370) describes the XML schema used to define the structure of a distribution.

This document describes the object model that the JavaScript code in a distribution definition file can use to manage user input and system properties.

## Topics

### Classes
- [Applications](applications.md)
  An object that provides methods to obtain information about running applications.
- [Choice](choice.md)
  A single installation choice. 
- [Files](files.md)
  An object that provides methods for accessing files. 
- [IORegistry](ioregistry.md)
  An object that provides access to the IOKit registry. 
- [ProcessInformation](processinformation.md)
  A dictionary (associative array) describing an application.
- [Result](result.md)
  An object that provides methods to obtain information about the result of an Installation Check or Volume Check script. 
- [System](system.md)
  An object that provides access to information about the target host. 
- [Target](target.md)
  An object that provides methods to obtain information about the installation volume.

## See Also

- [Distribution Definition XML Schema Reference](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DeveloperTools/Reference/DistributionDefinitionRef/Chapters/Introduction.html#//apple_ref/doc/uid/TP40005370)


---

*[View on Apple Developer](https://developer.apple.com/documentation/installer_js)*
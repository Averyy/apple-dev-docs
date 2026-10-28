# Color Management Module Component Interface

**Framework**: Application Services  
**Kind**: enum

Specify a CMM interface version.

## Declaration

```c
enum {
   CMMInterfaceVersion = 1
};
```

## Overview

If your CMM supports the ColorSync Manager version 2.x, it should return the constant defined by the following enumeration when the Component Manager calls your CMM with the `kComponentVersionSelect` request code.

In response to the `kComponentVersionSelect` request code, a CMM should set its entry point function’s result to the CMM version number. The high-order 16 bits represent the major version and the low-order 16 bits represent the minor version. The `CMMInterfaceVersion` constant represents the major version number.

A CMM that only supports ColorSync 1.0 returns 0 for the major version in response to the version request.

The `kComponentVersionSelect` request code is one of four required Component Manager requests your CMM must handle. 

## Topics

### Constants
- [CMMInterfaceVersion](./color_management_module_component_interface/cmminterfaceversion.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/color_management_module_component_interface)*
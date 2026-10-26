# xcselect

**Framework**: xcselect  
**Kind**: module  
**Role**: Framework

Access the path of the macOS SDK available on the host system.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

#### Overview

The system provides [`xcselect_host_sdk_path`](./xcselect_host_sdk_path.md), a function to locate the path to a macOS SDK version for building executables, libraries, and other content that runs on the local Mac. If you don’t use Xcode build tools, you can use this function to get the macOS SDK version you need.

> **Note**: The `xcselect` framework is not available in Swift.

## Topics

### macOS SDK Paths
- [xcselect_host_sdk_path](./xcselect_host_sdk_path.md)
  Returns the path to a version of the macOS SDK for building executables, libraries, and other content that run on the local Mac.
### Reference
- [Macros](./macros.md)
  Macros in the xcselect framework.
- [Enumerations](./enumerations.md)
  Enumerations in the xcselect framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcselect)*
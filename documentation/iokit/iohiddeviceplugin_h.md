# IOHIDDevicePlugIn.h

**Framework**: IOKit  
**Role**: API Collection

#### Overview

This documentation describes the details of the programming interface for accessing Human Interface Devices and interfaces from code running in user space. It is intended that user mode HID drivers properly implement all interfaces described here in order to be visible via the HID Manager.

This documentation assumes that you have a basic understanding of the material contained in [Introduction to Accessing Hardware From Applications](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Intro/AH_Intro.html#//apple_ref/doc/uid/TP40002714).

All of the information described in this document is contained in the header file `IOHIDLib.h` found at `/System/Library/Frameworks/IOKit.framework/Headers/hid/IOHIDDevicePlugIn.h`.

##### Included Headers

- <sys/cdefs.h>
- <CoreFoundation/CoreFoundation.h>
- <CoreFoundation/CFPlugInCOM.h>
- <IOKit/IOTypes.h>
- <IOKit/IOReturn.h>
- <IOKit/IOCFPlugIn.h>
- <IOKit/hid/IOHIDBase.h>
- <IOKit/hid/IOHIDKeys.h>
- <IOKit/hid/IOHIDLibObsolete.h>

## Topics

### Constants
- [Defines](./iohiddeviceplugin_h/defines.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddeviceplugin_h)*
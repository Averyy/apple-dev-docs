# USBPowerRequestTypes

**Framework**: IOKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
typedef enum USBPowerRequestTypes : unsigned int {
    ...
} USBPowerRequestTypes;
```

## Overview

Used to specify what kind of power will be reserved using the IOUSBDevice RequestExtraPower and ReturnExtraPower APIs.

## Topics

### Constants
- [kUSBPowerDuringSleep](./usbpowerrequesttypes/kusbpowerduringsleep.md)
- [kUSBPowerDuringWake](./usbpowerrequesttypes/kusbpowerduringwake.md)
- [kUSBPowerRequestWakeRelease](./usbpowerrequesttypes/kusbpowerrequestwakerelease.md)
- [kUSBPowerRequestSleepRelease](./usbpowerrequesttypes/kusbpowerrequestsleeprelease.md)
- [kUSBPowerRequestWakeReallocate](./usbpowerrequesttypes/kusbpowerrequestwakereallocate.md)
- [kUSBPowerRequestSleepReallocate](./usbpowerrequesttypes/kusbpowerrequestsleepreallocate.md)
- [kUSBPowerDuringWakeRevocable](./usbpowerrequesttypes/kusbpowerduringwakerevocable.md)
- [kUSBPowerDuringWakeUSB3](./usbpowerrequesttypes/kusbpowerduringwakeusb3.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usbpowerrequesttypes)*
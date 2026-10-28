# IOPSGetProvidingPowerSourceType(CFTypeRef)

**Framework**: IOKit  
**Kind**: func

Indicates the power source the computer is currently drawing from.

## Declaration

```c
CFStringRef IOPSGetProvidingPowerSourceType(
   CFTypeRef snapshot);
```

## Return Value

One of: CFSTR(kIOPMACPowerKey), CFSTR(kIOPMBatteryPowerKey), CFSTR(kIOPMUPSPowerKey)

## Overview

Determines which power source is providing power.

## Parameters

- `snapshot`: The CFTypeRef returned by IOPSCopyPowerSourcesInfo()

## See Also

### Power Source Descriptions
- [IOPSCopyExternalPowerAdapterDetails](../api-1523866-iopscopyexternalpoweradapterdeta.md)
  Returns a CFDictionary that describes the attached (AC) external power adapter (if any external power adapter is attached.
- [IOPSCopyPowerSourcesInfo](../api-1523839-iopscopypowersourcesinfo.md)
  Returns a blob of Power Source information in an opaque CFTypeRef.
- [IOPSCopyPowerSourcesList](../api-1523856-iopscopypowersourceslist.md)
  Returns a CFArray of Power Source handles, each of type CFTypeRef.
- [IOPSGetPowerSourceDescription](../api-1523867-iopsgetpowersourcedescription.md)
  Returns a CFDictionary with readable information about the specific power source.
- [IOPSNotificationCreateRunLoopSource](../api-1523868-iopsnotificationcreaterunloopsou.md)
  Returns a CFRunLoopSourceRef that notifies the caller when power source information changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopowersources_h/1810316-iopsgetprovidingpowersourcetype)*
# IOPSCopyPowerSourcesInfo

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Returns a blob of Power Source information in an opaque CFTypeRef.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
CFTypeRef IOPSCopyPowerSourcesInfo(void);
```

## Return Value

NULL if errors were encountered, a CFTypeRef otherwise. Caller must CFRelease() the return value when done accessing it.

## Discussion

Clients should not directly access data in the returned CFTypeRef - they should use the accessor functions IOPSCopyPowerSourcesList and IOPSGetPowerSourceDescription, instead.

## See Also

### Power Source Descriptions
- [IOPSCopyExternalPowerAdapterDetails](./api-1523866-iopscopyexternalpoweradapterdeta.md)
  Returns a CFDictionary that describes the attached (AC) external power adapter (if any external power adapter is attached.
- [IOPSCopyPowerSourcesList](./api-1523856-iopscopypowersourceslist.md)
  Returns a CFArray of Power Source handles, each of type CFTypeRef.
- [IOPSGetPowerSourceDescription](./api-1523867-iopsgetpowersourcedescription.md)
  Returns a CFDictionary with readable information about the specific power source.
- [IOPSGetProvidingPowerSourceType(CFTypeRef)](./iopowersources_h/api-1810316-iopsgetprovidingpowersourcetype.md)
  Indicates the power source the computer is currently drawing from.
- [IOPSNotificationCreateRunLoopSource](./api-1523868-iopsnotificationcreaterunloopsou.md)
  Returns a CFRunLoopSourceRef that notifies the caller when power source information changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1523839-iopscopypowersourcesinfo)*
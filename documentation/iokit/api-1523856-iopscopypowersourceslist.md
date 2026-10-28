# IOPSCopyPowerSourcesList

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Returns a CFArray of Power Source handles, each of type CFTypeRef.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
CFArrayRef IOPSCopyPowerSourcesList(CFTypeRef blob);
```

## Return Value

Returns NULL if errors were encountered, otherwise a CFArray of CFTypeRefs. Caller must CFRelease() the returned CFArrayRef.

## Discussion

The caller shouldn't directly access the CFTypeRefs, but should use IOPSGetPowerSourceDescription on each member of the CFArrayRef.

## Parameters

- `blob`: Takes the CFTypeRef returned by IOPSCopyPowerSourcesInfo()

## See Also

### Power Source Descriptions
- [IOPSCopyExternalPowerAdapterDetails](./api-1523866-iopscopyexternalpoweradapterdeta.md)
  Returns a CFDictionary that describes the attached (AC) external power adapter (if any external power adapter is attached.
- [IOPSCopyPowerSourcesInfo](./api-1523839-iopscopypowersourcesinfo.md)
  Returns a blob of Power Source information in an opaque CFTypeRef.
- [IOPSGetPowerSourceDescription](./api-1523867-iopsgetpowersourcedescription.md)
  Returns a CFDictionary with readable information about the specific power source.
- [IOPSGetProvidingPowerSourceType(CFTypeRef)](./iopowersources_h/api-1810316-iopsgetprovidingpowersourcetype.md)
  Indicates the power source the computer is currently drawing from.
- [IOPSNotificationCreateRunLoopSource](./api-1523868-iopsnotificationcreaterunloopsou.md)
  Returns a CFRunLoopSourceRef that notifies the caller when power source information changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1523856-iopscopypowersourceslist)*
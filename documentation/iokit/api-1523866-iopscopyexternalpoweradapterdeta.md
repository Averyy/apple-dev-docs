# IOPSCopyExternalPowerAdapterDetails

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Returns a CFDictionary that describes the attached (AC) external power adapter (if any external power adapter is attached.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
CFDictionaryRef IOPSCopyExternalPowerAdapterDetails(void);
```

## Return Value

Returns a CFDictionary on success. Caller must release the returned dictionary. If no adapter is attached, or if there's an error, returns NULL.

## Discussion

Use the kIOPSPowerAdapter... keys described in IOPSKeys.h to interpret the returned CFDictionary.

## See Also

### Power Source Descriptions
- [IOPSCopyPowerSourcesInfo](./api-1523839-iopscopypowersourcesinfo.md)
  Returns a blob of Power Source information in an opaque CFTypeRef.
- [IOPSCopyPowerSourcesList](./api-1523856-iopscopypowersourceslist.md)
  Returns a CFArray of Power Source handles, each of type CFTypeRef.
- [IOPSGetPowerSourceDescription](./api-1523867-iopsgetpowersourcedescription.md)
  Returns a CFDictionary with readable information about the specific power source.
- [IOPSGetProvidingPowerSourceType(CFTypeRef)](./iopowersources_h/api-1810316-iopsgetprovidingpowersourcetype.md)
  Indicates the power source the computer is currently drawing from.
- [IOPSNotificationCreateRunLoopSource](./api-1523868-iopsnotificationcreaterunloopsou.md)
  Returns a CFRunLoopSourceRef that notifies the caller when power source information changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1523866-iopscopyexternalpoweradapterdeta)*
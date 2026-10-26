# IOPSGetPowerSourceDescription

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Returns a CFDictionary with readable information about the specific power source.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
CFDictionaryRef IOPSGetPowerSourceDescription(CFTypeRef blob, CFTypeRef ps);
```

#### Return Value

Returns NULL if an error was encountered, otherwise a CFDictionary. Caller should NOT release the returned CFDictionary - it will be released as part of the CFTypeRef returned by IOPSCopyPowerSourcesInfo().

#### Discussion

See the C-strings defined in IOPSKeys.h for specific keys into the dictionary. Don't expect all keys to be present in any dictionary. Some power sources, for example, may not support the "Time Remaining To Empty" key and it will not be present in their dictionaries.

## Parameters

- `blob`: The CFTypeRef returned by IOPSCopyPowerSourcesInfo()
- `ps`: One of the CFTypeRefs in the CFArray returned by IOPSCopyPowerSourcesList()

## See Also

### Power Source Descriptions
- [IOPSCopyExternalPowerAdapterDetails](./api-1523866-iopscopyexternalpoweradapterdeta.md)
  Returns a CFDictionary that describes the attached (AC) external power adapter (if any external power adapter is attached.
- [IOPSCopyPowerSourcesInfo](./api-1523839-iopscopypowersourcesinfo.md)
  Returns a blob of Power Source information in an opaque CFTypeRef.
- [IOPSCopyPowerSourcesList](./api-1523856-iopscopypowersourceslist.md)
  Returns a CFArray of Power Source handles, each of type CFTypeRef.
- [IOPSGetProvidingPowerSourceType(CFTypeRef)](./iopowersources_h/api-1810316-iopsgetprovidingpowersourcetype.md)
  Indicates the power source the computer is currently drawing from.
- [IOPSNotificationCreateRunLoopSource](./api-1523868-iopsnotificationcreaterunloopsou.md)
  Returns a CFRunLoopSourceRef that notifies the caller when power source information changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1523867-iopsgetpowersourcedescription)*
# addSubunit

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Installs a virtual AVC subunit.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*addSubunit)(void *self, UInt32 subunitType, UInt32 numSourcePlugs, UInt32 numDestPlugs, void *refCon, IOFWAVCSubunitPlugHandlerCallback callback, UInt32 *pSubunitTypeAndID);
```

## Parameters

- `self`: Pointer to IOFireWireAVCLibProtocolInterface.
- `subunitType`: The type of subunit to create.
- `numSourcePlugs`: The number of source plugs for this subunit.
- `numDestPlugs`: The number of destination plugs for this subunit.
- `refCon`: Arbitrary value passed back as first argument of callback.
- `callback`: A pointer to the callback to receive plug management messages.
- `pSubunitTypeAndID`: A pointer to a byte to hold the returned subunit address for the new subunit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface/1508740-addsubunit)*
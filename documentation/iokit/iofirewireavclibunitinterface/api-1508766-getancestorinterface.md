# getAncestorInterface

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Creates a plug-in object for an ancestor (in the I/O Registry) of the AVC unit and returns an interface to it.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
void *(*getAncestorInterface)(void *self, char *object_class, REFIID pluginType, REFIID iid);
```

## Return Value

Returns a COM-style interface pointer. Returns 0 upon failure.

## Discussion

This function is only available if the interface version is > 1 (macOS 10.2.0 or later?).

## Parameters

- `self`: Pointer to IOFireWireAVCLibUnitInterface.
- `object_class`: Class name of ancestor of the device to get an interface for.
- `pluginType`: An ID number, of type CFUUIDBytes (see CFUUID.h), identifying the type of plug-in service to be returned for the ancestor.
- `iid`: An ID number, of type CFUUIDBytes (see CFUUID.h), identifying the type of interface to be returned for the created plug-in object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibunitinterface/1508766-getancestorinterface)*
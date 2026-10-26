# FindNextAltInterface

**Framework**: IOKit  
**Kind**: func

## Declaration

```c
IOUSBDescriptorHeader * ( *FindNextAltInterface)(
   void *self,
   const void *current,
   IOUSBFindInterfaceRequest *request);
```

#### Return Value

Pointer to a matching interface descriptor, or NULL if none match.

#### Overview

return alternate interface descriptor satisfying the requirements specified in request, or NULL if there aren't any. discussion request is updated with the properties of the returned interface.

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.
- `current`: interface descriptor to start searching from, NULL to start at alternate interface 0.
- `request`: specifies what properties an interface must have to match.

## See Also

### Miscellaneous
- [FindNextAssociatedDescriptor](./api-1809475-findnextassociateddescriptor.md)
  Find the next descriptor of the requested type associated with the interface.
- [GetBusFrameNumberWithTime](./api-1809485-getbusframenumberwithtime.md)
  Gets a recent frame number of the bus to which the device is attached, along with a system time corresponding to the start of that frame
- [GetPipePropertiesV2](./api-1809494-getpipepropertiesv2.md)
  Gets the properties for a pipe, including the USB SuperSpeed endpoint companion properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousblib_h/1809466-findnextaltinterface)*
# FindNextAssociatedDescriptor

**Framework**: IOKit  
**Kind**: func

Find the next descriptor of the requested type associated with the interface.

## Declaration

```c
IOUSBDescriptorHeader * ( *FindNextAssociatedDescriptor)(
   void *self,
   const void *currentDescriptor,
   UInt8 descriptorType);
```

#### Return Value

Pointer to the descriptor, or NULL if no matching descriptors found.

#### Overview

The interface does not have to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.
- `currentDescriptor`: Descriptor to start searching from, NULL to start from beginning of list.
- `descriptorType`: Descriptor type to search for, or kUSBAnyDesc to return any descriptor type.

## See Also

### Miscellaneous
- [FindNextAltInterface](./api-1809466-findnextaltinterface.md)
- [GetBusFrameNumberWithTime](./api-1809485-getbusframenumberwithtime.md)
  Gets a recent frame number of the bus to which the device is attached, along with a system time corresponding to the start of that frame
- [GetPipePropertiesV2](./api-1809494-getpipepropertiesv2.md)
  Gets the properties for a pipe, including the USB SuperSpeed endpoint companion properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousblib_h/1809475-findnextassociateddescriptor)*
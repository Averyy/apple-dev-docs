# IOUSBInterfaceAssociationDescriptor

**Framework**: IOKit  
**Kind**: tag

## Declaration

```c
struct IOUSBInterfaceAssociationDescriptor {
   UInt8 bLength;
   UInt8 bDescriptorType;
   UInt8 bFirstInterface;
   UInt8 bInterfaceCount;
   UInt8 bFunctionClass;
   UInt8 bFunctionSubClass;
   UInt8 bFunctionProtocol;
   UInt8 iFunction;
};
```

#### Overview

USB Inerface Association Descriptor. ECN to the USB 2.0 Spec. See the USB Specification at [http://www.usb.org](http://www.usb.org).

## See Also

### Related Documentation
- [IOUSBInterfaceAssociationDescriptor](../../kernel/iousbinterfaceassociationdescriptor.md)
  The descriptor that associates multiple interfaces to the same function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/usb_h_user-space/iousbinterfaceassociationdescriptor)*
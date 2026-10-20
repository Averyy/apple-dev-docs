# IOUSBInterfaceAssociationDescriptor

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

The descriptor that associates multiple interfaces to the same function.

**Availability**:
- macOS 10.3+

## Declaration

```c
typedef struct IOUSBInterfaceAssociationDescriptor IOUSBInterfaceAssociationDescriptor;
```

#### Discussion

See USB 3.2, 9.6.4 for more information.

## Topics

### Getting the Properties
- [bLength](./iousbinterfaceassociationdescriptor/api-1545909-blength.md)
  The size of the descriptor.
- [bDescriptorType](./iousbinterfaceassociationdescriptor/api-1546180-bdescriptortype.md)
  The type of the descriptor.
- [bFirstInterface](./iousbinterfaceassociationdescriptor/api-1546445-bfirstinterface.md)
  The first interface of the descriptor.
- [bInterfaceCount](./iousbinterfaceassociationdescriptor/api-1545905-binterfacecount.md)
  The number of interfaces.
- [bFunctionClass](./iousbinterfaceassociationdescriptor/api-1546273-bfunctionclass.md)
  The function class.
- [bFunctionSubClass](./iousbinterfaceassociationdescriptor/api-1546578-bfunctionsubclass.md)
  The function subclass.
- [bFunctionProtocol](./iousbinterfaceassociationdescriptor/api-1546423-bfunctionprotocol.md)
  The function protocol.
- [iFunction](./iousbinterfaceassociationdescriptor/api-1546285-ifunction.md)
  The descriptor’s function.

## See Also

### Interface Descriptors
- [IOUSBInterfaceDescriptor](./iousbinterfacedescriptor.md)
  A descriptor for a specific interface of a USB device.
- [IOUSBInterfaceDescriptorPtr](./iousbinterfacedescriptorptr.md)
  A pointer to a USB interface descriptor.
- [IOUSBInterfaceAssociationDescriptorPtr](./iousbinterfaceassociationdescriptorptr.md)
  A pointer to a USB interface association descriptor.
### Related Documentation
- [IOUSBInterfaceAssociationDescriptor](../iokit/usb_h_user-space/iousbinterfaceassociationdescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbinterfaceassociationdescriptor)*
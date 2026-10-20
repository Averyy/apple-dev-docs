# IOUSB20HubDescriptor

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

A structure that defines the descriptor for a USB 2.0 hub.

**Availability**:
- macOS 10.15+

## Declaration

```c
typedef struct IOUSB20HubDescriptor IOUSB20HubDescriptor;
```

#### Discussion

For more information about this descriptor type, see USB 2.0, 11.23.2.1.

## Topics

### Instance Properties
- [bDescriptorType](./iousb20hubdescriptor/api-3166550-bdescriptortype.md)
- [bHubControllerCurrent](./iousb20hubdescriptor/api-3166551-bhubcontrollercurrent.md)
- [bLength](./iousb20hubdescriptor/api-3166552-blength.md)
- [bNumberPorts](./iousb20hubdescriptor/api-3166553-bnumberports.md)
- [bPowerOnToPowerGood](./iousb20hubdescriptor/api-3166554-bpowerontopowergood.md)
- [deviceRemovable](./iousb20hubdescriptor/api-3166555-deviceremovable.md)
- [reserved](./iousb20hubdescriptor/api-3166556-reserved.md)
- [wHubCharacteristics](./iousb20hubdescriptor/api-3166557-whubcharacteristics.md)

## See Also

### Hub Descriptors
- [IOUSB3HubDescriptor](./iousb3hubdescriptor.md)
  A structure that defines the descriptor for a USB 3.0 hub.
- [IOUSBHubDescriptor](./iousbhubdescriptor.md)
  A structure that defines the descriptor for a USB hub.
- [IOUSBHubPortReEnumerateParam](./iousbhubportreenumerateparam.md)
  A structure for USB hub port reenumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousb20hubdescriptor)*
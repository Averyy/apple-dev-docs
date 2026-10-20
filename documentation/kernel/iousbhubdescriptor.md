# IOUSBHubDescriptor

**Framework**: Kernel  
**Kind**: struct  
**Role**: Structure

A structure that defines the descriptor for a USB hub.

**Availability**:
- macOS 10.8+

## Declaration

```c
typedef struct IOUSBHubDescriptor {
    ...
} IOUSBHubDescriptor;
```

## Topics

### Instance Properties
- [characteristics](./iousbhubdescriptor/api-1532467-characteristics.md)
- [hubCurrent](./iousbhubdescriptor/api-1532331-hubcurrent.md)
- [hubType](./iousbhubdescriptor/api-1532409-hubtype.md)
- [length](./iousbhubdescriptor/api-1532267-length.md)
- [numPorts](./iousbhubdescriptor/api-1532449-numports.md)
- [powerOnToGood](./iousbhubdescriptor/api-1532412-powerontogood.md)
- [pwrCtlPortFlags](./iousbhubdescriptor/api-1532245-pwrctlportflags.md)
- [removablePortFlags](./iousbhubdescriptor/api-1532236-removableportflags.md)

## See Also

### Hub Descriptors
- [IOUSB20HubDescriptor](./iousb20hubdescriptor.md)
  A structure that defines the descriptor for a USB 2.0 hub.
- [IOUSB3HubDescriptor](./iousb3hubdescriptor.md)
  A structure that defines the descriptor for a USB 3.0 hub.
- [IOUSBHubPortReEnumerateParam](./iousbhubportreenumerateparam.md)
  A structure for USB hub port reenumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhubdescriptor)*
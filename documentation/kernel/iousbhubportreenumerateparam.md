# IOUSBHubPortReEnumerateParam

**Framework**: Kernel  
**Kind**: struct  
**Role**: Structure

A structure for USB hub port reenumeration.

**Availability**:
- macOS 10.8+

## Declaration

```c
typedef struct IOUSBHubPortReEnumerateParam {
    ...
} IOUSBHubPortReEnumerateParam;
```

#### Overview

Use this structure to specify the port that needs reenumeration.

## Topics

### Instance Properties
- [options](./iousbhubportreenumerateparam/api-1532360-options.md)
- [portNumber](./iousbhubportreenumerateparam/api-1532365-portnumber.md)

## See Also

### Hub Descriptors
- [IOUSB20HubDescriptor](./iousb20hubdescriptor.md)
  A structure that defines the descriptor for a USB 2.0 hub.
- [IOUSB3HubDescriptor](./iousb3hubdescriptor.md)
  A structure that defines the descriptor for a USB 3.0 hub.
- [IOUSBHubDescriptor](./iousbhubdescriptor.md)
  A structure that defines the descriptor for a USB hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhubportreenumerateparam)*
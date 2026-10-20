# IOUSBHubStatus

**Framework**: Kernel  
**Kind**: struct  
**Role**: Structure

A structure that represents the USB hub status.

**Availability**:
- macOS 10.8+

## Declaration

```c
typedef struct IOUSBHubStatus {
    ...
} IOUSBHubStatus;
```

#### Overview

Use this structure when obtaining the port status and change flags with [`GetPortStatus`](./iousbhostdevice/api-3294636-getportstatus.md).

## Topics

### Instance Properties
- [changeFlags](./iousbhubstatus/api-1532400-changeflags.md)
- [statusFlags](./iousbhubstatus/api-1532354-statusflags.md)

## See Also

### Hub Port Status Requests
- [IOUSB30HubPortStatusExt](./iousb30hubportstatusext.md)
  A structure that represents an extension to the USB 3.0 hub port status.
- [IOUSBHubPortStatus](./iousbhubportstatus.md)
  A structure that contains the USB hub port status.
- [IOUSBHubStatusPtr](./iousbhubstatusptr.md)
  A pointer to a USB hub status structure.
### Related Documentation
- [pseudoSymbol-1807067](pseudoSymbol-1807067)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbhubstatus)*
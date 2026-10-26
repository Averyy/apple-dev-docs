# GetSCSIServiceResponse

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to get the SCSIServiceResponse from the SCSITask.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*GetSCSIServiceResponse)(void *task, SCSIServiceResponse *outServiceResponse);
```

#### Return Value

Returns kIOReturnSuccess or kIOReturnError.

#### Discussion

This method can be used to get the SCSIServiceResponse from the SCSITask.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.
- `outServiceResponse`: Pointer to an SCSIServiceResponse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575338-getscsiserviceresponse)*
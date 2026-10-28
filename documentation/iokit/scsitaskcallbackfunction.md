# SCSITaskCallbackFunction

**Framework**: IOKit  
**Kind**: tdef  
**Role**: Type Alias

Asynchronous callback routine definition.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
typedef void (*SCSITaskCallbackFunction)(SCSIServiceResponse serviceResponse, SCSITaskStatus taskStatus, UInt64 bytesTransferred, void *refCon);
```

## Discussion

Asynchronous callback routine definition. Any function which is used as a callback routine for SCSITasks must conform to this function definition.

## Parameters

- `serviceResponse`: An SCSIServiceResponse returned by the protocol transport.
- `taskStatus`: An SCSITaskStatus to indicate the task's status
- `bytesTransferred`: A total byte count of bytes transferred.
- `refCon`: The refCon passed when the task was executed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskcallbackfunction)*
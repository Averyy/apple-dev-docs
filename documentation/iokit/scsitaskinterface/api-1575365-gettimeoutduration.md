# GetTimeoutDuration

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to get the timeout duration for the SCSITask.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
UInt32 (*GetTimeoutDuration)(void *task);
```

## Return Value

Returns a value between zero and ULONG_MAX.

## Discussion

This method can be used to get the timeout duration for the SCSITask. The timeout duration is counted in milliseconds.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575365-gettimeoutduration)*
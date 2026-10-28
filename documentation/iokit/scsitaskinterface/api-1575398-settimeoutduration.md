# SetTimeoutDuration

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to set the timeout duration for the SCSITask.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*SetTimeoutDuration)(void *task, UInt32 inTimeoutDurationMS);
```

## Return Value

Returns kIOReturnSucces or kIOReturnError.

## Discussion

This method can be used to set the timeout duration for the SCSITask. The timeout duration is counted in milliseconds. A value of zero is equivalent to "Wait Forever", but on some buses, this isn't possible, so ULONG_MAX is used.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.
- `inTimeoutDurationMS`: UInt32 representing the timeout in milliseconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575398-settimeoutduration)*
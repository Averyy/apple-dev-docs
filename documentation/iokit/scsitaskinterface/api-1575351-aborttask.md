# AbortTask

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to abort the SCSITask.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*AbortTask)(void *task);
```

## Return Value

Returns kIOReturnSuccess, kIOReturnUnsupported or kIOReturnError.

## Discussion

This method can be used to abort an SCSITask which is already in progress.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575351-aborttask)*
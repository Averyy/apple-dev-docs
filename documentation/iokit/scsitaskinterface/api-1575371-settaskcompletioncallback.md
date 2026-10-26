# SetTaskCompletionCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to set the asynchronous completion routine for the SCSITask.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*SetTaskCompletionCallback)(void *task, SCSITaskCallbackFunction callback, void *refCon);
```

#### Return Value

Returns kIOReturnSuccess, kIOReturnError, or kIOReturnNotPermitted if the client has not called AddCallbackDispatcherToRunLoop on the SCSITaskDeviceInterface.

#### Discussion

This method can be used to set the asynchronous completion routine for the SCSITask.

## Parameters

- `task`: Pointer to an instance of an SCSITaskInterface.
- `callback`: SCSITaskCallbackFunction to be called upon completion of the SCSITask.
- `refCon`: A value to be returned to the caller upon completion of the routine. This field is not used by the SCSITaskInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskinterface/1575371-settaskcompletioncallback)*
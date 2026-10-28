# IsExclusiveAccessAvailable

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Method to find out if the device can be opened exclusively by the caller.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
Boolean (*IsExclusiveAccessAvailable)(void *self);
```

## Return Value

Returns false if the device has been opened for exclusive access, otherwise true.

## Discussion

Method to find out if the device can be opened exclusively by the caller.

## Parameters

- `self`: Pointer to an instance of an SCSITaskDeviceInterface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/scsitaskdeviceinterface/1575379-isexclusiveaccessavailable)*
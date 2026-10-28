# ReturnExtraPower

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Clients can use this API to tell the system that they will not use power that was previously reserved by using the RequestExtraPower API.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
IOReturn (*ReturnExtraPower)(void *self, UInt32 type, UInt32 powerReturned);
```

## Return Value

If the returnedPower was not previously allocated, an error will be returned. This will include the case for power that was requested for sleep but was returned for wake. Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService.

## Discussion

The device has to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBDeviceInterface.
- `type`: Indicates whether the power is to be used during wake or sleep (One of kUSBPowerDuringSleep or kUSBPowerDuringWake)
- `powerReturned`: Amount of power to be returned, in mA.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface320/1559629-returnextrapower)*
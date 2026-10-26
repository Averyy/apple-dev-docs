# GetExtraPowerAllocated

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Clients can use this API to ask how much extra power has already been reserved by this device. Units are milliAmps (mA).

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
IOReturn (*GetExtraPowerAllocated)(void *self, UInt32 type, UInt32 *powerAllocated);
```

#### Return Value

Value returned can be 0 if no power has been allocated. Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService.

#### Discussion

The device has to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBDeviceInterface.
- `type`: Indicates whether the allocated power was to be used during wake or sleep (One of kUSBPowerDuringSleep or kUSBPowerDuringWake)
- `powerAllocated`: Amount of power to be returned, in mA.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface320/1559557-getextrapowerallocated)*
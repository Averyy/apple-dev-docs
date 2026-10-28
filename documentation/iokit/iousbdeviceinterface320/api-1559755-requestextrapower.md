# RequestExtraPower

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Clients can use this API to reserve extra power for use by this device while the machine is asleep or while it is awake. Units are milliAmps (mA).

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
IOReturn (*RequestExtraPower)(void *self, UInt32 type, UInt32 requestedPower, UInt32 *powerAvailable);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnUnsupported is the bus doesn't support this function.

## Discussion

The device has to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBDeviceInterface.
- `type`: Indicates whether the power is to be used during wake or sleep (One of kUSBPowerDuringSleep or kUSBPowerDuringWake)
- `requestedPower`: Amount of power desired, in mA
- `powerAvailable`: Amount of power that was reserved, in mA


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface320/1559755-requestextrapower)*
# IOACPIAddressSpaceHandler

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.3+

## Declaration

```swift
typedef IOReturn (*IOACPIAddressSpaceHandler)(UInt32 operation, IOACPIAddress address, UInt64 *value, UInt32 bitWidth, UInt32 bitOffset, void *context);
```

## See Also

- [IOACPIPlatformDevice](ioacpiplatformdevice.md)
- [IOACPIPlatformExpert](ioacpiplatformexpert.md)
- [IOPMPowerSource](iopmpowersource.md)
- [IOPMPowerSourceList](iopmpowersourcelist.md)
- [IOPMrootDomain](iopmrootdomain.md)
- [IOPowerConnection](iopowerconnection.md)
- [IOPwrController](iopwrcontroller.md)
- [IOACPIAddress](ioacpiaddress.md)
- [IOACPIAddressSpaceDescriptor](ioacpiaddressspacedescriptor.md)
- [IOACPIAddressSpaceID](ioacpiaddressspaceid.md)
- [IOPMPowerState](iopmpowerstate.md)
- [acknowledgeSleepWakeNotification](1579170-acknowledgesleepwakenotification.md)
- [gIOACPIAddressKey](gioacpiaddresskey.md)
- [gIOACPIDeviceStatusKey](gioacpidevicestatuskey.md)
- [gIOACPIHardwareIDKey](gioacpihardwareidkey.md)
- [gIOACPIPlane](gioacpiplane.md)
- [gIOACPIUniqueIDKey](gioacpiuniqueidkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioacpiaddressspacehandler)*
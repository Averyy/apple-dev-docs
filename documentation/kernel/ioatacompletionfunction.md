# IOATACompletionFunction

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 11.0+

## Declaration

```swift
typedef void (IOATACommand *) IOATACompletionFunction;
```

#### Discussion

callback function for ATA disk devices.

## See Also

- [ATAOperationType](ataoperationtype.md)
- [ATARequestIdentifier](atarequestidentifier.md)
- [IOExtendedLBA](ioextendedlba.md)
  If 48-bit LBAs are supported, IOExtendedLBA is used to represent a 48-bit LBA. The driver examines the ATA identify data to determine if 48-bit addressing is supported.
- [IOATABusInfo](ioatabusinfo.md)
  used to indicate the capabilities of the bus the device is connected to, PIO and DMA modes supported, etc.
- [IOATADevConfig](ioatadevconfig.md)
  used for configuring and communicating the desired transfer modes of a device. A disk driver would typically use this object in conjunction with the 512-bytes of identification data from the drive and the IOATABusInfo object for the bus it is connected to. This object will determine the best matching transfer speeds available. the device driver will then send a series of Set Features commands to configure the drive and this object to the bus through the IOATADevice nub in order to configure the optimum transfer mode. The driver for the disk drive may choose to populate this object with whatever transfer mode desired, in the event that a different mode is required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatacompletionfunction)*
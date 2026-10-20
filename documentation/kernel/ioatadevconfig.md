# IOATADevConfig

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

used for configuring and communicating the desired transfer modes of a device. A disk driver would typically use this object in conjunction with the 512-bytes of identification data from the drive and the IOATABusInfo object for the bus it is connected to. This object will determine the best matching transfer speeds available. the device driver will then send a series of Set Features commands to configure the drive and this object to the bus through the IOATADevice nub in order to configure the optimum transfer mode. The driver for the disk drive may choose to populate this object with whatever transfer mode desired, in the event that a different mode is required.

**Availability**:
- macOS 11.0+

## Declaration

```cpp
class IOATADevConfig : OSObject
```

#### Overview

usually use the initWithBestSelection to make a best mode match. The Mode accessors use bit significance to indicate a selected mode or supported modes(s) ie, 00000001b indicates Mode-0, 00000010b indicates mode 1, etc. Selected mode is indicated by a single set bit. No bit set indicates no mode in that class is selected. ie, a bus will support multiple possible modes, but will only have one mode selected at that time.

## Topics

### Miscellaneous
- [atadevconfig](./ioatadevconfig/api-1811729-atadevconfig.md)
  static creator function.
- [bitSigToNumeric](./ioatadevconfig/api-1811736-bitsigtonumeric.md)
  converts a bit-significant field to a numerical value. Note that a bit field of 0x00 has no defined result.
- [getDMACycleTime](./ioatadevconfig/api-1811744-getdmacycletime.md)
- [getDMAMode](./ioatadevconfig/api-1811750-getdmamode.md)
- [getPacketConfig](./ioatadevconfig/api-1811758-getpacketconfig.md)
- [getPIOCycleTime](./ioatadevconfig/api-1811768-getpiocycletime.md)
- [getPIOMode](./ioatadevconfig/api-1811774-getpiomode.md)
- [getUltraMode](./ioatadevconfig/api-1811781-getultramode.md)
- [initWithBestSelection](./ioatadevconfig/api-1811790-initwithbestselection.md)
  Handy initializer: pass the 512-byte result of the Identify Device or Identify Packet Device in endian-order for your platform (byte-swapped on PPC) and the IOATABusInfo object for the bus. The object will initialize all fields and select the best transfer modes that match on bus and device. If the return value was 0 (success or noErr), then a matching mode is supported. Examine the PIO and UDMA/DMA fields and to generate the apropriate SET FEATURES parameters for your drive and send this initialised object to the IOATAController when requesting a speed configuration. failure means no supported transfer modes matched between bus and device info.
- [setDMACycleTime](./ioatadevconfig/api-1811797-setdmacycletime.md)
- [setDMAMode](./ioatadevconfig/api-1811803-setdmamode.md)
- [setPacketConfig](./ioatadevconfig/api-1811808-setpacketconfig.md)
  For ATAPI devices, if the device asserts interrupt after the Packet Command when it is ready to accept the packet, set this value to true (mostly older devices). If the device accepts the packet only by asserting DRQ bit in status, then set this value false. Tells the bus controller whether to wait for packet acceptance or set pending interrupt.
- [setPIOCycleTime](./ioatadevconfig/api-1811814-setpiocycletime.md)
- [setPIOMode](./ioatadevconfig/api-1811821-setpiomode.md)
- [setUltraMode](./ioatadevconfig/api-1811827-setultramode.md)
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [reserved](./ioatadevconfig/reserved.md)
### Instance Methods
- [- assignFromData](./ioatadevconfig/api-1589972-assignfromdata.md)
- [- bitSigToNumeric](./ioatadevconfig/api-1589968-bitsigtonumeric.md)
- [- getDMACycleTime](./ioatadevconfig/api-1589980-getdmacycletime.md)
- [- getDMAMode](./ioatadevconfig/api-1589978-getdmamode.md)
- [- getMetaClass](./ioatadevconfig/api-1589965-getmetaclass.md)
- [- getPIOCycleTime](./ioatadevconfig/api-1589967-getpiocycletime.md)
- [- getPIOMode](./ioatadevconfig/api-1589973-getpiomode.md)
- [- getPacketConfig](./ioatadevconfig/api-1589977-getpacketconfig.md)
- [- getUltraMode](./ioatadevconfig/api-1589983-getultramode.md)
- [- init](./ioatadevconfig/api-1589979-init.md)
- [- initWithBestSelection](./ioatadevconfig/api-1589975-initwithbestselection.md)
- [- setDMACycleTime](./ioatadevconfig/api-1589971-setdmacycletime.md)
- [- setDMAMode](./ioatadevconfig/api-1589969-setdmamode.md)
- [- setPIOCycleTime](./ioatadevconfig/api-1589984-setpiocycletime.md)
- [- setPIOMode](./ioatadevconfig/api-1589981-setpiomode.md)
- [- setPacketConfig](./ioatadevconfig/api-1589976-setpacketconfig.md)
- [- setUltraMode](./ioatadevconfig/api-1589970-setultramode.md)
### Type Methods
- [+ atadevconfig](./ioatadevconfig/api-1589974-atadevconfig.md)
- [+ sDriveExtendedLBASize](./ioatadevconfig/api-1589982-sdriveextendedlbasize.md)
- [+ sDriveSupports48BitLBA](./ioatadevconfig/api-1589966-sdrivesupports48bitlba.md)

## Relationships

### Inherits From
- [OSObject](./osobject.md)

## See Also

### Base Types
- [ATAOperationType](./ataoperationtype.md)
- [ATARequestIdentifier](./atarequestidentifier.md)
- [IOExtendedLBA](./ioextendedlba.md)
  If 48-bit LBAs are supported, IOExtendedLBA is used to represent a 48-bit LBA. The driver examines the ATA identify data to determine if 48-bit addressing is supported.
- [IOATABusInfo](./ioatabusinfo.md)
  used to indicate the capabilities of the bus the device is connected to, PIO and DMA modes supported, etc.
- [IOATACompletionFunction](./ioatacompletionfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatadevconfig)*
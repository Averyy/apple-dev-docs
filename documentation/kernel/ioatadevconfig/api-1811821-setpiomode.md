# setPIOMode

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
void setPIOMode(
 UInt8inModeBitMap);
```

## Parameters

- `inModeBitMap`: bit-significant map of PIO mode

## See Also

- [atadevconfig](ioatadevconfig/1811729-atadevconfig.md)
  static creator function.
- [bitSigToNumeric](ioatadevconfig/1811736-bitsigtonumeric.md)
  converts a bit-significant field to a numerical value. Note that a bit field of 0x00 has no defined result.
- [getDMACycleTime](ioatadevconfig/1811744-getdmacycletime.md)
- [getDMAMode](ioatadevconfig/1811750-getdmamode.md)
- [getPacketConfig](ioatadevconfig/1811758-getpacketconfig.md)
- [getPIOCycleTime](ioatadevconfig/1811768-getpiocycletime.md)
- [getPIOMode](ioatadevconfig/1811774-getpiomode.md)
- [getUltraMode](ioatadevconfig/1811781-getultramode.md)
- [initWithBestSelection](ioatadevconfig/1811790-initwithbestselection.md)
  Handy initializer: pass the 512-byte result of the Identify Device or Identify Packet Device in endian-order for your platform (byte-swapped on PPC) and the IOATABusInfo object for the bus. The object will initialize all fields and select the best transfer modes that match on bus and device. If the return value was 0 (success or noErr), then a matching mode is supported. Examine the PIO and UDMA/DMA fields and to generate the apropriate SET FEATURES parameters for your drive and send this initialised object to the IOATAController when requesting a speed configuration. failure means no supported transfer modes matched between bus and device info.
- [setDMACycleTime](ioatadevconfig/1811797-setdmacycletime.md)
- [setDMAMode](ioatadevconfig/1811803-setdmamode.md)
- [setPacketConfig](ioatadevconfig/1811808-setpacketconfig.md)
  For ATAPI devices, if the device asserts interrupt after the Packet Command when it is ready to accept the packet, set this value to true (mostly older devices). If the device accepts the packet only by asserting DRQ bit in status, then set this value false. Tells the bus controller whether to wait for packet acceptance or set pending interrupt.
- [setPIOCycleTime](ioatadevconfig/1811814-setpiocycletime.md)
- [setUltraMode](ioatadevconfig/1811827-setultramode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatadevconfig/1811821-setpiomode)*
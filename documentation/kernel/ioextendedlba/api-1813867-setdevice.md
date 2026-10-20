# setDevice

**Framework**: Kernel  
**Kind**: instm

Taskfile access. Registers are named in accordance with ATA Standards conventions

## Declaration

```cpp
virtual void setDevice(
 UInt8 inDevice );
```

## See Also

### Miscellaneous
- [getCommand](./api-1813831-getcommand.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getDevice](./api-1813835-getdevice.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getExtendedLBA](./api-1813840-getextendedlba.md)
  convenience method that gets a 48-bit LBA
- [getFeatures16](./api-1813845-getfeatures16.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getLBAHigh16](./api-1813850-getlbahigh16.md)
  convenience method that gets the high 16 bits of a 48-bit LBA
- [getLBALow16](./api-1813853-getlbalow16.md)
  convenience method that gets the lower 16 bits of a 48-bit LBA
- [getLBAMid16](./api-1813856-getlbamid16.md)
  convenience method that gets the middle 16 bits of a 48-bit LBA
- [getSectorCount16](./api-1813860-getsectorcount16.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setCommand](./api-1813863-setcommand.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setExtendedLBA](./api-1813870-setextendedlba.md)
  convenience method that sets the taskfile registers into a 48-bit LBA address, along with sector count, and unit selected and LBA bit set
- [setFeatures16](./api-1813873-setfeatures16.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setLBAHigh16](./api-1813876-setlbahigh16.md)
  convenience method that sets the high 16 bits of a 48-bit LBA
- [setLBALow16](./api-1813879-setlbalow16.md)
  convenience method that sets the lower 16 bits of a 48-bit LBA
- [setLBAMid16](./api-1813881-setlbamid16.md)
  convenience method that sets the middle 16 bits of a 48-bit LBA
- [setSectorCount16](./api-1813884-setsectorcount16.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [zeroData](./api-1813886-zerodata.md)
  convenience method that zeros out the lba, sector count, features, device, and command member variables


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioextendedlba/1813867-setdevice)*
# InitElement

**Framework**: Kernel  
**Kind**: tag

## Declaration

```swift
struct InitElement {
   IOPhysicalAddress start;
   IOPhysicalLength length;
   IOOptionBits tag;
};
```

## Topics

### Fields
- [start](iodevicememory/initelement/start.md)
  First physical address in the range.
- [length](iodevicememory/initelement/length.md)
  Length of the range.
- [tag](iodevicememory/initelement/tag.md)
  32-bit value not interpreted by IODeviceMemory or IOMemoryDescriptor, for use by the bus family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodevicememory/initelement)*
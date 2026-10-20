# InitElement

**Framework**: Kernel  
**Kind**: tag

## Declaration

```c
struct InitElement {
   IOPhysicalAddress start;
   IOPhysicalLength length;
   IOOptionBits tag;
};
```

## Topics

### Fields
- [start](./initelement/start.md)
  First physical address in the range.
- [length](./initelement/length.md)
  Length of the range.
- [tag](./initelement/tag.md)
  32-bit value not interpreted by IODeviceMemory or IOMemoryDescriptor, for use by the bus family.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodevicememory/initelement)*
# fat_header

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.8+

## Declaration

```swift
struct fat_header {
    ...
};
```

## Topics

### Instance Properties
- [magic](fat_header/1558632-magic.md)
  An integer containing the value `0xCAFEBABE` in big-endian byte order format. On a big-endian host CPU, this can be validated using the constant `FAT_MAGIC`; on a little-endian host CPU, it can be validated using the constant `FAT_CIGAM`.
- [nfat_arch](fat_header/1558629-nfat_arch.md)
  An integer specifying the number of [`fat_arch`](fat_arch.md) data structures that follow. This is the number of architectures contained in this binary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/fat_header)*
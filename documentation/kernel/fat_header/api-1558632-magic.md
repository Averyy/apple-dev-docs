# magic

**Framework**: Kernel  
**Kind**: structp

An integer containing the value `0xCAFEBABE` in big-endian byte order format. On a big-endian host CPU, this can be validated using the constant `FAT_MAGIC`; on a little-endian host CPU, it can be validated using the constant `FAT_CIGAM`.

**Availability**:
- macOS 10.8+

## Declaration

```swift
uint32_t magic;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/fat_header/1558632-magic)*
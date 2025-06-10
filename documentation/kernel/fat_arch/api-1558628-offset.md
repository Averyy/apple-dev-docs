# offset

**Framework**: Kernel  
**Kind**: structp

Offset to the beginning of the data for this CPU.

**Availability**:
- macOS 10.8+

## Declaration

```swift
uint32_t offset;
```

## See Also

- [cpusubtype](fat_arch/1558623-cpusubtype.md)
  An enumeration value of type `cpu_subtype_t`. Specifies the specific member of the CPU family on which this entry may be used or a constant specifying all members.
- [size](fat_arch/1558631-size.md)
  Size of the data for this CPU.
- [align](fat_arch/1558625-align.md)
  The power of 2 alignment for the offset of the object file for the architecture specified in `cputype` within the binary. This is required to ensure that, if this binary is changed, the contents it retains are correctly aligned for virtual memory paging and other uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/fat_arch/1558628-offset)*
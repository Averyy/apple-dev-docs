# relocation_info

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.8+

## Declaration

```swift
struct relocation_info {
    ...
};
```

## Topics

### Instance Properties
- [r_address](relocation_info/1577793-r_address.md)
  In `MH_OBJECT` files, an offset from the start of the section to the item containing the address requiring relocation.
- [r_extern](relocation_info/1577784-r_extern.md)
  Indicates whether the `r_symbolnum` field is an index into the symbol table (1) or a section number (0).
- [r_length](relocation_info/1577791-r_length.md)
  Indicates the length of the item containing the address to be relocated. 
- [r_pcrel](relocation_info/1577785-r_pcrel.md)
  Indicates whether the item containing the address to be relocated is part of a CPU instruction that uses PC-relative addressing.
- [r_symbolnum](relocation_info/1577798-r_symbolnum.md)
  Indicates either an index into the symbol table (when the `r_extern` field is set to 1) or a section number (when the `r_extern` field is set to 0). As previously mentioned, sections are ordered from 1 to 255 in the order in which they appear in the `LC_SEGMENT` load commands. This field is set to `R_ABS` for relocation entries for absolute symbols, which need no relocation.
- [r_type](relocation_info/1577790-r_type.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/relocation_info)*
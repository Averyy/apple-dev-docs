# n_sect

**Framework**: Kernel  
**Kind**: structp

An integer specifying the number of the section that this symbol can be found in, or `NO_SECT` if the symbol is not to be found in any section of this image. The sections are contiguously numbered across segments, starting from 1, according to the order they appear in the `LC_SEGMENT` load commands.

**Availability**:
- macOS 10.8+

## Declaration

```swift
uint8_t n_sect;
```

## See Also

- [n_un](nlist_64/1583922-n_un.md)
  A union that holds an index into the string table, `n_strx`. To specify an empty string (`""`), set this value to 0.
- [n_type](nlist_64/1583944-n_type.md)
  A byte value consisting of data accessed using four bit masks:
- [n_desc](nlist_64/1583957-n_desc.md)
  A 16-bit value providing additional information about the nature of this symbol. The reference flags can be accessed using the `REFERENCE_TYPE` mask (0xF) and are defined as follows:


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/nlist_64/1583960-n_sect)*
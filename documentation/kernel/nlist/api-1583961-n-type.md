# n_type

**Framework**: Kernel  
**Kind**: structp

A byte value consisting of data accessed using four bit masks:

**Availability**:
- macOS 10.8+

## Declaration

```swift
uint8_t n_type;
```

## See Also

- [n_un](nlist/1583921-n_un.md)
  A union that holds an index into the string table, `n_strx`. To specify an empty string (`""`), set this value to 0. The `n_name` field is not used in Mach-O files.
- [n_sect](nlist/1583924-n_sect.md)
  An integer specifying the number of the section that this symbol can be found in, or `NO_SECT` if the symbol is not to be found in any section of this image. The sections are contiguously numbered across segments, starting from 1, according to the order they appear in the `LC_SEGMENT` load commands.
- [n_desc](nlist/1583952-n_desc.md)
  A 16-bit value providing additional information about the nature of this symbol for non-stab symbols. The reference flags can be accessed using the `REFERENCE_TYPE` mask (0xF) and are defined as follows:
- [n_value](nlist/1583940-n_value.md)
  An integer that contains the value of the symbol. The format of this value is different for each type of symbol table entry (as specified by the `n_type` field). For the `N_SECT` symbol type, `n_value` is the address of the symbol. See the description of the `n_type` field for information on other possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/nlist/1583961-n_type)*
# nlist

**Framework**: Kernel  
**Kind**: tag

Describes an entry in the symbol table for 32-bit architectures. Declared in `/usr/include/mach-o/nlist.h`. See also [`nlist_64`](nlist_64.md).

**Availability**:
- macOS 10.8+

## Declaration

```swift
struct nlist {
    ...
};
```

#### Discussion

Common symbols must be of type `N_UNDF` and must have the `N_EXT` bit set. The `n_value` for a common symbol is the size (in bytes) of the data of the symbol. In C, a common symbol is a variable that is declared but not initialized in this file. Common symbols can appear only in `MH_OBJECT` Mach-O files.

## Topics

### Fields
- [n_un](nlist/1583921-n_un.md)
  A union that holds an index into the string table, `n_strx`. To specify an empty string (`""`), set this value to 0. The `n_name` field is not used in Mach-O files.
- [n_type](nlist/1583961-n_type.md)
  A byte value consisting of data accessed using four bit masks:
- [n_sect](nlist/1583924-n_sect.md)
  An integer specifying the number of the section that this symbol can be found in, or `NO_SECT` if the symbol is not to be found in any section of this image. The sections are contiguously numbered across segments, starting from 1, according to the order they appear in the `LC_SEGMENT` load commands.
- [n_desc](nlist/1583952-n_desc.md)
  A 16-bit value providing additional information about the nature of this symbol for non-stab symbols. The reference flags can be accessed using the `REFERENCE_TYPE` mask (0xF) and are defined as follows:
- [n_value](nlist/1583940-n_value.md)
  An integer that contains the value of the symbol. The format of this value is different for each type of symbol table entry (as specified by the `n_type` field). For the `N_SECT` symbol type, `n_value` is the address of the symbol. See the description of the `n_type` field for information on other possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/nlist)*
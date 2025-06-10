# r_address

**Framework**: Kernel  
**Kind**: structp

In `MH_OBJECT` files, an offset from the start of the section to the item containing the address requiring relocation.

**Availability**:
- macOS 10.8+

## Declaration

```swift
int32_t r_address;
```

#### Discussion

In images used by the dynamic linker, this is an offset from the virtual memory address of the data of the first [`segment_command`](segment_command.md) that appears in the file (not necessarily the one with the lowest address). For images with the `MH_SPLIT_SEGS` flag set, this is an offset from the virtual memory address of data of the first read/write [`segment_command`](segment_command.md).

If the high bit of this field is set (which you can check using the `R_SCATTERED` bit mask), the relocation_info structure is actually a [`scattered_relocation_info`](scattered_relocation_info.md) structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/relocation_info/1577793-r_address)*
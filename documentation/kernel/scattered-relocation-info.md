# scattered_relocation_info

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.8+

## Declaration

```swift
struct scattered_relocation_info {
    ...
};
```

## Topics

### Instance Properties
- [r_address](scattered_relocation_info/1577782-r_address.md)
- [r_length](scattered_relocation_info/1577783-r_length.md)
- [r_pcrel](scattered_relocation_info/1577780-r_pcrel.md)
  Indicates whether the item containing the address to be relocated is part of a CPU instruction that uses PC-relative addressing.
- [r_scattered](scattered_relocation_info/1577787-r_scattered.md)
  If this bit is 0, this structure is actually a [`relocation_info`](relocation_info.md) structure.
- [r_type](scattered_relocation_info/1577795-r_type.md)
  Indicates the type of relocation to be performed. Possible values for this field are shared between this structure and the `relocation_info` data structure; see the description of the `r_type` field in the [`relocation_info`](relocation_info.md) data structure for more details.
- [r_value](scattered_relocation_info/1577799-r_value.md)
  The address of the relocatable expression for the item in the file that needs to be updated if the address is changed. For relocatable expressions with the difference of two section addresses, the address from which to subtract (in mathematical terms, the minuend) is contained in the first relocation entry and the address to subtract (the subtrahend) is contained in the second relocation entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scattered_relocation_info)*
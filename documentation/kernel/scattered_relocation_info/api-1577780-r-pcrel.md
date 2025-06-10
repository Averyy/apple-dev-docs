# r_pcrel

**Framework**: Kernel  
**Kind**: structp

Indicates whether the item containing the address to be relocated is part of a CPU instruction that uses PC-relative addressing.

**Availability**:
- macOS 10.8+

## Declaration

```swift
uint32_t r_pcrel:1;
```

#### Discussion

For addresses contained in PC-relative instructions, the CPU adds the address of the instruction to the address contained in the instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scattered_relocation_info/1577780-r_pcrel)*
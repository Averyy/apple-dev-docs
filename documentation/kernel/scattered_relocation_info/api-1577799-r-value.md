# r_value

**Framework**: Kernel  
**Kind**: structp

The address of the relocatable expression for the item in the file that needs to be updated if the address is changed. For relocatable expressions with the difference of two section addresses, the address from which to subtract (in mathematical terms, the minuend) is contained in the first relocation entry and the address to subtract (the subtrahend) is contained in the second relocation entry.

**Availability**:
- macOS 10.8+

## Declaration

```swift
int32_t r_value;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/scattered_relocation_info/1577799-r_value)*
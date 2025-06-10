# GetOffset

**Framework**: Kernel  
**Kind**: instm

Returns the offset from the original start of the memory block.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
uint64_t GetOffset(void);
```

#### Return_value

The number of bytes from the start of the original block of memory to the first byte of this memory map object.

#### Discussion

When creating a memory map object, you can map to a location in the middle of the underlying buffer. You might do this to access a specific structure inside that buffer. This method returns the offset from the original start of the buffer to the first byte of your mapping.

## See Also

- [- GetAddress](../driverkit/iomemorymap/getaddress.md)
  Returns the address of the memory block.
- [- GetLength](../driverkit/iomemorymap/getlength.md)
  Returns the length of the memory block in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorymap/3438204-getoffset)*
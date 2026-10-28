# GetAddress

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns the address of the memory block.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```c
uint64_t GetAddress(void);
```

## Return Value

The address of the first byte of the memory block in the current process.

## See Also

### Getting the Map Attributes
- [- GetLength](./api-3180657-getlength.md)
  Returns the length of the memory block in bytes.
- [- GetOffset](./api-3438204-getoffset.md)
  Returns the offset from the original start of the memory block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorymap/3180656-getaddress)*
# GetLength

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns the length of the memory block in bytes.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```c
uint64_t GetLength(void);
```

## Return Value

The number of bytes in the memory block.

## Discussion

The length represents the number of bytes that are accessible to the current process.

## See Also

### Getting the Map Attributes
- [- GetAddress](./api-3180656-getaddress.md)
  Returns the address of the memory block.
- [- GetOffset](./api-3438204-getoffset.md)
  Returns the offset from the original start of the memory block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorymap/3180657-getlength)*
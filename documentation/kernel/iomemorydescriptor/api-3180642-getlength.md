# GetLength

**Framework**: Kernel  
**Kind**: instm

Returns the length of the memory block represented by this object.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
kern_return_t GetLength(uint64_t *returnLength);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes). 

#### Discussion

This method returns the effective size of the memory block, which might be less than the block's total capacity.  

## Parameters

- `returnLength`: A variable in which to put the length of the current memory block. 

## See Also

- [- SetLength](iobuffermemorydescriptor/3180454-setlength.md)
  Changes the length of the memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/3180642-getlength)*
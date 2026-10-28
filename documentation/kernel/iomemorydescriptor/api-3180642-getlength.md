# GetLength

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Returns the length of the memory block represented by this object.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```c
kern_return_t GetLength(uint64_t *returnLength);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md). 

## Discussion

This method returns the effective size of the memory block, which might be less than the block's total capacity.  

## Parameters

- `returnLength`: A variable in which to put the length of the current memory block. 

## See Also

### Related Documentation
- [- SetLength](../iobuffermemorydescriptor/api-3180454-setlength.md)
  Changes the length of the memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/3180642-getlength)*
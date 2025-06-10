# getBytesNoCopy

**Framework**: Kernel  
**Kind**: instm

Returns the virtual address of an offset into the memory buffer. 

**Availability**:
- macOS 10.15.2+

## Declaration

```swift
virtual void * getBytesNoCopy(vm_size_t start, vm_size_t withLength);
```

#### Return_value

The address at the specified offset into the bufer, or `NULL` if the offset and length yield an invalid address range.

## Parameters

- `start`: The offset from the beginning of the memory buffer.
- `withLength`: The number of bytes you want. 

## See Also

- [- getBytesNoCopy](iobuffermemorydescriptor/1574840-getbytesnocopy.md)
  Returns the virtual address of the beginning of the memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/3516445-getbytesnocopy)*
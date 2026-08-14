# Create

**Framework**: Kernel  
**Kind**: clm

Creates a new memory buffer descriptor object in the current process space.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
static kern_return_t Create(uint64_t options, uint64_t capacity, uint64_t alignment, IOBufferMemoryDescriptor **memory);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes). 

## Parameters

- `options`: The direction in which buffer data moves, relative to your process. For example, specify [`kIOMemoryDirectionIn`](https://developer.apple.com/documentation/driverkit/kiomemorydirectionin) if your driver only reads from the buffer. For a list of possible values, see `Memory Buffer Options`.
- `capacity`: The maximum number of bytes to allocate for the memory buffer. The buffer's initial length is set to the value in this parameter. You can change the length later by calling the [`SetLength`](iobuffermemorydescriptor/3180454-setlength.md) method.
- `alignment`: The minimum required alignment of the buffer in bytes. For example, specify 256 to align the buffer on an address where bits 0 to 7 are `0`. Specify `0` if you don't require a specific alignment. 
- `memory`: A variable in which to store the newly created buffer memory descriptor. 

## See Also

- [- init](../driverkit/iobuffermemorydescriptor/init.md)
  Initializes the buffer memory descriptor object.
- [- free](iobuffermemorydescriptor/3180456-free.md)
  Performs any final cleanup for the memory buffer descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/3180450-create)*
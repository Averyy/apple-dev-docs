# withCapacity

**Framework**: Kernel  
**Kind**: clm

Creates a buffer memory descriptor and allocates enough bytes to meet the specified capacity.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
static OSPtr<IOBufferMemoryDescriptor> withCapacity(vm_size_t capacity, IODirection withDirection, bool withContiguousMemory);
```

## Parameters

- `capacity`: The number of bytes to allocate.
- `withDirection`: The direction of the I/O transfer. For example: kIODirectionOut, kIODirectionIn.
- `withContiguousMemory`: A Boolean value that indicates whether to use a contiguous block of memory for the descriptor’s buffer. 

## See Also

- [inTaskWithOptions](iobuffermemorydescriptor/1813824-intaskwithoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ inTaskWithOptions](iobuffermemorydescriptor/1574847-intaskwithoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ inTaskWithOptions](iobuffermemorydescriptor/3516446-intaskwithoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [inTaskWithPhysicalMask](iobuffermemorydescriptor/1813825-intaskwithphysicalmask.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ inTaskWithPhysicalMask](iobuffermemorydescriptor/1574843-intaskwithphysicalmask.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [- initWithPhysicalMask](iobuffermemorydescriptor/1574833-initwithphysicalmask.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ withOptions](iobuffermemorydescriptor/1574835-withoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ withBytes](iobuffermemorydescriptor/1574834-withbytes.md)
  Creates a buffer memory descriptor and fills it with the specified bytes.
- [+ withCopy](iobuffermemorydescriptor/3074961-withcopy.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [- free](../driverkit/iobuffermemorydescriptor/free.md)
  Performs any final cleanup for the memory buffer descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/1574841-withcapacity)*
# withBytes

**Framework**: Kernel  
**Kind**: clm

Creates a buffer memory descriptor and fills it with the specified bytes.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
static OSPtr<IOBufferMemoryDescriptor> withBytes(const void *bytes, vm_size_t withLength, IODirection withDirection, bool withContiguousMemory);
```

## Parameters

- `bytes`: The bytes to copy into the newly allocated buffer. 
- `withLength`: The number of bytes in the   parameter.
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
- [+ withCapacity](iobuffermemorydescriptor/1574841-withcapacity.md)
  Creates a buffer memory descriptor and allocates enough bytes to meet the specified capacity.
- [+ withCopy](iobuffermemorydescriptor/3074961-withcopy.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [- free](../driverkit/iobuffermemorydescriptor/free.md)
  Performs any final cleanup for the memory buffer descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/1574834-withbytes)*
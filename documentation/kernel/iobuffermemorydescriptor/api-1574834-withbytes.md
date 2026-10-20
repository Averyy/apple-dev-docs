# withBytes

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

Creates a buffer memory descriptor and fills it with the specified bytes.

**Availability**:
- macOS 10.11.4+

## Declaration

```c
static OSPtr<IOBufferMemoryDescriptor> withBytes(const void *bytes, vm_size_t withLength, IODirection withDirection, bool withContiguousMemory);
```

## Parameters

- `bytes`: The bytes to copy into the newly allocated buffer. 
- `withLength`: The number of bytes in the `bytes` parameter.
- `withDirection`: The direction of the I/O transfer. For example: kIODirectionOut, kIODirectionIn.
- `withContiguousMemory`: A Boolean value that indicates whether to use a contiguous block of memory for the descriptor’s buffer. 

## See Also

### Creating a Memory Buffer Descriptor
- [inTaskWithOptions](./api-1813824-intaskwithoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ inTaskWithOptions](./api-1574847-intaskwithoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ inTaskWithOptions](./api-3516446-intaskwithoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [inTaskWithPhysicalMask](./api-1813825-intaskwithphysicalmask.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ inTaskWithPhysicalMask](./api-1574843-intaskwithphysicalmask.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [- initWithPhysicalMask](./api-1574833-initwithphysicalmask.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ withOptions](./api-1574835-withoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ withCapacity](./api-1574841-withcapacity.md)
  Creates a buffer memory descriptor and allocates enough bytes to meet the specified capacity.
- [+ withCopy](./api-3074961-withcopy.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [- free](./api-3180456-free.md)
  Performs any final cleanup for the memory buffer descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/1574834-withbytes)*
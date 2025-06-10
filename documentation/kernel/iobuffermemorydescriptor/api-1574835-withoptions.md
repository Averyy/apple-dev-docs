# withOptions

**Framework**: Kernel  
**Kind**: clm

Creates a memory buffer with memory descriptor for that buffer.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
static OSPtr<IOBufferMemoryDescriptor> withOptions(IOOptionBits options, vm_size_t capacity, vm_offset_t alignment);
```

#### Return_value

Returns an instance of class IOBufferMemoryDescriptor to be released by the caller, which will free the memory desriptor and associated buffer.

#### Discussion

Added in OS X 10.2, this method allocates a memory buffer with a given size and alignment in the task's address space specified, and returns a memory descriptor instance representing the memory. It is recommended that memory allocated for I/O or sharing via mapping be created via IOBufferMemoryDescriptor. Options passed with the request specify the kind of memory to be allocated - pageablity and sharing are specified with option bits. This function may block and so should not be called from interrupt level or while a simple lock is held.

## Parameters

- `options`: kIOMapWriteCombineCache - allocate memory with writecombined cache setting.
- `capacity`: The number of bytes to allocate.
- `alignment`: The minimum required alignment of the buffer in bytes - 1 is the default for no required alignment. For example, pass 256 to get memory allocated at an address with bits 0-7 zero.

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
- [+ withBytes](iobuffermemorydescriptor/1574834-withbytes.md)
  Creates a buffer memory descriptor and fills it with the specified bytes.
- [+ withCapacity](iobuffermemorydescriptor/1574841-withcapacity.md)
  Creates a buffer memory descriptor and allocates enough bytes to meet the specified capacity.
- [+ withCopy](iobuffermemorydescriptor/3074961-withcopy.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [- free](../driverkit/iobuffermemorydescriptor/free.md)
  Performs any final cleanup for the memory buffer descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/1574835-withoptions)*
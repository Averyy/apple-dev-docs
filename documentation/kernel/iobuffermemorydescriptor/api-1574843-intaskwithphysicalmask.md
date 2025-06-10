# inTaskWithPhysicalMask

**Framework**: Kernel  
**Kind**: clm

Creates a memory buffer with memory descriptor for that buffer.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
static OSPtr<IOBufferMemoryDescriptor> inTaskWithPhysicalMask(task_t inTask, IOOptionBits options, mach_vm_size_t capacity, mach_vm_address_t physicalMask);
```

#### Return_value

Returns an instance of class IOBufferMemoryDescriptor to be released by the caller, which will free the memory desriptor and associated buffer.

#### Discussion

Added in OS X 10.5, this method allocates a memory buffer with a given size and alignment in the task's address space specified, and returns a memory descriptor instance representing the memory. It is recommended that memory allocated for I/O or sharing via mapping be created via IOBufferMemoryDescriptor. Options passed with the request specify the kind of memory to be allocated - pageablity and sharing are specified with option bits. This function may block and so should not be called from interrupt level or while a simple lock is held.

## Parameters

- `inTask`: The task the buffer will be mapped in. Pass NULL to create memory unmapped in any task (eg. for use as a DMA buffer).
- `options`: kIOMapWriteCombineCache - allocate memory with writecombined cache setting.
- `capacity`: The number of bytes to allocate.
- `physicalMask`: The buffer will be allocated with pages such that physical addresses will only have bits set present in physicalMask. For example, pass 0x00000000FFFFFFFFULL for a buffer to be accessed by hardware that has 32 address bits.

## See Also

- [inTaskWithOptions](iobuffermemorydescriptor/1813824-intaskwithoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ inTaskWithOptions](iobuffermemorydescriptor/1574847-intaskwithoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ inTaskWithOptions](iobuffermemorydescriptor/3516446-intaskwithoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [inTaskWithPhysicalMask](iobuffermemorydescriptor/1813825-intaskwithphysicalmask.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [- initWithPhysicalMask](iobuffermemorydescriptor/1574833-initwithphysicalmask.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ withOptions](iobuffermemorydescriptor/1574835-withoptions.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/1574843-intaskwithphysicalmask)*
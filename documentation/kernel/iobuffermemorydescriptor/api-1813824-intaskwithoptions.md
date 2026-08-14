# inTaskWithOptions

**Framework**: Kernel  
**Kind**: instm

Creates a memory buffer with memory descriptor for that buffer.

## Declaration

```swift
static IOBufferMemoryDescriptor * inTaskWithOptions( 
 task_t inTask, 
 IOOptionBits options, 
 vm_size_t capacity, 
 vm_offset_t alignment = 1);
```

#### Return_value

Returns an instance of class IOBufferMemoryDescriptor to be released by the caller, which will free the memory desriptor and associated buffer.

#### Overview

Added in OS X 10.2, this method allocates a memory buffer with a given size and alignment in the task's address space specified, and returns a memory descriptor instance representing the memory. It is recommended that memory allocated for I/O or sharing via mapping be created via IOBufferMemoryDescriptor. Options passed with the request specify the kind of memory to be allocated - pageablity and sharing are specified with option bits. This function may block and so should not be called from interrupt level or while a simple lock is held.

## Parameters

- `inTask`: The task the buffer will be allocated in.
- `options`: Options for the allocation: kIODirectionOut, kIODirectionIn - set the direction of the I/O transfer. kIOMemoryPhysicallyContiguous - pass to request memory be physically contiguous. This option is heavily discouraged. The request may fail if memory is fragmented, may cause large amounts of paging activity, and may take a very long time to execute. kIOMemoryPageable - pass to request memory be non-wired - the default for kernel allocated memory is wired. kIOMemoryPurgeable - pass to request memory that may later have its purgeable state set with IOMemoryDescriptor::setPurgeable. Only supported for kIOMemoryPageable allocations. kIOMemoryKernelUserShared - pass to request memory that will be mapped into both the kernel and client applications. kIOMapInhibitCache - allocate memory with inhibited cache setting. kIOMapWriteThruCache - allocate memory with writethru cache setting. kIOMapCopybackCache - allocate memory with copyback cache setting. kIOMapWriteCombineCache - allocate memory with writecombined cache setting.
- `capacity`: The number of bytes to allocate.
- `alignment`: The minimum required alignment of the buffer in bytes - 1 is the default for no required alignment. For example, pass 256 to get memory allocated at an address with bits 0-7 zero.

## See Also

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
- [+ withCapacity](iobuffermemorydescriptor/1574841-withcapacity.md)
  Creates a buffer memory descriptor and allocates enough bytes to meet the specified capacity.
- [+ withCopy](iobuffermemorydescriptor/3074961-withcopy.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [- free](iobuffermemorydescriptor/3180456-free.md)
  Performs any final cleanup for the memory buffer descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/1813824-intaskwithoptions)*
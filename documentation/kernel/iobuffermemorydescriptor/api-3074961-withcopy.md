# withCopy

**Framework**: Kernel  
**Kind**: clm

Creates a memory buffer with memory descriptor for that buffer.

**Availability**:
- macOS 10.15+

## Declaration

```swift
static OSPtr<IOBufferMemoryDescriptor> withCopy(task_t inTask, IOOptionBits options, vm_map_t sourceMap, mach_vm_address_t source, mach_vm_size_t size);
```

#### Return_value

Returns an instance of class IOBufferMemoryDescriptor to be released by the caller, which will free the memory desriptor and associated buffer.

## Parameters

- `inTask`: The task the buffer will be allocated in.
- `options`: kIOMapWriteCombineCache - allocate memory with writecombined cache setting.
- `sourceMap`: The memory map to copy from.
- `source`: The address at which to start copying.
- `size`: The number of bytes to copy.

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
- [+ withCapacity](iobuffermemorydescriptor/1574841-withcapacity.md)
  Creates a buffer memory descriptor and allocates enough bytes to meet the specified capacity.
- [- free](../driverkit/iobuffermemorydescriptor/free.md)
  Performs any final cleanup for the memory buffer descriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/3074961-withcopy)*
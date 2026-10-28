# IOBufferMemoryDescriptor

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

A simple memory descriptor that allocates its own buffer memory.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOBufferMemoryDescriptor : IOGeneralMemoryDescriptor
```

## Overview

Use an [`IOBufferMemoryDescriptor`](./iobuffermemorydescriptor.md) object to store data and share it with the kernel. 

## Topics

### Creating a Memory Buffer Descriptor
- [inTaskWithOptions](./iobuffermemorydescriptor/api-1813824-intaskwithoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ inTaskWithOptions](./iobuffermemorydescriptor/api-1574847-intaskwithoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ inTaskWithOptions](./iobuffermemorydescriptor/api-3516446-intaskwithoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [inTaskWithPhysicalMask](./iobuffermemorydescriptor/api-1813825-intaskwithphysicalmask.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ inTaskWithPhysicalMask](./iobuffermemorydescriptor/api-1574843-intaskwithphysicalmask.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [- initWithPhysicalMask](./iobuffermemorydescriptor/api-1574833-initwithphysicalmask.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ withOptions](./iobuffermemorydescriptor/api-1574835-withoptions.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [+ withBytes](./iobuffermemorydescriptor/api-1574834-withbytes.md)
  Creates a buffer memory descriptor and fills it with the specified bytes.
- [+ withCapacity](./iobuffermemorydescriptor/api-1574841-withcapacity.md)
  Creates a buffer memory descriptor and allocates enough bytes to meet the specified capacity.
- [+ withCopy](./iobuffermemorydescriptor/api-3074961-withcopy.md)
  Creates a memory buffer with memory descriptor for that buffer.
- [- free](./iobuffermemorydescriptor/api-3180456-free.md)
  Performs any final cleanup for the memory buffer descriptor object.
### Configuring the Descriptor
- [- getCapacity](./iobuffermemorydescriptor/api-1574844-getcapacity.md)
  Returns the number of bytes the buffer is capable of holding. 
- [- setDirection](./iobuffermemorydescriptor/api-1574826-setdirection.md)
  Changes the direction associated with the buffer’s memory transfers.
- [- setLength](./iobuffermemorydescriptor/api-1574850-setlength.md)
  Sets the length of the data in the buffer.
### Adding Data to the Buffer
- [- appendBytes](./iobuffermemorydescriptor/api-1574849-appendbytes.md)
  Adds the specified data to the end of the memory buffer.
### Getting the Buffer Contents
- [- getBytesNoCopy](./iobuffermemorydescriptor/api-1574840-getbytesnocopy.md)
  Returns the virtual address of the beginning of the memory buffer.
- [- getBytesNoCopy](./iobuffermemorydescriptor/api-3516445-getbytesnocopy.md)
  Returns the virtual address of an offset into the memory buffer. 
### Managing Internal Structures
- [ExpansionData](./ioservice/expansiondata.md)
- [reserved](./iobuffermemorydescriptor/reserved.md)
- [+ Create](./iobuffermemorydescriptor/api-3180450-create.md)
  Creates a new memory buffer descriptor object in the current process space.
- [+ Create_Impl](./iobuffermemorydescriptor/api-3074954-create_impl.md)
- [+ Create_Invoke](./iobuffermemorydescriptor/api-3180451-create_invoke.md)
- [- GetAddressRange](./iobuffermemorydescriptor/api-3180453-getaddressrange.md)
  Returns the address and length of the memory buffer.
- [- getMetaClass](./iobuffermemorydescriptor/api-1574832-getmetaclass.md)
- [+ SetLength_Invoke](./iobuffermemorydescriptor/api-3131492-setlength_invoke.md)
- [- SetLength](./iobuffermemorydescriptor/api-3180454-setlength.md)
  Changes the length of the memory buffer.
- [- SetLength_Impl](./iobuffermemorydescriptor/api-3131491-setlength_impl.md)
- [- Dispatch](./iobuffermemorydescriptor/api-3180452-dispatch.md)

## Relationships

### Inherits From
- [IOGeneralMemoryDescriptor](./iogeneralmemorydescriptor.md)

## See Also

### Descriptors
- [IODeviceMemory](./iodevicememory.md)
  An IOMemoryDescriptor used for device physical memory ranges.
- [IOGeneralMemoryDescriptor](./iogeneralmemorydescriptor.md)
- [IOInterleavedMemoryDescriptor](./iointerleavedmemorydescriptor.md)
  The IOInterleavedMemoryDescriptor object describes a memory area made up of portions of several other IOMemoryDescriptors.
- [IOMultiMemoryDescriptor](./iomultimemorydescriptor.md)
  The IOMultiMemoryDescriptor object describes a memory area made up of several other IOMemoryDescriptors.
- [IOSubMemoryDescriptor](./iosubmemorydescriptor.md)
  The IOSubMemoryDescriptor object describes a memory area made up of a portion of another IOMemoryDescriptor.
- [IOMemoryDescriptor](./iomemorydescriptor.md)
  An abstract base class that defines common methods for describing physical or virtual memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor)*
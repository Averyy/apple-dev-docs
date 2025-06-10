# Create_Impl

**Framework**: Kernel  
**Kind**: clm

**Availability**:
- macOS 10.15+

## Declaration

```swift
static kern_return_t Create_Impl(uint64_t options, uint64_t capacity, uint64_t alignment, IOBufferMemoryDescriptor **memory);
```

## See Also

- [ExpansionData](ioservice/expansiondata.md)
- [reserved](iobuffermemorydescriptor/reserved.md)
- [+ Create](../driverkit/iobuffermemorydescriptor/create.md)
  Creates a new memory buffer descriptor object in the current process space.
- [+ Create_Invoke](iobuffermemorydescriptor/3180451-create_invoke.md)
- [- GetAddressRange](../driverkit/iobuffermemorydescriptor/getaddressrange.md)
  Returns the address and length of the memory buffer.
- [- getMetaClass](iobuffermemorydescriptor/1574832-getmetaclass.md)
- [+ SetLength_Invoke](iobuffermemorydescriptor/3131492-setlength_invoke.md)
- [- SetLength](../driverkit/iobuffermemorydescriptor/setlength.md)
  Changes the length of the memory buffer.
- [- SetLength_Impl](iobuffermemorydescriptor/3131491-setlength_impl.md)
- [- Dispatch](iobuffermemorydescriptor/3180452-dispatch.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/3074954-create_impl)*
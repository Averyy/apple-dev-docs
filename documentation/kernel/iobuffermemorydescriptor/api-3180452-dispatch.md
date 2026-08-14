# Dispatch

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.15+

## Declaration

```swift
virtual kern_return_t Dispatch(const IORPC rpc);
```

## See Also

- [ExpansionData](ioservice/expansiondata.md)
- [reserved](iobuffermemorydescriptor/reserved.md)
- [+ Create](iobuffermemorydescriptor/3180450-create.md)
  Creates a new memory buffer descriptor object in the current process space.
- [+ Create_Impl](iobuffermemorydescriptor/3074954-create_impl.md)
- [+ Create_Invoke](iobuffermemorydescriptor/3180451-create_invoke.md)
- [- GetAddressRange](iobuffermemorydescriptor/3180453-getaddressrange.md)
  Returns the address and length of the memory buffer.
- [- getMetaClass](iobuffermemorydescriptor/1574832-getmetaclass.md)
- [+ SetLength_Invoke](iobuffermemorydescriptor/3131492-setlength_invoke.md)
- [- SetLength](iobuffermemorydescriptor/3180454-setlength.md)
  Changes the length of the memory buffer.
- [- SetLength_Impl](iobuffermemorydescriptor/3131491-setlength_impl.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/3180452-dispatch)*
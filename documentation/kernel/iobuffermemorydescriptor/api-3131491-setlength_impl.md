# SetLength_Impl

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.15+

## Declaration

```c
kern_return_t SetLength_Impl(uint64_t length);
```

## See Also

### Managing Internal Structures
- [ExpansionData](../ioservice/expansiondata.md)
- [reserved](./reserved.md)
- [+ Create](./api-3180450-create.md)
  Creates a new memory buffer descriptor object in the current process space.
- [+ Create_Impl](./api-3074954-create_impl.md)
- [+ Create_Invoke](./api-3180451-create_invoke.md)
- [- GetAddressRange](./api-3180453-getaddressrange.md)
  Returns the address and length of the memory buffer.
- [- getMetaClass](./api-1574832-getmetaclass.md)
- [+ SetLength_Invoke](./api-3131492-setlength_invoke.md)
- [- SetLength](./api-3180454-setlength.md)
  Changes the length of the memory buffer.
- [- Dispatch](./api-3180452-dispatch.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/3131491-setlength_impl)*
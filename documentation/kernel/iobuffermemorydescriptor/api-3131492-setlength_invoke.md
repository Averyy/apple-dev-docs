# SetLength_Invoke

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

**Availability**:
- macOS 10.15+

## Declaration

```c
static kern_return_t SetLength_Invoke(const IORPC rpc, OSMetaClassBase *target, SetLength_Handler func);
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
- [- SetLength](./api-3180454-setlength.md)
  Changes the length of the memory buffer.
- [- SetLength_Impl](./api-3131491-setlength_impl.md)
- [- Dispatch](./api-3180452-dispatch.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor/3131492-setlength_invoke)*
# CreateMapping_Impl

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.15+

## Declaration

```c
kern_return_t CreateMapping_Impl(uint64_t options, uint64_t address, uint64_t offset, uint64_t length, uint64_t alignment, IOMemoryMap **map);
```

## See Also

### Managing Internal Structures
- [reserved](./reserved.md)
- [+ initialize](./api-1441798-initialize.md)
- [- Dispatch](./api-3180641-dispatch.md)
- [+ CreateMapping_Invoke](./api-3174976-createmapping_invoke.md)
- [- populateDevicePager](./api-1442017-populatedevicepager.md)
- [- CreateMapping](./api-3174974-createmapping.md)
- [- Map](./api-3180643-map.md)
  Maps memory internally. 
- [- addMapping](./api-1442013-addmapping.md)
- [- removeMapping](./api-1441778-removemapping.md)
- [- makeMapping](./api-1441923-makemapping.md)
- [- doMap](./api-1441941-domap.md)
- [- doUnmap](./api-1441883-dounmap.md)
- [- handleFault](./api-1441782-handlefault.md)
- [- redirect](./api-1441871-redirect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/3174975-createmapping_impl)*
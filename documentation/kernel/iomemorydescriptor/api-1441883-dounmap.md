# doUnmap

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn doUnmap(vm_map_t addressMap, IOVirtualAddress logical, IOByteCount length);
```

## See Also

- [reserved](iomemorydescriptor/reserved.md)
- [+ initialize](iomemorydescriptor/1441798-initialize.md)
- [- Dispatch](iomemorydescriptor/3180641-dispatch.md)
- [+ CreateMapping_Invoke](iomemorydescriptor/3174976-createmapping_invoke.md)
- [- populateDevicePager](iomemorydescriptor/1442017-populatedevicepager.md)
- [- CreateMapping](iomemorydescriptor/3174974-createmapping.md)
- [- CreateMapping_Impl](iomemorydescriptor/3174975-createmapping_impl.md)
- [- Map](../driverkit/iomemorydescriptor/map.md)
  Maps memory internally.
- [- addMapping](iomemorydescriptor/1442013-addmapping.md)
- [- removeMapping](iomemorydescriptor/1441778-removemapping.md)
- [- makeMapping](iomemorydescriptor/1441923-makemapping.md)
- [- doMap](iomemorydescriptor/1441941-domap.md)
- [- handleFault](iomemorydescriptor/1441782-handlefault.md)
- [- redirect](iomemorydescriptor/1441871-redirect.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1441883-dounmap)*
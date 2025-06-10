# setMapping

**Framework**: Kernel  
**Kind**: instm

Establishes an already existing mapping.

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual OSPtr<IOMemoryMap> setMapping(task_t task, IOVirtualAddress mapAddress, IOOptionBits options);
```

#### Return_value

A IOMemoryMap object created to represent the mapping.

#### Discussion

This method tells the IOMemoryDescriptor about a mapping that exists, but was created elsewhere. It allows later callers of the map method to share this externally created mapping. The IOMemoryMap object returned is created to represent it. This method is not commonly needed.

## Parameters

- `task`: Address space in which the mapping exists.
- `mapAddress`: Virtual address of the mapping.
- `options`: Caching and read-only attributes of the mapping.

## See Also

- [createMappingInTask](iomemorydescriptor/1812752-createmappingintask.md)
  Maps an IOMemoryDescriptor into a task.
- [- createMappingInTask](iomemorydescriptor/1441859-createmappingintask.md)
  Maps an IOMemoryDescriptor into a task.
- [map](iomemorydescriptor/1812830-map.md)
  Maps an IOMemoryDescriptor into the kernel map.
- [- map](iomemorydescriptor/1441908-map.md)
  Maps an IOMemoryDescriptor into the kernel map.
- [setMapping](iomemorydescriptor/1812859-setmapping.md)
  Establishes an already existing mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/1441948-setmapping)*
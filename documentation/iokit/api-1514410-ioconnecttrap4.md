# IOConnectTrap4(_:_:_:_:_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func IOConnectTrap4(_ connect: io_connect_t, _ index: UInt32, _ p1: UInt, _ p2: UInt, _ p3: UInt, _ p4: UInt) -> kern_return_t
```

```c
kern_return_t IOConnectTrap4(io_connect_t connect, uint32_t index, uintptr_t p1, uintptr_t p2, uintptr_t p3, uintptr_t p4);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514410-ioconnecttrap4)*
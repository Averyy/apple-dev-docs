# IOConnectTrap1(_:_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func IOConnectTrap1(_ connect: io_connect_t, _ index: UInt32, _ p1: UInt) -> kern_return_t
```

```c
kern_return_t IOConnectTrap1(io_connect_t connect, uint32_t index, uintptr_t p1);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514816-ioconnecttrap1)*
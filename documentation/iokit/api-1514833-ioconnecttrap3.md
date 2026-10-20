# IOConnectTrap3(_:_:_:_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func IOConnectTrap3(_ connect: io_connect_t, _ index: UInt32, _ p1: UInt, _ p2: UInt, _ p3: UInt) -> kern_return_t
```

```c
kern_return_t IOConnectTrap3(io_connect_t connect, uint32_t index, uintptr_t p1, uintptr_t p2, uintptr_t p3);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514833-ioconnecttrap3)*
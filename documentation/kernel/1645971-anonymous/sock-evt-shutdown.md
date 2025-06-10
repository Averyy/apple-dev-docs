# sock_evt_shutdown

**Framework**: Kernel  
**Kind**: econst

**Availability**:
- macOS 10.12+

## Declaration

```swift
sock_evt_shutdown = 6
```

#### Discussion

The read and or write side(s) of the connection have been shutdown. The param will point to an integer that indicates the direction that has been shutdown. See 'man 2 shutdown' for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1645971-anonymous/sock_evt_shutdown)*
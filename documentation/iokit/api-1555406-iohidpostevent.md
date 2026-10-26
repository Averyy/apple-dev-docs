# IOHIDPostEvent

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 18.4+ - Deprecated in 14.2
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```c
kern_return_t IOHIDPostEvent(io_connect_t connect, UInt32 eventType, IOGPoint location, const NXEventData *eventData, UInt32 eventDataVersion, IOOptionBits eventFlags, IOOptionBits options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1555406-iohidpostevent)*
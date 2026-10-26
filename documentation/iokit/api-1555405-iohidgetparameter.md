# IOHIDGetParameter

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.12

## Declaration

```c
kern_return_t IOHIDGetParameter(io_connect_t handle, CFStringRef key, IOByteCount maxSize, void *bytes, IOByteCount *actualSize);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1555405-iohidgetparameter)*
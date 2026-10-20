# IOServiceAuthorize(_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func IOServiceAuthorize(_ service: io_service_t, _ options: UInt32) -> kern_return_t
```

```c
kern_return_t IOServiceAuthorize(io_service_t service, uint32_t options);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514533-ioserviceauthorize)*
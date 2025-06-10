# filterInterruptEventSource

**Framework**: Kernel  
**Kind**: clm

**Availability**:
- macOS 10.15.2+

## Declaration

```swift
static OSPtr<IOFilterInterruptEventSource> filterInterruptEventSource(OSObject *owner, IOService *provider, int intIndex, IOInterruptEventSource::ActionBlock action, FilterBlock filter);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterinterrupteventsource/3516454-filterinterrupteventsource)*
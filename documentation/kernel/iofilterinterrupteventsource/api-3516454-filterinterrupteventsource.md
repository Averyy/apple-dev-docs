# filterInterruptEventSource

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

**Availability**:
- macOS 10.15.2+

## Declaration

```cpp
static OSPtr<IOFilterInterruptEventSource> filterInterruptEventSource(OSObject *owner, IOService *provider, int intIndex, IOInterruptEventSource::ActionBlock action, FilterBlock filter);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofilterinterrupteventsource/3516454-filterinterrupteventsource)*
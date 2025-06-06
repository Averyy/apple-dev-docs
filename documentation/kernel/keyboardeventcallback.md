# KeyboardEventCallback

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.3+

## Declaration

```swift
typedef void (*KeyboardEventCallback)(OSObject *target, unsigned int eventType, unsigned int flags, unsigned int key, unsigned int charCode, unsigned int charSet, unsigned int origCharCode, unsigned int origCharSet, unsigned int keyboardType, bool repeat, AbsoluteTime ts, OSObject *sender, void *refcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/keyboardeventcallback)*
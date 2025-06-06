# KeyboardSpecialEventCallback

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.3+

## Declaration

```swift
typedef void (*KeyboardSpecialEventCallback)(OSObject *target, unsigned int eventType, unsigned int flags, unsigned int key, unsigned int flavor, UInt64 guid, bool repeat, AbsoluteTime ts, OSObject *sender, void *refcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/keyboardspecialeventcallback)*
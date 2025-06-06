# KeyboardEventAction

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.0+

## Declaration

```swift
typedef void (*KeyboardEventAction)(OSObject *target, unsigned int eventType, unsigned int flags, unsigned int key, unsigned int charCode, unsigned int charSet, unsigned int origCharCode, unsigned int origCharSet, unsigned int keyboardType, bool repeat, AbsoluteTime ts);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/keyboardeventaction)*
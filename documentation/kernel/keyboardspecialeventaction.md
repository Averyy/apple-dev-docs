# KeyboardSpecialEventAction

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- macOS 10.0+

## Declaration

```c
typedef void (*KeyboardSpecialEventAction)(OSObject *target, unsigned int eventType, unsigned int flags, unsigned int key, unsigned int flavor, UInt64 guid, bool repeat, AbsoluteTime ts);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/keyboardspecialeventaction)*
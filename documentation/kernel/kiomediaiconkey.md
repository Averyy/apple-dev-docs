# kIOMediaIconKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

A property of any object in the media stack.

**Availability**:
- macOS 10.2+

## Declaration

```c
#define kIOMediaIconKey
```

#### Discussion

kIOMediaIconKey is a property of any object in the media stack that wishes to override the default icon shown for the media objects in the stack. It is usually defined in a provider object below the media object. It has an OSDictionary value, with properties identical to the kIOIconKey definition, that is, kCFBundleIdentifierKey and kIOBundleResourceFileKey.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kiomediaiconkey)*
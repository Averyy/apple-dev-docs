# asyncRefCon

**Framework**: Core Services  
**Kind**: structp

A pointer to an arbitrary application-definedvalue, passed in the Carbon event notifying you of an application’slaunch or termination (if you have registered for such notification).The value of this field can be `NULL`.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

## Declaration

```swift
var asyncRefCon: UnsafeMutableRawPointer!
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/lslaunchfsrefspec/1450600-asyncrefcon)*
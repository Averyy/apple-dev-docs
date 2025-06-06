# FSEventStreamCopyDescription(_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
func FSEventStreamCopyDescription(_ streamRef: ConstFSEventStreamRef) -> CFString
```

#### Return_value

A CFStringRef containing the description of the supplied stream. Ownership follows the Copy rule.

#### Discussion

Returns a CFStringRef containing the description of the supplied stream. For debugging only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442676-fseventstreamcopydescription)*
# CollatorRef

**Framework**: Core Services  
**Kind**: tdef

Refers to an opaque object that encapsulates locale and collation information for the purpose of performing Unicode string comparison.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias CollatorRef = OpaquePointer
```

#### Discussion

You can obtain a `CollatorRef` value from the function  [`UCCreateCollator(_:_:_:_:)`](1390403-uccreatecollator.md). 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/collatorref)*
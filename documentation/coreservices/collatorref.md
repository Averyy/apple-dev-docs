# CollatorRef

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Refers to an opaque object that encapsulates locale and collation information for the purpose of performing Unicode string comparison.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias CollatorRef = OpaquePointer
```

```c
typedef struct OpaqueCollatorRef *CollatorRef;
```

## Discussion

You can obtain a `CollatorRef` value from the function  [`UCCreateCollator(_:_:_:_:)`](./api-1390403-uccreatecollator.md). 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/collatorref)*
# UTTypeConformsTo(_:_:)

**Framework**: Core Services  
**Kind**: func

Returns whether a uniform type identifier conforms to another uniform type identifier.

**Availability**:
- iOS 3.0+ - Deprecated in 15.0
- iPadOS 3.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.3+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 8.0

## Declaration

```swift
func UTTypeConformsTo(_ inUTI: CFString, _ inConformsToUTI: CFString) -> Bool
```

#### Return_value

Returns `true` if the uniform type identifier is equal to or conforms to the second type.

## Parameters

- `inUTI`: A uniform type identifier to compare.
- `inConformsToUTI`: The uniform type identifier to compare it to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444079-uttypeconformsto)*
# UTTypeEqual(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns whether two uniform type identifiers are equal.

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
func UTTypeEqual(_ inUTI1: CFString, _ inUTI2: CFString) -> Bool
```

```c
Boolean UTTypeEqual(CFStringRef inUTI1, CFStringRef inUTI2);
```

## Return Value

Returns `true` if the two uniform type identifiers are equivalent.

## Parameters

- `inUTI1`: A uniform type identifier.
- `inUTI2`: The uniform type identifier to compare it to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447783-uttypeequal)*
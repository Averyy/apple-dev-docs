# XPCLiteralValue

**Framework**: XPC  
**Kind**: struct

A type that bridges Swift literal values to XPC objects for use in dictionary literals.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS ?+
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct XPCLiteralValue
```

#### Overview

This type enables ergonomic dictionary literal syntax:

```swift
let dict: XPCDictionary = [
    "name": "John",
    "age": 30,
    "isActive": true,
    "score": 95.5
]
```

## Topics

### Initializers
- [init<T>(T)](xpcliteralvalue/init(_:)-1dqub.md)
  Creates an XPCLiteralValue from a signed integer.
- [init(String)](xpcliteralvalue/init(_:)-1iznz.md)
  Creates an XPCLiteralValue from a String.
- [init(xpc_object_t)](xpcliteralvalue/init(_:)-381hb.md)
  Creates an XPCLiteralValue from an xpc_object_t.
- [init(Bool)](xpcliteralvalue/init(_:)-75v42.md)
  Creates an XPCLiteralValue from a Bool.
- [init<T>(T)](xpcliteralvalue/init(_:)-89roz.md)
  Creates an XPCLiteralValue from a floating-point number.
- [init(XPCDictionary)](xpcliteralvalue/init(_:)-98a24.md)
  Creates an XPCLiteralValue from an XPCDictionary.
- [init<T>(T)](xpcliteralvalue/init(_:)-nb1u.md)
  Creates an XPCLiteralValue from an unsigned integer.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByBooleanLiteral](../swift/expressiblebybooleanliteral.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByFloatLiteral](../swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../swift/expressiblebyintegerliteral.md)
- [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcliteralvalue)*
# XPCLiteralValue

**Framework**: XPC  
**Kind**: struct  
**Role**: Structure

A type that bridges Swift literal values to XPC objects for use in dictionary literals.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS
- watchOS 27.0+

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
- [init<T>(T)](./xpcliteralvalue/init%28_%29-1dqub.md)
  Creates an XPCLiteralValue from a signed integer.
- [init(String)](./xpcliteralvalue/init%28_%29-1iznz.md)
  Creates an XPCLiteralValue from a String.
- [init(xpc_object_t)](./xpcliteralvalue/init%28_%29-381hb.md)
  Creates an XPCLiteralValue from an xpc_object_t.
- [init(Bool)](./xpcliteralvalue/init%28_%29-75v42.md)
  Creates an XPCLiteralValue from a Bool.
- [init<T>(T)](./xpcliteralvalue/init%28_%29-89roz.md)
  Creates an XPCLiteralValue from a floating-point number.
- [init(XPCDictionary)](./xpcliteralvalue/init%28_%29-98a24.md)
  Creates an XPCLiteralValue from an XPCDictionary.
- [init<T>(T)](./xpcliteralvalue/init%28_%29-nb1u.md)
  Creates an XPCLiteralValue from an unsigned integer.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByBooleanLiteral](../Swift/expressiblebybooleanliteral.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByFloatLiteral](../Swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../Swift/expressiblebyintegerliteral.md)
- [ExpressibleByStringLiteral](../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/expressiblebyunicodescalarliteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcliteralvalue)*
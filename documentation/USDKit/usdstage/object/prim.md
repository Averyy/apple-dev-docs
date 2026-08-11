# prim

**Framework**: USDKit  
**Kind**: property

The nearest prim that contains this object.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var prim: USDPrim { get }
```

#### Discussion

If this object is a [`USDPrim`](usdprim.md), the value of this property is that same prim. If this object is a [`USDPrim.Attribute`](usdprim/attribute.md) or a [`USDPrim.Relationship`](usdprim/relationship.md), the value of this property is the nearest prim that contains this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/object/prim)*
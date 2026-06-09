# relationship(named:)

**Framework**: USDKit  
**Kind**: method

Returns the relationship with a given name on this prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func relationship(named name: USDToken) -> USDPrim.Relationship?
```

#### Discussion

If no relationship named `name` exists on this prim, returns an invalid relationship handle.

## See Also

- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship](usdprim/relationship(at:).md)
  Returns the relationship at a given path, relative to this prim.
- [func hasRelationship(named: USDToken) -> Bool](usdprim/hasrelationship(named:).md)
  Returns true if a relationship with a given name exists on this prim.
- [USDPrim.Relationship](usdprim/relationship.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/relationship(named:))*
# relationship(at:)

**Framework**: USDKit  
**Kind**: method

Returns the relationship at a given path, relative to this prim.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func relationship(at path: USDLayer.Path) -> USDPrim.Relationship
```

#### Discussion

If `path` is relative, it is anchored to this prim’s path. If no relationship exists at the resolved path, returns an invalid relationship handle.

## See Also

- [func relationship(named: USDToken) -> USDPrim.Relationship?](usdprim/relationship(named:).md)
  Returns the relationship with a given name on this prim.
- [func hasRelationship(named: USDToken) -> Bool](usdprim/hasrelationship(named:).md)
  Returns true if a relationship with a given name exists on this prim.
- [USDPrim.Relationship](usdprim/relationship.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/relationship(at:))*
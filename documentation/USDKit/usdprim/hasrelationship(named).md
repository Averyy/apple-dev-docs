# hasRelationship(named:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Returns true if a relationship with a given name exists on this prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func hasRelationship(named name: USDToken) -> Bool
```

## See Also

### Accessing relationships
- [func relationship(named: USDToken) -> USDPrim.Relationship](./relationship%28named%29.md)
  Returns the relationship with a given name on this prim.
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship](./relationship%28at%29.md)
  Returns the relationship at a given path, relative to this prim.
- [USDPrim.Relationship](./relationship.md)
  A property that connects a prim to one or more other objects in the stage by their paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/hasrelationship(named:))*
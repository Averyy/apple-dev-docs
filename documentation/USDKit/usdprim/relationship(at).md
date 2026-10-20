# relationship(at:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Returns the relationship at a given path, relative to this prim.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func relationship(at path: USDLayer.Path) -> USDPrim.Relationship
```

#### Discussion

If `path` is relative, it is anchored to this prim’s path. If no relationship exists at the resolved path, returns an invalid relationship handle.

## See Also

### Accessing relationships
- [func relationship(named: USDToken) -> USDPrim.Relationship](./relationship%28named%29.md)
  Returns the relationship with a given name on this prim.
- [func hasRelationship(named: USDToken) -> Bool](./hasrelationship%28named%29.md)
  Returns true if a relationship with a given name exists on this prim.
- [USDPrim.Relationship](./relationship.md)
  A property that connects a prim to one or more other objects in the stage by their paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/relationship(at:))*
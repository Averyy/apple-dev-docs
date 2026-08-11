# makeRelationship(named:custom:)

**Framework**: USDKit  
**Kind**: method

Creates a relationship with the given name on this prim, or returns the existing relationship if one already exists.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
func makeRelationship(named name: USDToken, custom: Bool = true) -> USDPrim.Relationship
```

#### Return Value

The relationship with the given name.

## Parameters

- `name`: The name of the relationship to create.
- `custom`: A Boolean value that indicates whether the relationship is a custom relationship not defined by a schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/makerelationship(named:custom:))*
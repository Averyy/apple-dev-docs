# PartRenderer.Action

**Framework**: hvf  
**Kind**: enum

Action requested by the render context after processing an instruction

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
enum Action
```

## Topics

### Operators
- [static func == (PartRenderer.Action, PartRenderer.Action) -> Bool](partrenderer/action/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [PartRenderer.Action.continue](partrenderer/action/continue.md)
  Continue rendering
- [PartRenderer.Action.skip](partrenderer/action/skip.md)
  Skip this part (only in response to beginPart)
- [PartRenderer.Action.stop](partrenderer/action/stop.md)
  Stop rendering
### Instance Properties
- [var hashValue: Int](partrenderer/action/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](partrenderer/action/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](partrenderer/action/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/action)*
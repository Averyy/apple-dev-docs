# init(initialState:)

**Framework**: os  
**Kind**: init  
**Role**: Initializer

Creates a lock object that maintains and protects state data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
init(initialState: State)
```

Available when `State` conforms to `Sendable`.

## Parameters

- `initialState`: The starting state of the operation.

## See Also

### Creating a lock object
- [init()](./init%28%29.md)
  Creates a lock object that doesn’t protect state data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/os/osallocatedunfairlock/init(initialstate:))*
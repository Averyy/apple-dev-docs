# subscript(_:)

**Framework**: Playground Support  
**Kind**: instsub

Reads or stores the value associated with the given key in the key-value store.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
subscript(key: String) -> PlaygroundValue? { get set }
```

#### Return_value

The value associated with the `key` parameter.

## Parameters

- `key`: The key to find in the key-value store.

## See Also

- [static let current: PlaygroundKeyValueStore](playgroundkeyvaluestore/3029533-current.md)
  A reference to the key-value store for the current playground book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundkeyvaluestore/3029534-subscript)*
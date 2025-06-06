# PlaygroundValue

**Framework**: Playground Support  
**Kind**: enum

The types you can save in the key-value store or send in messages to live views.

**Availability**:
- Xcode 10.2+
- Swift Playgrounds 2.0+

## Declaration

```swift
enum PlaygroundValue
```

#### Overview

The example below stores a dictionary in a [`PlaygroundValue`](playgroundvalue.md) instance and then stores the value in a [`PlaygroundKeyValueStore`](playgroundkeyvaluestore.md).

```swift
let myData = [
    "animal": PlaygroundValue.string("Llama"),
    "count": PlaygroundValue.integer(5)
]

PlaygroundKeyValueStore.current.keyValueStore["AnimalCountDict"] = .dictionary(myData)
```

For information about using [`PlaygroundValue`](playgroundvalue.md) instances to send messages, see [`Send and Receive Messages`](messaging_between_a_playground_page_and_the_always-on_live_view#3034522.md).

## Topics

### Representing Data
- [PlaygroundValue.boolean(_:)](playgroundvalue/boolean.md)
  A value that represents a Boolean.
- [PlaygroundValue.data(_:)](playgroundvalue/data.md)
  A value that represents raw data.
- [PlaygroundValue.date(_:)](playgroundvalue/date.md)
  A value that represents a date.
- [PlaygroundValue.floatingPoint(_:)](playgroundvalue/floatingpoint.md)
  A value that represents a floating-point number.
- [PlaygroundValue.integer(_:)](playgroundvalue/integer.md)
  A value that represents an integer.
- [PlaygroundValue.string(_:)](playgroundvalue/string.md)
  A value that represents a string.
### Representing Data Collections
- [case array([PlaygroundValue])](playgroundvalue/array.md)
  A value that represents an array that contains [`PlaygroundValue`](playgroundvalue.md) instances.
- [case dictionary([String : PlaygroundValue])](playgroundvalue/dictionary.md)
  A value that represents a mapping from strings to [`PlaygroundValue`](playgroundvalue.md) instances.

## See Also

- [class PlaygroundKeyValueStore](playgroundkeyvaluestore.md)
  A data storage container you use to persist information across different sessions.
- [let playgroundSharedDataDirectory: URL](playgroundshareddatadirectory.md)
  The path to the directory containing data shared between all playgrounds in Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/playgroundsupport/playgroundvalue)*
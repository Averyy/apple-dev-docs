# map(_:)

**Framework**: XPC  
**Kind**: method

Returns an array containing the results of mapping the given closure over the sequence’s elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func map<ReturnType>(_ transform: (XPCDictionary.KeyValuePair) throws -> ReturnType) rethrows -> [ReturnType]
```

#### Return Value

An array containing the transformed elements of this sequence.

## Parameters

- `transform`: A mapping closure.   accepts an element of this sequence as its parameter and returns a transformed value of the same or of a different type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/map(_:))*
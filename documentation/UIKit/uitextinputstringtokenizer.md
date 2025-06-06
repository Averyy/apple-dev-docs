# UITextInputStringTokenizer

**Framework**: UIKit  
**Kind**: class

A base implementation of the text-input tokenizer protocol.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITextInputStringTokenizer
```

#### Overview

If you want to take advantage of this base implementation of the [`UITextInputTokenizer`](uitextinputtokenizer.md) protocol, you should subclass this class and handle application-specific directions and granularities affected by layout. When you instantiate a class you must supply the document class that’s adopting the [`UITextInput`](uitextinput.md) protocol for your application.

##### Subclassing Notes

When you subclass [`UITextInputStringTokenizer`](uitextinputstringtokenizer.md), override all [`UITextInputTokenizer`](uitextinputtokenizer.md) methods, calling the superclass implementation (`super`) when method parameters aren’t affected by layout. For example, the subclass needs a custom implementation of all methods for line granularity. For the left direction, it needs to decide whether left corresponds at a given position to forward or backward, and then call `super` passing in the storage direction ([`UITextStorageDirection`](uitextstoragedirection.md)).

## Topics

### Initializing a tokenizer
- [init(textInput: any UIResponder & UITextInput)](uitextinputstringtokenizer/init(textinput:).md)
  Returns an object initialized with the document object that directly communicates with the text input system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UITextInputTokenizer](uitextinputtokenizer.md)

## See Also

- [protocol UITextInputTokenizer](uitextinputtokenizer.md)
  A tokenizer, which is an object that allows the text input system to evaluate text units of different granularities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputstringtokenizer)*
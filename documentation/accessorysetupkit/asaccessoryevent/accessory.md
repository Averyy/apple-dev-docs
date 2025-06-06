# accessory

**Framework**: AccessorySetupKit  
**Kind**: property

The accessory involved in the event, if any.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@NSCopying
var accessory: ASAccessory? { get }
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Discussion

The session populates this member for event types like [`ASAccessoryEventType.accessoryAdded`](asaccessoryeventtype/accessoryadded.md) and [`ASAccessoryEventType.accessoryChanged`](asaccessoryeventtype/accessorychanged.md), but not for life cycle or picker events like [`ASAccessoryEventType.activated`](asaccessoryeventtype/activated.md) or [`ASAccessoryEventType.pickerDidPresent`](asaccessoryeventtype/pickerdidpresent.md).

## See Also

- [class ASAccessory](asaccessory.md)
  An accessory discovered by the accessory session.
- [var eventType: ASAccessoryEventType](asaccessoryevent/eventtype.md)
  The type of event, such as accessory addition or removal, or picker presentation or removal.
- [enum ASAccessoryEventType](asaccessoryeventtype.md)
  An enumeration of the types of events encountered during accessory discovery


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessoryevent/accessory)*
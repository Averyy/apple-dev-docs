# eventType

**Framework**: AccessorySetupKit  
**Kind**: property

The type of event, such as accessory addition or removal, or picker presentation or removal.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var eventType: ASAccessoryEventType { get }
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Discussion

Some event types may indicate that the event is a subclass of [`ASAccessoryEvent`](asaccessoryevent.md) that provides additional properties.

## See Also

- [var accessory: ASAccessory?](asaccessoryevent/accessory.md)
  The accessory involved in the event, if any.
- [class ASAccessory](asaccessory.md)
  An accessory discovered by the accessory session.
- [enum ASAccessoryEventType](asaccessoryeventtype.md)
  An enumeration of the types of events encountered during accessory discovery


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessoryevent/eventtype)*
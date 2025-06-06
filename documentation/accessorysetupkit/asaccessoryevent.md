# ASAccessoryEvent

**Framework**: AccessorySetupKit  
**Kind**: class

Properties of an event encountered during accessory discovery.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
class ASAccessoryEvent
```

## Mentions

- [Discovering and configuring accessories](discovering-and-configuring-accessories.md)

#### Overview

The event handler you register with the session’s [`activate(on:eventHandler:)`](asaccessorysession/activate(on:eventhandler:).md) method receives objects of this type from the session. Each event identifies the type of event and which accessory (if any) is involved.

## Topics

### Inspecting the event
- [var accessory: ASAccessory?](asaccessoryevent/accessory.md)
  The accessory involved in the event, if any.
- [class ASAccessory](asaccessory.md)
  An accessory discovered by the accessory session.
- [var eventType: ASAccessoryEventType](asaccessoryevent/eventtype.md)
  The type of event, such as accessory addition or removal, or picker presentation or removal.
- [enum ASAccessoryEventType](asaccessoryeventtype.md)
  An enumeration of the types of events encountered during accessory discovery
### Handling errors
- [var error: (any Error)?](asaccessoryevent/error.md)
  The error associated with the event, if any.

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

## See Also

- [enum ASAccessoryEventType](asaccessoryeventtype.md)
  An enumeration of the types of events encountered during accessory discovery
- [class ASDiscoveryDescriptor](asdiscoverydescriptor.md)
  Descriptive traits used to discover accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessoryevent)*
# ASAccessoryEventType

**Framework**: AccessorySetupKit  
**Kind**: enum

An enumeration of the types of events encountered during accessory discovery

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+

## Declaration

```swift
enum ASAccessoryEventType
```

## Topics

### Creating an event type instance
- [init?(rawValue: Int)](asaccessoryeventtype/init(rawvalue:).md)
### Accessory events
- [ASAccessoryEventType.accessoryAdded](asaccessoryeventtype/accessoryadded.md)
  The session added an accessory.
- [ASAccessoryEventType.accessoryChanged](asaccessoryeventtype/accessorychanged.md)
  The properties of an accessory changed.
- [ASAccessoryEventType.accessoryRemoved](asaccessoryeventtype/accessoryremoved.md)
  The session removed an accessory.
### Life cycle events
- [ASAccessoryEventType.activated](asaccessoryeventtype/activated.md)
  The discovery session activated.
- [ASAccessoryEventType.invalidated](asaccessoryeventtype/invalidated.md)
  The discovery session invalidated.
### Picker events
- [ASAccessoryEventType.pickerDidPresent](asaccessoryeventtype/pickerdidpresent.md)
  The discovery session picker appeared.
- [ASAccessoryEventType.pickerDidDismiss](asaccessoryeventtype/pickerdiddismiss.md)
  The discovery session picker dismissed.
- [ASAccessoryEventType.pickerSetupBridging](asaccessoryeventtype/pickersetupbridging.md)
  The discovery session picker started bridging with an accessory.
- [ASAccessoryEventType.pickerSetupPairing](asaccessoryeventtype/pickersetuppairing.md)
  The discovery session picker started pairing with a Bluetooth accessory.
- [ASAccessoryEventType.pickerSetupFailed](asaccessoryeventtype/pickersetupfailed.md)
  The discovery session picker setup failed.
- [ASAccessoryEventType.pickerSetupRename](asaccessoryeventtype/pickersetuprename.md)
  The discovery session picker started renaming an accessory.
### Migration events
- [ASAccessoryEventType.migrationComplete](asaccessoryeventtype/migrationcomplete.md)
  The migration of an accessory completed.
### Unclassified events
- [ASAccessoryEventType.unknown](asaccessoryeventtype/unknown.md)
  An unknown event occurred.
### Default Implementations
- [Equatable Implementations](asaccessoryeventtype/equatable-implementations.md)
- [RawRepresentable Implementations](asaccessoryeventtype/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class ASAccessoryEvent](asaccessoryevent.md)
  Properties of an event encountered during accessory discovery.
- [class ASDiscoveryDescriptor](asdiscoverydescriptor.md)
  Descriptive traits used to discover accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessoryeventtype)*
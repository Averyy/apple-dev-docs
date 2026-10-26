# AXError

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

Error codes returned by accessibility functions.

**Availability**:
- macOS 10.2+

## Declaration

```swift
enum AXError : Int32, @unchecked Sendable
```

```c
typedef enum AXError : SInt32 {
    ...
} AXError;
```

## Topics

### Enumeration Cases
- [AXError.apiDisabled](./axerror/apidisabled.md)
  Assistive applications are not enabled in System Preferences.
- [AXError.actionUnsupported](./axerror/actionunsupported.md)
  The referenced action is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [AXError.attributeUnsupported](./axerror/attributeunsupported.md)
  The referenced attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [AXError.cannotComplete](./axerror/cannotcomplete.md)
  A fundamental error has occurred, such as a failure to allocate memory during processing.
- [AXError.failure](./axerror/failure.md)
- [AXError.illegalArgument](./axerror/illegalargument.md)
  The value received in this event is an invalid value for this attribute. This also applies for invalid parameters in parameterized attributes.
- [AXError.invalidUIElement](./axerror/invaliduielement.md)
  The accessibility object received in this event is invalid.
- [AXError.invalidUIElementObserver](./axerror/invaliduielementobserver.md)
  The observer for the accessibility object received in this event is invalid.
- [AXError.noValue](./axerror/novalue.md)
- [AXError.notEnoughPrecision](./axerror/notenoughprecision.md)
- [AXError.notImplemented](./axerror/notimplemented.md)
- [AXError.notificationAlreadyRegistered](./axerror/notificationalreadyregistered.md)
- [AXError.notificationNotRegistered](./axerror/notificationnotregistered.md)
- [AXError.notificationUnsupported](./axerror/notificationunsupported.md)
- [AXError.parameterizedAttributeUnsupported](./axerror/parameterizedattributeunsupported.md)
  The parameterized attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [AXError.success](./axerror/success.md)
### Constants
- [kAXErrorAPIDisabled](./axerror/kaxerrorapidisabled.md)
  Assistive applications are not enabled in System Preferences.
- [kAXErrorActionUnsupported](./axerror/kaxerroractionunsupported.md)
  The referenced action is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [kAXErrorAttributeUnsupported](./axerror/kaxerrorattributeunsupported.md)
  The referenced attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [kAXErrorCannotComplete](./axerror/kaxerrorcannotcomplete.md)
  A fundamental error has occurred, such as a failure to allocate memory during processing.
- [kAXErrorFailure](./axerror/kaxerrorfailure.md)
- [kAXErrorIllegalArgument](./axerror/kaxerrorillegalargument.md)
  The value received in this event is an invalid value for this attribute. This also applies for invalid parameters in parameterized attributes.
- [kAXErrorInvalidUIElement](./axerror/kaxerrorinvaliduielement.md)
  The accessibility object received in this event is invalid.
- [kAXErrorInvalidUIElementObserver](./axerror/kaxerrorinvaliduielementobserver.md)
  The observer for the accessibility object received in this event is invalid.
- [kAXErrorNoValue](./axerror/kaxerrornovalue.md)
- [kAXErrorNotEnoughPrecision](./axerror/kaxerrornotenoughprecision.md)
- [kAXErrorNotImplemented](./axerror/kaxerrornotimplemented.md)
- [kAXErrorNotificationAlreadyRegistered](./axerror/kaxerrornotificationalreadyregistered.md)
- [kAXErrorNotificationNotRegistered](./axerror/kaxerrornotificationnotregistered.md)
- [kAXErrorNotificationUnsupported](./axerror/kaxerrornotificationunsupported.md)
- [kAXErrorParameterizedAttributeUnsupported](./axerror/kaxerrorparameterizedattributeunsupported.md)
  The parameterized attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [kAXErrorSuccess](./axerror/kaxerrorsuccess.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/axerror)*
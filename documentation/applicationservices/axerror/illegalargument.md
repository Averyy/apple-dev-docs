# AXError.illegalArgument

**Framework**: Application Services  
**Kind**: enumelt

The value received in this event is an invalid value for this attribute. This also applies for invalid parameters in parameterized attributes.

**Availability**:
- macOS 10.2+

## Declaration

```swift
case illegalArgument = -25201
```

## See Also

- [AXError.invalidUIElement](axerror/invaliduielement.md)
  The accessibility object received in this event is invalid.
- [AXError.invalidUIElementObserver](axerror/invaliduielementobserver.md)
  The observer for the accessibility object received in this event is invalid.
- [AXError.cannotComplete](axerror/cannotcomplete.md)
  A fundamental error has occurred, such as a failure to allocate memory during processing.
- [AXError.attributeUnsupported](axerror/attributeunsupported.md)
  The referenced attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [AXError.actionUnsupported](axerror/actionunsupported.md)
  The referenced action is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [AXError.apiDisabled](axerror/apidisabled.md)
  Assistive applications are not enabled in System Preferences.
- [AXError.parameterizedAttributeUnsupported](axerror/parameterizedattributeunsupported.md)
  The parameterized attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/axerror/illegalargument)*
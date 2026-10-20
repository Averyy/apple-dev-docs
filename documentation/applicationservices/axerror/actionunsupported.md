# AXError.actionUnsupported

**Framework**: Application Services  
**Kind**: enumelt  
**Role**: Enumeration Case

The referenced action is not supported. Alternatively, you can return the `eventNotHandledErr` error.

**Availability**:
- macOS 10.2+

## Declaration

```swift
case actionUnsupported = -25206
```

## See Also

### Result Codes
- [AXError.illegalArgument](./illegalargument.md)
  The value received in this event is an invalid value for this attribute. This also applies for invalid parameters in parameterized attributes.
- [AXError.invalidUIElement](./invaliduielement.md)
  The accessibility object received in this event is invalid.
- [AXError.invalidUIElementObserver](./invaliduielementobserver.md)
  The observer for the accessibility object received in this event is invalid.
- [AXError.cannotComplete](./cannotcomplete.md)
  A fundamental error has occurred, such as a failure to allocate memory during processing.
- [AXError.attributeUnsupported](./attributeunsupported.md)
  The referenced attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [AXError.apiDisabled](./apidisabled.md)
  Assistive applications are not enabled in System Preferences.
- [AXError.parameterizedAttributeUnsupported](./parameterizedattributeunsupported.md)
  The parameterized attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/axerror/actionunsupported)*
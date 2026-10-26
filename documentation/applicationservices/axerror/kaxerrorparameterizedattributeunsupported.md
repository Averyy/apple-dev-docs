# kAXErrorParameterizedAttributeUnsupported

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

The parameterized attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.

**Availability**:
- macOS 10.3+

## Declaration

```c
kAXErrorParameterizedAttributeUnsupported = -25213
```

## See Also

### Result Codes
- [kAXErrorIllegalArgument](./kaxerrorillegalargument.md)
  The value received in this event is an invalid value for this attribute. This also applies for invalid parameters in parameterized attributes.
- [kAXErrorInvalidUIElement](./kaxerrorinvaliduielement.md)
  The accessibility object received in this event is invalid.
- [kAXErrorInvalidUIElementObserver](./kaxerrorinvaliduielementobserver.md)
  The observer for the accessibility object received in this event is invalid.
- [kAXErrorCannotComplete](./kaxerrorcannotcomplete.md)
  A fundamental error has occurred, such as a failure to allocate memory during processing.
- [kAXErrorAttributeUnsupported](./kaxerrorattributeunsupported.md)
  The referenced attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [kAXErrorActionUnsupported](./kaxerroractionunsupported.md)
  The referenced action is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [kAXErrorAPIDisabled](./kaxerrorapidisabled.md)
  Assistive applications are not enabled in System Preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/axerror/kaxerrorparameterizedattributeunsupported)*
# AXUIElementCopyAttributeValue(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Returns the value of an accessibility object's attribute.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func AXUIElementCopyAttributeValue(_ element: AXUIElement, _ attribute: CFString, _ value: UnsafeMutablePointer<CFTypeRef?>) -> AXError
```

```c
AXError AXUIElementCopyAttributeValue(AXUIElementRef element, CFStringRef attribute, CFTypeRef  _Nullable *value);
```

#### Return Value

If unsuccessful, `AXUIElementCopyAttributeValue` may return one of the following error codes, among others:

- **`kAXErrorAttributeUnsupported`**: The specified AXUIElementRef does not support the specified attribute.
- **`kAXErrorNoValue`**: The specified attribute does not have a value.
- **`kAXErrorIllegalArgument`**: One or more of the arguments is an illegal value.
- **`kAXErrorInvalidUIElement`**: The AXUIElementRef is invalid.
- **`kAXErrorCannotComplete`**: The function cannot complete because messaging has failed in some way.
- **`kAXErrorNotImplemented`**: The process does not fully support the accessibility API.

## Parameters

- `element`: The AXUIElementRef representing the accessibility object.
- `attribute`: The attribute name.
- `value`: On return, the value associated with the specified attribute.

## See Also

### Miscellaneous
- [func AXIsProcessTrusted() -> Bool](./api-1460720-axisprocesstrusted.md)
  Returns whether the current process is a trusted accessibility client.
- [func AXIsProcessTrustedWithOptions(CFDictionary?) -> Bool](./api-1459186-axisprocesstrustedwithoptions.md)
  Returns whether the current process is a trusted accessibility client.
- [func AXUIElementCopyActionDescription(AXUIElement, CFString, UnsafeMutablePointer<CFString?>) -> AXError](./api-1462075-axuielementcopyactiondescription.md)
  Returns a localized description of the specified accessibility object's action.
- [func AXUIElementCopyActionNames(AXUIElement, UnsafeMutablePointer<CFArray?>) -> AXError](./api-1462053-axuielementcopyactionnames.md)
  Returns a list of all the actions the specified accessibility object can perform.
- [func AXUIElementCopyAttributeNames(AXUIElement, UnsafeMutablePointer<CFArray?>) -> AXError](./api-1459475-axuielementcopyattributenames.md)
  Returns a list of all the attributes supported by the specified accessibility object.
- [func AXUIElementCopyAttributeValues(AXUIElement, CFString, CFIndex, CFIndex, UnsafeMutablePointer<CFArray?>) -> AXError](./api-1462060-axuielementcopyattributevalues.md)
  Returns an array of attribute values for the accessibility object's attribute, starting at the specified index.
- [func AXUIElementCopyElementAtPosition(AXUIElement, Float, Float, UnsafeMutablePointer<AXUIElement?>) -> AXError](./api-1462077-axuielementcopyelementatposition.md)
  Returns the accessibility object at the specified position in top-left relative screen coordinates.
- [func AXUIElementCopyMultipleAttributeValues(AXUIElement, CFArray, AXCopyMultipleAttributeOptions, UnsafeMutablePointer<CFArray?>) -> AXError](./api-1462051-axuielementcopymultipleattribute.md)
  Returns the values of multiple attributes in the accessibility object.
- [func AXUIElementCopyParameterizedAttributeNames(AXUIElement, UnsafeMutablePointer<CFArray?>) -> AXError](./api-1458783-axuielementcopyparameterizedattr.md)
  Returns a list of all the parameterized attributes supported by the specified accessibility object.
- [func AXUIElementCopyParameterizedAttributeValue(AXUIElement, CFString, CFTypeRef, UnsafeMutablePointer<CFTypeRef?>) -> AXError](./api-1461203-axuielementcopyparameterizedattr.md)
  Returns the value of an accessibility object's parameterized attribute.
- [func AXUIElementCreateApplication(pid_t) -> AXUIElement](./api-1459374-axuielementcreateapplication.md)
  Creates and returns the top-level accessibility object for the application with the specified process ID.
- [func AXUIElementCreateSystemWide() -> AXUIElement](./api-1462095-axuielementcreatesystemwide.md)
  Returns an accessibility object that provides access to system attributes.
- [func AXUIElementGetAttributeValueCount(AXUIElement, CFString, UnsafeMutablePointer<CFIndex>) -> AXError](./api-1459066-axuielementgetattributevaluecoun.md)
  Returns the count of the array of an accessibility object's attribute value.
- [func AXUIElementGetPid(AXUIElement, UnsafeMutablePointer<pid_t>) -> AXError](./api-1460337-axuielementgetpid.md)
  Returns the process ID associated with the specified accessibility object.
- [func AXUIElementGetTypeID() -> CFTypeID](./api-1460085-axuielementgettypeid.md)
  Returns the unique type identifier for the AXUIElementRef type.
- [func AXUIElementIsAttributeSettable(AXUIElement, CFString, UnsafeMutablePointer<DarwinBoolean>) -> AXError](./api-1459972-axuielementisattributesettable.md)
  Returns whether the specified accessibility object's attribute can be modified.
- [func AXUIElementPerformAction(AXUIElement, CFString) -> AXError](./api-1462091-axuielementperformaction.md)
  Requests that the specified accessibility object perform the specified action.
- [func AXUIElementSetAttributeValue(AXUIElement, CFString, CFTypeRef) -> AXError](./api-1460434-axuielementsetattributevalue.md)
  Sets the accessibility object's attribute to the specified value.
- [func AXUIElementSetMessagingTimeout(AXUIElement, Float) -> AXError](./api-1459345-axuielementsetmessagingtimeout.md)
  Sets the timeout value used in the accessibility API.
- [AXAPIEnabled](./api-1462072-axapienabled.md)
  Returns whether the accessibility API is enabled.
- [AXMakeProcessTrusted](./api-1462083-axmakeprocesstrusted.md)
  Attempts to make the process represented by the specified path a trusted accessibility client.
- [AXUIElementPostKeyboardEvent](./api-1462057-axuielementpostkeyboardevent.md)
  Posts keys to the specified application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462085-axuielementcopyattributevalue)*
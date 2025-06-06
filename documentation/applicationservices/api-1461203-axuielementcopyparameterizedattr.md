# AXUIElementCopyParameterizedAttributeValue(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func

Returns the value of an accessibility object's parameterized attribute.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func AXUIElementCopyParameterizedAttributeValue(_ element: AXUIElement, _ parameterizedAttribute: CFString, _ parameter: CFTypeRef, _ result: UnsafeMutablePointer<CFTypeRef?>) -> AXError
```

#### Return_value

If unsuccessful, `AXUIElementCopyParameterizedAttributeValue` may return one of the following error codes, among others:

## Parameters

- `element`: The AXUIElementRef representing the accessibility object.
- `parameterizedAttribute`: The parameterized attribute.
- `parameter`: The parameter.
- `result`: On return, the value of the parameterized attribute.

## See Also

- [func AXIsProcessTrusted() -> Bool](1460720-axisprocesstrusted.md)
  Returns whether the current process is a trusted accessibility client.
- [func AXIsProcessTrustedWithOptions(CFDictionary?) -> Bool](1459186-axisprocesstrustedwithoptions.md)
  Returns whether the current process is a trusted accessibility client.
- [func AXUIElementCopyActionDescription(AXUIElement, CFString, UnsafeMutablePointer<CFString?>) -> AXError](1462075-axuielementcopyactiondescription.md)
  Returns a localized description of the specified accessibility object's action.
- [func AXUIElementCopyActionNames(AXUIElement, UnsafeMutablePointer<CFArray?>) -> AXError](1462053-axuielementcopyactionnames.md)
  Returns a list of all the actions the specified accessibility object can perform.
- [func AXUIElementCopyAttributeNames(AXUIElement, UnsafeMutablePointer<CFArray?>) -> AXError](1459475-axuielementcopyattributenames.md)
  Returns a list of all the attributes supported by the specified accessibility object.
- [func AXUIElementCopyAttributeValue(AXUIElement, CFString, UnsafeMutablePointer<CFTypeRef?>) -> AXError](1462085-axuielementcopyattributevalue.md)
  Returns the value of an accessibility object's attribute.
- [func AXUIElementCopyAttributeValues(AXUIElement, CFString, CFIndex, CFIndex, UnsafeMutablePointer<CFArray?>) -> AXError](1462060-axuielementcopyattributevalues.md)
  Returns an array of attribute values for the accessibility object's attribute, starting at the specified index.
- [func AXUIElementCopyElementAtPosition(AXUIElement, Float, Float, UnsafeMutablePointer<AXUIElement?>) -> AXError](1462077-axuielementcopyelementatposition.md)
  Returns the accessibility object at the specified position in top-left relative screen coordinates.
- [func AXUIElementCopyMultipleAttributeValues(AXUIElement, CFArray, AXCopyMultipleAttributeOptions, UnsafeMutablePointer<CFArray?>) -> AXError](1462051-axuielementcopymultipleattribute.md)
  Returns the values of multiple attributes in the accessibility object.
- [func AXUIElementCopyParameterizedAttributeNames(AXUIElement, UnsafeMutablePointer<CFArray?>) -> AXError](1458783-axuielementcopyparameterizedattr.md)
  Returns a list of all the parameterized attributes supported by the specified accessibility object.
- [func AXUIElementCreateApplication(pid_t) -> AXUIElement](1459374-axuielementcreateapplication.md)
  Creates and returns the top-level accessibility object for the application with the specified process ID.
- [func AXUIElementCreateSystemWide() -> AXUIElement](1462095-axuielementcreatesystemwide.md)
  Returns an accessibility object that provides access to system attributes.
- [func AXUIElementGetAttributeValueCount(AXUIElement, CFString, UnsafeMutablePointer<CFIndex>) -> AXError](1459066-axuielementgetattributevaluecoun.md)
  Returns the count of the array of an accessibility object's attribute value.
- [func AXUIElementGetPid(AXUIElement, UnsafeMutablePointer<pid_t>) -> AXError](1460337-axuielementgetpid.md)
  Returns the process ID associated with the specified accessibility object.
- [func AXUIElementGetTypeID() -> CFTypeID](1460085-axuielementgettypeid.md)
  Returns the unique type identifier for the AXUIElementRef type.
- [func AXUIElementIsAttributeSettable(AXUIElement, CFString, UnsafeMutablePointer<DarwinBoolean>) -> AXError](1459972-axuielementisattributesettable.md)
  Returns whether the specified accessibility object's attribute can be modified.
- [func AXUIElementPerformAction(AXUIElement, CFString) -> AXError](1462091-axuielementperformaction.md)
  Requests that the specified accessibility object perform the specified action.
- [func AXUIElementSetAttributeValue(AXUIElement, CFString, CFTypeRef) -> AXError](1460434-axuielementsetattributevalue.md)
  Sets the accessibility object's attribute to the specified value.
- [func AXUIElementSetMessagingTimeout(AXUIElement, Float) -> AXError](1459345-axuielementsetmessagingtimeout.md)
  Sets the timeout value used in the accessibility API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1461203-axuielementcopyparameterizedattr)*
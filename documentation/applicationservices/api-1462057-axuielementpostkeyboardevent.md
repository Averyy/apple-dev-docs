# AXUIElementPostKeyboardEvent

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Posts keys to the specified application.

**Availability**:
- macOS 10.0+ - Deprecated in 10.9

## Declaration

```c
AXError AXUIElementPostKeyboardEvent(AXUIElementRef application, CGCharCode keyChar, CGKeyCode virtualKey, Boolean keyDown);
```

## Return Value

If unsuccessful, `AXUIElementPostKeyboardEvent` may return one of the following error codes, among others:

- **`kAXErrorIllegalArgument`**: One or more of the arguments is an illegal value.
- **`kAXErrorInvalidUIElement`**: The AXUIElementRef is invalid.
- **`kAXErrorFailure`**: There is some sort of system memory failure.
- **`kAXErrorCannotComplete`**: The function cannot complete because messaging has failed in some way.
- **`kAXErrorNotImplemented`**: The process does not fully support the accessibility API.

## Discussion

This is similar to [`CGPostKeyboardEvent`](../CoreGraphics/cgpostkeyboardevent%28_,_,_%29.md) (which synthesizes a low-level keyboard event on the local machine), but it allows you to specify the target application as opposed to always sending the events to the active application. If the system-wide accessibility object is passed in the `application` parameter, the event is sent to the active application.

You can only pass in the system-wide or application AXUIElementRef.

## Parameters

- `application`: The AXUIElementRef representing the application (or the system-wide accessibility object).
- `keyChar`: 
- `virtualKey`: 
- `keyDown`: 

## See Also

### Miscellaneous
- [AXAPIEnabled](./api-1462072-axapienabled.md)
  Returns whether the accessibility API is enabled.
- [AXIsProcessTrusted](./api-1460720-axisprocesstrusted.md)
  Returns whether the current process is a trusted accessibility client.
- [AXIsProcessTrustedWithOptions](./api-1459186-axisprocesstrustedwithoptions.md)
  Returns whether the current process is a trusted accessibility client.
- [AXMakeProcessTrusted](./api-1462083-axmakeprocesstrusted.md)
  Attempts to make the process represented by the specified path a trusted accessibility client.
- [AXUIElementCopyActionDescription](./api-1462075-axuielementcopyactiondescription.md)
  Returns a localized description of the specified accessibility object's action.
- [AXUIElementCopyActionNames](./api-1462053-axuielementcopyactionnames.md)
  Returns a list of all the actions the specified accessibility object can perform.
- [AXUIElementCopyAttributeNames](./api-1459475-axuielementcopyattributenames.md)
  Returns a list of all the attributes supported by the specified accessibility object.
- [AXUIElementCopyAttributeValue](./api-1462085-axuielementcopyattributevalue.md)
  Returns the value of an accessibility object's attribute.
- [AXUIElementCopyAttributeValues](./api-1462060-axuielementcopyattributevalues.md)
  Returns an array of attribute values for the accessibility object's attribute, starting at the specified index.
- [AXUIElementCopyElementAtPosition](./api-1462077-axuielementcopyelementatposition.md)
  Returns the accessibility object at the specified position in top-left relative screen coordinates.
- [AXUIElementCopyMultipleAttributeValues](./api-1462051-axuielementcopymultipleattribute.md)
  Returns the values of multiple attributes in the accessibility object.
- [AXUIElementCopyParameterizedAttributeNames](./api-1458783-axuielementcopyparameterizedattr.md)
  Returns a list of all the parameterized attributes supported by the specified accessibility object.
- [AXUIElementCopyParameterizedAttributeValue](./api-1461203-axuielementcopyparameterizedattr.md)
  Returns the value of an accessibility object's parameterized attribute.
- [AXUIElementCreateApplication](./api-1459374-axuielementcreateapplication.md)
  Creates and returns the top-level accessibility object for the application with the specified process ID.
- [AXUIElementCreateSystemWide](./api-1462095-axuielementcreatesystemwide.md)
  Returns an accessibility object that provides access to system attributes.
- [AXUIElementGetAttributeValueCount](./api-1459066-axuielementgetattributevaluecoun.md)
  Returns the count of the array of an accessibility object's attribute value.
- [AXUIElementGetPid](./api-1460337-axuielementgetpid.md)
  Returns the process ID associated with the specified accessibility object.
- [AXUIElementGetTypeID](./api-1460085-axuielementgettypeid.md)
  Returns the unique type identifier for the AXUIElementRef type.
- [AXUIElementIsAttributeSettable](./api-1459972-axuielementisattributesettable.md)
  Returns whether the specified accessibility object's attribute can be modified.
- [AXUIElementPerformAction](./api-1462091-axuielementperformaction.md)
  Requests that the specified accessibility object perform the specified action.
- [AXUIElementSetAttributeValue](./api-1460434-axuielementsetattributevalue.md)
  Sets the accessibility object's attribute to the specified value.
- [AXUIElementSetMessagingTimeout](./api-1459345-axuielementsetmessagingtimeout.md)
  Sets the timeout value used in the accessibility API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462057-axuielementpostkeyboardevent)*
# AXMakeProcessTrusted

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Attempts to make the process represented by the specified path a trusted accessibility client.

**Availability**:
- macOS 10.4+ - Deprecated in 10.9

## Declaration

```c
AXError AXMakeProcessTrusted(CFStringRef executablePath);
```

#### Return Value

An AXError that indicates success or failure.

#### Discussion

Use this function to make a process a trusted accessibility client. Note: The caller must be running as `root` to successfully call this function. In addition, the caller should relaunch the process after this function returns successfully for the trusted status to take effect.

## Parameters

- `executablePath`: The path to the executable of the process to make trusted.

## See Also

### Miscellaneous
- [AXAPIEnabled](./api-1462072-axapienabled.md)
  Returns whether the accessibility API is enabled.
- [AXIsProcessTrusted](./api-1460720-axisprocesstrusted.md)
  Returns whether the current process is a trusted accessibility client.
- [AXIsProcessTrustedWithOptions](./api-1459186-axisprocesstrustedwithoptions.md)
  Returns whether the current process is a trusted accessibility client.
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
- [AXUIElementPostKeyboardEvent](./api-1462057-axuielementpostkeyboardevent.md)
  Posts keys to the specified application.
- [AXUIElementSetAttributeValue](./api-1460434-axuielementsetattributevalue.md)
  Sets the accessibility object's attribute to the specified value.
- [AXUIElementSetMessagingTimeout](./api-1459345-axuielementsetmessagingtimeout.md)
  Sets the timeout value used in the accessibility API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1462083-axmakeprocesstrusted)*
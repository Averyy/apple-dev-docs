# AXUIElement.h

**Framework**: Application Services

#### Overview

See the Overview section above for header-level documentation.

##### 1678823

Assistive applications use the functions defined in this header file to communicate with and control accessible applications running in macOS.

Each accessible user interface element in an application is represented by an AXUIElementRef, which is a CFTypeRef. AXUIElementRefs (like all CFTypeRefs) can be used with all the Core Foundation polymorphic functions, such as [`CFRetain`](https://developer.apple.com/documentation/corefoundation/1521269-cfretain), [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease), and [`CFEqual(_:_:)`](https://developer.apple.com/documentation/corefoundation/cfequal(_:_:)).

All functions defined in this header file return `kAXErrorSuccess` on success. If there is some sort of system memory failure, such as the failure to allocate an object, all functions can return `kAXErrorFailure`. In the unlikely event that some process does not fully support the accessibility API, a function can return `kAXErrorNotImplemented`.

In addition, some functions can return the following error codes:

For more information on the definition and use of accessibility objects and in macOS accessibility support in general, see [`Accessibility Programming Guide for OS X`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/index.html#//apple_ref/doc/uid/TP40001078).

###### 1777679

- <AvailabilityMacros.h>
- <CoreFoundation/CoreFoundation.h>
- <ApplicationServices/ApplicationServices.h>

## Topics

### Notification API
- [func AXObserverAddNotification(AXObserver, AXUIElement, CFString, UnsafeMutableRawPointer?) -> AXError](1462089-axobserveraddnotification.md)
  Registers the specified observer to receive notifications from the specified accessibility object.
- [func AXObserverCreate(pid_t, AXObserverCallback, UnsafeMutablePointer<AXObserver?>) -> AXError](1460133-axobservercreate.md)
  Creates a new observer that can receive notifications from the specified application.
- [func AXObserverCreateWithInfoCallback(pid_t, AXObserverCallbackWithInfo, UnsafeMutablePointer<AXObserver?>) -> AXError](1460610-axobservercreatewithinfocallback.md)
  Creates a new observer that can receive notifications with an information dictionary from the specified application.
- [func AXObserverGetRunLoopSource(AXObserver) -> CFRunLoopSource](1459139-axobservergetrunloopsource.md)
  Returns the observer's run loop source.
- [func AXObserverGetTypeID() -> CFTypeID](1461244-axobservergettypeid.md)
  Returns the unique type identifier for the AXObserverRef type.
- [func AXObserverRemoveNotification(AXObserver, AXUIElement, CFString) -> AXError](1462066-axobserverremovenotification.md)
  Removes the specified notification from the list of notifications the observer wants to receive from the accessibility object.
### Miscellaneous
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
- [func AXUIElementCopyParameterizedAttributeValue(AXUIElement, CFString, CFTypeRef, UnsafeMutablePointer<CFTypeRef?>) -> AXError](1461203-axuielementcopyparameterizedattr.md)
  Returns the value of an accessibility object's parameterized attribute.
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
### Callbacks
- [typealias AXObserverCallback](axobservercallback.md)
- [typealias AXObserverCallbackWithInfo](axobservercallbackwithinfo.md)
### Data Types
- [struct AXCopyMultipleAttributeOptions](axcopymultipleattributeoptions.md)
- [class AXObserver](axobserver.md)
- [class AXUIElement](axuielement.md)
  A structure used to refer to an accessibility object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/axuielement_h)*
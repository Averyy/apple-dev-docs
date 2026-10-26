# Carbon Accessibility

**Framework**: Application Services  
**Role**: API Collection

#### Overview

This section describes the functions some Carbon developers may need to use to access-enable their applications.

This section describes the constants that define accessibility events and aspects of accessibility objects. The accessibility event constants are defined in `CarbonEvents.h` in the Carbon framework. The accessibility object constants are defined in header files in the ApplicationServices framework.

##### Overview

This document describes the Carbon accessibility API. You use this API to make your Carbon application accessible to assistive applications and technologies, a process called access enabling.

###### Who Should Read This Document?

All Carbon application developers should read this document for information on specific functions and constants they may need to access-enable their applications. If you’re unsure which parts of the Carbon accessibility API you need, or if you’re new to accessibility in macOS, be sure to read the documents listed in [See Also](./carbon_accessibility.md#1655632).

###### Organization of This Document

This document contains API reference in the following sections:

- [Carbon Accessibility](./carbon_accessibility.md) documents the functions some Carbon applications use to create and manipulate accessibility objects.
- [Carbon Accessibility](./carbon_accessibility.md) documents accessibility Carbon events and the constants that define the accessibility event parameters, object attributes, and notifications.
- [Result Codes](./carbon_accessibility.md#1658117) describes some of the error codes returned by the Carbon accessibility implementation.

###### See Also

For more information on accessibility in general and access enabling Carbon applications in particular, you should read the following documents:

- Getting Started With Accessibility
- [Accessibility Programming Guide for OS X](https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/index.html#//apple_ref/doc/uid/TP40001078)
- Accessibility Programming Guidelines for Carbon

## Topics

### Accessibility Events
- [Accessibility Event Class](./carbon_accessibility/accessibility_event_class.md)
  Defines the event class for accessibility events.
### Accessibility Object Constants
- [Roles](./carbon_accessibility/roles.md)
  Define the values an accessibility object’s role attribute can have.
- [Subroles](./carbon_accessibility/subroles.md)
  Define the values for an accessibility object’s subrole attribute.
- [Attributes](./carbon_accessibility/attributes.md)
  Define the attributes available for accessibility objects. 
- [Parameterized Attributes](./carbon_accessibility/parameterized_attributes.md)
  Define the parameterized attributes an accessibility object can have.
- [Actions](./carbon_accessibility/actions.md)
  Define the actions an accessibility object can perform.
- [Notifications](./carbon_accessibility/notifications.md)
  Define the notifications that can be broadcast by an accessibility object.
- [Orientations and Sort Directions](./carbon_accessibility/orientations_and_sort_directions.md)
  Define the values for the orientation and sort-direction attributes of some accessibility objects.
### Result Codes
- [AXError.illegalArgument](./axerror/illegalargument.md)
  The value received in this event is an invalid value for this attribute. This also applies for invalid parameters in parameterized attributes.
- [AXError.invalidUIElement](./axerror/invaliduielement.md)
  The accessibility object received in this event is invalid.
- [AXError.invalidUIElementObserver](./axerror/invaliduielementobserver.md)
  The observer for the accessibility object received in this event is invalid.
- [AXError.cannotComplete](./axerror/cannotcomplete.md)
  A fundamental error has occurred, such as a failure to allocate memory during processing.
- [AXError.attributeUnsupported](./axerror/attributeunsupported.md)
  The referenced attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [AXError.actionUnsupported](./axerror/actionunsupported.md)
  The referenced action is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [AXError.apiDisabled](./axerror/apidisabled.md)
  Assistive applications are not enabled in System Preferences.
- [AXError.parameterizedAttributeUnsupported](./axerror/parameterizedattributeunsupported.md)
  The parameterized attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [kAXErrorIllegalArgument](./axerror/kaxerrorillegalargument.md)
  The value received in this event is an invalid value for this attribute. This also applies for invalid parameters in parameterized attributes.
- [kAXErrorInvalidUIElement](./axerror/kaxerrorinvaliduielement.md)
  The accessibility object received in this event is invalid.
- [kAXErrorInvalidUIElementObserver](./axerror/kaxerrorinvaliduielementobserver.md)
  The observer for the accessibility object received in this event is invalid.
- [kAXErrorCannotComplete](./axerror/kaxerrorcannotcomplete.md)
  A fundamental error has occurred, such as a failure to allocate memory during processing.
- [kAXErrorAttributeUnsupported](./axerror/kaxerrorattributeunsupported.md)
  The referenced attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [kAXErrorActionUnsupported](./axerror/kaxerroractionunsupported.md)
  The referenced action is not supported. Alternatively, you can return the `eventNotHandledErr` error.
- [kAXErrorAPIDisabled](./axerror/kaxerrorapidisabled.md)
  Assistive applications are not enabled in System Preferences.
- [kAXErrorParameterizedAttributeUnsupported](./axerror/kaxerrorparameterizedattributeunsupported.md)
  The parameterized attribute is not supported. Alternatively, you can return the `eventNotHandledErr` error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/carbon_accessibility)*
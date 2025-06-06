# Application Services

**Framework**: Application Services

Perform common application tasks.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

#### Overview

This collection of documents provides the API reference for the Application Services framework, which includes several services that are essential to Carbon applications. The Application Services framework also includes support for a number of legacy technologies—such as QuickDraw and the Font Manager—that have been superseded with newer technologies like Quartz 2D and ATSUI. 

## Topics

### Managers
- [Apple Event Manager](apple_event_manager.md)
- [ColorSync Manager](colorsync_manager.md)
- [Speech Synthesis Manager](speech_synthesis_manager.md)
### Reference
- [Carbon Accessibility](carbon_accessibility.md)
- [Core Printing](core_printing.md)
- [AXActionConstants.h](axactionconstants_h.md)
  Many UIElements have a set of actions that they can perform. Actions are designed to be simple. Actions roughly correspond to things you could do with a single click of the mouse on the UIElement. Buttons and menu items, for example, have a single action: push or pick, respectively. A scroll bar has several actions: page up, page down, up one line, down one line.
- [AXAttributeConstants.h](axattributeconstants_h.md)
- [AXError.h](axerror_h.md)
  These error codes can be returned from the accessibility functions defined in AXUIElement.h.
- [AXNotificationConstants.h](axnotificationconstants_h.md)
- [AXRoleConstants.h](axroleconstants_h.md)
- [AXTextAttributedString.h](axtextattributedstring_h.md)
  This header file contains definitions of constants used with accessibility objects that represent attributed strings. An attributed string is an association of a range of characters and their attributes, such as color and font. If an accessibility object represents an attributed string, the value of its `kAXParameterizedAttributeStringAttribute` attribute is an attributed string object (a `CFAttributedStringRef` or an `NSAttributedString`) that uses the constants defined in this header file to define its attributes.
- [AXUIElement.h](axuielement_h.md)
- [AXValue.h](axvalue_h.md)
  This header contains functions and data types for working with AXValueType wrappers.
- [AXValueConstants.h](axvalueconstants_h.md)
- [UniversalAccess.h](universalaccess_h.md)
  This header file contains functions that give applications the ability to control the zoom focus. Using these functions, an application can tell the macOS Universal Access zoom feature what part of its user interface needs focus.
- [ApplicationServices Structures](applicationservices_structures.md)
- [ApplicationServices Enumerations](applicationservices_enumerations.md)
- [ApplicationServices Constants](applicationservices_constants.md)
- [ApplicationServices Functions](applicationservices_functions.md)
- [ApplicationServices Data Types](applicationservices_data_types.md)
### Classes
- [class ColorSyncCMM](../colorsync/colorsynccmm.md)
- [class ColorSyncMutableProfile](../colorsync/colorsyncmutableprofile.md)
- [class ColorSyncProfile](../coregraphics/colorsyncprofile.md)
- [class ColorSyncTransform](../colorsync/colorsynctransform.md)
- [class HIMutableShape](himutableshape.md)
- [class HIShape](hishape.md)
- [class Pasteboard](pasteboard.md)
- [class Translation](translation.md)
- [class AXTextMarker](axtextmarker.md)
- [class AXTextMarkerRange](axtextmarkerrange.md)
### Protocols
- [protocol PDEPanel](pdepanel.md)
- [protocol PDEPlugIn](pdeplugin.md)
- [protocol PDEPlugInCallbackProtocol](pdeplugincallbackprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices)*
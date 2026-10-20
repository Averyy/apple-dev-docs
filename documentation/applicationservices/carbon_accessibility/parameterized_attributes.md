# Parameterized Attributes

**Framework**: Application Services

Define the parameterized attributes an accessibility object can have.

#### Overview

Parameterized attributes allow you to pass in additional values to get more specific information about the text associated with an accessibility object.

## Topics

### Constants
- [var kAXLineForIndexParameterizedAttribute: String](kaxlineforindexparameterizedattribute.md)
  Given an indexed character, the line number of the text associated with this accessibility object that contains the character.
- [var kAXRangeForLineParameterizedAttribute: String](kaxrangeforlineparameterizedattribute.md)
  Given a line number, the range of characters of the text associated with this accessibility object that contains the line number.
- [var kAXStringForRangeParameterizedAttribute: String](kaxstringforrangeparameterizedattribute.md)
  A substring of the text associated with this accessibility object that is specified by the given character range.
- [var kAXRangeForPositionParameterizedAttribute: String](kaxrangeforpositionparameterizedattribute.md)
- [var kAXRangeForIndexParameterizedAttribute: String](kaxrangeforindexparameterizedattribute.md)
- [var kAXBoundsForRangeParameterizedAttribute: String](kaxboundsforrangeparameterizedattribute.md)
  The bounding rectangle of the text associated with this accessibility object that is specified by the given range. This is the bounding rectangle a sighted user would see on the display screen, in pixels.
- [var kAXRTFForRangeParameterizedAttribute: String](kaxrtfforrangeparameterizedattribute.md)
  The RTF representation of the text associated with this accessibility object that is specified by the given range. 
- [var kAXAttributedStringForRangeParameterizedAttribute: String](kaxattributedstringforrangeparameterizedattribute.md)
  The CFAttributedStringType representation of the text associated with this accessibility object that is specified by the given range.
- [var kAXStyleRangeForIndexParameterizedAttribute: String](kaxstylerangeforindexparameterizedattribute.md)
  Given a character index, the range of text associated with this accessibility object over which the style in effect at that character index applies.

## See Also

- [Roles](carbon_accessibility/roles.md)
  Define the values an accessibility object’s role attribute can have.
- [Subroles](carbon_accessibility/subroles.md)
  Define the values for an accessibility object’s subrole attribute.
- [Attributes](carbon_accessibility/attributes.md)
  Define the attributes available for accessibility objects. 
- [Actions](carbon_accessibility/actions.md)
  Define the actions an accessibility object can perform.
- [Notifications](carbon_accessibility/notifications.md)
  Define the notifications that can be broadcast by an accessibility object.
- [Orientations and Sort Directions](carbon_accessibility/orientations_and_sort_directions.md)
  Define the values for the orientation and sort-direction attributes of some accessibility objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/carbon_accessibility/parameterized_attributes)*
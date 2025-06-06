# Attributes

**Framework**: Application Services

Define the attributes available for accessibility objects. 

#### Overview

See the “Roles and Associated Attributes” appendix in [`Accessibility Programming Guide for OS X`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/index.html#//apple_ref/doc/uid/TP40001078) for more information on which attributes are associated with a specific role.

## Topics

### Constants
- [var kAXRoleAttribute: String](kaxroleattribute.md)
  The role, or type, of this accessibility object (for example, `AXButton`). This string is for identification purposes only and does not need to be localized. All accessibility objects must include this attribute.
- [var kAXSubroleAttribute: String](kaxsubroleattribute.md)
- [var kAXRoleDescriptionAttribute: String](kaxroledescriptionattribute.md)
- [var kAXHelpAttribute: String](kaxhelpattribute.md)
  A localized string containing help text for this accessibility object. An accessibility object that provides help information should include this attribute.
- [var kAXTitleAttribute: String](kaxtitleattribute.md)
- [var kAXValueAttribute: String](kaxvalueattribute.md)
- [var kAXMinValueAttribute: String](kaxminvalueattribute.md)
  The minimum value this accessibility object can display (for example, the minimum value of a scroller control). This attribute is used only in conjunction with the `AXValue` attribute. 
- [var kAXMaxValueAttribute: String](kaxmaxvalueattribute.md)
  The maximum value this accessibility object can display (for example, the maximum value of a scroller control). This attribute is used only in conjunction with the `AXValue` attribute.
- [var kAXValueIncrementAttribute: String](kaxvalueincrementattribute.md)
  The amount an accessibility object’s value changes as the result of a single action (for example, how far a scroller travels with one mouse click). This attribute is used only in conjunction with the `AXValue` attribute.
- [var kAXAllowedValuesAttribute: String](kaxallowedvaluesattribute.md)
- [var kAXEnabledAttribute: String](kaxenabledattribute.md)
- [var kAXFocusedAttribute: String](kaxfocusedattribute.md)
- [var kAXParentAttribute: String](kaxparentattribute.md)
  This accessibility object’s parent object in the accessibility hierarchy. This attribute is required for all accessibility objects except the application-level accessibility object.
- [var kAXChildrenAttribute: String](kaxchildrenattribute.md)
- [var kAXSelectedChildrenAttribute: String](kaxselectedchildrenattribute.md)
- [var kAXVisibleChildrenAttribute: String](kaxvisiblechildrenattribute.md)
- [var kAXWindowAttribute: String](kaxwindowattribute.md)
- [var kAXPositionAttribute: String](kaxpositionattribute.md)
- [var kAXTopLevelUIElementAttribute: String](kaxtopleveluielementattribute.md)
- [var kAXSizeAttribute: String](kaxsizeattribute.md)
  The vertical and horizontal dimensions of this accessibility object. This attribute is required for all accessibility objects that are visible on the screen.
- [var kAXOrientationAttribute: String](kaxorientationattribute.md)
- [var kAXDescriptionAttribute: String](kaxdescriptionattribute.md)
- [var kAXSelectedTextAttribute: String](kaxselectedtextattribute.md)
  The currently selected text within this accessibility object. This attribute is required for all accessibility objects that represent editable text elements. 
- [var kAXSelectedTextRangeAttribute: String](kaxselectedtextrangeattribute.md)
  Indicates the range of characters (not bytes) that defines the currently selected text within this accessibility object. This attribute is required for all accessibility objects that represent editable text elements. 
- [var kAXVisibleCharacterRangeAttribute: String](kaxvisiblecharacterrangeattribute.md)
- [var kAXNumberOfCharactersAttribute: String](kaxnumberofcharactersattribute.md)
  The total number of characters (not bytes) in the editable text element represented by this accessibility object. This attribute is required for all accessibility objects that represent editable text elements. 
- [var kAXSharedTextUIElementsAttribute: String](kaxsharedtextuielementsattribute.md)
- [var kAXSharedCharacterRangeAttribute: String](kaxsharedcharacterrangeattribute.md)
- [var kAXMainAttribute: String](kaxmainattribute.md)
- [var kAXMinimizedAttribute: String](kaxminimizedattribute.md)
  Indicates whether the window represented by this accessibility object is currently minimized in the Dock. This attribute is recommended for all accessibility objects that represent windows that can be minimized.
- [var kAXCloseButtonAttribute: String](kaxclosebuttonattribute.md)
- [var kAXZoomButtonAttribute: String](kaxzoombuttonattribute.md)
- [var kAXMinimizeButtonAttribute: String](kaxminimizebuttonattribute.md)
- [var kAXToolbarButtonAttribute: String](kaxtoolbarbuttonattribute.md)
- [var kAXGrowAreaAttribute: String](kaxgrowareaattribute.md)
- [var kAXProxyAttribute: String](kaxproxyattribute.md)
- [var kAXModalAttribute: String](kaxmodalattribute.md)
  Indicates whether the window represented by this accessibility object is modal. This attribute is recommended for all accessibility objects that represent windows.
- [var kAXDefaultButtonAttribute: String](kaxdefaultbuttonattribute.md)
- [var kAXCancelButtonAttribute: String](kaxcancelbuttonattribute.md)
- [var kAXMenuItemCmdCharAttribute: String](kaxmenuitemcmdcharattribute.md)
  The primary key in the keyboard shortcut for the command represented by this accessibility object. For example, “O” is the primary key in the keyboard shortcut for the Open command.
- [var kAXMenuItemCmdVirtualKeyAttribute: String](kaxmenuitemcmdvirtualkeyattribute.md)
- [var kAXMenuItemCmdGlyphAttribute: String](kaxmenuitemcmdglyphattribute.md)
- [var kAXMenuItemCmdModifiersAttribute: String](kaxmenuitemcmdmodifiersattribute.md)
  An integer mask that represents the modifier keys held down in the keyboard shortcut for the command represented by this accessibility object.
- [var kAXMenuItemMarkCharAttribute: String](kaxmenuitemmarkcharattribute.md)
- [var kAXMenuItemPrimaryUIElementAttribute: String](kaxmenuitemprimaryuielementattribute.md)
- [var kAXMenuBarAttribute: String](kaxmenubarattribute.md)
- [var kAXWindowsAttribute: String](kaxwindowsattribute.md)
  An array of accessibility objects representing this application’s windows. This attribute is recommended for all application-level accessibility objects.
- [var kAXFrontmostAttribute: String](kaxfrontmostattribute.md)
  Indicates whether the application represented by this accessibility object is active. This attribute is recommended for all application-level accessibility objects.
- [var kAXHiddenAttribute: String](kaxhiddenattribute.md)
  Indicates whether the application represented by this accessibility object is hidden. This attribute is recommended for all application-level accessibility objects.
- [var kAXMainWindowAttribute: String](kaxmainwindowattribute.md)
  The accessibility object representing this application’s main window. This attribute is recommended for all application-level accessibility objects.
- [var kAXFocusedWindowAttribute: String](kaxfocusedwindowattribute.md)
  The accessibility object that represents the currently focused window of this application. This attribute is recommended for all application-level accessibility objects.
- [var kAXHeaderAttribute: String](kaxheaderattribute.md)
- [var kAXEditedAttribute: String](kaxeditedattribute.md)
- [var kAXTitleUIElementAttribute: String](kaxtitleuielementattribute.md)
  An accessibility object that represents a static text title associated with another accessibility object.
- [var kAXValueWrapsAttribute: String](kaxvaluewrapsattribute.md)
  Indicates whether the value displayed in the user interface element represented by this accessibility object wraps around.
- [var kAXTabsAttribute: String](kaxtabsattribute.md)
- [var kAXHorizontalScrollBarAttribute: String](kaxhorizontalscrollbarattribute.md)
- [var kAXVerticalScrollBarAttribute: String](kaxverticalscrollbarattribute.md)
- [var kAXOverflowButtonAttribute: String](kaxoverflowbuttonattribute.md)
  Identifies which child of an accessibility object representing a toolbar is the overflow button (if any). This attribute is optional.
- [var kAXFilenameAttribute: String](kaxfilenameattribute.md)
  The filename associated with this accessibility object. This attribute is optional.
- [var kAXExpandedAttribute: String](kaxexpandedattribute.md)
  Indicates whether the menu displayed by the combo box or pop-up menu represented by this accessibility object is currently expanded. This attribute is recommended for all accessibility objects that display a pop-up menu.
- [var kAXSelectedAttribute: String](kaxselectedattribute.md)
  Indicates whether the row or column element represented by this accessibility object is selected. This attribute is recommended for all accessibility objects that represent selectable rows or columns.
- [var kAXSplittersAttribute: String](kaxsplittersattribute.md)
  An array of views and splitter bar elements displayed by the split view represented by this accessibility object. This is a convenience attribute that helps an assistive application easily find these elements.
- [var kAXNextContentsAttribute: String](kaxnextcontentsattribute.md)
- [var kAXPreviousContentsAttribute: String](kaxpreviouscontentsattribute.md)
- [var kAXDocumentAttribute: String](kaxdocumentattribute.md)
  The URL of the open document represented by this accessibility object. This attribute represents the URL as a string object.
- [var kAXIncrementButtonAttribute: String](kaxincrementbuttonattribute.md)
- [var kAXDecrementButtonAttribute: String](kaxdecrementbuttonattribute.md)
  The decrement element associated with the user interface object this accessibility object represents. This attribute can be used to provide convenient access to the decrement area of a custom user interface object.
- [var kAXContentsAttribute: String](kaxcontentsattribute.md)
- [var kAXIncrementorAttribute: String](kaxincrementorattribute.md)
  The incrementor of a time or date field represented by this accessibility object. This attribute is required for accessibility objects that represent time or date field elements that display an incrementor.
- [var kAXHourFieldAttribute: String](kaxhourfieldattribute.md)
  The hour field of a time field represented by this accessibility object. This attribute is required for accessibility objects that represent time fields that display hours.
- [var kAXMinuteFieldAttribute: String](kaxminutefieldattribute.md)
  The minute field of a time field represented by this accessibility object. This attribute is required for accessibility objects that represent time fields that display minutes.
- [var kAXSecondFieldAttribute: String](kaxsecondfieldattribute.md)
  The second field of a time field represented by this accessibility object. This attribute is required for accessibility objects that represent time fields that display seconds.
- [var kAXAMPMFieldAttribute: String](kaxampmfieldattribute.md)
  The AM/PM field of a time field represented by this accessibility object. This attribute is required for accessibility objects that represent time fields that display AM/PM settings.
- [var kAXDayFieldAttribute: String](kaxdayfieldattribute.md)
  The day field of a time field represented by this accessibility object. This attribute is required for accessibility objects that represent time fields that display days.
- [var kAXMonthFieldAttribute: String](kaxmonthfieldattribute.md)
  The month field of a time field represented by this accessibility object. This attribute is required for accessibility objects that represent time fields that display months.
- [var kAXYearFieldAttribute: String](kaxyearfieldattribute.md)
  The year field of a time field represented by this accessibility object. This attribute is required for accessibility objects that represent time fields that display years.
- [var kAXColumnTitleAttribute: String](kaxcolumntitleattribute.md)
- [var kAXURLAttribute: String](kaxurlattribute.md)
  The URL that describes the location of the document or application represented by this accessibility object.
- [var kAXLabelUIElementsAttribute: String](kaxlabeluielementsattribute.md)
- [var kAXLabelValueAttribute: String](kaxlabelvalueattribute.md)
  The value of the label represented by this accessibility object. This attribute is required for all accessibility objects that represent labels.
- [var kAXShownMenuUIElementAttribute: String](kaxshownmenuuielementattribute.md)
  An array of accessibility objects that represent the contextual or Dock menus provided by this accessibility object.
- [var kAXServesAsTitleForUIElementsAttribute: String](kaxservesastitleforuielementsattribute.md)
- [var kAXLinkedUIElementsAttribute: String](kaxlinkeduielementsattribute.md)
- [var kAXRowsAttribute: String](kaxrowsattribute.md)
  An array of the accessibility objects representing the rows in this table or outline view.
- [var kAXVisibleRowsAttribute: String](kaxvisiblerowsattribute.md)
  An array of the accessibility objects representing the currently visible rows in this table or outline view.
- [var kAXSelectedRowsAttribute: String](kaxselectedrowsattribute.md)
  An array of the accessibility objects representing the currently selected rows in this table or outline view.
- [var kAXColumnsAttribute: String](kaxcolumnsattribute.md)
  An array of the accessibility objects representing the columns in this browser view.
- [var kAXVisibleColumnsAttribute: String](kaxvisiblecolumnsattribute.md)
  An array of the accessibility objects representing the currently visible columns in this browser view.
- [var kAXSelectedColumnsAttribute: String](kaxselectedcolumnsattribute.md)
  An array of the accessibility objects representing the currently selected columns in this browser view.
- [var kAXSortDirectionAttribute: String](kaxsortdirectionattribute.md)
  The sort direction of this accessibility object’s contents. For example, a list view’s contents may be sorted in ascending or descending order.
- [var kAXColumnHeaderUIElementsAttribute: String](kaxcolumnheaderuielementsattribute.md)
  An array of accessibility objects representing the column headers of this table or browser view.
- [var kAXIndexAttribute: String](kaxindexattribute.md)
  The index of the row or column represented by this accessibility object.
- [var kAXDisclosingAttribute: String](kaxdisclosingattribute.md)
  Indicates whether a row in an outline view represented by this accessibility object has an open or closed disclosure triangle. `true` indicates an open disclosure triangle; `false` indicates a closed disclosure triangle.
- [var kAXDisclosedRowsAttribute: String](kaxdisclosedrowsattribute.md)
  An array of accessibility objects representing the disclosed rows of this user interface element.
- [var kAXDisclosedByRowAttribute: String](kaxdisclosedbyrowattribute.md)
  The accessibility object representing the disclosing row.
- [var kAXMatteHoleAttribute: String](kaxmatteholeattribute.md)
  The accessibility object that represents the area available to the user through the matte hole.
- [var kAXMatteContentUIElementAttribute: String](kaxmattecontentuielementattribute.md)
  The accessibility object clipped by the matte.
- [var kAXIsApplicationRunningAttribute: String](kaxisapplicationrunningattribute.md)
  Indicates if the application represented by the Dock icon this accessibility object represents is currently running.
- [var kAXFocusedApplicationAttribute: String](kaxfocusedapplicationattribute.md)
- [var kAXInsertionPointLineNumberAttribute: String](kaxinsertionpointlinenumberattribute.md)
  The line number of the insertion point in the text associated with this accessibility object.

## See Also

- [Roles](carbon_accessibility/roles.md)
  Define the values an accessibility object’s role attribute can have.
- [Subroles](carbon_accessibility/subroles.md)
  Define the values for an accessibility object’s subrole attribute.
- [Parameterized Attributes](carbon_accessibility/parameterized_attributes.md)
  Define the parameterized attributes an accessibility object can have.
- [Actions](carbon_accessibility/actions.md)
  Define the actions an accessibility object can perform.
- [Notifications](carbon_accessibility/notifications.md)
  Define the notifications that can be broadcast by an accessibility object.
- [Orientations and Sort Directions](carbon_accessibility/orientations_and_sort_directions.md)
  Define the values for the orientation and sort-direction attributes of some accessibility objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/carbon_accessibility/attributes)*
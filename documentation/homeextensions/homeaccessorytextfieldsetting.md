# HomeAccessoryTextFieldSetting

**Framework**: HomeExtensions  
**Kind**: class  
**Role**: Class

A setting that contains a single line of editable text.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@propertyWrapper
final class HomeAccessoryTextFieldSetting
```

## Overview

The Home app presents this setting as a text field with a Clear button. Your extension receives the new value after a person finishes editing, not after every keystroke.

## Topics

### Creating a text field setting
- [init(id: String, label: HomeAccessorySettingLabel, isEnabled: Bool, defaultValue: String?, currentValue: String?, placeholder: LocalizedStringResource?)](./homeaccessorytextfieldsetting/init%28id,label,isenabled,defaultvalue,currentvalue,placeholder%29.md)
  Creates a text field setting.
### Configuring presentation
- [var label: HomeAccessorySettingLabel](./homeaccessorytextfieldsetting/label.md)
  The label to display for this setting.
- [var isEnabled: Bool](./homeaccessorytextfieldsetting/isenabled.md)
  A Boolean value that indicates whether people can change the setting.
- [var isHidden: Bool](./homeaccessorytextfieldsetting/ishidden.md)
  A Boolean value that indicates whether the setting is hidden.
### Accessing the value
- [var wrappedValue: String?](./homeaccessorytextfieldsetting/wrappedvalue.md)
  The setting’s current text, or its default text if it has none.
- [var projectedValue: HomeAccessoryTextFieldSetting](./homeaccessorytextfieldsetting/projectedvalue.md)
  The setting itself, which you access with a dollar sign prefix.

## Relationships

### Conforms To
- [HomeAccessorySetting](./homeaccessorysetting.md)
- [Identifiable](../Swift/identifiable.md)

## See Also

### Defining accessory settings
- [protocol HomeAccessorySetting](./homeaccessorysetting.md)
  A type that represents a single accessory setting.
- [struct HomeAccessorySettingLabel](./homeaccessorysettinglabel.md)
  The text that the Home app displays for a setting or an option.
- [class HomeAccessoryEnumSetting](./homeaccessoryenumsetting.md)
  A setting that offers a choice among several options.
- [protocol HomeAccessoryEnumSettingConstant](./homeaccessoryenumsettingconstant.md)
  A type whose cases are the options for an enumeration setting.
- [class HomeAccessoryInformationSetting](./homeaccessoryinformationsetting.md)
  A read-only setting that displays a label and a value.
- [class HomeAccessoryRangeSetting](./homeaccessoryrangesetting.md)
  A setting that represents a numeric value within a range.
- [protocol HomeAccessoryRangeSettingDescriptor](./homeaccessoryrangesettingdescriptor.md)
  A type that describes the bounds of a range setting.
- [class HomeAccessoryToggleSetting](./homeaccessorytogglesetting.md)
  A setting that offers a binary choice, such as on or off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorytextfieldsetting)*
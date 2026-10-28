# HomeAccessoryEnumSetting

**Framework**: HomeExtensions  
**Kind**: class  
**Role**: Class

A setting that offers a choice among several options.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@propertyWrapper
final class HomeAccessoryEnumSetting<Value> where Value : HomeAccessoryEnumSettingConstant
```

## Overview

Define the options with a type that adopts [`HomeAccessoryEnumSettingConstant`](./homeaccessoryenumsettingconstant.md), and specify how they appear with [`HomeAccessoryEnumSetting.SelectionStyle`](./homeaccessoryenumsetting/selectionstyle.md).

## Topics

### Creating an enumeration setting
- [init(id: String, label: HomeAccessorySettingLabel, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, style: HomeAccessoryEnumSetting<Value>.SelectionStyle)](./homeaccessoryenumsetting/init%28id,label,isenabled,defaultvalue,currentvalue,style%29.md)
  Creates an enumeration setting.
- [HomeAccessoryEnumSetting.SelectionStyle](./homeaccessoryenumsetting/selectionstyle.md)
  Styles for presenting an enumeration setting’s options.
### Configuring presentation
- [var label: HomeAccessorySettingLabel](./homeaccessoryenumsetting/label.md)
  The label to display for this setting.
- [var isEnabled: Bool](./homeaccessoryenumsetting/isenabled.md)
  A Boolean value that indicates whether people can change the setting.
- [var isHidden: Bool](./homeaccessoryenumsetting/ishidden.md)
  A Boolean value that indicates whether the setting is hidden.
### Accessing the selection
- [var wrappedValue: Value?](./homeaccessoryenumsetting/wrappedvalue.md)
  The selected option, or the default option if nothing is selected.
- [var selectedValues: Set<Value>?](./homeaccessoryenumsetting/selectedvalues.md)
  The selected options, for a setting that supports multiple selection.
- [var projectedValue: HomeAccessoryEnumSetting<Value>](./homeaccessoryenumsetting/projectedvalue.md)
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
- [protocol HomeAccessoryEnumSettingConstant](./homeaccessoryenumsettingconstant.md)
  A type whose cases are the options for an enumeration setting.
- [class HomeAccessoryInformationSetting](./homeaccessoryinformationsetting.md)
  A read-only setting that displays a label and a value.
- [class HomeAccessoryRangeSetting](./homeaccessoryrangesetting.md)
  A setting that represents a numeric value within a range.
- [protocol HomeAccessoryRangeSettingDescriptor](./homeaccessoryrangesettingdescriptor.md)
  A type that describes the bounds of a range setting.
- [class HomeAccessoryTextFieldSetting](./homeaccessorytextfieldsetting.md)
  A setting that contains a single line of editable text.
- [class HomeAccessoryToggleSetting](./homeaccessorytogglesetting.md)
  A setting that offers a binary choice, such as on or off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryenumsetting)*
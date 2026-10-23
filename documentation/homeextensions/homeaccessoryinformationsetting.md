# HomeAccessoryInformationSetting

**Framework**: HomeExtensions  
**Kind**: class  
**Role**: Class

A read-only setting that displays a label and a value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@propertyWrapper
final class HomeAccessoryInformationSetting
```

#### Overview

People can view the value but can’t change it. The Home app displays the value exactly as you provide it, so format and localize it beforehand.

## Topics

### Creating an information setting
- [init(id: String, label: HomeAccessorySettingLabel, value: String?)](./homeaccessoryinformationsetting/init%28id,label,value%29.md)
  Creates an information setting.
### Configuring presentation
- [var label: HomeAccessorySettingLabel](./homeaccessoryinformationsetting/label.md)
  The label to display for this setting.
- [var isHidden: Bool](./homeaccessoryinformationsetting/ishidden.md)
  A Boolean value that indicates whether the setting is hidden.
### Accessing the value
- [var wrappedValue: String?](./homeaccessoryinformationsetting/wrappedvalue.md)
  The setting’s value.
- [var projectedValue: HomeAccessoryInformationSetting](./homeaccessoryinformationsetting/projectedvalue.md)
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
- [class HomeAccessoryRangeSetting](./homeaccessoryrangesetting.md)
  A setting that represents a numeric value within a range.
- [protocol HomeAccessoryRangeSettingDescriptor](./homeaccessoryrangesettingdescriptor.md)
  A type that describes the bounds of a range setting.
- [class HomeAccessoryTextFieldSetting](./homeaccessorytextfieldsetting.md)
  A setting that contains a single line of editable text.
- [class HomeAccessoryToggleSetting](./homeaccessorytogglesetting.md)
  A setting that offers a binary choice, such as on or off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryinformationsetting)*
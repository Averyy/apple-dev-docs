# HomeAccessoryToggleSetting

**Framework**: HomeExtensions  
**Kind**: class  
**Role**: Class

A setting that offers a binary choice, such as on or off.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@propertyWrapper
final class HomeAccessoryToggleSetting
```

#### Overview

The Home app displays this setting as a toggle.

## Topics

### Creating a toggle setting
- [init(id: String, label: HomeAccessorySettingLabel, isEnabled: Bool, defaultValue: Bool?, currentValue: Bool?, onLabel: HomeAccessorySettingLabel?, offLabel: HomeAccessorySettingLabel?)](./homeaccessorytogglesetting/init%28id,label,isenabled,defaultvalue,currentvalue,onlabel,offlabel%29.md)
  Creates a toggle setting.
### Configuring presentation
- [var label: HomeAccessorySettingLabel](./homeaccessorytogglesetting/label.md)
  The label to display for this setting.
- [var isEnabled: Bool](./homeaccessorytogglesetting/isenabled.md)
  A Boolean value that indicates whether people can change the setting.
- [var isHidden: Bool](./homeaccessorytogglesetting/ishidden.md)
  A Boolean value that indicates whether the setting is hidden.
### Accessing the value
- [var wrappedValue: Bool?](./homeaccessorytogglesetting/wrappedvalue.md)
  The setting’s current value, or its default value if it has none.
- [var projectedValue: HomeAccessoryToggleSetting](./homeaccessorytogglesetting/projectedvalue.md)
  The setting itself, which you access with a dollar sign prefix.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
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
- [class HomeAccessoryTextFieldSetting](./homeaccessorytextfieldsetting.md)
  A setting that contains a single line of editable text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorytogglesetting)*
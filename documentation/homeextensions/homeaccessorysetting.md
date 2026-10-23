# HomeAccessorySetting

**Framework**: HomeExtensions  
**Kind**: protocol  
**Role**: Protocol

A type that represents a single accessory setting.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
protocol HomeAccessorySetting : Identifiable where Self.ID == String
```

#### Overview

You don’t adopt this protocol directly. Instead, use one of the setting property wrappers, such as [`HomeAccessoryToggleSetting`](./homeaccessorytogglesetting.md) or [`HomeAccessoryRangeSetting`](./homeaccessoryrangesetting.md).

## Topics

### Definining a setting
- [var id: String](./homeaccessorysetting/id.md)
  A unique identifier for the setting.

## Relationships

### Inherits From
- [Identifiable](../Swift/identifiable.md)
### Conforming Types
- [HomeAccessoryEnumSetting](./homeaccessoryenumsetting.md)
- [HomeAccessoryInformationSetting](./homeaccessoryinformationsetting.md)
- [HomeAccessoryRangeSetting](./homeaccessoryrangesetting.md)
- [HomeAccessoryTextFieldSetting](./homeaccessorytextfieldsetting.md)
- [HomeAccessoryToggleSetting](./homeaccessorytogglesetting.md)

## See Also

### Defining accessory settings
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
- [class HomeAccessoryToggleSetting](./homeaccessorytogglesetting.md)
  A setting that offers a binary choice, such as on or off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorysetting)*
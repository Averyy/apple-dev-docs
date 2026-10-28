# HomeAccessoryEnumSettingConstant

**Framework**: HomeExtensions  
**Kind**: protocol  
**Role**: Protocol

A type whose cases are the options for an enumeration setting.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
protocol HomeAccessoryEnumSettingConstant : CaseIterable, Hashable, RawRepresentable where Self.RawValue : LosslessStringConvertible
```

## Overview

For example, the following code defines an enumeration that has a string raw value:

```swift
enum FanSpeed: String, HomeAccessoryEnumSettingConstant {
    case low, medium, high

    var value: HomeAccessorySettingLabel {
        switch self {
        case .low: HomeAccessorySettingLabel("Low", systemImage: "wind")
        case .medium: HomeAccessorySettingLabel("Medium", systemImage: "wind.circle")
        case .high: HomeAccessorySettingLabel("High", systemImage: "wind.circle.fill")
        }
    }
}
```

## Topics

### Providing a label
- [var value: HomeAccessorySettingLabel](./homeaccessoryenumsettingconstant/value.md)
  The label to display for this setting.

## Relationships

### Inherits From
- [CaseIterable](../Swift/caseiterable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)

## See Also

### Defining accessory settings
- [protocol HomeAccessorySetting](./homeaccessorysetting.md)
  A type that represents a single accessory setting.
- [struct HomeAccessorySettingLabel](./homeaccessorysettinglabel.md)
  The text that the Home app displays for a setting or an option.
- [class HomeAccessoryEnumSetting](./homeaccessoryenumsetting.md)
  A setting that offers a choice among several options.
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

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryenumsettingconstant)*
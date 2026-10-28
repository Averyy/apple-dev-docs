# HomeAccessoryRangeSettingDescriptor

**Framework**: HomeExtensions  
**Kind**: protocol  
**Role**: Protocol

A type that describes the bounds of a range setting.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
protocol HomeAccessoryRangeSettingDescriptor<Bound>
```

## Overview

You don’t adopt this protocol directly. Standard range types, such as `ClosedRange`, adopt it, so you can pass a range expression like `0...100`.

## Topics

### Definining a range
- [var rangeLowerBound: Self.Bound?](./homeaccessoryrangesettingdescriptor/rangelowerbound.md)
  The range’s lower bound, if it has one.
- [var rangeUpperBound: Self.Bound?](./homeaccessoryrangesettingdescriptor/rangeupperbound.md)
  The range’s upper bound, if it has one.
- [associatedtype Bound : Comparable, Numeric](./homeaccessoryrangesettingdescriptor/bound.md)
  The type of the range’s bounds.

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
- [class HomeAccessoryTextFieldSetting](./homeaccessorytextfieldsetting.md)
  A setting that contains a single line of editable text.
- [class HomeAccessoryToggleSetting](./homeaccessorytogglesetting.md)
  A setting that offers a binary choice, such as on or off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryrangesettingdescriptor)*
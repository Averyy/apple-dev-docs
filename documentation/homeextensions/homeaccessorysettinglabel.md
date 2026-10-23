# HomeAccessorySettingLabel

**Framework**: HomeExtensions  
**Kind**: struct  
**Role**: Structure

The text that the Home app displays for a setting or an option.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
struct HomeAccessorySettingLabel
```

## Topics

### Creating a label
- [init(LocalizedStringResource, detailedLabel: LocalizedStringResource?, systemImage: String?)](./homeaccessorysettinglabel/init%28_,detailedlabel,systemimage%29.md)
  Creates a label with primary text, and optional detail text and symbol.
### Setting the label text
- [let label: LocalizedStringResource](./homeaccessorysettinglabel/label.md)
  The primary text.
- [let detailedLabel: LocalizedStringResource?](./homeaccessorysettinglabel/detailedlabel.md)
  Optional text that describes the setting in more detail.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/expressiblebyunicodescalarliteral.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Defining accessory settings
- [protocol HomeAccessorySetting](./homeaccessorysetting.md)
  A type that represents a single accessory setting.
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

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorysettinglabel)*
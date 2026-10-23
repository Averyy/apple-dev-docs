# HomeAccessoryEnumSetting.SelectionStyle

**Framework**: HomeExtensions  
**Kind**: enum  
**Role**: Enumeration

Styles for presenting an enumeration setting’s options.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
enum SelectionStyle
```

## Topics

### Presentation styles
- [HomeAccessoryEnumSetting.SelectionStyle.expanded](./selectionstyle/expanded.md)
  A section that lists each option in its own row.
- [HomeAccessoryEnumSetting.SelectionStyle.inline](./selectionstyle/inline.md)
  A row that contains a pop-up menu of options.
- [HomeAccessoryEnumSetting.SelectionStyle.navigation](./selectionstyle/navigation.md)
  A row that displays the current selection and opens a list of options.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Creating an enumeration setting
- [init(id: String, label: HomeAccessorySettingLabel, isEnabled: Bool, defaultValue: Value?, currentValue: Value?, style: HomeAccessoryEnumSetting<Value>.SelectionStyle)](./init%28id,label,isenabled,defaultvalue,currentvalue,style%29.md)
  Creates an enumeration setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryenumsetting/selectionstyle)*
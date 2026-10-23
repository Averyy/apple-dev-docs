# init(id:label:isEnabled:defaultValue:currentValue:style:)

**Framework**: HomeExtensions  
**Kind**: init  
**Role**: Initializer

Creates an enumeration setting.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(id: String, label: HomeAccessorySettingLabel, isEnabled: Bool = true, defaultValue: Value? = nil, currentValue: Value? = nil, style: HomeAccessoryEnumSetting<Value>.SelectionStyle = .inline)
```

## Parameters

- `id`: A unique identifier for the setting.
- `label`: The setting’s label.
- `isEnabled`: A Boolean value that indicates whether people can change the setting. The default is `true`.
- `defaultValue`: The option to use when nothing is selected.
- `currentValue`: The selected option.
- `style`: The style for presenting the options. The default is [`HomeAccessoryEnumSetting.SelectionStyle.inline`](./selectionstyle/inline.md).

## See Also

### Creating an enumeration setting
- [HomeAccessoryEnumSetting.SelectionStyle](./selectionstyle.md)
  Styles for presenting an enumeration setting’s options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryenumsetting/init(id:label:isenabled:defaultvalue:currentvalue:style:))*
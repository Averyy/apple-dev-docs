# init(id:label:isEnabled:defaultValue:currentValue:placeholder:)

**Framework**: HomeExtensions  
**Kind**: init  
**Role**: Initializer

Creates a text field setting.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(id: String, label: HomeAccessorySettingLabel, isEnabled: Bool = true, defaultValue: String? = nil, currentValue: String? = nil, placeholder: LocalizedStringResource? = nil)
```

## Parameters

- `id`: A unique identifier for the setting.
- `label`: The setting’s label.
- `isEnabled`: A Boolean value that indicates whether people can change the setting. The default is `true`.
- `defaultValue`: The text to use when there’s no current value.
- `currentValue`: The setting’s current text.
- `placeholder`: The text to display when the field is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorytextfieldsetting/init(id:label:isenabled:defaultvalue:currentvalue:placeholder:))*
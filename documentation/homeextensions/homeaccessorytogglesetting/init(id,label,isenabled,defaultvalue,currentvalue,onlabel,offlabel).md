# init(id:label:isEnabled:defaultValue:currentValue:onLabel:offLabel:)

**Framework**: HomeExtensions  
**Kind**: init  
**Role**: Initializer

Creates a toggle setting.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(id: String, label: HomeAccessorySettingLabel, isEnabled: Bool = true, defaultValue: Bool? = nil, currentValue: Bool? = nil, onLabel: HomeAccessorySettingLabel? = nil, offLabel: HomeAccessorySettingLabel? = nil)
```

## Parameters

- `id`: A unique identifier for the setting.
- `label`: The setting’s label.
- `isEnabled`: A Boolean value that indicates whether people can change the setting. The default is `true`.
- `defaultValue`: The value to use when there’s no current value.
- `currentValue`: The setting’s current value.
- `onLabel`: The label to display when the setting is on.
- `offLabel`: The label to display when the setting is off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorytogglesetting/init(id:label:isenabled:defaultvalue:currentvalue:onlabel:offlabel:))*
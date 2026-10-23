# init(_:detailedLabel:systemImage:)

**Framework**: HomeExtensions  
**Kind**: init  
**Role**: Initializer

Creates a label with primary text, and optional detail text and symbol.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(_ label: LocalizedStringResource, detailedLabel: LocalizedStringResource? = nil, systemImage: String? = nil)
```

## Parameters

- `label`: The primary text.
- `detailedLabel`: Optional text that describes the setting in more detail.
- `systemImage`: The name of an optional system symbol to display with the label, such as for an enumeration option. The Home app doesn’t display it for a setting’s own label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessorysettinglabel/init(_:detailedlabel:systemimage:))*
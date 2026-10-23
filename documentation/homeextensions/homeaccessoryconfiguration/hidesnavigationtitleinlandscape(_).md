# hidesNavigationTitleInLandscape(_:)

**Framework**: HomeExtensions  
**Kind**: method  
**Role**: Instance Method

Hides or shows the Home app’s navigation title and app icon in landscape.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
func hidesNavigationTitleInLandscape(_ hides: Bool = true) -> HomeAccessoryConfiguration
```

#### Return Value

A configuration that reflects the new setting.

#### Discussion

The Close or Back button remains visible, so people can always dismiss the view.

## Parameters

- `hides`: A Boolean value that indicates whether to hide the title and icon. The default is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homeextensions/homeaccessoryconfiguration/hidesnavigationtitleinlandscape(_:))*
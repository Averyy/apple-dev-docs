# pushTokensDidChange(controls:)

**Framework**: WidgetKit  
**Kind**: method  
**Required**: Yes

Handle push tokens changing for configured controls.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func pushTokensDidChange(controls: [ControlInfo])
```

#### Discussion

This function always provides information for all controls that support push updates even if only some of the tokens have changed.

## Parameters

- `controls`: Information about controls that support push   updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlpushhandler/pushtokensdidchange(controls:))*
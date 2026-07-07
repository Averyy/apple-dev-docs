# widgetURL(_:)

**Framework**: WidgetKit  
**Kind**: method

Sets the URL that opens the corresponding app of a Live Activity when a user taps on the Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
func widgetURL(_ url: URL?) -> DynamicIsland
```

#### Return Value

The configuration object for the Dynamic Island with the specified URL.

#### Discussion

By setting the URL with this function, it becomes the default URL for deep linking into the app for each view of the Live Activity. However, if you include a [`Link`](https://developer.apple.com/documentation/SwiftUI/Link) in the Live Activity, the link takes priority over the default URL. When a person taps on the `Link`, it takes them to the place in the app that corresponds to the URL of the `Link`.

## Parameters

- `url`: The URL that opens the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/dynamicisland/widgeturl(_:))*
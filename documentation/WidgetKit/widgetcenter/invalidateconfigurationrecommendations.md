# invalidateConfigurationRecommendations()

**Framework**: Widgetkit  
**Kind**: method

Invalidates and refreshes the preconfigured intent configurations for user-customizable widgets.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
func invalidateConfigurationRecommendations()
```

## Mentions

- [Making a configurable widget](making-a-configurable-widget.md)

#### Discussion

In watchOS, call this function when your app receives new data for preconfigured widgets you’d like to appear in the list of available watch complications.

> **Note**: On platforms that offer a dedicated user interface for configuring widgets — for example, iOS or macOS — `invalidateConfigurationRecommendations()` is inactive.

On platforms that offer a dedicated user interface for configuring widgets — for example, iOS or macOS — `invalidateConfigurationRecommendations()` is inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetcenter/invalidateconfigurationrecommendations())*
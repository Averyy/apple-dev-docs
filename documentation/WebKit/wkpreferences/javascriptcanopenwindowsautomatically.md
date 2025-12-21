# javaScriptCanOpenWindowsAutomatically

**Framework**: WebKit  
**Kind**: property

A Boolean value that indicates whether JavaScript can open windows without user interaction.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var javaScriptCanOpenWindowsAutomatically: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/Swift/false) in iOS and [`true`](https://developer.apple.com/documentation/Swift/true) in macOS.

## See Also

- [var isSiteSpecificQuirksModeEnabled: Bool](wkpreferences/issitespecificquirksmodeenabled.md)
  A Boolean that indicates whether to apply site-specific compatibility workarounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpreferences/javascriptcanopenwindowsautomatically)*
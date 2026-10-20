# javaScriptCanOpenWindowsAutomatically

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether JavaScript can open windows without user interaction.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+

## Declaration

```swift
var javaScriptCanOpenWindowsAutomatically: Bool { get set }
```

```objc
@property (nonatomic) BOOL javaScriptCanOpenWindowsAutomatically;
```

#### Discussion

The default value is [`false`](../../Swift/false.md) in iOS and [`true`](../../Swift/true.md) in macOS.

## See Also

### Setting Java and JavaScript Preferences
- [var isSiteSpecificQuirksModeEnabled: Bool](./issitespecificquirksmodeenabled.md)
  A Boolean that indicates whether to apply site-specific compatibility workarounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpreferences/javascriptcanopenwindowsautomatically)*
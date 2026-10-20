# isSiteSpecificQuirksModeEnabled

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether to apply site-specific compatibility workarounds.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- visionOS 1.0+

## Declaration

```swift
var isSiteSpecificQuirksModeEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isSiteSpecificQuirksModeEnabled) BOOL siteSpecificQuirksModeEnabled;
```

#### Discussion

The default value for this preference is [`true`](../../Swift/true.md).

## See Also

### Setting Java and JavaScript Preferences
- [var javaScriptCanOpenWindowsAutomatically: Bool](./javascriptcanopenwindowsautomatically.md)
  A Boolean value that indicates whether JavaScript can open windows without user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkpreferences/issitespecificquirksmodeenabled)*
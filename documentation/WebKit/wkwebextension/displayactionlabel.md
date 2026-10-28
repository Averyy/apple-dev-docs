# displayActionLabel

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The default localized extension action label.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var displayActionLabel: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * displayActionLabel;
```

## Discussion

Returns `nil` if there was no default action label specified.

This label serves as a default and should be used to represent the extension in contexts like action sheets or toolbars prior to the extension being loaded into an extension context. Once the extension is loaded, use the [`action(for:)`](../wkwebextensioncontext/action%28for%29.md) API to get the tab-specific label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/displayactionlabel)*
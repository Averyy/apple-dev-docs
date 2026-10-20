# defaultLocale

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

The default locale for the extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var defaultLocale: Locale? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSLocale * defaultLocale;
```

#### Discussion

Returns `nil` if there was no default locale specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/defaultlocale)*
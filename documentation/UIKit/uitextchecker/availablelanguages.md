# availableLanguages

**Framework**: UIKit  
**Kind**: property

Returns the languages that the text checker’s class can perform spell-checking for.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class var availableLanguages: [String] { get }
```

#### Return Value

An array of strings representing ISO 639-1 language codes or combined ISO 639-1 language codes and ISO 3166-1 regional codes (for example, `en_US`).

#### Discussion

The languages represented by the strings in the returned array are in user-preference order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextchecker/availablelanguages)*
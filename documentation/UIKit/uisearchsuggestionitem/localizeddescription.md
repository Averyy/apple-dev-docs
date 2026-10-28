# localizedDescription

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A description of the suggestion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var localizedDescription: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * localizedDescription;
```

## Discussion

The system uses this description for accessibility.

## See Also

### Describing a search suggestion
- [var localizedSuggestion: String?](./localizedsuggestion.md)
  A label for the suggestion, usually the search term the suggestion represents.
- [var localizedAttributedSuggestion: NSAttributedString?](./localizedattributedsuggestion.md)
  An attributed label for the suggestion, usually the search term the suggestion represents.
- [var iconImage: UIImage?](./iconimage.md)
  An image for display on the suggestion.
- [var representedObject: Any?](./representedobject.md)
  An object for tracking supplementary information about the search suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/localizeddescription)*
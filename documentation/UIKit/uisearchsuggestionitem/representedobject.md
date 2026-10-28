# representedObject

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object for tracking supplementary information about the search suggestion.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var representedObject: Any? { get set }
```

```objc
@property (nonatomic, strong, nullable) id representedObject;
```

## Discussion

Use this property to associate the search suggestion with a corresponding object.

## See Also

### Describing a search suggestion
- [var localizedSuggestion: String?](./localizedsuggestion.md)
  A label for the suggestion, usually the search term the suggestion represents.
- [var localizedAttributedSuggestion: NSAttributedString?](./localizedattributedsuggestion.md)
  An attributed label for the suggestion, usually the search term the suggestion represents.
- [var localizedDescription: String?](./localizeddescription.md)
  A description of the suggestion.
- [var iconImage: UIImage?](./iconimage.md)
  An image for display on the suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/representedobject)*
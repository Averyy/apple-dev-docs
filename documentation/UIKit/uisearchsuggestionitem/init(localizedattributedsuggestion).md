# init(localizedAttributedSuggestion:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a search suggestion with the specified attributed label.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
init(localizedAttributedSuggestion suggestion: NSAttributedString)
```

```objc
- (instancetype) initWithLocalizedAttributedSuggestion:(NSAttributedString *) suggestion;
```

## Parameters

- `suggestion`: An attributed label for the suggestion, usually the search term the suggestion represents.

## See Also

### Creating a search suggestion
- [init(localizedSuggestion: String, localizedDescription: String?, iconImage: UIImage?)](./init%28localizedsuggestion,localizeddescription,iconimage%29.md)
  Creates a search suggestion with the specified text and image attributes.
- [init(localizedAttributedSuggestion: NSAttributedString, localizedDescription: String?, iconImage: UIImage?)](./init%28localizedattributedsuggestion,localizeddescription,iconimage%29.md)
  Creates a search suggestion with the specified attributed label, accessibility description, and image.
- [init(localizedSuggestion: String, localizedDescription: String?)](./init%28localizedsuggestion,localizeddescription%29.md)
  Creates a search suggestion with the specified label and accessibility description.
- [init(localizedAttributedSuggestion: NSAttributedString, localizedDescription: String?)](./init%28localizedattributedsuggestion,localizeddescription%29.md)
  Creates a search suggestion with the specified attributed label and accessibility description.
- [init(localizedSuggestion: String)](./init%28localizedsuggestion%29.md)
  Creates a search suggestion with the specified label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/init(localizedattributedsuggestion:))*
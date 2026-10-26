# init(localizedSuggestion:localizedDescription:iconImage:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a search suggestion with the specified text and image attributes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(localizedSuggestion suggestion: String, localizedDescription description: String?, iconImage: UIImage?)
```

```objc
- (instancetype) initWithLocalizedSuggestion:(NSString *) suggestion localizedDescription:(NSString *) description iconImage:(UIImage *) iconImage;
```

## Parameters

- `suggestion`: A label for the suggestion, usually the search term the suggestion represents.
- `description`: A description of the suggestion. The system uses this description for accessibility.
- `iconImage`: An image for display on the suggestion.

## See Also

### Creating a search suggestion
- [init(localizedAttributedSuggestion: NSAttributedString, localizedDescription: String?, iconImage: UIImage?)](./init%28localizedattributedsuggestion,localizeddescription,iconimage%29.md)
  Creates a search suggestion with the specified attributed label, accessibility description, and image.
- [init(localizedSuggestion: String, localizedDescription: String?)](./init%28localizedsuggestion,localizeddescription%29.md)
  Creates a search suggestion with the specified label and accessibility description.
- [init(localizedAttributedSuggestion: NSAttributedString, localizedDescription: String?)](./init%28localizedattributedsuggestion,localizeddescription%29.md)
  Creates a search suggestion with the specified attributed label and accessibility description.
- [init(localizedSuggestion: String)](./init%28localizedsuggestion%29.md)
  Creates a search suggestion with the specified label.
- [init(localizedAttributedSuggestion: NSAttributedString)](./init%28localizedattributedsuggestion%29.md)
  Creates a search suggestion with the specified attributed label.
- [+ suggestionWithLocalizedSuggestion:descriptionString:iconImage:](./suggestionwithlocalizedsuggestion_descriptionstring_iconimage_.md)
  Creates a search suggestion with the specified text and image attributes.
- [+ suggestionWithLocalizedAttributedSuggestion:descriptionString:iconImage:](./suggestionwithlocalizedattributedsuggestion_descriptionstring_iconimage_.md)
  Creates a search suggestion with the specified attributed label, accessibility description, and image.
- [+ suggestionWithLocalizedSuggestion:descriptionString:](./suggestionwithlocalizedsuggestion_descriptionstring_.md)
  Creates a search suggestion with the specified label and accessibility description.
- [+ suggestionWithLocalizedAttributedSuggestion:descriptionString:](./suggestionwithlocalizedattributedsuggestion_descriptionstring_.md)
  Creates a search suggestion with the specified attributed label and accessibility description.
- [+ suggestionWithLocalizedSuggestion:](./suggestionwithlocalizedsuggestion_.md)
  Creates a search suggestion with the specified label.
- [+ suggestionWithLocalizedAttributedSuggestion:](./suggestionwithlocalizedattributedsuggestion_.md)
  Creates a search suggestion with the specified attributed label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/init(localizedsuggestion:localizeddescription:iconimage:))*
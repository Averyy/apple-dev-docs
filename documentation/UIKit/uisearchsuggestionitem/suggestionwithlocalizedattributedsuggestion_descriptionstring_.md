# suggestionWithLocalizedAttributedSuggestion:descriptionString:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a search suggestion with the specified attributed label and accessibility description.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) suggestionWithLocalizedAttributedSuggestion:(NSAttributedString *) suggestion descriptionString:(NSString *) description;
```

## Parameters

- `suggestion`: An attributed label for the suggestion, usually the search term the suggestion represents.
- `description`: A description of the suggestion. The system uses this description for accessibility.

## See Also

### Creating a search suggestion
- [init(localizedSuggestion: String, localizedDescription: String?, iconImage: UIImage?)](./init%28localizedsuggestion,localizeddescription,iconimage%29.md)
  Creates a search suggestion with the specified text and image attributes.
- [init(localizedAttributedSuggestion: NSAttributedString, localizedDescription: String?, iconImage: UIImage?)](./init%28localizedattributedsuggestion,localizeddescription,iconimage%29.md)
  Creates a search suggestion with the specified attributed label, accessibility description, and image.
- [+ suggestionWithLocalizedSuggestion:descriptionString:iconImage:](./suggestionwithlocalizedsuggestion_descriptionstring_iconimage_.md)
  Creates a search suggestion with the specified text and image attributes.
- [+ suggestionWithLocalizedAttributedSuggestion:descriptionString:iconImage:](./suggestionwithlocalizedattributedsuggestion_descriptionstring_iconimage_.md)
  Creates a search suggestion with the specified attributed label, accessibility description, and image.
- [init(localizedSuggestion: String, localizedDescription: String?)](./init%28localizedsuggestion,localizeddescription%29.md)
  Creates a search suggestion with the specified label and accessibility description.
- [init(localizedAttributedSuggestion: NSAttributedString, localizedDescription: String?)](./init%28localizedattributedsuggestion,localizeddescription%29.md)
  Creates a search suggestion with the specified attributed label and accessibility description.
- [+ suggestionWithLocalizedSuggestion:descriptionString:](./suggestionwithlocalizedsuggestion_descriptionstring_.md)
  Creates a search suggestion with the specified label and accessibility description.
- [init(localizedSuggestion: String)](./init%28localizedsuggestion%29.md)
  Creates a search suggestion with the specified label.
- [init(localizedAttributedSuggestion: NSAttributedString)](./init%28localizedattributedsuggestion%29.md)
  Creates a search suggestion with the specified attributed label.
- [+ suggestionWithLocalizedSuggestion:](./suggestionwithlocalizedsuggestion_.md)
  Creates a search suggestion with the specified label.
- [+ suggestionWithLocalizedAttributedSuggestion:](./suggestionwithlocalizedattributedsuggestion_.md)
  Creates a search suggestion with the specified attributed label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/suggestionwithlocalizedattributedsuggestion:descriptionstring:)*
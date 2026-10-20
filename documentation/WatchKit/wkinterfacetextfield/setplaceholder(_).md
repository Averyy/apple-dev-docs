# setPlaceholder(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the text field’s placeholder.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func setPlaceholder(_ placeholder: String?)
```

```objc
- (void) setPlaceholder:(NSString *) placeholder;
```

#### Discussion

Use placeholders to describe the text field’s expected content to the user. An empty text field displays the placeholder, and any entered text hides the placeholder. The system automatically formats the placeholder, making it obvious that it’s not a valid text entry.

## See Also

### Setting a Placeholder
- [func setAttributedPlaceholder(NSAttributedString?)](./setattributedplaceholder%28_%29.md)
  Sets the text field’s placeholder using styled text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield/setplaceholder(_:))*
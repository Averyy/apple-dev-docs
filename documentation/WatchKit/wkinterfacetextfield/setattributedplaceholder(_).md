# setAttributedPlaceholder(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the text field’s placeholder using styled text.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func setAttributedPlaceholder(_ attributedPlaceholder: NSAttributedString?)
```

```objc
- (void) setAttributedPlaceholder:(NSAttributedString *) attributedPlaceholder;
```

## Discussion

Use placeholders to describe the text field’s expected content to the user. An empty text field displays the placeholder, and any entered text hides the placeholder. The system automatically formats the placeholder, making it obvious that it’s not a valid text entry.

## See Also

### Setting a Placeholder
- [func setPlaceholder(String?)](./setplaceholder%28_%29.md)
  Sets the text field’s placeholder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield/setattributedplaceholder(_:))*